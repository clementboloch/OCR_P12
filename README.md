# OCR_P12
Développeur d'Application Python - Projet 12



## Setup

### Directory setup
It is recommended to create a dedicated directory to download the project.
In a terminal:
`mkdir dir_name`
`cd dir_name`

### Git setup
Then clone the remote repository in your local repository with the https link. You will find the https link is in the "code" drop-down menu:
`git clone https://github.com/clementboloch/OCR_P12.git`

### Virtual environment setup
Go inside the `OCR_P12` directory and initialize a new virtual environment using venv before installing the dependencies:
`cd OCR_P12`
`python3 -m venv env`
Active the virtual environment:
`source env/bin/activate`

Install the required packages from the requirement.txt file:
`pip install -r requirement.txt`

## Database setup
Ensure you have PostgreSQL installed on your machine. You can download and install it from the official PostgreSQL website.
`https://www.postgresql.org/download/`

Ensure PostgreSQL is running and access the PostgreSQL command line interface (CLI) by typing:
`psql postgres`
Then, run the following SQL commands to create the database and user with the specified settings:
`CREATE DATABASE epicevents;`
`CREATE USER admin WITH SUPERUSER PASSWORD '9090';`
`GRANT ALL PRIVILEGES ON DATABASE epicevents TO admin;`


Go to src folder:
`cd src`
Make the migrations:
`python manage.py migrate`
And create the groups:
`python manage.py add_custom_groups`

## Run test
To run the tests, in the `src` folder run the command:
`pytest`

## Launch the program
Launch the local server:
`python manage.py runserver`