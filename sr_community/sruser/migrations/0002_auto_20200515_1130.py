# Generated by Django 3.0.6 on 2020-05-15 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sruser', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sruser',
            options={'verbose_name': '선린 사용자', 'verbose_name_plural': '선린 사용자'},
        ),
        migrations.AlterModelTable(
            name='sruser',
            table='sunrin_sruser',
        ),
    ]
