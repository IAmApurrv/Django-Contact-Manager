from django.db import models

# Create your models here.

class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
	nickname =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	mobileNumber = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	pincode =  models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.name}")





# from django.db import models
# import django.utils.timezone as timezone


# class Contact(models.Model):
#     created_at = models.DateTimeField(default=timezone.now)
#     name = models.CharField(max_length=50)
#     nickname = models.CharField(max_length=50)
#     email = models.CharField(max_length=100)
#     mobileNumber = models.CharField(max_length=15)
#     address = models.CharField(max_length=100)
#     city = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     pincode = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name
