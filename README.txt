# For install
Install python 3.8
Install NodeJS

pip install -r requirements.txt
npm ci

# start venv windows
venv\Scripts\activate

#start venv linux
source venv/Scripts/activate

# Launch Debug have to start both
cd /webapp
npm start
cd ..
python manage.py runserver

# BUILD Prod
# set debug=false in settings.py
cd /webapp
npm run-script build
cd ..
python manage.py collectstatic --noinput 
python manage.py runserver



# VSCode settings.json
{
    "python.pythonPath": "venv\\Scripts\\python.exe"
}

#VSCode debug launch.json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
    
        {
            "name": "Launch Chrome",
            "request": "launch",
            "type": "pwa-chrome",
            "url": "http://127.0.0.1:7000",
            "webRoot": "${workspaceFolder}/webapp"
        },
        {
            "name": "Python: Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": [
                "runserver",
                "127.0.0.1:7000"
            ],
            "django": true
        }
    ]
}