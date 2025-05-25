# Deployment Instructions
As of right now we deploy the project within the VS Code IDE. Once the code folder is opened within this application, you will want to
follow the following instructions based on your operating system. These commands can be copy pasted in the VS Code Terminal.

Note: Python should be downloaded to your computer as well.
## For Mac
1. python3 -m venv env
2. source env/bin/activate
3. python3 -m pip install -r requirements.txt
4. cd laf
5. python3 manage.py migrate
6. python3 manage.py runserver
7. Hold the command key and click on the server url

## For Windows
1. python -m venv env
2. env\Scripts\activate
3. python -m pip install -r requirements.txt
4. cd laf
5. python manage.py migrate
6. python manage.py runserver
7. Hold control key and click on the server url

After clicking on the server url, you will be taken to the prototype site. Here, you can upload, claim, and give descriptions for items.
