# Generated by Django 4.1.2 on 2022-11-18 13:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('login', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['login'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=255)),
                ('site', models.CharField(max_length=255)),
                ('personal_account', models.CharField(max_length=255)),
                ('user_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='energy.user')),
            ],
        ),
        migrations.CreateModel(
            name='Data_transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_transfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='energy.service')),
            ],
        ),
    ]