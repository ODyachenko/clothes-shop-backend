from django.db import models
# Create your models here.
# class UserAccountManager(BaseUserManager):
#     def create_user(self, first_name, last_name, email, passwword=None):
#         if not email:
#             raise ValueError('Users must have an email address')

#         email = self.normalize_email(email)
#         user = self.model(email=email, first_name=first_name, last_name=last_name)

#         user.set_password(passwword)
#         user.save()

#         return user

#     # def create_superuser():


# class UserAccount(AbstractBaseUser, PermissionsMixin):
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.EmailField(unique=True)

#     objects = UserAccountManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']

#     def get_first_name(self):
#         return self.first_name

#     def get_last_name(self):
#         return self.last_name

#     def __str__(self):
#         return self.email

# class CustomUser(AbstractUser):
#     age = models.PositiveSmallIntegerField()
#     bio = models.TextField(max_length=500)