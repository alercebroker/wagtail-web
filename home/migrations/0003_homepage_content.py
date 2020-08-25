# Generated by Django 3.1 on 2020-08-25 22:17

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('banner', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('short_text', wagtail.core.blocks.CharBlock()), ('background_image', wagtail.images.blocks.ImageChooserBlock())])), ('text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('text', wagtail.core.blocks.RichTextBlock())])), ('form', wagtail.core.blocks.StructBlock([('publish_url', wagtail.core.blocks.URLBlock())]))], null=True),
        ),
    ]