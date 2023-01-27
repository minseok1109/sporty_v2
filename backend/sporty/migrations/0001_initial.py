# Generated by Django 3.2.4 on 2023-01-27 03:39

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
                ('start_date_time', models.CharField(max_length=50, verbose_name='시작 날짜')),
                ('location', models.CharField(max_length=100, verbose_name='장소')),
                ('cruit', models.IntegerField(null=True, verbose_name='모집인원')),
                ('amountOfGym', models.IntegerField(default=0, verbose_name='참가비')),
                ('sex', models.CharField(default='', max_length=5, verbose_name='성별')),
                ('isRunning', models.CharField(default='', max_length=4, verbose_name='달리기 여부')),
                ('description', models.CharField(max_length=100, verbose_name='설명')),
                ('questionToApplyer', models.CharField(default='', max_length=50, verbose_name='신청자한테 궁금한 점')),
                ('apply_user_set', models.ManyToManyField(blank=True, related_name='apply_workpost_set', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_workpost_set', to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('message', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sporty.workpost')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='FreePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_date_time', models.CharField(max_length=50, verbose_name='시작 날짜')),
                ('location', models.CharField(max_length=100, verbose_name='장소')),
                ('cruit', models.IntegerField(null=True, verbose_name='모집인원')),
                ('amountOfGym', models.IntegerField(default=0, verbose_name='참가비')),
                ('sex', models.CharField(default='', max_length=5, verbose_name='성별')),
                ('description', models.CharField(max_length=100, verbose_name='설명')),
                ('apply_user_set', models.ManyToManyField(blank=True, related_name='apply_freepost_set', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_freepost_set', to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FreeComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('message', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sporty.freepost')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='BasketPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_date_time', models.CharField(max_length=50, verbose_name='시작 날짜')),
                ('location', models.CharField(max_length=100, verbose_name='장소')),
                ('amountOfGym', models.IntegerField(default=0, verbose_name='참가비')),
                ('level', models.CharField(max_length=10, verbose_name='실력')),
                ('cruit', models.IntegerField(verbose_name='모집인원')),
                ('sex', models.CharField(default='', max_length=5, verbose_name='성별')),
                ('description', models.CharField(max_length=100, verbose_name='설명')),
                ('questionToApplyer', models.CharField(default='', max_length=50, verbose_name='신청자한테 궁금한 점')),
                ('apply_user_set', models.ManyToManyField(blank=True, related_name='apply_basketpost_set', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_basketballpost_set', to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BasketComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('message', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sporty.basketpost')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
