0. These scripts should work with sqlite and mysql (not tested with postgre, for example).
For trying it out the first time, start with sqlite (uncomment the sqlite-scpecific lines in 
config.py). It'll create app.db and app_data.db in the top-level folder.
For working with mysql:
    a. Comment out the sqlite related lines in config.py, and uncomment the mysql related lines
    b. You need to include the credentials in the instances.py as a dictionary (a fake 
    fake_instances.py is included).
    c. Create a new user in your mysql server, create new databases as you name them in your
    instances.py, and grant the new user all access on those databases

1. Running the csv_to_db.py should create the appropriate tables in the database. If using sqilte,
copy the app.db and app_data.db into the data folder of the collegescorecard app. If using mysql, make
sure that the collegescorecard app has the right credentials available to access the tables you just
created.
