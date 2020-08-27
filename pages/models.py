from django.db import models

from wagtail.admin.edit_handlers import Page, FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from .blocks import TextBlock

# Create your models here.
class MiscPage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        related_name="+",
        help_text="Banner background image",
        on_delete=models.SET_NULL
    )
    short_description = models.TextField(null=True, blank=True)

    content = StreamField(
        [
            ("text", TextBlock()),
        ],
        null=True,
        blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("short_description"),
        StreamFieldPanel("content"),
        ImageChooserPanel("image")
    ]

class ListPage(Page):

    short_description = models.TextField(
        blank=True,
        max_length=500
    )

    content_panels = Page.content_panels + [
        FieldPanel('short_description')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['children'] = self.get_children().live().public().specific()
        return context
