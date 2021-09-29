from accounts.models import CustomUser
from django.db import models

# Create your models here.
class Board(models.Model):

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー',on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル',max_length=40)
    created_at = models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    updated_at =models.DateTimeField(verbose_name='更新日時',auto_now=True)

    class Meta:
        verbose_name_plural = 'board'
    def __str__(self):
        return self.title 
    
class Coment(models.Model):

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー',on_delete=models.PROTECT)
    coment = models.CharField(verbose_name='コメント',max_length=100)
    board = models.ForeignKey(Board, verbose_name='スレッド', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    updated_at =models.DateTimeField(verbose_name='更新日時',auto_now=True)

    class Meta:
        verbose_name_plural = 'coment'
    def __str__(self):
        return self.coment








