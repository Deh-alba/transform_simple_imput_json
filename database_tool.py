import pymongo
import urllib.parse


#class for configure and use database
class databaseTool:
    
    def __init__(self):    
        self.client = pymongo.MongoClient("mongodb+srv://aalba:"+urllib.parse.quote("XXX")+"@cluster0.r96e6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        #self.db = self.client.test
        #self.db = self.client.gettingStarted
        #self.logs = None
        self.db = self.client.gettingStarted
        self.logs = self.db.logs

    
    def test_database(self):
        print(self.client.list_database_names())
        
    def test_create_collection(self):
        self.db = self.client.gettingStarted
        self.logs = self.db.logs


    def insert_data(self,data):
        #mydict = { "name": "John", "address": "Highway 37" }
        x = self.logs.insert_many(data)
        #self.mydb = self.myclient["mydb"]
