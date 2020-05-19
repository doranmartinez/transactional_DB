# Database class that implements a DIY database with CRUD capabilities for integers

class Database:

    def __init__(self):
        self.integers = {}

    def SET(self, name, value):
        try:
            self.integers[name] = value
        except:
            print("Error Setting Value to Database: " + str(Exception))
            return False

    def GET(self, name):
        try:
            print(self.integers[name])
        except:
            print("NULL")
            return False

    def UNSET(self, name):
        try:
            del self.integers[name]
        except:
            print("Error Unsetting Value from Database: " + str(Exception))
            return False
        
    def NUMWITHVALUE(self, value):
        try:
            count = 0
            for item in self.integers.values():
                if item == value:
                    count += 1
            print(count)
        except:
            print("Error Counting Num With Value from Database: " + str(Exception))