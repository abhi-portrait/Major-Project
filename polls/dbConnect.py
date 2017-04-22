#  Created by Harshit Bhat on 13/03/17.
#  Copyright 2017 Harshit Bhat. All rights reserved.

import MySQLdb

class Connect:
    def __init__(self,username,password,dbName):
        self.username = username
        self.password = password
        self.dbName = dbName
        self.serverName = '127.0.0.1'

    def connectToDb(self):
        cursor = None
        try:
            db = MySQLdb.connect(self.serverName,self.username,self.password,self.dbName)
            cursor = db.cursor()
        except:
            print ("Cannot connect to server " + self.serverName + " or " + "username or password or name of database are wrong")

        return cursor
