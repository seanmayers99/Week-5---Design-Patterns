# Sean Mayers
# 11/22/2020
# Week 5 Design Patterns - Facade Design Patterns

""" Used to hide specific information  --> employee personal data   """
class DatabaseFacade():
    
    def __init__(self, provider=None, dbname=None, host=None, user=None, password=None):
        
        self.provider = args[0]
        self.dbname = dbname
        self.host = host
        self.user = user
        self.password = password

    def connect(self):
        DBConnection = None
        # Allows for connection to mysql database
        if self.provider.lower() == 'mysql':
            DBConnection = MySQLConnection.connect('localhost', dbname)
        # Allows for connection to postgres database
        elif self.provider.loewr() == 'postgres':
            DBConnection = PostgresConnection.connect(host, user, password, dbname)

def main():
    db = DatabaseFacade()
    db = DatabaseFacade('mysql', dbname='Employee Personal Data')
    db = DatabaseFacade(provider='postgres', dbname='Employee Personal Data')

    connection = db.connect()