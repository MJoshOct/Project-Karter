from django.db import models

# Create your models here.
class signin(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
   

    
class createacc (models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(null=False, blank=False)
    password = models.TextField()

    def __str__(self) -> str:
        return self.fullname



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    contact_address = models.TextField(blank=True, null=True)

    def _str_(self):
        return self.full_name if self.full_name else self.user.username
