#3rd Assignment by Aung Kaung Khant

try:
    import pymongo
    url = "mongodb+srv://aungkaungkhant:AungKaungKhant@cluster0.tmba9.mongodb.net/mini-banking-system?retryWrites=true&w=majority"
    connection = pymongo.MongoClient(url)
    database = connection["mini-banking-system"]
    collection = database["User Info"]

except:
    print("Cannot connect at the moment.")

import random

class MiniBank():
    storage = {}

    def get(self):
        for i in collection.find():
            _id = i['_id']
            username = i['username']
            passcode = i['passcode']
            amount = i['amount']
            data = {_id:{'username':username, 'passcode':passcode, 'amount':amount}}
            self.storage.update(data)

        print("Your data: ", self.storage)

    def option(self):
        option:int = int(input("Press 1 to login\nPress 2 to register\nYour Option:"))

        if option == 1:
            self.loginInput()
        
        elif option == 2:
            self.register()

    def menu(self, username):
        menu:int = int(input("Press 1 to transfer\nPress 2 to withdraw\nPress 3 to update user info\nPress 0 to exit\nYour Option:"))
        if menu == 1:
            r_username = input("Please enter username to transfer:")
            amount:int = int(input("Please enter amount to tranfer:"))
            self.transfer(username, r_username, amount)

        elif menu == 2:
            amount:int = int(input("Please enter amount to withdraw:"))
            self.withdraw(username, amount)

        elif menu == 3:

            while True:
                flag = self.update(username)

                if flag == False:
                    break

        else:
            return False

        self.get()

    def loginInput(self):
        print("----------Login----------")
        username:str = input("Please enter username:")
        passcode:int = int(input("Please enter passcode:"))
        self.login(username, passcode)

    def login(self, username, passcode):
        flag = self.check(username, passcode)

        if flag:
            print("\nSuccess\n")

            while True:
                flag2 = self.menu(username)

                if flag2 == False:
                    break

        else:
            print("\nIncorrect username or password\n")

    def exist(self, username):
        for i in self.storage:
            if username == self.storage.get(i)['username']:
                return True

        return False

    def check(self, username, passcode):
        for i in self.storage:
            if username == self.storage.get(i)['username'] and passcode == self.storage.get(i)['passcode']:
                return True

        return False

    def register(self):
        print("----------Register----------")
        username:str = input("Please enter username:")
        passcode:int = int(input("Please enter passcode:"))
        passcode2:int = int(input("Please enter passcode again to confirm:"))
        amount:int = int(input("Please enter amount:"))

        if passcode == passcode2:
            flag = self.exist(username)

            if not flag:
                randomNum = random.randint(000000,999999)
                info = {"_id":randomNum, "username":username, "passcode":passcode, "amount":amount}
                collection.insert_one(info)
                print("\nSuccess\n")
                self.get()
                self.login(username, passcode)
                
            else:
                print("\nUsername already exists.\n")

        else:
            print("\nPasscodes are not the same.\n")
        
    def transfer(self, username, r_username, amount):
        if username == r_username:
            print("\nSame username...\n")

        else:
            query = {"username":username}
            data = collection.find(query)
            for i in data:
                oldAmount = i['amount']
                oldAmountDict = {'amount': i['amount']}
            newAmount = {'$set': {'amount': oldAmount-amount}}
            collection.update_one(oldAmountDict, newAmount)

            query2 = {"username":r_username}
            data2 = collection.find(query2)
            for j in data2:
                oldAmount2 = j['amount']
                oldAmountDict2 = {'amount': j['amount']}
            newAmount2 = {"$set": {'amount': oldAmount2+amount}}
            collection.update_one(oldAmountDict2, newAmount2)

    def withdraw(self, username, amount):
        query = {"username":username}
        data = collection.find(query)
        for i in data:
            oldAmount = i['amount']
            oldAmountDict = {'amount': i['amount']}
        newAmount = {'$set': {'amount': oldAmount-amount}}
        collection.update_one(oldAmountDict, newAmount)

    def update(self, username):
        menu:int = int(input("Press 1 to update amount\nPress 2 to update username\nPress 3 to change passcode\nPress 0 to exit\nYour Option:"))
        
        if menu == 1:
            amount:int = int(input("Amount:"))
            self.changeAmount(username, amount)

        elif menu == 2:
            username2 = input("New Username:")
            flag = self.exist(username2)

            if not flag:
                self.changeUsername(username, username2)

            else:
                print("This username exists...")

        elif menu == 3:
            passcode = int(input("Old Passcode:"))
            flag = self.check(username, passcode)
            
            if flag:
                passcode2 = int(input("New Passcode:"))

                if passcode != passcode2:
                    self.changePassword(username, passcode2)
                
                else:
                    print("\nSame Passcode...\n")
            
            else:
                print("Wrong Passcode...")
                return False

        else:
            return False

        self.get()

    def changeAmount(self, username, amount):
        query = {"username":username}
        data = collection.find(query)
        for i in data:
            oldAmountDict = {'amount': i['amount']}
        newAmount = {'$set': {'amount': amount}}
        collection.update_one(oldAmountDict, newAmount)

    def changeUsername(self, username, data):
        query = {"username": username}
        newQuery = {"$set": {"username": data}}
        collection.update_one(query, newQuery)

    def changePassword(self, username, passcode):
        query = {"username":username}
        data = collection.find(query)
        for i in data:
            oldPasscode = {'passcode': i['passcode']}
        newPasscode = {'$set': {'passcode': passcode}}
        collection.update_one(oldPasscode, newPasscode)

if __name__ == "__main__":
    miniBank:MiniBank = MiniBank()

    miniBank.storage = {}
    for i in collection.find():
        _id = i['_id']
        username = i['username']
        passcode = i['passcode']
        amount = i['amount']
        data = {_id:{'username':username, 'passcode':passcode, 'amount':amount}}
        miniBank.storage.update(data)

    print("Your data: ", miniBank.storage)

    while True:
    
        try:
            miniBank.option()
        except:
            print("Error")