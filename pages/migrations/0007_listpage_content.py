# Generated by Django 3.1 on 2020-08-31 20:05

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20200827_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='listpage',
            name='content',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock())]))], blank=True, null=True),
        ),
    ]
