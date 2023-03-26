import sys

class BasePasswordManager:
    
    def __init__(self):
        # Members
        self.oldpasswords = []
        
    # Methods
    def get_password(self):
        if(self.oldpasswords != []):
            return self.oldpasswords[-1]
        else:
            return 'null'
    
    def is_correct(self, confirmpwd):
        
        if(self.oldpasswords == []):
            return 0
        if(self.oldpasswords[-1] == confirmpwd):
            return 1
        else:
            return 0

class PasswordManager(BasePasswordManager):
    
    # Methods
    def get_level(self, pwd):
        
        if(pwd.isalpha() or pwd.isnumeric()):
            return '0'
        elif(pwd.isalnum()):
            return '1'
        else:
            return '2'
        
    def set_password(self, newpassword):
        
        if(len(newpassword) >= 6):
            if(self.oldpasswords == [] or (self.get_level(newpassword) > self.get_level(self.oldpasswords[-1]))):
                self.oldpasswords.append(newpassword)
                print("Password Updated")
            else:
                print("Security Level is equal or less than Current Password.")
        else:
            print("Password Length Minimum Required : 6.")


if __name__ == '__main__':

    ob = PasswordManager()

    while(True):
        
        choice = input('Press any key to continue or "E" for Exit. : ' )
        if(choice == 'e' or choice == 'E'):
            sys.exit()
            
        print('Current Password : ', ob.get_password())
        print('Security Level : ', ob.get_level(ob.get_password()))
        pwd = input("Enter the new password : ")
        if(ob.is_correct(pwd) == 0):
            ob.set_password(pwd)
        else:
            print('Password Unchanged')
