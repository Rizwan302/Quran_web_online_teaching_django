# Generated by Django 4.1.3 on 2023-02-01 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('timesp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
