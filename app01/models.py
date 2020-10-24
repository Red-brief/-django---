from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish_date = models.DateField(auto_now_add=True)

    # 一对多
    publish = models.ForeignKey(to='Publish')
    # 多对多
    authors = models.ManyToManyField(to='Author')


class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    email = models.EmailField()
    # 该字段类型不会给models看的，而是给我们后面会学到的校验性组件看的  varchar(254)


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    # 一对一
    Author_detail = models.OneToOneField(to="AuthorDetail")


class AuthorDetail(models.Model):
    phone = models.BigIntegerField()  # 电话号码用BigIntegerField或者直接用CharField
    addr = models.CharField(max_length=64)
