# Generated by Django 4.0.4 on 2022-06-14 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campsites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('address', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Poi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campsiteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_api.campsites')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=75)),
                ('campsite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_api.campsites')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='campsites',
            name='poi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_api.poi'),
        ),
        migrations.AddField(
            model_name='campsites',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_campsites', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='campsites',
            name='userLists',
            field=models.ManyToManyField(related_name='campsites', through='app_api.UserList', to=settings.AUTH_USER_MODEL),
        ),
    ]
