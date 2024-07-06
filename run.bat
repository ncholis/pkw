@echo off

echo Activating virtual environment...
call venv\Scripts\activate


echo Starting the web...
python .\pkw\manage.py runserver

echo done
pause
