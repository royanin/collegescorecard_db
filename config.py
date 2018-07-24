import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#Uncomment the following line and comment out the line above if using mysql
#SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@localhost/{}'.format(ENV_VAR['DB_USER'],ENV_VAR['PASSWD'],ENV_VAR['DB_1'])
SQLALCHEMY_BINDS = {
    'message' : 'sqlite:///' + os.path.join(basedir, 'app_data.db')
    #Uncomment the following line and comment out the line above if using mysql
    #'message':      'mysql://{}:{}@localhost/{}'.format(ENV_VAR['DB_USER'],ENV_VAR['PASSWD'],ENV_VAR['DB_2'])    
}

