# Generated by Django 3.2.12 on 2022-03-06 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('punish', '0003_auto_20220306_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='polcom',
            fields=[
                ('polcomid', models.AutoField(primary_key=True, serialize=False)),
                ('polcom', models.CharField(max_length=300, verbose_name='polcom')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('designation', models.CharField(max_length=50, verbose_name='designation')),
                ('mobileno', models.CharField(max_length=50, verbose_name='mobileno')),
            ],
        ),
    ]
