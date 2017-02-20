from django.db import models

# Create your models here.
class users(models.Model):
    name = models.TextField()
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length = 250)
    def __str__(self):
        return "%s: Number(%s), Email(%s), address(%s)" % (self.name, self.phone, self.email, self.address)
class code(models.Model):
    user = models.ForeignKey(users , on_delete = models.CASCADE)
    code = models.CharField(max_length = 250)
    show_name = models.BooleanField()
    show_email = models.BooleanField()
    show_phone = models.BooleanField()
    show_address = models.BooleanField()
    def name(self):
        if self.show_name:
            return self.user.name
        else:
            return False
    def phone(self):
        if self.show_phone:
            return self.user.phone
        else:
            return False
    def email(self):
        if self.show_email:
            return self.user.email
        else:
            return False
    def address(self):
        if self.show_address:
            return self.user.address
        else:
            return False
