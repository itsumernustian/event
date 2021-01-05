# Generated by Django 3.1.3 on 2020-12-21 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=100)),
                ('event_head', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('date', models.DateField()),
                ('s_time', models.TimeField()),
                ('e_time', models.TimeField()),
                ('event_desc', models.CharField(max_length=300)),
                ('event_type', models.CharField(max_length=20)),
                ('event_price', models.CharField(max_length=20)),
                ('event_value', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'event_creation',
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('pwd', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('cms_id', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'registered user',
            },
        ),
    ]