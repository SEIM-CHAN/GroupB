from re import template
from django.core.checks import messages
from django.db import models
from accounts.models import CustomUser
from django.utils import timezone
# Create your models here.
class Thread(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', blank=False, null=True, on_delete=models.SET_NULL)
    title = models.CharField(verbose_name='タイトル', null=True, max_length=40)
    exp = models.TextField(verbose_name='説明文', max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)

    class Meta:
        verbose_name_plural= 'thread'

    def __str__(self):
        return self.title
        
class Comment(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー',blank=True, null=True, on_delete=models.SET_NULL)
    thread = models.ForeignKey(Thread, verbose_name='スレッド', on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='コメント', max_length=250)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)

    class Meta:
        verbose_name_plural= 'comment'

    def __str__(self):
        return self.comment
    