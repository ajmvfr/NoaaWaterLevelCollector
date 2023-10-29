To create virtual enviroment    
    py -3 -m venv venv

script for command terminal line to attach to virtuall enviroment
    venv\Scripts\activate.bat

To execute code
    python -m app.main

setup git hub
    git init
    git add --all
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/ajmvfr/NoaaWaterLevelCollector.git
    git push -u origin main

Pushing changes with github
    #make changes to code and save changes
    #command line   
        git add --all
        git commit -m "New Code to test deploy"
        git push origin main

install alembic
    pip install alembic

    help
        alembic --help
    init
        alembic init alembic   #second alembic is directory,  creates elembic folder and alembic.ini file
        edit alembic\env.py to add DB call
        edit alembic.ini to sqlalchemy.url
    deply DB    
        alembic revision -m "create posts table"  #creates post table  find version, edit
    find current version
        alembic current
    deployalembic revision -m "create posts table"
        alembic upgrade {revision numner}    #get from revision file
    get the head version, this is the newest versioin
        alembic heads
    to upgrate to head version
        alembic upgrade head
    to see alembic history
        alembic history 
    to autogenerate based on model
        alembic revision --autogenerate -m "some name here"   
        alembic revision --autogenerate -m "initial create tables"    

Digital ocean 
    using terminal ssh to digital ocean
        ssh ajm@138.197.36.167
        "yes" to fingerprint
        enter password

    Install app
        mkdir noaa-weather-collector
        cd noaa-weather-collector
        virtualenv venv      #make virtual enviroment
        ls -la               #to see folder
        source venv/bin/activate   # to activate enviroment
        deactivate                 # to leave virtual enviroment
        mkdir src                  # make source directory
        cd src                     # change to dir
    generate ssh key
        ssh-keygen -t rsa -b 4096 -C "ajmvfr@gmail.com"
        eval "$(ssh-agent -s)"
        ssh-add ~/.ssh/id_rsa
        cat ~/.ssh/id_rsa.pub
    pull code oeval "$(ssh-agent -s)"nto vm from github
        git clone git@github.com:ajmvfr/NoaaWaterLevelCollector.git .  #make user of space dot to install in current dir
    activate code
        cd ..   to get back to root of app
        source venv/bin/activate   # to activate enviroment
        cd src
        cat requirements.txt   # do this to see requirements
        pip install -r requirements.txt   #install all requirements
    handle error from missing library
        deactivate  # get out of virtual enviroment
        #find library in error and lookup install
        sudo apt install libpq-dev     #this is the issue from this install
        source venv/bin/activate    # back into virtual enviroment
        pip install -r requirements.txt   #try again
    start application
        uvicorn app.main:app    #same as on pc
    create enviroment variables
        export varname=variables  #to set
        unset varname   #to remove
    to see enviroment variables
        printenv 
    to set them in batch
        cd ~ #get back to root
        touch .env  #create empty file  Do not put this in app directory
        vi .env  to maually to it, it usecd ~s export as above
        source .env # to set variables
    to set env variables from a copy of local .env file
        #paste in varables from .env local
        set -o allexport; source /home/ajm/.env; set +o allexport
        vi .profile #this makes the env variables autorun
        sudo reboot  #reboot machine or close terminal
    to deploy db table
        source venv/bin/activate #start virtual server
        cd fastapi  #app dir
        cd src/alembic/versions to see versions 
        alembic upgrade head #to deploy tables  this should be from src folder
