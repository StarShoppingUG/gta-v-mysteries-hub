from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Theory(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='theories/', blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Theories"

    def __str__(self):
        return self.title

class CheatCode(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    platform = models.CharField(max_length=20, choices=[
        ('pc', 'PC'),
        ('xbox', 'Xbox'),
        ('ps', 'PlayStation')
    ])
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.platform})"


class Developer(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='developers/',
        default='developers/default.png',
        blank=True
    )

    def __str__(self):
        return f"{self.name} - {self.role}"

