from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    
    def register(self):
        self.save()
        # self.first_name()


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False
    
    @staticmethod
    def get_customer_by_password(password):
        try:
            return Customer.objects.filter(password = password)
        except:
            return False

    



    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False
    
     