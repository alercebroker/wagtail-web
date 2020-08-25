
import wagtail.core.blocks as blocks
from wagtail.core.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock

class TextBlock(blocks.StructBlock):
    text = RichTextBlock()
    class Meta:
        icon = "text"
        template = "pages/blocks/text_block.html"
