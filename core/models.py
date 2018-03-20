from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    # name = models.CharField(max_length=255, blank=True)
    # profile_name = models.CharField(max_length=255, unique=True, default="NewUser")
    # password = models.CharField(max_length=255)
    # email = models.CharField(max_length=255)
    # icon = models.ImageField(null=True)

    def __str__(self):
        return self.username
