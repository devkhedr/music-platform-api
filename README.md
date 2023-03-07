# Welcome to Music Platform 
Backend rest API server that provides and handle albums, artists, songs and relations between them with authentication and permissions and testing it.
# Installation and setup

#### Clone the project


```Bash
git clone https://github.com/MohamedKhedr07/music-platform.git
```
#### Run the API server
   - create your virtual environment, and activate it.
   
   - If you run the app for the first time, run the following 2 commands
        - ```Bash
            pip install -r requirements.txt
            python manage.py migrate --run-syncdb
            ```
        then
        - ```Bash
            python manage.py runserver
            ```
        to start the API server.
