from django.db import models
from django.urls import reverse
from django.contrib.auth import  get_user_model

# Create your models here.
class ToDo_obj(models.Model):
    STATUS_CHOICES = [
        ('O', 'Open'),
        ('C', 'Close'),
    ]

    title = models.CharField(max_length=200)
    explaination = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='O'
    )
    
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home")
    