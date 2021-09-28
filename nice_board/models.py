from django.db import models
from accounts.models import CustomUser


class NiceThread(models.Model):
    """掲示板モデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', blank=False, null=True, on_delete=models.SET_NULL)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    desc = models.TextField(verbose_name='説明文', max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural= 'nice_thred'

    def __str__(self):
        return self.title


class NiceComment(models.Model):
    """コメントモデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー',blank=True, null=True, on_delete=models.SET_NULL)
    nice_thread = models.ForeignKey(NiceThread, verbose_name='スレッド', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='コメント', null=True, max_length=250)
    ban = models.BooleanField(verbose_name='コメントアウト' ,default=False)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)

    class Meta:
        verbose_name_plural= 'nice_comments'

    def __str__(self):
        return "投稿"
