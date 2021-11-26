# Generated by Django 3.2.9 on 2021-11-24 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalsParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=50)),
                ('nameLocal', models.TextField(blank=True)),
                ('map_party', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='media/databaseImageLocal')),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(blank=True)),
                ('name_party', models.CharField(blank=True, max_length=50)),
                ('date', models.DateTimeField(blank=True)),
                ('count_ticket', models.IntegerField(blank=True)),
                ('ID_Local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='party.localsparty')),
                ('ID_Party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='party.party')),
            ],
        ),
    ]