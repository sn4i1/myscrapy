# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'pok'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['pok.spiders']
NEWSPIDER_MODULE = 'pok.spiders'
ITEM_PIPELINES = [
        'pok.pipelines.PokPipeline'
    ]
DEFAULT_ITEM_CLASS = 'pok.items.PokItem'
