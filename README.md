## Prerequisites
### PIP
Get the file: https://bootstrap.pypa.io/get-pip.py
```
python get-pip.py
```
### VIRTUALENV
```
sudo pip install virtualenv
brew install python3
```
### RUN INTO A VIRTUALENV
```
virtualenv -p /usr/local/bin/python3 venv
. venv/bin/activate
pip install -r requirements.txt
python forest.py
```
