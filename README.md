```
  ____        ____       _
 |  _ \ _   _|  _ \ _ __(_)_   _____
 | |_) | | | | | | | '__| \ \ / / _ \
 |  __/| |_| | |_| | |  | |\ V /  __/
 |_|    \__, |____/|_|  |_| \_/ \___|
        |___/
```

PyDrive allows to upload and download files from google drive

## How to Install

```
git clone https://github.com/We4theReport/PyDrive.git
cd PyDrive
pip install --upgrade google-api-python-client

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

python pydryve.py -f -a [filenime]
