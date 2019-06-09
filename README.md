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
        d. pip install psycopg2
    5.  Install web3
        Mac:  pip install web3
    6.  Create Database or determine parameters for the code to handle the database. The code is setup for PSQL with a database called drsdb and user drs with  password abcd12345.  You will need to manually set that up.  Additionally we have it setup to handle data objects with the field as so account_number, name, details, days, pub_date.
    7.  Database migration.  If you choose to use our database python manage.py migrate.

# Running
    1.  To activate your virtual environment use the 'workon' command with the name of your environment.

    2. To Determine your environment use, which defaults to dev
          export APP_ENV=production

    3.  You can configure production mode by setting your variables like so:
          export DRS_SECRET_KEY={Secret Key}
          export DRS_CONTRACT_ADDRESS={Address}
          export DRS_SERVICE_ID={Address}
    4. python manage.py runserver

# Administration
  TODO:  Included more details on Administration
  To create a new admin use the command   and follow the prompts to set a username and password
    $ python manage.py createsuperuser
  Then login to the admin page at http://127.0.0.1:8000/admin/
  You can use this to view, manage and update your data and database.


# Summary
  this code allows you to pass paramaters to the gatekeeper endpoint as so
    gatekeeper/<str:address_id>/<str:signature_id>/<str:message_hash>/<str:parameter>/<str:key>
  to access data.  This code is 0.1V it is usable but more testing and cleaning will need to be done.  Please notify us on github if any issues are found.
