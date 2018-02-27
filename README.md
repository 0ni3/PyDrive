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

PyDrive allows to upload and download files from google drive

## How to Install

```
git clone https://github.com/We4theReport/PyDrive.git
cd PyDrive
pip install --upgrade google-api-python-client
pip install -r requirements.txt

```
## Usage

python pydrive.py -h

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

python pydrive.py -f -a upload [filename]
