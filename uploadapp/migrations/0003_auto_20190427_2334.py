# Generated by Django 2.1.7 on 2019-04-27 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadapp', '0002_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='description',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
