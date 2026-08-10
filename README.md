to start run:
cd server
source ../venv/bin/activate
uvicorn main:app --reload

to install a new package run:
source ../venv/bin/activate
pip install <package_name>
pip freeze > requirements.txt