import sqlalchemy as db

class DB(object):

    def __init__(self, dbpath):
        self.dbpath = dbpath
        self.init_db()

    def init_db(self):
        engine = db.create_engine('sqlite:///{}.sqlite'.format(self.dbpath))
        self.connection = engine.connect()
