# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'pok'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['pok.spiders']
NEWSPIDER_MODULE = 'pok.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
ITEM_PIPELINES = [
        'pok.pipelines.PokPipeline'
    ]
DEFAULT_ITEM_CLASS = 'pok.items.PokItem'
