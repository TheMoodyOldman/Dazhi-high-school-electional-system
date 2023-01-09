from django.db import models

# Create your models here.
class Election(models.Model):
    # 選舉名稱
    name = models.CharField('投票名稱', max_length=50)

    # 簡述選舉內容
    content = models.CharField('內容概述', max_length=200)

    # 選舉建立時間
    date_created = models.DateField('建立時間', auto_now_add=True)

    # 選舉開始時間
    date_start = models.DateField('投票開始時間')


class HouSyuanRen(models.Model):
    #  candidate
    # 這個候選人屬於哪一場選舉
    election_id = models.IntegerField()

    # 候選人姓名
    first_name = models.CharField('姓氏', max_length=12)
    name = models.CharField('名稱', max_length=12)

    # 候選人出生年月日
    birth = models.DateField('出生年月日')

    # 候選人性別
    gender = models.CharField('性別', max_length=5)

    # 候選人黨籍
    party = models.CharField('黨籍', max_length=20)

    # 候選人學歷
    academy = models.TextField('學歷', max_length=100)

    # 候選人資歷
    seniority = models.TextField('資歷', max_length=150)

    # 候選人政見
    politics = models.TextField('政見', max_length=10000)

    # 當前得票
    poll = models.IntegerField(default=0)



