from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from wtknowledgebase import blocks


class StreamFieldBodyMixin(Page):
    body = StreamField(blocks.stream_builder.blocks(), use_json_field=True)

    class Meta:
        abstract = True


class KbIndexPage(StreamFieldBodyMixin, Page):
    subpage_types = [
        'wtknowledgebase.KbCategoryPage',
        'wtknowledgebase.KbArticlePage',
    ]

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]


class KbCategoryPage(StreamFieldBodyMixin, Page):
    subpage_types = [
        'wtknowledgebase.KbCategoryPage',
        'wtknowledgebase.KbArticlePage',
    ]

    category_name = models.CharField(max_length=250)

    content_panels = Page.content_panels + [
        FieldPanel('category_name'),
        FieldPanel('body'),
    ]


class KbArticlePage(StreamFieldBodyMixin, Page):
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
