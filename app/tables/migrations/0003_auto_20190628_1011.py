# Generated by Django 2.2.2 on 2019-06-28 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0002_auto_20190628_0123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tableattachment',
            options={'verbose_name': '레시피 첨부파일', 'verbose_name_plural': '레시피 첨부파일 목록'},
        ),
        migrations.AlterField(
            model_name='tableattachment',
            name='file',
            field=models.FileField(upload_to='.media/2019-06-28/DiH8QEVj'),
        ),
    ]