# Generated by Django 2.1.1 on 2018-09-28 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geomanager', '0003_auto_20180928_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='description',
            field=models.CharField(default='jdhfjh', max_length=200),
            preserve_default=False,
        ),
    ]
