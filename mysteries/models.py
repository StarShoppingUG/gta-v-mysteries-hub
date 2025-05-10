from django.db import models

class Theory(models.Model):
    category = models.CharField(max_length=20, choices=[
            ('team', 'Team'),
            ('community', 'Community')
        ], default='community')
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='theories/', default='theories/default.png')
    username = models.CharField(max_length=100, blank=True)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Theories"

    def __str__(self):
        return self.title

class CheatCode(models.Model):
    code = models.CharField(max_length=100)
    platform = models.CharField(max_length=20, choices=[
        ('pc', 'PC'),
        ('xbox', 'Xbox'),
        ('ps', 'PlayStation')
    ])
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} ({self.description})"


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

