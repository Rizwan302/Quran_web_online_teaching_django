# Generated by Django 4.1.3 on 2023-02-01 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardOne',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('cardnumber', models.CharField(max_length=60)),
                ('cardmonth', models.CharField(max_length=10)),
                ('cardyear', models.CharField(max_length=10)),
                ('cardcvv', models.CharField(max_length=3)),
            ],
        ),
    ]
