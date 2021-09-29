from accounts.models import CustomUser
from django.db import models


class Threads(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField('タイトル', max_length=200, blank=False)
    #メッセージ
    message = models.TextField('メッセージ', blank=False)
    #登録日時
    pub_date = models.DateTimeField('登録日時', auto_now_add=True, editable=False)

    class Meta:
        verbose_name_plural = 'Threads'

    def __str__(self):
        return self.title

class Comments(models.Model):

    thread = models.ForeignKey(Threads, verbose_name='スレッド', on_delete=models.PROTECT)
    #メッセージ
    message = models.CharField('メッセージ', max_length=200, blank=False)
    #登録日時
    pub_date = models.DateTimeField('登録日時', auto_now_add=True, editable=False)

    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.message