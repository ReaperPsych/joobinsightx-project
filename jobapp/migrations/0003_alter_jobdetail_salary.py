# Generated by Django 4.2.7 on 2024-02-02 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0002_alter_jobdetail_employer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdetail',
            name='salary',
            field=models.CharField(max_length=150),
        ),
    ]