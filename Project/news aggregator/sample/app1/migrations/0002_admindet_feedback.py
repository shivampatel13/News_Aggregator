# Generated by Django 3.1.2 on 2021-01-11 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='admindet',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('psw', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('fid', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=100)),
                ('emailid', models.CharField(max_length=70)),
                ('contactno', models.CharField(max_length=20)),
                ('feedback', models.TextField()),
                ('status', models.BooleanField()),
            ],
        ),
    ]