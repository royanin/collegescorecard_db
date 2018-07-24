#This file is necessary if you are using the mysql server. Copy this file into instances.py, and replace the DB_USER etc. variables
#with what you have for your mysql user and databases. Also, please refer to the README.
ENV_VAR = {
    'DB_USER' : 'YOUR_USER',
    'PASSWD': 'YOUR_PASSWORD',
    'DB_1' : 'YOUR_DB1', #This stores the "static" data -- e.g., the information coming from the CollegeScoreCard.ed.gov 
    'DB_2' : 'YOUR_DB2' #This stores the data generated from the app (essentially, keeps a copy of the messages sent from the website)
}
