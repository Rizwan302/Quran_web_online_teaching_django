# Generated by Django 4.1.3 on 2023-02-05 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_admission_fname_alter_admission_lname_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admission',
        ),
    ]
