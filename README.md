# GateKeeper-Python

# Installation
    Mac.  This installation assumes you already have psql installed.  Additionally, you can choose to skip step 1 if you already have python3 and the virtual environment installed or you have your own process
      1.  Install Python3 and virtual Environment
        a. brew search python
        b. brew install python3
        c. python3 --version
        d. pip install virtualenv
        e. pip install virtualenvwrapper
        f. mkdir ~/.virtualenvs
        g.  Open your .bashrc file and add:
                export WORKON_HOME=~/.virtualenvs
                source /usr/local/bin/virtualenvwrapper.sh
        h. source .bashrc
        i.  To create virtual environment
        j.  mkvirtualenv --python=python3_path myenv
    2. pip install Django
    3. Git clone or download repo
    4. Install Pythereum.  May need to use other commands based on system
        a. sudo apt-get install libssl-dev build-essential automake pkg-config libtool libffi-dev libgmp-dev libyaml-cpp-dev
        b. git clone https://github.com/ethereum/pyethereum/
        c. cd pyethereum
        d. python setup.py install
    5.  Install web3
        Mac:  pip install web3
    6.  Create Database or determine parameters for the code to handle the database. The code is setup for PSQL with a database called drsdb and user drs with  password abcd12345.  Additionally we have it setup to handle data objects with the field as so account_number, name, details, days, pub_date.
    7.  Database migration.  To either use our database or your own run python manage.py makemigrations gatekeeper and python manage.py migrate.  This will load what ever tables you have into psql.  For other setups or downloading your DBs into django please review the Django manuals.

# Running
    1. python manage.py runserver


# Summary
  this code allows you to pass paramaters to the gatekeeper endpoint as so
    gatekeeper/<str:address_id>/<str:signature_id>/<str:message_hash>/<str:parameter>/<str:key>
  to access data.  This code is 0.1V it is usable but more testing and cleaning will need to be done.  Please notify us on github if any issues are found.
