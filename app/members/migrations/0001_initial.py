# Generated by Django 2.1.7 on 2019-05-20 12:25

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=20, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('phone_number', models.CharField(blank=True, max_length=12, null=True, verbose_name='Phone Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'verbose_name': '유저',
                'verbose_name_plural': '유저 목록',
                'ordering': ['date_joined'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gender', models.BooleanField(default=True, verbose_name='Gender')),
                ('height', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Height')),
                ('weight', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Weight')),
                ('renal_disease', models.CharField(blank=True, choices=[('1단계', 'GFR > 90'), ('2단계', 'GFR 60~90'), ('3단계', 'GFR 30~60'), ('4단계', 'GFR 15~30'), ('5단계', 'GFR < 15(신부전, 투석)')], default='1단계', max_length=3, null=True)),
                ('hospital', models.CharField(blank=True, max_length=30, null=True, verbose_name='Hospital')),
                ('attending_physician', models.CharField(blank=True, max_length=30, null=True, verbose_name='Attending Physician')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
