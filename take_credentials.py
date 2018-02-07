from __future__ import print_function
import os

from oauth2client.file import Storage


def get_credentials(name_json):
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    credential_path = os.path.join(credential_dir, name_json)
    store = Storage(credential_path)
    credentials = store.get()

    return credentials
