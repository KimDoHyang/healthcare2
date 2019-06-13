# Generated by Django 2.1.7 on 2019-06-13 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0013_auto_20190614_0510'),
    ]

    operations = [
        migrations.CreateModel(
            name='HFA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(blank=True, max_length=80, null=True, verbose_name='원료명')),
                ('company', models.CharField(blank=True, max_length=30, null=True, verbose_name='회사명')),
                ('daily_intake', models.CharField(blank=True, max_length=80, null=True, verbose_name='1일 권 섭취량')),
                ('feature', models.TextField(blank=True, null=True, verbose_name='주요 기능성')),
                ('caution', models.TextField(blank=True, null=True, verbose_name='섭취 주의사항')),
            ],
            options={
                'verbose_name': '건강기능성식품 기능성 원료인정현황',
                'verbose_name_plural': '건강기능성식품 기능성 원료인정현황 목록',
            },
        ),
    ]
