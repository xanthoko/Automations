'''Update my passwords.kdbx file in google drive.

.kdbx file is the database that KeePassXC uses to store pesonal passwords.
'''
import os
import shutil
from pathlib import Path

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

DST_FOLDER_ID = '10VnF6q-NwDUgoaKJnLytJecktBzGfEvs'
SRC_FILE_PATH = f'{Path.home()}/Documents/Passwords.kdbx'
TEMP_FILE_NAME = 'Passwords.kdbx'

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

shutil.copy(SRC_FILE_PATH, TEMP_FILE_NAME)

passwords_drive_query = drive.ListFile({'q': "title='Passwords.kdbx'"}).GetList()
if passwords_drive_query:
    # update file
    gfile = passwords_drive_query[0]
else:
    gfile = drive.CreateFile({'parents': [{'id': DST_FOLDER_ID}]})

gfile.SetContentFile(TEMP_FILE_NAME)
gfile.Upload()

os.remove(TEMP_FILE_NAME)
