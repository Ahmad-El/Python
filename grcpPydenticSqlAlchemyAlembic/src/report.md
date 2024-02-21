## From first terminal start server
-   run `make server` or `python reporting_server.py` running server is the same for all tasks.

## From second terminal connect to server 
-   run `make test` or `python reporting_client.py ....` 6 float or integer parameters

-   In second task run file `reporting_client_v2.py ....`
### In third task 
-   start postgresql server
-   change values of .env file write your postgresql server datas 
-   run file `python reporting_client_v3.py ....` to print data and add data to postgres db
-   run `make traitors` or `python reporting_client_v3.py list_traitors` to see list of traitors.

### Third Bonus
-   if there is no alembic files 
    -   initialize alembic `alembic init alembic` to project folder
    -   create revision to `create revision -m'type of changes you want'`
    -   apply new changes `alembic upgrade head`



I hope you can create and use python venv or any other virtual environments...  

##### ***clues***
[venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)

#### Postgresql 
-   host: `localhost`
-   port by default is: `5432`
-   creating user, giving privileges and setting password
```psql
CREATE USER myuser WITH PASSWORD 'mypassword';
CREATE DATABASE mydatabase;
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
```
    