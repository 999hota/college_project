from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib import admin

class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user
 

class User(AbstractBaseUser, PermissionsMixin):
	# user field
	username = models.CharField(max_length=100, unique=True, null=True,blank=True)
	password = models.TextField(null=True,blank=True)
	email = models.EmailField(null=True,blank=True)
	first_name = models.CharField(max_length=100, null=True)
	last_name = models.CharField(max_length=100, null=True)
	
	is_staff = models.BooleanField(default=False)
	created_on = models.DateField(auto_now_add=True)
	is_active = models.BooleanField(default=True)
	otp = models.CharField(max_length=255, null=True, blank=True)

	contact_number = models.CharField(max_length=10, null=True)
	USERNAME_FIELD = "username"	
	REQUIRED_FIELDS = ["email","password"]

	objects = MyAccountManager()

	def save(self, *args, **kwargs):
		super(User, self).save(*args, **kwargs)

	def create_new_token():
		pass
		
	def get_full_name(self):
		full_name = None
		if self.first_name or self.last_name:
			full_name = self.first_name + " " + self.last_name
		return full_name if full_name else self.email

	@property
	def full_name(self):
		return self.get_full_name()

class StudentDetails(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
	cv=models.ImageField(upload_to="cv/", null=True, blank=True)
	cgpa = models.CharField(max_length=255, null=True, blank=True)
	tenth_marks=models.CharField(max_length=255, null=True, blank=True)
	twelveth_marks=models.CharField(max_length=255, null=True, blank=True)
	dob=models.CharField(max_length=255, null=True, blank=True)
	skills=models.CharField(max_length=255, null=True, blank=True)
	coding_langs=models.CharField(max_length=255, null=True, blank=True)
	address=models.CharField(max_length=255, null=True, blank=True)
	pan=models.CharField(max_length=255, null=True, blank=True)
	aadhaar=models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return self.aadhaar

class Jobs(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True)

	package= models.CharField(max_length=255, null=True, blank=True)

	company = models.CharField(max_length=255, null=True, blank=True)

	openings = models.CharField(max_length=255, null=True, blank=True)

	profile = models.CharField(max_length=255, null=True, blank=True)

	start_date = models.CharField(max_length=255, null=True, blank=True)

	end_date = models.CharField(max_length=255, null=True, blank=True)

	minimum_cgpa = models.CharField(max_length=255, null=True, blank=True)


	def __str__(self):
		return self.title

STATUS_S=(
		('NA','NA'),
		('in_process','in_process'),
		('selected','selected'),
		('failed','failed')
	)
class AppliedJobs(models.Model):
	
	user=models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True )
	job=models.ForeignKey(Jobs,on_delete=models.CASCADE, null=True, blank=True )
	result=models.CharField(max_length=255, null=True, blank=True )
	status=models.CharField(max_length=255, choices=STATUS_S, default='NA' )
