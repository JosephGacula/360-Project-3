# Deployment Instructions
As of right now we deploy the project within the VS Code IDE.

Dependencies to download if not already installed on your computer;

1. Python 3.13.3 Link: https://www.python.org/downloads/release/python-3133/
2. VS Code Link: https://code.visualstudio.com/download
3. Python VS Code Extension Link: https://marketplace.visualstudio.com/items?itemName=ms-python.python


Download the zip for this code on github. Once the root folder is opened within this application, you will want to follow the following instructions based on your operating system.
Open the terminal within VS Code (Can be done by navigating to the top tab and clicking Terminal -> New Terminal, or Ctrl+ ~ )These commands can then be copy pasted in the VS Code Terminal in order.

## For Mac
python3 -m venv env


source env/bin/activate


python3 -m pip install -r requirements.txt


cd laf


python3 manage.py migrate


python3 manage.py runserver


Hold the command key and click on the server url

## For Windows
python -m venv env


env\Scripts\activate


cd 360-Project-3-main


cd lost-and-found-sea 2

Hold the command key and click on the server url

  Note: The root folder should be the one you selected to open at the beginning, if this is not the case, simply navigate to the  lost-and-found-sea 2 directory with cd commands.

python -m pip install -r requirements.txt
cd laf
python manage.py migrate
python manage.py runserver

At this point, hold control key and click on the server url. After clicking on the server url, you will be taken to the prototype site. Here, you can upload, claim, and give descriptions for items.
