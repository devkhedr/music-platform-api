# Welcome to Music Platform 
Backend rest API server that provides and handle albums, artists, songs and relations between them with authentication and permissions and testing it.
# Installation and setup

#### Clone the project


```Bash
git clone https://github.com/MohamedKhedr07/music-platform.git
```
#### Run the API server

   - You should have python poetry installed on your local machine (poetry is a python package manager) [installing tutorial](https://python-poetry.org/docs/)
   - If you run the app for the first time after cloning, run the following 2 commands
        - ```Bash
            poetry update
            poetry run python musicplatform/manage.py migrate --run-syncdb
            ```
        then
        - ```Bash
            poetry run python musicplatform/manage.py runserver
            ```
        to start the API server.
