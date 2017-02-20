from main import secrets
from baseconv import BaseConverter
#get the used codes from the database
dummy_dict = {}

""""
The baseconv is a module integrated into django. Authors and information of usage on:
https://github.com/semente/python-baseconv
The letters are chosen based on crockford to have an url friendly characters and readable human friendly urls, for more about crockford:
http://www.crockford.com/wrmg/base32.html """

base32 = BaseConverter('0123456789ABCDEFGHJKMNPQRSTVWXYZ')

def available(agn, codes_dict = dummy_dict):
    """Author :Mohammed Salman
        Contact: m.salman@zinkki.com
        Metropolia University of applied science
        This function takes an integer and checks it against the dictionary of used numbers in the database. Dict should be the dictionary imported from the database.
        It will return true if the number is not found in the database, and false if it is found.
     """
    #The minimum agn should be 4 characters. 3 characters should be reserved for api orders.
    if (len(str(agn))>3):
        if not(agn in codes_dict):
            #The code is 4 characters and it is taken so:
            return True
    else:
        return False

def generate_agn(codes_dict, user, upperlimit=1048575):
    """Author :Mohammed Salman
        Contact: m.salman@zinkki.com
        Metropolia University of applied science
        Takes a codes dictionary and a user index and generate a new Auto Generated Number, it returns a tuple.
        The first item of the tuple is the random number in decimal, the second item in the tuple is the encoded base32 number.

     """
    rand = secrets.randbelow(upperlimit)
    while not(available(rand)):
        rand = secrets.randbelow(upperlimit)
        print(rand, ' is reserved')
    else:
        encoded = base32.encode(rand)
        save_agn(encoded, user)
        return rand, encoded


def save_agn(agn, user, codes_dict = dummy_dict):
    codes_dict[agn] = user
#Test for the generated codes
for i in range(50):
    print(generate_agn(dict, 66))
print (dummy_dict)
