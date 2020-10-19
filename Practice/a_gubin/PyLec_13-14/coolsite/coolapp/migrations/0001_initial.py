# Generated by Django 3.0.8 on 2020-10-17 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
        ),
    ]