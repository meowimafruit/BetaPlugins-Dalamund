# Dalamud Beta Plugins Auto-Enabler

A Python-based utility tool that automatically enables beta plugin testing for FFXIV's XIVLauncher.

## Technical Overview
This tool performs the following operations:
1. Fetches the latest beta keys from the official Dalamud repository (`https://github.com/goatcorp/dalamud-declarative`)
2. Locates your XIVLauncher configuration at `%APPDATA%\XIVLauncher\dalamudConfig.json`
3. Creates a timestamped backup of your current configuration
4. Updates the configuration with:
   - Enables plugin testing (`DoPluginTest: true`)
   - Sets the latest beta key from staging track
   - Updates the beta kind to 'stg'

## Features
- **Automated Key Updates**: Pulls latest beta keys directly from Dalamud's GitHub repository
- **Safe Configuration**: Creates timestamped backups (format: `dalamudConfig_YYYYMMDD_HHMM.json`)
- **One-Click Execution**: Compiled as a standalone .exe requiring no Python installation
- **Error Handling**: Provides clear feedback for common issues

## Usage
1. Download `Dalamund-Beta-Plugins-AutoEnabler.exe` from the releases page
2. Run the executable (requires admin rights)
3. Wait for confirmation message
4. Press Enter to close

## Requirements
- Windows Operating System
- XIVLauncher installed
- Internet connection (to fetch latest beta keys)
- Administrative privileges (for config file access)

## Technical Details
The executable is a compiled version of `betaPluginsEnablerAuto.py` using PyInstaller, which:
- Uses `requests` library for GitHub API calls
- Employs `yaml` for config parsing
- Handles file operations with built-in Python libraries
- Creates unique backups using datetime stamps

## Safety Features
- Automatic backup creation before any changes
- Non-destructive configuration updates
- Validation of config file existence
- Exception handling for common errors

## License
MIT License - See LICENSE file for details

## Disclaimer
This tool is not affiliated with SQUARE ENIX CO., LTD. or XIVLauncher. Use at your own risk.
All configuration changes are made to XIVLauncher settings only, no game files are modified.
