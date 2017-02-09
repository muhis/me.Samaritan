import secrets
from baseconv import BaseConverter
dummy_dict = {}
""""
The baseconv is a module integrated into django. Authors and information of usage on:
https://github.com/semente/python-baseconv
The letters chosen is based on crockford to have an url friendly characters and readable human friendly urls, for more about crockford:
From http://www.crockford.com/wrmg/base32.html """

base32 = BaseConverter('0123456789ABCDEFGHJKMNPQRSTVWXYZ')
#get the used codes from the database
def is_free(agn, codes_dict = dummy_dict):
    """Author :Mohammed Salman
        Contact: m.salman@zinkki.com
        Metropolia University of applied science
        This function takes an integer and checks it against the dictionary of used numbers in the database. Dict should be the dictionary imported from the database.
        It will return true if the number is not found in the database, and false if it is found.
     """
    if not(agn in codes_dict):
        return True
    else:
        return False
def generate_agn(codes_dict, user, upperlimit=1048575):
    """Author :Mohammed Salman
        Contact: m.salman@zinkki.com
        Metropolia University of applied science
        Takes a codes dictionary and a user index and generate a new Auto Generated Number, it returns a tuple, the first item is True if it succeed
        Second item is the random number generated. Third item is the base32 number will be used as the url later.
     """
    rand = secrets.randbelow(upperlimit)
    while not(is_free(rand)):
        rand= secrets.randbelow(upperlimit)
        print(rand, ' is reserved')
    else:
        encoded = base32.encode(rand)
        save_agn(encoded, user)
        return True , rand, encoded
def save_agn(agn, user):
    codes_dict[rand] = user

for i in range(50):
    print(generate_agn(dict, 66))
