#!/Users/user/.virtualenvs/automations/bin/python3
'''Update my passwords.kdbx file in google drive.

.kdbx file is the database that KeePassXC uses to store pesonal passwords.

Had to add the following lines in pydrive/settings.py line:145 in order to
accept the custom settings. They need to be a dictionary, while the library
produced a list of dictionaries.
`
s = {}
for d in data:
    s.update(d)
return s
`
'''
import os
import shutil
from pathlib import Path

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

DST_FOLDER_ID = '10VnF6q-NwDUgoaKJnLytJecktBzGfEvs'  # Personal directory
SRC_FILE_PATH = f'{Path.home()}/Documents/Passwords.kdbx'
TEMP_FILE_NAME = 'Passwords.kdbx'
CUSTOM_SETTINGS_PATH = f'{Path.home()}/Documents/Automations/update_pass_DB/custom_settings.yaml'

gauth = GoogleAuth(settings_file=CUSTOM_SETTINGS_PATH)
drive = GoogleDrive(gauth)

shutil.copy(SRC_FILE_PATH, TEMP_FILE_NAME)

passwords_drive_query = drive.ListFile({'q': "title='Passwords.kdbx'"}).GetList()
if passwords_drive_query:
    # update file
    gfile = passwords_drive_query[0]
else:
    # create new file
    gfile = drive.CreateFile({'parents': [{'id': DST_FOLDER_ID}]})

gfile.SetContentFile(TEMP_FILE_NAME)
gfile.Upload()

os.remove(TEMP_FILE_NAME)
