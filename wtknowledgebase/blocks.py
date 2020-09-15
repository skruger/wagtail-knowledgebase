from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


BASIC_BLOCKS = [
    ('richtext', blocks.RichTextBlock()),
    ('image', ImageChooserBlock()),
    ('quote', blocks.BlockQuoteBlock()),
    ('page', blocks.PageChooserBlock()),
]


class CardBlock(blocks.StructBlock):
    header_title = blocks.RichTextBlock(required=False)
    card_classes = blocks.CharBlock(required=False, help_text="Be sure to include 'card'")
    card_header_classes = blocks.CharBlock(required=False, help_text="Be sure to include 'card-header'")
    card_body_classes = blocks.CharBlock(required=False, help_text="Be sure to include 'card-body'")
    body = blocks.StreamBlock(BASIC_BLOCKS)

    class Meta:  # noqa
        icon = ''
        label = "Card"
        template = 'wtknowledgebase/card_block.html'

BASIC_BLOCKS.append(('card', CardBlock()))


class GridCellBlock(blocks.StructBlock):
    class_name = blocks.CharBlock(required=True)
    body = blocks.StreamBlock(BASIC_BLOCKS)

    class Meta:  # noqa
        icon = 'plus'
        label = "Grid Cell"
        template = 'wtknowledgebase/grid_cell_block.html'


class GridRowBlock(blocks.StructBlock):
    class_name = blocks.CharBlock(required=False)
    cells = blocks.ListBlock(GridCellBlock)

    class Meta:  # noqa
        icon = 'table'
        label = "Grid Row"
        template = 'wtknowledgebase/grid_row_block.html'

BASIC_BLOCKS.append(('grid_row', GridRowBlock()))
