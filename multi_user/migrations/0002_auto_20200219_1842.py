# Generated by Django 2.2.10 on 2020-02-19 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multi_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='color',
            field=models.CharField(max_length=2),
        ),
        migrations.DeleteModel(
            name='Color',
        ),
    ]
