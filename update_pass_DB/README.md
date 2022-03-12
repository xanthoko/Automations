## Info
Uploads the .kdbx file to my google drive.
This file is used by KeePassXC to store passwords and is saved locally.

### Steps to run
First of all, I needed to create a Google Cloud Project and enable API ([Create Project](https://developers.google.com/workspace/guides/create-project))

Then create cedentials for a desktop application. ([Create credentials](https://developers.google.com/workspace/guides/create-credentials))

Local steps:
1. `chmod +x update_kdbx.py` to make the script executable
2. Add the project directory to the **$PATH**
3. Run *update_kdbx.py*

### NOTE
Had to add the following lines in pydrive/settings.py line:145 in order to
accept the custom settings. They needed to be a dictionary, while the library
produced a list of dictionaries.
```
s = {}
for d in data:
    s.update(d)
return s
```
