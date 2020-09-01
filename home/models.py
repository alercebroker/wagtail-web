from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import (
    FieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
    RichTextField
)
from wagtail.core.fields import StreamField
from .blocks import BannerBlock, TextBlock, FormEmbedBlock, PageLinksBlock, EventListBlock


class HomePage(Page):

    content = StreamField(
        [("banner", BannerBlock()), ("text", TextBlock()), ("form", FormEmbedBlock()), ("buttons", PageLinksBlock()), ("events", EventListBlock())],
        null=True,
    )

    content_panels = Page.content_panels + [StreamFieldPanel("content")]
