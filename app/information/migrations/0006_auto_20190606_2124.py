# Generated by Django 2.1.7 on 2019-06-06 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0005_auto_20190606_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fni',
            name='food_group',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='식품군'),
        ),
        migrations.AlterField(
            model_name='fni',
            name='food_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='식품명'),
        ),
    ]