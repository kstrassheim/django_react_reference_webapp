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
python manage.py collectstatic
python manage.py runserver