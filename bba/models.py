from django.db import models
from django.urls import reverse

# Create your models here.
class Thread(models.Model):
    subject = models.CharField(max_length=50)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    def __str__(self):
        return self.subject

class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, null=True, related_name='threads')
    name = models.CharField(max_length=15)
    message = models.CharField(max_length=100)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)

    def __str__(self):
        title = str(self.thread) + "/" + str(self.created_at)
        return title

    def get_absolute_url(self):
    # get_absolute_urlで遷移先を指定
        return reverse("bba:comment", args={self.pk})