from main import secrets
from baseconv import BaseConverter

""""
The baseconv is a module integrated into django. Authors and information of usage on:
https://github.com/semente/python-baseconv
The letters are chosen based on crockford to have an url friendly characters and readable human friendly urls, for more about crockford:
http://www.crockford.com/wrmg/base32.html """

base32 = BaseConverter('0123456789ABCDEFGHJKMNPQRSTVWXYZ')

def FixLength(agn):
    """Author :Mohammed Salman
        Contact: m.salman@zinkki.com
        Metropolia University of applied science
        This function takes an integer and checks it against the dictionary of used numbers in the database. Dict should be the dictionary imported from the database.
        It will return true if the number is not found in the database, and false if it is found.
     """
    #The minimum agn should be 4 characters. 3 characters should be reserved for api orders.
    if (len(str(agn))<4):
        diff = 4 - len(str(agn))
        new_agn = (str('0') * diff) + str(agn)
        return new_agn
    else:
        return str(agn)

def GenerateAgn(upperlimit=1048575):
    """Author :Mohammed Salman
        Contact: m.salman@zinkki.com
        Metropolia University of applied science
        Takes a codes dictionary and a user index and generate a new Auto Generated Number, it returns a string.
        The first item of the tuple is the random number in decimal, the second item in the tuple is the encoded base32 number.

     """
    rand = secrets.randbelow(upperlimit)
    encoded = str(base32.encode(rand))
    encoded = FixLength(encoded)
    return encoded
