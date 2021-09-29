from django.db import models
from django.urls import reverse
from accounts.models import CustomUser

# Create your models here.
class Thread(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    subject = models.CharField(max_length=50)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    def __str__(self):
        return self.subject

class Comment(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.PROTECT)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='threads')
    name = models.CharField(max_length=15)
    message = models.CharField(max_length=100)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)

    def __str__(self):
        title = str(self.thread) + "/" + str(self.created_at)
        return title