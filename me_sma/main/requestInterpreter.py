from main.models import code, users
def is_okay(data):
    newcode = code(user = users.objects.get(pk=1))
    if 'show_name' in data:
        newcode.show_name = True
    else:
        newcode.show_name = False
    if 'show_email' in data:
        newcode.show_email = True
    else:
        newcode.show_email = Flase
    if 'show_phone' in data:
        newcode.show_phone = True
    else:
        newcode.show_phone = False
    if 'show_address' in data:
        newcode.show_address = True
    else:
        newcode.show_address = False
    newcode.save()
    url = '/' + newcode.code
    return url
