# Generated by Django 3.2.9 on 2021-11-23 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_party', models.CharField(blank=True, max_length=50)),
                ('image_party', models.ImageField(blank=True, upload_to='media/databaseImageParty')),
                ('info_party', models.TextField(blank=True)),
                ('age_party', models.IntegerField(blank=True)),
            ],
        ),
    ]
