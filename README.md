# Django-CRUD-application

Django is a Python framework, so we must install Latest Python to machine.
To Install Python, go to website https://python.org/downloads/. Download and Install it into your machine.
After installation, open the command prompt and check that the Python version matches the version you installed by executing:
> py –version

After this, we need pip because it is a Python package manager, and it helps to install and uninstall python packages like Django.

Install Django into your machine with a simple line of code into your command prompt
> py -m pip install Django

Now, We need Database to store and retrieve data for our application. So, we will install relational database Postgresql.
To install Postgres, go to https://www.postgresql.org/download/. Download and Install it into your machine.
Now, create a Database EmployeeDB  in Postgres.	

Download this code zip and run these codes into your terminal or command prompt. Make sure you're in the folder —
>   python manage.py makemigrations employee_register
>   python manage.py sqlmigrate employee_register 0001	
>   python manage.py migrate
>   python manage.py server
