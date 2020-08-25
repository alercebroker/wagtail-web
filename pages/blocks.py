
import wagtail.core.blocks as blocks
from wagtail.core.blocks import PageChooserBlock, RichTextBlock, URLBlock, IntegerBlock
from wagtail.images.blocks import ImageChooserBlock

class TextBlock(blocks.StructBlock):
    text = RichTextBlock()
    class Meta:
        icon = "text"
        template = "pages/text_block.html"
