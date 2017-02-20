from django.test import TestCase
from main.models import users, code

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        users.objects.create(name = 'name', email='name@com.com', phone = '0123456789', address = 'address')
        user = users.objects.get(pk=1)
        code.objects.create(user = user, code = 'XXXX', show_name = True, show_email = True, show_phone = False, show_address = False)
        code.objects.create(user = user,code = 'YYYY', show_phone = True, show_address = True, show_name = False, show_email = False)
    def test_codes_info(self):
        code1 = code.objects.get(code = 'XXXX')
        code2 = code.objects.get(code = 'YYYY')
        self.assertEqual(code1.name(), 'name')
        self.assertEqual(code1.email(), 'name@com.com')
        self.assertEqual(code1.phone(), False)
        self.assertEqual(code2.phone(), int('0123456789'))
        self.assertEqual(code2.address(), 'address')
