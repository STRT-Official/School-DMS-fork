# Generated by Django 3.2.21 on 2023-09-20 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busManage', '0003_auto_20230920_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentlist',
            name='classs',
            field=models.CharField(choices=[('xii', 'XII'), ('xi', 'XI'), ('x', 'X')], max_length=100),
        ),
    ]