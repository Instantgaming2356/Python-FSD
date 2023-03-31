#
# Patient Management Application

Course-end Project 1 

DESCRIPTION

Many patients visit AB Hospital for a routine health checkup, accidental injuries or any other ailment treatment. Each patient has to register with the hospital if they are visiting the hospital for the first time. So, it gets very difficult for the reception boy Suresh to manage the records of every patient in a logbook manually as if the user has already registered he has to search the patient’s name throughout the book containing thousands of records.

Objective: To develop an application in Django that checks if the patient is already registered and registers the patient if they’re not.

Domain:  Customer Support

Steps to perform:            

Tasks -

    Set up the required tools

 

Tools/Packages
	

Django 1.8

Python 2.7

SQLite
	

The packages are pre-installed in the environment. In case if you want to install any other package then use either apt/pip.

OS Version
	

Ubuntu 16.04 LTS
	

1 GB - 4 GB RAM and 1 - 4 vCPU.

Application port
	

Port 8000 is mapped port 80
	

Application server runs on port 8000 in the virtual machine. This port is forwarded to port 80 publicly -- which is accessible via the live preview of the IDE.

 

     2. Do the following to execute your application

    python manage.py migrate
     
    Click on the build button.
     
    You can view the Live preview of your application by appending /commoninfo in the Live preview URL i.e “<LivePreviewURL>/commoninfo”.
     
    You can visit the registration page by appending /add to the live preview URL i.e. “<LivePreviewURL>/commoninfo/add”.
     
    You can visit the page to check if patient is registered or not by appending /fetch to the live preview URL i.e. “<LivePreviewURL>/commoninfo/fetch”.

 

     3. Use sqlite database in auth_user and create a  model named UserInfo in models.py to store uniqueID and Date Of Birth.

     4. In views.py implement the logic for adding the user data in addUserInfo and for fetching the user data on the basis of uniqueID in fetchUserInfo.

     5. Use any front-end framework to change the layout and design of the application.

    /commoninfo

Consists of two buttons Register and Check.

    /commoninfo/add

 

Consists of user registration form. After adding the required details and clicking on the SUBMIT button it should show successfully added!!

    /commoninfo/fetch

 

Consists of a textbox to enter UID after clicking on SUBMIT it should show patient’s name, Unique ID and DOB.

#

# Password Manager

Course-end Project 2 

DESCRIPTION

Zara is developing a new version of password manager. Earlier, she was using some third-party password manager but she figured out that it can't keep track of all the passwords which has been set for the respective account. As she is very concerned about the security, she decided to develop her own version of the password manager

Objective: To develop a custom password manager using Python

Domain:  Security

Steps to perform:            

    Implement the following design

class BasePasswordManager

    members

        old_passwords: is a list that holds all of the user's past

                           passwords.

                           The last item of the list is the user's current password.

    methods

        get_password method that returns the current password as a string.

 

        is_correct method that receives a string and returns a boolean

             True or False depending on whether the string is equal to

             the current password or not.

 

class PasswordManager

    This class inherits from BasePasswordManager

 

        methods

        set_password method that sets the user's password.

             Password change is successful only if:

                    - Security level of the new password is greater.

                    - Length of new password is minimum 6

 

             However, if the old password already has the highest security level,

             new password must be of the highest security level for a successful password change.

 

        get_level method that returns the security level of the current password.

             It can also check and return the security level of a new password passed as a string.

 

Security levels:

         level 0 - password consists of alphabets or numbers only.

        level 1 - Alphanumeric passwords.

             level 2 - Alphanumeric passwords with special characters.


#
# Python Decorators

Course-end Project 3 

DESCRIPTION

Implement a Python decorator that should take whatever the decorated function returns, and write it to a file in a new line. For the sake of this problem, let us assume that the decorated functions always return a string. The decorator should be named log_message and should write to the file /tmp/decorator_logs.txt.

Objective: To develop a Python decorator

Domain:  Web Development

Steps to perform:            

    Implement the following design

@log_message

def a_function_that_returns_a_string():

      return "A string"

@log_message

def a_function_that_returns_a_string_with_newline(s):

      return "{}\n".format(s)

@log_message

def a_function_that_returns_another_string(string=""):

            return "Another string"
