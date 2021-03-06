# Generated by Django 3.2.9 on 2022-01-06 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_contact_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=150)),
                ('date_of_event', models.DateField()),
                ('description', models.TextField(max_length=1000)),
                ('link', models.URLField()),
                ('thumbnail', models.ImageField(upload_to='posts/%Y/%m/%d/')),
                ('facebook_link', models.URLField()),
                ('twitter_link', models.URLField()),
                ('youtube_link', models.URLField()),
            ],
        ),
    ]
