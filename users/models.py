from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.shortcuts import get_object_or_404


GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female')
]


class ProfileManager(models.Manager):
    def get_auth_profile(self, profile, user, *args, **kwargs):
        return get_object_or_404(self, pk=profile, user=user)

    def check_auth_profile(self, user, *args, **kwargs):
        try:
            obj = self.get(user=user)
            if obj:
                return obj
        except Profile.DoesNotExist:
            return None


class User(AbstractUser):
    name = models.CharField(verbose_name="Name of User", blank=True, max_length=255)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25, default="nogi")
    last_name = models.CharField(max_length=25, default="kak u gogi")
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, default=1, choices=GENDER_CHOICES)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    objects = ProfileManager()

    def __str__(self, *args, **kwargs):
        return self.first_name

    def get_absolute_url(self, *args, **kwargs):
        return reverse('profiles-detail', kwargs={'id': self.pk})

    def get_update_url(self, *args, **kwargs):
        return reverse('profiles-update', kwargs={'id': self.pk})

    def get_delete_url(self, *args, **kwargs):
        return reverse('profiles-delete', kwargs={'id': self.pk})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
