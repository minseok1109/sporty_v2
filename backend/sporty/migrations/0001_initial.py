# Generated by Django 3.2.4 on 2022-12-23 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, null=True, verbose_name='제목')),
                ('date', models.CharField(max_length=50, verbose_name='날짜')),
                ('location', models.CharField(max_length=100, verbose_name='장소')),
                ('purpose', models.CharField(max_length=10, verbose_name='목표거리')),
                ('cruit', models.IntegerField(null=True, verbose_name='모집인원')),
                ('description', models.CharField(max_length=100, verbose_name='설명')),
                ('apply_user_set', models.ManyToManyField(blank=True, related_name='apply_workpost_set', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_workpost_set', to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FreePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, null=True, verbose_name='제목')),
                ('date', models.CharField(max_length=50, verbose_name='날짜')),
                ('location', models.CharField(max_length=100, verbose_name='장소')),
                ('cruit', models.IntegerField(null=True, verbose_name='모집인원')),
                ('description', models.CharField(max_length=100, verbose_name='설명')),
                ('apply_user_set', models.ManyToManyField(blank=True, related_name='apply_freepost_set', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_freepost_set', to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BasketPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, null=True, verbose_name='제목')),
                ('start_date_time', models.CharField(max_length=50, verbose_name='시작 날짜')),
                ('end_date_time', models.CharField(max_length=50, verbose_name='끝나는 날짜')),
                ('location', models.CharField(max_length=100, verbose_name='장소')),
                ('level', models.CharField(max_length=10, verbose_name='실력')),
                ('cruit', models.CharField(max_length=10, verbose_name='모집인원')),
                ('gameinfo', models.CharField(max_length=20, verbose_name='경기정보')),
                ('description', models.CharField(max_length=100, verbose_name='설명')),
                ('apply_user_set', models.ManyToManyField(blank=True, related_name='apply_basketpost_set', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_basketballpost_set', to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
