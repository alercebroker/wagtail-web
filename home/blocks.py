import wagtail.core.blocks as blocks
from wagtail.images.blocks import ImageChooserBlock
from events.models import EventListPage


class PageLinkBlock(blocks.StructBlock):
    page = blocks.PageChooserBlock()

    class Meta:
        icon = "user"
        template = "home/blocks/page_link_block.html"


class PageLinksBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    buttons = blocks.StreamBlock([("button", PageLinkBlock())])

    class Meta:
        template = "home/blocks/page_links_block.html"


class BannerBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    short_text = blocks.CharBlock()
    background_image = ImageChooserBlock(required=False)

    class Meta:
        template = "home/blocks/banner_block.html"


class TextBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.RichTextBlock()

    class Meta:
        template = "home/blocks/text_block.html"


class FormEmbedBlock(blocks.StructBlock):
    publish_url = blocks.URLBlock()

    class Meta:
        icon = "presentation"
        template = "home/blocks/form_embed_block.html"


class EventLinkBlock(blocks.StructBlock):
    event = blocks.PageChooserBlock(page_type=EventListPage)
    class Meta:
        icon = "user"
        template = "home/blocks/event_link_block.html"


class EventListBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    events = blocks.StreamBlock([("event", EventLinkBlock())])

    class Meta:
        template = "home/blocks/event_list_block.html"
