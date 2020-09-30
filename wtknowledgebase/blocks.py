from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from django.conf import settings


class CustomStruct(blocks.StructBlock):
    type_classes = (
        ('char', blocks.CharBlock),
        ('text', blocks.TextBlock),
        ('email', blocks.EmailBlock),
        ('url', blocks.URLBlock),
        ('rich_text', blocks.RichTextBlock),
        ('image', ImageChooserBlock),
        ('quote', blocks.BlockQuoteBlock),
        ('page', blocks.PageChooserBlock),
        ('choice', blocks.ChoiceBlock),
        ('boolean', blocks.BooleanBlock),
        ('integer', blocks.IntegerBlock),
        ('decimal', blocks.DecimalBlock),
    )

    def __init__(self, **kwargs):
        cfg_local_blocks = kwargs.pop('blocks')
        local_blocks = list()
        for name, block_args in cfg_local_blocks or []:
            local_blocks.append(
                (name, self._block_args_to_block(**block_args))
            )

        super().__init__(local_blocks, **kwargs)

    def _block_args_to_block(self, type_name=None, **type_kwargs):
        types = dict(self.type_classes)
        type_class = types.get(type_name, blocks.CharBlock)
        return type_class(**type_kwargs)


class StreamBuilder:
    default_blocks = [
        ('richtext', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('quote', blocks.BlockQuoteBlock()),
        ('page', blocks.PageChooserBlock()),
    ]

    def __init__(self, initial_blocks=None):
        self.initial_blocks = initial_blocks or self.default_blocks

        for name, block_kwargs in getattr(settings, 'WTKNOWLEDGEBASE_STATIC_BLOCKS', []):
            self.initial_blocks.append(
                (name, blocks.StaticBlock(**block_kwargs))
            )

        for name, block_kwargs in getattr(settings, 'WTKNOWLEDGEBASE_STRUCT_BLOCKS', []):
            self.initial_blocks.append(
                (name, CustomStruct(**block_kwargs))
            )

        self._blocks = list()

    def blocks(self, local_blocks=None):
        names = set()
        for name, block in self.initial_blocks:
            assert name not in names, f"Duplicate name in initial_blocks! {name}"
            names.add(name)
            yield name, block
        for name, block in self._blocks:
            assert name not in names, f"Duplicate name in initial_blocks! {name}"
            names.add(name)
            yield name, block

        if local_blocks is not None:
            for name, block in local_blocks:
                assert name not in names, f"Duplicate name in initial_blocks! {name}"
                names.add(name)
                yield name, block

    def add_extra_block(self, name, block):
        self._blocks.append((name, block))

    def inject_block(self, name, block):
        pass


stream_builder = StreamBuilder()


class CardBlock(blocks.StructBlock):
    header_title = blocks.RichTextBlock(required=False)
    card_classes = blocks.CharBlock(required=False, help_text="Be sure to include 'card'")
    card_header_classes = blocks.CharBlock(required=False, help_text="Be sure to include 'card-header'")
    card_body_classes = blocks.CharBlock(required=False, help_text="Be sure to include 'card-body'")
    body = blocks.StreamBlock(stream_builder.blocks())

    class Meta:  # noqa
        icon = ''
        label = "Card"
        template = 'wtknowledgebase/card_block.html'


stream_builder.add_extra_block('card', CardBlock())


class GridCellBlock(blocks.StructBlock):
    class_name = blocks.CharBlock(required=True)
    body = blocks.StreamBlock(stream_builder.blocks())

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


stream_builder.add_extra_block('grid_row', GridRowBlock())


class JumbotronBlock(blocks.StructBlock):
    extra_class = blocks.CharBlock(required=False)
    body = blocks.StreamBlock(stream_builder.blocks())

    class Meta:  # noqa
        icon = 'table'
        label = "Jumbotron"
        template = 'wtknowledgebase/jumbotron_block.html'


stream_builder.add_extra_block('jumbotron', JumbotronBlock())
