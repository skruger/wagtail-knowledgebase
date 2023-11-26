# Generated by Django 4.2.7 on 2023-11-26 22:33

from django.db import migrations
import wagtail.blocks
import wagtail.blocks.static_block
import wagtail.fields
import wagtail.images.blocks
import wtknowledgebase.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wtknowledgebase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kbarticlepage',
            name='body',
            field=wagtail.fields.StreamField([('richtext', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('quote', wagtail.blocks.BlockQuoteBlock()), ('page', wagtail.blocks.PageChooserBlock()), ('special_template', wagtail.blocks.static_block.StaticBlock(admin_text='This is a special static template', icon='doc-full', label='Special Template', template='_special_template.html')), ('card', wagtail.blocks.StructBlock([('header_title', wagtail.blocks.RichTextBlock(required=False)), ('card_classes', wagtail.blocks.CharBlock(help_text="Be sure to include 'card'", required=False)), ('card_header_classes', wagtail.blocks.CharBlock(help_text="Be sure to include 'card-header'", required=False)), ('card_body_classes', wagtail.blocks.CharBlock(help_text="Be sure to include 'card-body'", required=False)), ('body', wagtail.blocks.StreamBlock([('richtext', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('quote', wagtail.blocks.BlockQuoteBlock()), ('page', wagtail.blocks.PageChooserBlock()), ('special_template', wagtail.blocks.static_block.StaticBlock(admin_text='This is a special static template', icon='doc-full', label='Special Template', template='_special_template.html'))]))])), ('grid_row', wagtail.blocks.StructBlock([('class_name', wagtail.blocks.CharBlock(required=False)), ('cells', wagtail.blocks.ListBlock(wtknowledgebase.blocks.GridCellBlock))])), ('jumbotron', wagtail.blocks.StructBlock([('extra_class', wagtail.blocks.CharBlock(required=False)), ('body', wagtail.blocks.StreamBlock([('richtext', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('quote', wagtail.blocks.BlockQuoteBlock()), ('page', wagtail.blocks.PageChooserBlock()), ('special_template', wagtail.blocks.static_block.StaticBlock(admin_text='This is a special static template', icon='doc-full', label='Special Template', template='_special_template.html')), ('card', wagtail.blocks.StructBlock([('header_title', wagtail.blocks.RichTextBlock(required=False)), ('card_classes', wagtail.blocks.CharBlock(help_text="Be sure to include 'card'", required=False)), ('card_header_classes', wagtail.blocks.CharBlock(help_text="Be sure to include 'card-header'", required=False)), ('card_body_classes', wagtail.blocks.CharBlock(help_text="Be sure to include 'card-body'", required=False)), ('body', wagtail.blocks.StreamBlock([('richtext', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('quote', wagtail.blocks.BlockQuoteBlock()), ('page', wagtail.blocks.PageChooserBlock()), ('special_template', wagtail.blocks.static_block.StaticBlock(admin_text='This is a special static template', icon='doc-full', label='Special Template', template='_special_template.html'))]))])), ('grid_row', wagtail.blocks.StructBlock([('class_name', wagtail.blocks.CharBlock(required=False)), ('cells', wagtail.blocks.ListBlock(wtknowledgebase.blocks.GridCellBlock))]))]))]))], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='kbcategorypage',
            name='body',
            field=wagtail.fields.StreamField([('richtext', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('quote', wagtail.blocks.BlockQuoteBlock()), ('page', wagtail.blocks.PageChooserBlock()), ('special_template', wagtail.blocks.static_block.StaticBlock(admin_text='This is a special static template', icon='doc-full', label='Special Template', template='_special_template.html')), ('card', wagtail.blocks.StructBlock([('header_title', wagtail.blocks.RichTextBlock(required=False)), ('card_classes', wagtail.blocks.CharBlock(help_text="Be sure to include 'card'", required=False)), ('card_header_classes', wagtail.blocks.CharBlock(help_text="Be sure to include 'card-header'", required=False)), ('card_body_classes', wagtail.blocks.CharBlock(help_text="Be sure to include 'card-body'", required=False)), ('body', wagtail.blocks.StreamBlock([('richtext', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('quote', wagtail.blocks.BlockQuoteBlock()), ('page', wagtail.blocks.PageChooserBlock()), ('special_template', wagtail.blocks.static_block.StaticBlock(admin_text='This is a special static template', icon='doc-full', label='Special Template', template='_special_template.html'))]))])), ('grid_row', wagtail.blocks.StructBlock([('class_name', wagtail.blocks.CharBlock(required=False)), ('cells', wagtail.blocks.ListBlock(wtknowledgebase.blocks.GridCellBlock))])), ('jumbotron', wagtail.blocks.StructBlock([('extra_class', wagtail.blocks.CharBlock(required=False)), ('body', wagtail.blocks.StreamBlock([('richtext', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('quote', wagtail.blocks.BlockQuoteBlock()), ('page', wagtail.blocks.PageChooserBlock()), ('special_template', wagtail.blocks.static_block.StaticBlock(admin_text='This is a special static template', icon='doc-full', label='Special Template', template='_special_template.html')), ('card', wagtail.blocks.StructBlock([('header_title', wagtail.blocks.RichTextBlock(required=False)), ('card_classes', wagtail.blocks.CharBlock(help_text="Be sure to include 'card'", required=False)), ('card_header_classes', wagtail.blocks.CharBlock(help_text="Be sure to include 'card-header'", required=False)), ('card_body_classes', wagtail.blocks.CharBlock(help_text="Be sure to include 'card-body'", required=False)), ('body', wagtail.blocks.StreamBlock([('richtext', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('quote', wagtail.blocks.BlockQuoteBlock()), ('page', wagtail.blocks.PageChooserBlock()), ('special_template', wagtail.blocks.static_block.StaticBlock(admin_text='This is a special static template', icon='doc-full', label='Special Template', template='_special_template.html'))]))])), ('grid_row', wagtail.blocks.StructBlock([('class_name', wagtail.blocks.CharBlock(required=False)), ('cells', wagtail.blocks.ListBlock(wtknowledgebase.blocks.GridCellBlock))]))]))]))], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='kbindexpage',
            name='body',
            field=wagtail.fields.StreamField([('richtext', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('quote', wagtail.blocks.BlockQuoteBlock()), ('page', wagtail.blocks.PageChooserBlock()), ('special_template', wagtail.blocks.static_block.StaticBlock(admin_text='This is a special static template', icon='doc-full', label='Special Template', template='_special_template.html')), ('card', wagtail.blocks.StructBlock([('header_title', wagtail.blocks.RichTextBlock(required=False)), ('card_classes', wagtail.blocks.CharBlock(help_text="Be sure to include 'card'", required=False)), ('card_header_classes', wagtail.blocks.CharBlock(help_text="Be sure to include 'card-header'", required=False)), ('card_body_classes', wagtail.blocks.CharBlock(help_text="Be sure to include 'card-body'", required=False)), ('body', wagtail.blocks.StreamBlock([('richtext', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('quote', wagtail.blocks.BlockQuoteBlock()), ('page', wagtail.blocks.PageChooserBlock()), ('special_template', wagtail.blocks.static_block.StaticBlock(admin_text='This is a special static template', icon='doc-full', label='Special Template', template='_special_template.html'))]))])), ('grid_row', wagtail.blocks.StructBlock([('class_name', wagtail.blocks.CharBlock(required=False)), ('cells', wagtail.blocks.ListBlock(wtknowledgebase.blocks.GridCellBlock))])), ('jumbotron', wagtail.blocks.StructBlock([('extra_class', wagtail.blocks.CharBlock(required=False)), ('body', wagtail.blocks.StreamBlock([('richtext', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('quote', wagtail.blocks.BlockQuoteBlock()), ('page', wagtail.blocks.PageChooserBlock()), ('special_template', wagtail.blocks.static_block.StaticBlock(admin_text='This is a special static template', icon='doc-full', label='Special Template', template='_special_template.html')), ('card', wagtail.blocks.StructBlock([('header_title', wagtail.blocks.RichTextBlock(required=False)), ('card_classes', wagtail.blocks.CharBlock(help_text="Be sure to include 'card'", required=False)), ('card_header_classes', wagtail.blocks.CharBlock(help_text="Be sure to include 'card-header'", required=False)), ('card_body_classes', wagtail.blocks.CharBlock(help_text="Be sure to include 'card-body'", required=False)), ('body', wagtail.blocks.StreamBlock([('richtext', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('quote', wagtail.blocks.BlockQuoteBlock()), ('page', wagtail.blocks.PageChooserBlock()), ('special_template', wagtail.blocks.static_block.StaticBlock(admin_text='This is a special static template', icon='doc-full', label='Special Template', template='_special_template.html'))]))])), ('grid_row', wagtail.blocks.StructBlock([('class_name', wagtail.blocks.CharBlock(required=False)), ('cells', wagtail.blocks.ListBlock(wtknowledgebase.blocks.GridCellBlock))]))]))]))], use_json_field=True),
        ),
    ]