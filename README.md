```
88888888ba              88888888ba,              88
88      "8b             88      `"8b             ""
88      ,8P             88        `8b
88aaaaaa8P' 8b       d8 88         88 8b,dPPYba, 88 8b       d8  ,adPPYba,
88""""""'   `8b     d8' 88         88 88P'   "Y8 88 `8b     d8' a8P_____88
88           `8b   d8'  88         8P 88         88  `8b   d8'  8PP"""""""
88            `8b,d8'   88      .a8P  88         88   `8b,d8'   "8b,   ,aa
88              Y88'    88888888Y"'   88         88     "8"      `"Ybbd8"'
                d8'                                                         
               d8'             
```

PyDrive allows to upload and download files from Google Drive


## How to enable the Google Drive API

 - Use [this wizard](https://console.developers.google.com/start/api?id=drive) to create or select a project in the Google Developers Console and automatically turn on the API. Click **Continue**, then **Go to credentials**.
 - On the **Add credentials to your project** page, click the **Cancel** button.
 - At the top of the page, select the **OAuth consent screen** tab. Select an **Email address**, enter a **Product name** if not already set, and click the **Save** button.
 - Select the **Credentials** tab, click the **Create credentials** button and select **OAuth client ID**.
 - Select the application type **Other**, enter the name "**PyDrive**", and click the **Create** button.
 - Click **OK** to dismiss the resulting dialog.
 - Click the file_download (Download JSON) button to the right of the client ID.
 - Move this file to your PyDrive directory and rename it client_secret.json.


## How to Install

```
git clone https://github.com/We4theReport/PyDrive.git
cd PyDrive
pip install --upgrade google-api-python-client
pip install -r requirements.txt
```

## Usage

```
usage: pydrive.py [-h] [-f <file>] [-a <action>]

optional arguments:
  -h, --help            show this help message and exit
  -f <file>, --file <file>
                        Specify a file
  -a <action>, --action <action>
                        Specify an action ex.[upload, download, find, list]
```

**Examples**

    python pydrive.py -a upload -f [path_to_filename]
