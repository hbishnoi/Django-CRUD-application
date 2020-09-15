# Django-CRUD-application

Django is a Python framework, so we must install Latest Python to machine.

To Install Python, go to website https://python.org/downloads/. Download and Install it into your machine.
After installation, open the command prompt and check that if the Python version matches the version you installed by executing:
> py –version

After this, we need pip because it is a Python package manager, and it helps to install and uninstall python packages like Django.

Install Django into your machine with a simple line of code into your command prompt:
> py -m pip install Django

Now, We need Database to store and retrieve data for our application. So, we will install relational database Postgresql.
To install Postgres, go to https://www.postgresql.org/download/. Download and Install it into your machine.

Open Postgresql and Create a Database 'EmployeeDB' in it.

Download this code zip and run these codes into your terminal or command prompt. Make sure you're in the folder —

To apply changes into database like creating the table for the application with some other tables run this command:
> python manage.py migrate

To run server where the project will run into your browser run this command:
> python manage.py server

Now click on the link http://127.0.0.1:8000/ in your terminal or command prompt which ever you are using.

Now if you see error in opening the webpage of the application. Add '/employee/' to your url and hit enter.

