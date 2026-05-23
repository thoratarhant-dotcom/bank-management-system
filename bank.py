class Bank:
    total_account=0
    def __init__(self,name):
        self.name=name
        self.Accounts=[]
    def createAccount(self,account):
        f=0
        for i in self.Accounts:
            if i.account_num==account.account_num:
                print("Account Already Exists!")
                f=1
                return
        if f==0:
            self.Accounts.append(account)
            Bank.total_account+=1
            print(f"Account created successfully by the name {account.name}")

    def findAccount(self,AccNum):
        f=0
        for i in self.Accounts:
            if i.account_num==AccNum:
                f=1
                return i
        
        if f==0:
            return None

    def deleteAccount(self,AcntNum):
        f=0
        for i in self.Accounts:
            if i.account_num==AcntNum:
                self.Accounts.remove(i)
                f=1
                print(f"Account with name {i.name} deleted from {self.name} bank.")
                break
        if f==0:
            print("No such account exists!")

print("Yes")