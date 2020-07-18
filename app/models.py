from django.conf import settings
from django.db import models
from datetime import datetime
from django.utils import timezone


class User(models.Model):
    class Meta:
        db_table = 'user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자 목록'

    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    point = models.IntegerField(default=0)
    image = models.ImageField(upload_to="user")


class Recycle(models.Model):
    class Meta:
        db_table = 'recycle'
        verbose_name = '재활용'
        verbose_name_plural = '재활용 목록'

    recycleId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='userId', default=0)
    image = models.ImageField(upload_to="recycle")
    time = models.DateTimeField(default=datetime.now)
    lat = models.FloatField(default=0.0)
    lon = models.FloatField(default=0.0)


class RecycleItem(models.Model):
    class Meta:
        db_table = 'recycleItem'
        verbose_name = '재활용 아이템'
        verbose_name_plural = '재활용 아이템 목록'

    CATEGORIES = (
        (0, 'paper'),
        (1, 'can'),
        (2, 'metal'),
        (3, 'bottle'),
        (4, 'plastic'),
        (5, 'styrofoam'),
        (6, 'vinyl'),
        (7, 'lamp'),
        (8, 'battery')
    )

    itemId = models.AutoField(primary_key=True)
    recycleId = models.ForeignKey(Recycle, on_delete=models.DO_NOTHING, db_column='recycleId', default=0, related_name='items')
    category = models.SmallIntegerField(choices=CATEGORIES, default=1)
    count = models.IntegerField(default=0)


class Rating(models.Model):
    class Meta:
        db_table = 'rating'
        verbose_name = '평가'
        verbose_name_plural = '평가 목록'

    ratingId = models.AutoField(primary_key=True)
    recycleId = models.ForeignKey(Recycle, on_delete=models.DO_NOTHING, db_column='recycleId', default=0)
    good = models.IntegerField(default=0)
    bad = models.IntegerField(default=0)


class BadReason(models.Model):
    class Meta:
        db_table = 'badReason'
        verbose_name = '코멘트'
        verbose_name_plural = '코멘트 목록'

    badReasonId = models.AutoField(primary_key=True)
    ratingId = models.ForeignKey(Rating, on_delete=models.DO_NOTHING, db_column='ratingId', default=0)
    reason = models.CharField(max_length=200)
