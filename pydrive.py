#!/usr/bin/env python
# -*- coding: utf -*-
from __future__ import print_function
import httplib2
import os
import sys

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaFileUpload, MediaIoBaseDownload

try:
    import argparse
    from terminaltables import SingleTable
    #flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    flags=tools.argparser.parse_args(args=[])
except ImportError:
    print("Error in the import libraries!")
    sys.exit(-1)
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/google-drive-credentials.json
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'PyDrive'


class Colors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'


class GoogleDriveAuth:
    def __init__(self,SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME):
        self.SCOPES = SCOPES
        self.CLIENT_SECRET_FILE = CLIENT_SECRET_FILE
        self.APPLICATION_NAME = APPLICATION_NAME

    def getCredentials(self):
        """Gets valid user credentials from storage.
        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.
        Returns:
            Credentials, the obtained credential.
        """
        current_dir = os.getcwd()
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'google-drive-credentials.json')
        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(self.CLIENT_SECRET_FILE, self.SCOPES)
            flow.user_agent = self.APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else: # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print((color.GREEN) + 'Storing credentials to ' + credential_path + (color.ENDC))
            os.remove(os.path.join(current_dir, CLIENT_SECRET_FILE))
        return credentials


class PyDrive:
    def __init__(self):
        GDAuth = GoogleDriveAuth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
        credentials = GDAuth.getCredentials()
        http = credentials.authorize(httplib2.Http())
        self.drive_service = discovery.build('drive', 'v3', http=http)

    def show_banner(self):
        with open('banner', 'r') as f:
            data = f.read()
            print((color.GREEN) + (data) + (color.ENDC))

    def validate_args(self):
        parser = argparse.ArgumentParser(description="")
        parser.add_argument("-f", "--file", metavar="<file>", dest="file",
                            default=None, help="Specify a file")
        parser.add_argument("-a", "--action", metavar="<action>", dest="action",
                            default=None, help="Specify an action ex.[upload, download, find, list]")
        args = parser.parse_args()
        if not args.action:
            print((color.RED) + ("Missing '-a' or '--action' argument!") + (color.ENDC))
            sys.exit(-1)
        if args.action == "upload":
            if not args.file:
               print((color.RED) + ("Missing '-f' or '--file' argument!") + (color.ENDC))
               sys.exit(-1)
            if not os.path.exists(args.file):
               print((color.RED) + ("The file doesn't exists!") + (color.ENDC))
               sys.exit(-1)
            self.upload(args)
        elif args.action == "download":
            if not args.file:
               print((color.RED) + ("Missing '-f' or '--file' argument!") + (color.ENDC))
               sys.exit(-1)
            self.download(args)
        elif args.action == "list":
            self.list(args)
        elif args.action == "find":
            if not args.file:
               print((color.RED) + ("Missing '-f' or '--file' argument!") + (color.ENDC))
               sys.exit(-1)
            self.find(args)
        else:
            print((color.RED) + ("Missing command argument!") + (color.ENDC))
            sys.exit(-1)
        return args

    def upload(self, args):
        print(color.RED + "upload a file " + args.file + color.ENDC)
        # vedere su google api drive per completare il comando
        
    def download(self, args):
        print(color.GREEN + "download a file " + args.file + color.ENDC)
        # vedere su google api drive per completare il comando
   
    def find(self, args):
        print(color.BLUE + "find a file " + args.file + color.ENDC)
        # vedere su google api drive per completare il comando
      
    def list(self, args):
        results = self.drive_service.files().list(
            pageSize=10,fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
        else:
            print((color.PURPLE) + ('List all files') + (color.ENDC))
            data = [['ID','Name']]
            for item in items:
                data.append([item['name'],item['id']])
            t = SingleTable(data) #AsciiTable()
            print(t.table)

if __name__ == '__main__':
    color = Colors()
    pydrive = PyDrive()
    pydrive.show_banner()
    print("\n")
    pydrive.validate_args()
