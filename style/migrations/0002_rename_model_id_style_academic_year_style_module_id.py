# Generated by Django 4.1.3 on 2022-11-27 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('style', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='style',
            old_name='model_id',
            new_name='academic_year',
        ),
        migrations.AddField(
            model_name='style',
            name='module_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
