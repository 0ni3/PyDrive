#!/usr/bin/env python
# -*- coding: utf -*-
from __future__ import print_function
import os
import sys

try:
    import argparse
    from terminaltables import SingleTable
    import httplib2
    from apiclient import discovery
    from oauth2client import client
    from oauth2client import tools
    from oauth2client.file import Storage

except ImportError:
    flags = None
    #print("Error in the import libraries")
    #sys.exit(0)


# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
CLIENT_SECRET_FILE = 'client_id.json'
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


class PyDrive:

    def __init__(self):
        self.service = ""

    def show_banner(self):
        with open('banner', 'r') as f:
            data = f.read()
            print(color.GREEN + data + color.ENDC)

    def validate_args(self):
        parser = argparse.ArgumentParser(description="")
        parser.add_argument("-f", "--file", metavar="<file>", dest="file",
                            default=None, help="Specify a file")
        parser.add_argument("-a", "--action", metavar="<action>", dest="action",
                            default=None, help="Specify an action ex.[upload, download, find, list]")
        args = parser.parse_args()
        if not args.action:
            print("Missing '-a' or '--action' argument!")
            sys.exit(-1)
        #if not args.file:
        #   print("Missing '-f' or '--file' argument!")
        #   sys.exit(-1)
        #if not os.path.exists(args.file):
        #    print("the file doesn't exist")
        #    sys.exit(-1)
        if args.action == "upload":
            self.upload(args)
        elif args.action == "download":
            self.download(args)
        elif args.action == "list":
            self.list(args)
        elif args.action == "find":
            self.find(args)
        else:
            print("missing command argument")
            sys.exit(-1)
        return args

    def get_credentials(self):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        credential_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'client_id.json')
        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else:
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials

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
        print((color.PURPLE) + ("list all files ") + (color.ENDC))
        credentials = self.get_credentials()
        http = credentials.authorize(httplib2.Http())
        self.service = discovery.build('drive', 'v3', http=http)
        results = self.service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print('{0} ({1})'.format(item['name'], item['id']))


if __name__ == '__main__':
    color = Colors()
    pydrive = PyDrive()
    pydrive.show_banner()
    pydrive.validate_args()
