#   PyBase
# A JSON based python database
# by Atlas @https://github.com/AtlasMerc
# This is a Python database that impliments json. No extra
# modules are required.
#
# Note: the .json file must be in the same directory
# that you are running your interpreter from!

import json # for reading JSON file
import os # for cwd

class search(object): # creates the search class

    def __init__(self): # __init__function

        # Commands
        self.SEARCH = {1: 'name', 2: 'description', 3: 'location'}
        self.QUERY = {}
        self.VIEW = {}

        # Errors
        self.interror = "[!] Int error"
        # Loads JSON file
        self.db = None
        # Shows help on startup
        self.help()

    def main(self): # main function

        self.loadb() # loads the database

        print
        print(" MAIN MENU ")
        print

        trigger = None
        search = None

        trigger = (raw_input(":: "))

        trigger = self.valerror(trigger) # calls value error function

        if trigger is False:
            self.main() # loops to the main function
        else:
            try:

                {
                    1: self.search,
                    2: self.query,
                    3: self.view,
                    4: self.help,
                    5: self.delete
                }[trigger]()
                self.main()

            except Exception as e: # for sub-menus
                print(e)


    def search(self): # search function

        print
        print(" SEARCH MENU ")
        print
        print(json.dumps(self.SEARCH, indent=4, sort_keys=True)) # fancy search menu
        print

        t = raw_input(":: ")
        s = raw_input(":: ")

        t = self.valerror(t) # calls value error function
        if t is False:
            return
        else:
            pass

        print
        print("--------------------------------")

        l = 0
        gen = (x for x in self.db if s in x[self.SEARCH[t]]) # quick way to combine for and if statements
        for i in gen:
            print(json.dumps([i[x] for x in i], indent=4, sort_keys=True)) # displays fancy search results
            l = l+1
        else:
            print("--------------------------------")
            print("[*] End of list. %s objects found" %l)

    def query(self): #query function

        data = {}

        name = raw_input("Name:: ")
        location = raw_input("Location:: ")
        description = raw_input("Description:: ")
        quantity = raw_input("Quantity:: ")

        data = {
        "description": description,
        "location": location,
        "name": name,
        "quantity": quantity,
        "ID": None             # blank ID is established later
        }

        self.db.append(data) # appends the current data from the db
        self.modb() # puts the updated data back onto the db


    def view(self): #view function

        l = 0

        print
        print(" VIEW MENU ")
        print

        limit = raw_input("Limit:: ")
        print
        print("--------------------------------")

        limit = self.valerror(limit) # calls value error function
        if limit is False:
            return
        else:
            pass
        try:

            for i in range(limit): # prints limited search
                print(json.dumps([self.db[l]], indent=4, sort_keys=True)) # fancy search
                l = l+1

        except IndexError: # error handeling
            pass

        print("--------------------------------")
        print("[*] End of list. %s objects shown" %l)

    def delete(self): # delete function

        delID = raw_input("ID to delete:: ") # ID to delete

        delID = self.valerror(delID) # calls value error function
        if delID is False:
            return
        else:
            pass

        del self.db[delID] # delets item with ebtered ID from the db
        self.modb() # updates the db

    def help(self): # help function

        print
        print(
"""
PyBase
A JSON based python database
by Atlas @https://github.com/AtlasMerc

1 = Search
2 = Query
3 = View
4 = Help
5 = Delete
"""
        )
        print

    def valerror(self, x): # integer checking function

        try:

            x = int(x)
            return x

        except ValueError: # error handeling
            print(self.interror)
            return False

    def loadb(self): # adds and resets the database

        with open('pydb.json', 'r+') as filedb: # opens db json file
            self.db = json.load(filedb)
            idn = 0
            for a in self.db:                   # assigns ID's
                a["ID"] = idn
                idn = idn + 1
            self.modb()                         # updates the db

    def modb(self): # update function

        with open('pydb.json', 'w') as filedb: # opens db json file
            json.dump(self.db, filedb, indent=4, sort_keys=True) # updates the db

Search = search() # creates the class
Search.main() # runs the script
