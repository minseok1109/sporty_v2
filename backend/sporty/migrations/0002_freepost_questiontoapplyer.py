# Generated by Django 3.2.4 on 2023-02-10 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sporty', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='freepost',
            name='questionToApplyer',
            field=models.CharField(default='', max_length=50, verbose_name='신청자한테 궁금한 점'),
        ),
    ]
