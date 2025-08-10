#A quick script to update the config for xivlauncher, changing the betaKey and betaKind strings to enable the beta
import json
import os
import sys
import requests
import yaml
from datetime import datetime
from pathlib import Path

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def main():
    try:
        keysUrl = "https://raw.githubusercontent.com/goatcorp/dalamud-declarative/main/config.yaml"
        response = requests.get(keysUrl, allow_redirects=True)
        content = response.content.decode("utf-8")
        content = yaml.safe_load(content)

        appdataPath = os.getenv('APPDATA')
        configPath = os.path.join(appdataPath, 'XIVLauncher', 'dalamudConfig.json')
        # Add hours and minutes to timestamp for unique backups
        current_date = datetime.now().strftime('%Y%m%d_%H%M')
        backupPath = configPath.replace('.json', f'_backup_{current_date}.json')

        if os.path.exists(configPath):
            import shutil
            shutil.copy2(configPath, backupPath)
            print(f'Backup created at {backupPath}')
            
            with open(configPath) as f:
                dalamudConfig = json.load(f)
                dalamudConfig['DoPluginTest'] = True
                dalamudConfig['DalamudBetaKey'] = content['tracks']['stg']['key']
                dalamudConfig['DalamudBetaKind'] = 'stg'    

            with open(configPath, 'w', encoding='utf-8') as f:
                json.dump(dalamudConfig, f, ensure_ascii=False, indent=4)

            print('Successfully updated dalamudConfig')
        else:
            print('DalamudConfig.json could not be found at ' + configPath)
            
    except Exception as e:
        print(f'Error: {e}')
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
