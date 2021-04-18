#class to identify data type of an object
#Camel casing the class name

class DataType():

    #class initialize method
    def __init__(self,number):
        self.number=number

    #Method to check for integer data type
    def isint(self):
        num = self.number
        if num.isdigit():
            return True
        else:
            return False

    #Method to check for float data type
    def isfloat(self):
        num = self.number
        if num.isdigit():
            return False
        else:
            try:
                num = float(num)
                return True
            except:
                return False

    #method to check for string data type
    def isstring(self):
        num = self.number
        if num.isdigit():
            return False
        else:
            try:
                num = float(num)
                return False
            except:
                try:
                    num = complex(num)
                    return False
                except:
                    return True
    #method to check for complex data type
    def iscomplex(self):
        num = self.number
        if num.isdigit():
            return False
        else:
            try:
                num = float(num)
                return False
            except:
                try:
                    num = complex(num)
                    return True
                except:
                    return False

    #string representation of print call
    def __str__(self):
        return f'{self.number}'

    #telling del function what to print when an object is deleted
    def __del__(self):
        print('The object is deleted')