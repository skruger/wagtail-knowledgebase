from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from wtknowledgebase import blocks


class StreamFieldBodyMixin(Page):
    body = StreamField(blocks.stream_builder.blocks())

    class Meta:
        abstract = True


class KbIndexPage(StreamFieldBodyMixin, Page):
    subpage_types = [
        'wtknowledgebase.KbCategoryPage',
        'wtknowledgebase.KbArticlePage',
    ]

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class KbCategoryPage(StreamFieldBodyMixin, Page):
    subpage_types = [
        'wtknowledgebase.KbCategoryPage',
        'wtknowledgebase.KbArticlePage',
    ]

    category_name = models.CharField(max_length=250)

    content_panels = Page.content_panels + [
        FieldPanel('category_name'),
        StreamFieldPanel('body'),
    ]


class KbArticlePage(StreamFieldBodyMixin, Page):
    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
