def log_message3(fn):

        def wrapper(*args):   
                f = open('decorator_logs.txt', 'a+')
                f.write(fn(*args))  
                f.write("\n")
                f.close()
                return fn
        
        return wrapper

@log_message3
def a_function_that_returns_a_string():

    return "A string"

@log_message3
def a_function_that_returns_a_string_with_newline(s):

    return "{}\n".format(s)

@log_message3
def a_function_that_returns_another_string(string=""):

    return "Another string"


if __name__ == '__main__':
        a_function_that_returns_a_string()
        a_function_that_returns_a_string_with_newline("Hello World")
        a_function_that_returns_another_string()
        

