
from django.db import models
from django.conf import settings
class Complaint(models.Model):
    LEVEL_CHOICES = (('student','Student'),('staff','Staff'),('security','Security'))
    filer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    access_level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='student')
    resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
