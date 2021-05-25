from db import DB

class Hello(DB):

    def __init__(self, dbpath="local"):
        super().__init__(dbpath)
    
    def get_instance(self):
        return self.connection

if __name__ == '__main__':
    h = Hello()
    print(h.get_instance())
