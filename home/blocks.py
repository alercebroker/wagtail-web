import wagtail.core.blocks as blocks
from wagtail.core.blocks import PageChooserBlock, RichTextBlock, URLBlock, IntegerBlock
from wagtail.images.blocks import ImageChooserBlock

class PageLinkBlock(blocks.StructBlock):
    page = blocks.PageChooserBlock()

    class Meta:
        icon = "user"
        template = "home/blocks/page_link_block.html"


class BannerBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    short_text = blocks.CharBlock()
    background_image = ImageChooserBlock()

    class Meta:
        template = "home/blocks/banner_block.html"


class TextBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.RichTextBlock()

    class Meta:
        template = "home/blocks/text_block.html"


class FormEmbedBlock(blocks.StructBlock):
    publish_url = URLBlock()
    class Meta:
        icon = "presentation"
        template = "home/blocks/form_embed_block.html"
