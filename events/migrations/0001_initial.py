# Generated by Django 3.1 on 2020-08-25 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0003_listpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPage',
            fields=[
                ('miscpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.miscpage')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
            bases=('pages.miscpage',),
        ),
    ]
