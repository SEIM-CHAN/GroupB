from accounts.models import CustomUser
from django.db import models

#スレッドモデル
class Thread(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    #コメントの配列（runserverする度に初期化されてしまうので注意！）
    comments = []

    class Meta:
        verbose_name_plural = 'Thread'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.comments.clear()
    
    def __str__(self):
        return self.title

    def addComments(self, commentModel):
        #コメントの追加
        self.comments.insert(0, commentModel)

    # def addComments(self, changedComment):
    #     self.comments[self.comments.index('a')] = changedComment

    # def removeComments(self, commentModel):
    #     self.comments.pop(0, commentModel)

#コメントモデル
class Comment(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.DO_NOTHING)
    content = models.TextField(verbose_name='本文', blank=True, null=True)
    title = models.IntegerField(verbose_name='タイトル')
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Comment'
    
    def __str__(self):
        return self.content