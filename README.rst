========================
wagtail-knowledgebase
========================
Knowledgebase Site Pages for Wagtail.

Usage
-----
#. ``pip install wagtail-knowledgebase``

#. Add "wtknowledgebase" to ``INSTALLED_APPS`` in your settings.py

#. Optionally add a list of ``('name', **kwargs)`` tuples to
   ``WTKNOWLEDGEBASE_STATIC_BLOCKS`` setting to define static
   blocks to be included in page types.

Reuse stream blocks
-------------------

The block designed for these pages could be useful for other pages,
you can use the stream builder that is defined in blocks to make use
of the blocks defined for knowledgebase pages.

::

  from wagtail.core.models import Page
  from wagtail.core.fields import StreamField
  from wtknowledgebase import blocks

  class HomePage(Page):
      body = StreamField(blocks.stream_builder.blocks([
          ('my_extra_static', StaticBlock(
              template='_my_template.html',
              label="Admin UI Label",
              icon='doc-full',
              admin_text="This is a deeper description",
      ])

