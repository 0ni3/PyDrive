#!/usr/bin/env python
# -*- coding: utf -*-
from __future__ import print_function
import httplib2
import os
import sys

from googleapiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

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
        credential_path = os.path.join(credential_dir, 'google-drive-credentials.json')
        store = Storage(credential_path)
        try:
            credentials = store.get()
        except:
            print('Working with flow-based credentials instantiation')
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(self.CLIENT_SECRET_FILE, self.SCOPES)
            flow.user_agent = self.APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else: # Needed only for compatibility with Python 2.6
                credentials = tools.run_flow(flow, store)
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
                            default=None, help="Specify an action ex.[upload, download, find, list, delete]")
        args = parser.parse_args()
        if not args.action:
            print((color.RED) + ("Missing '-a' or '--action' argument!") + (color.ENDC))
            sys.exit(-1)

            if args.action == "upload":
                if not args.file:
                    print((color.RED) + ("Missing '-f' or '--file' argument!") + (color.ENDC))
                    sys.exit(-1)

                    if ',' in args.file:
                        files = args.file.split(',')

                        for f in files:
                            if not os.path.exists(f):
                                print((color.RED) + ("The file doesn't exists!") + (color.ENDC))
                                sys.exit(-1)
                            else:
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
                                    elif args.action == "search":
                                        if not args.file:
                                            print((color.RED) + ("Missing '-f' or '--file' argument!") + (color.ENDC))
                                            sys.exit(-1)
                                            self.search(args)
                                        elif args.action == "delete":
                                            if not args.file:
                                                print((color.RED) + ("Missing '-f' or '--file' argument!") + (color.ENDC))
                                                sys.exit(-1)
                                                self.delete(args)
                                            else:
                                                print((color.RED) + ("Missing command argument!") + (color.ENDC))
                                                sys.exit(-1)
                                                return args

    def upload(self, args):
        files = args.file.split(',')
        for f in files:
            print(color.RED + "Uploading " + f + color.ENDC)
            filename = os.path.basename(f)
            file_metadata = {'name': filename}
            media = MediaFileUpload(f, mimetype='application/octet-stream')
            file = self.drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            print('File Name: %s\nFile ID: %s' % (file.get('name'),file.get('id')))

    def download(self, args):
    	print(color.GREEN + "Downloading... " + args.file + color.ENDC)
    	results = self.drive_service.files().list(pageSize=10,fields="nextPageToken, files(id, name)").execute()
        #items = results.get('files', [])
        # if not items:
        #     print('No files found.')
        # else:
        #     for item in items:
        # 	if item['name'] == args.file:
        #         request = self.drive_service.files().get_media(fileId=item['id'])
        # 		fh = io.BytesIO()
        # 		downloader = MediaIoBaseDownload(fh, request)
        # 		done = False
        #         while done is False:
        #             status, done = downloader.next_chunk()
        # 			print("Downloading %d%%." % int(status.progress() * 100))
        # 			directory = os.path.join(os.getcwd(), 'downloads')
        #             if not os.path.exists(directory):
        #                 os.makedirs(directory)
        #                 with io.open(os.path.join(directory, item['name']),'wb') as f:
        #                     fh.seek(0)
        #                     f.write(fh.read())

    def search(self, args):
    	print(color.BLUE + "Searching... " + args.file + color.ENDC)
    	results = self.drive_service.files().list(
                pageSize=10,fields="nextPageToken, files(id, name)").execute()
            # items = results.get('files', [])
            # if not items:
            #     print('No files found.')
            # else:
    	    # for item in items:
    		# if item['name'] == args.file:
    		#         print('File trovato! Ha come ID {0}'.format(item['id']))

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

    def delete(self, args):
    	print(color.BLUE + "delete" + args.file + color.ENDC)
    	results = self.drive_service.files().list(
                pageSize=10,fields="nextPageToken, files(id, name)").execute()
            # items = results.get('files', [])
            # if not items:
            #     print('No files found.')
            # else:
    	    # for item in items:
    		# if item['name'] == args.file:
    		# 	self.drive_service.files().delete(fileId=item['id']).execute()
    		#         print('File cancellato!')

if __name__ == '__main__':
    color = Colors()
    pydrive = PyDrive()
    pydrive.show_banner()
    print("\n")
    pydrive.validate_args()
