from django.db import models

# Create your models here.

class HouSyuanRen(models.Model):

    # 候選人姓名
    first_name = models.CharField('姓', max_length=12)
    name = models.CharField('名', max_length=12)

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