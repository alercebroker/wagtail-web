from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import (
    FieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
    RichTextField,
)
from wagtail.core.fields import StreamField
import wagtail.core.blocks as blocks
from wagtail.images.edit_handlers import ImageChooserPanel


class PageLinkBlock(blocks.StructBlock):
    page = blocks.PageChooserBlock()

    class Meta:
        icon = "user"
        template = "home/page_link_block.html"


class HomePage(Page):
    subtitle = models.TextField(
        max_length=140, help_text="Banner lead text", blank=True
    )
    description = RichTextField(blank=True, help_text="Description below lead text")

    background_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        help_text="Banner background image",
        on_delete=models.SET_NULL,
    )

    center_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        help_text="Image over the title",
        on_delete=models.SET_NULL,
    )

    buttons = StreamField([("button", PageLinkBlock())], blank=True, null=True)

    secondary_subtitle = models.TextField(
        max_length=140, help_text="Secondary title", blank=True
    )

    secondary_text = RichTextField(
        blank=True, help_text="Secondary text information. For example welcome message"
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("center_image", classname="full"),
        FieldPanel("subtitle", classname="full"),
        FieldPanel("description", classname="full"),
        ImageChooserPanel("background_image", classname="full"),
        StreamFieldPanel("buttons"),
        FieldPanel("secondary_subtitle", classname="full"),
        FieldPanel("secondary_text", classname="full"),
    ]
