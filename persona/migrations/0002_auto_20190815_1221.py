# Generated by Django 2.2.4 on 2019-08-15 12:21

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='none/public'),
        ),
    ]
