#1st Assignment by Aung Kaung Khant

class MiniBank():
    storage:dict = {}

    def option(self):
        option:int = int(input("Press 1 to login\nPress 2 to register\nYour Option:"))

        if option == 1:
            self.login()
        
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

        print("Total data:", self.storage)

    def login(self):
        print("----------Login----------")
        username:str = input("Please enter username:")
        passcode:int = int(input("Please enter passcode:"))
        flag = self.exist(username, passcode)

        if flag:
            print("Success")

            while True:
                flag2 = self.menu(username)

                if flag2 == False:
                    break

        else:
            print("Incorrect username or password")

    def exist(self, username, passcode):
        length:int = self.count()

        for i in range(1, length):

            if self.storage[i]["username"] == username and self.storage[i]["passcode"] == passcode:
                return True

        return False

    def register(self):
        print("----------Register----------")
        id = self.count()
        username:str = input("Please enter username:")
        passcode:int = int(input("Please enter passcode:"))
        passcode2:int = int(input("Please enter passcode again to confirm:"))
        amount:int = int(input("Please enter amount:"))

        if passcode == passcode2:
            flag = self.exist(username, passcode)

            if not flag:
                info = {id:{"username":username, "passcode":passcode, "amount":amount}}
                self.storage.update(info)
                print("Success")
                print("Total data:",self.storage)

            else:
                print("Username already exists.\n")

        else:
            print("Passcodes are not the same.\n")
        
    def count(self):
        length = len(self.storage)
        return length + 1

    def transfer(self, username, r_username, amount):
        length:int = self.count()

        for i in range(1, length):

            if self.storage[i]["username"] == username:
                self.storage[i]["amount"] = self.storage[i]["amount"] - amount

            elif self.storage[i]["username"] == r_username:
                self.storage[i]["amount"] = self.storage[i]["amount"] + amount

    def withdraw(self, username, amount):
        length:int = self.count()

        for i in range(1, length):

            if self.storage[i]["username"] == username:
                self.storage[i]["amount"] = self.storage[i]["amount"] - amount

    def update(self, username):
        menu:int = int(input("Press 1 to update amount\nPress 2 to update username\nPress 3 to change passcode\nPress 0 to exit\nYour Option:"))
        
        if menu == 1:
            amount:int = int(input("Amount:"))
            self.changeAmount(username, amount)

        elif menu == 2:
            username2 = input("New Username:")
            self.changeInfo(username, "username", username2)

        elif menu == 3:
            passcode = int(input("Old Passcode:"))
            passcode2 = int(input("New Passcode:"))

            if passcode == passcode2:
                self.changeInfo(username, "passcode", passcode2)
            
            else:
                print("Not the same.\n")

        else:
            return False

        print("Total data:", self.storage)

    def changeAmount(self, username, data):
        length:int = self.count()

        for i in range(1, length):

            if self.storage[i]["username"] == username:
                self.storage[i]["amount"] = data

    def changeInfo(self, username, data, data2):
        length:int = self.count()

        for i in range(1, length):

            if self.storage[i]["username"] == username:
                self.storage[i][data] = data2

if __name__ == "__main__":
    miniBank:MiniBank = MiniBank()

    while True:
        
        try:
            miniBank.option()
        except:
            print("Error")