from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.


class Kitchen(models.Model):
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    checkIn = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Cat(models.Model):

    ISNEUTERED = (
        ('T', 'TRUE'),
        ('F', 'FALSE'),
        ('U', 'UNKNOWN')
    )
    GENDER = (
        ('M', "MALE"),
        ("F", "FEMALE"),
        ("U", "UNKNOWN")
    )

    name = models.CharField(max_length=100, null=False, blank=False)
    breed = models.CharField(max_length=20, null=False, blank=False)
    isNeutered = models.CharField(max_length=1, choices=ISNEUTERED, null=False, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER, null=False, blank=False)
    feature = models.TextField(null=True, blank=True)
    favoriteKitchen = models.ForeignKey(Kitchen, on_delete=models.PROTECT, null=False, blank=False)

    def __str__(self):
        return self.name


class CatPost(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    article = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CatPhoto(models.Model):
    post = models.ForeignKey(CatPost, on_delete=models.CASCADE, null=False, blank=False)
    image = models.ImageField(upload_to='images/', null=False, blank=False)


class CatMention(models.Model):
    pass


class KitchenMention(models.Model):
    pass

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, nickname, phoneNumber, longitude, latitude, address, password=None):
        if not email:
            raise ValueError("Email Needed")
        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            phoneNumber=phoneNumber,
            longitude=longitude,
            latitude=latitude,
            address=address,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):
        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            phoneNumber=0,
            longitude=0,
            latitude=0,
            address=0,
            password=password
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    objects = UserManager()

    email = models.EmailField(max_length=255, unique=True)
    nickname = models.CharField(max_length=20, null=False, blank=False, unique=True)
    phoneNumber = models.IntegerField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to='images/user/', null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=100, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']