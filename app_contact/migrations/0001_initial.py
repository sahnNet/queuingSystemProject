# Generated by Django 4.0.1 on 2022-01-06 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200, verbose_name='Subject')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('text', models.TextField(verbose_name='Message')),
                ('is_read', models.BooleanField(default=False, verbose_name='Read / Unread')),
            ],
            options={
                'verbose_name': 'Contact users',
                'verbose_name_plural': 'User calls',
            },
        ),
    ]