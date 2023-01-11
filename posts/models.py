from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    TYPE = [
        ('Танки', 'tank'),
        ('Хилы', 'heal'),
        ('ДД', 'dd'),
        ('Торговцы', 'trader'),
        ('Гильдмастеры', 'guildmaster'),
        ('Квестгиверы', 'quest'),
        ('Кузнецы', 'smith'),
        ('Кожевники', 'tanner'),
        ('Зельевары', 'potion'),
        ('Мастера заклинаний', 'spellmaster')
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()
    category = models.CharField(max_length=20, choices=TYPE)
    date = models.DateTimeField(auto_now_add=True)


class Response(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.BooleanField

