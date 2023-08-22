# Create New Job Folders

## Description
This application facilitates generating a standard job/project folder structure. The user provides inputs such as job number, part number, project name, and part name. The program then generates a hierarchically nested directory structure.

## Usage

The scripts can be run via a right-click context menu in Windows Explorer.

To setup the context menu entry, modify the Windows Registry or use third-party software (like ShellNewHandler, FileMenu Tools, Custom Context Menu) to add an entry with the following command:

```command
cmd /c "path\to\your\scripts\createNewJobFolder.bat" \"%V\"
```

The `\"%V\"` argument passes the full directory path (where the user right-clicked) to the batch script, which transfers it to the Python script.

## Scripts

### `createNewJobFolder.bat`

This batch file sets up and activates a Python virtual environment, upgrades pip to ensure the latest version is used, installs necessary dependencies and runs the `createNewJobFolders.py` script.

### `createNewJobFolders.py`

This Python script reads a predefined list of folders from a YAML configuration file (`config.yaml`). It then creates these directories at the location provided as a command-line argument, or in the current working directory if no location is specified.

### `GUI.py`

This Python script generates a simple GUI to collect user input, which includes the job number, part number, project name, and part name for the new folder structure.

## Dependencies

This script requires the following to be installed:

- Python 3
- pip
- PyYAML
- PyQt5