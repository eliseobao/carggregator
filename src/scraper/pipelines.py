# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scraper.utils import has_numbers, get_only_numbers, get_only_letters


class CleanUpPipeline:

    def process_item(self, item, spider):

        for key in list(item.keys()):
            value = item[key]

            if item[key] in ["-", ""]:
                del item[key]
                continue

            if key not in ["url", "image", "publisher"]:
                item[key] = item[key].title()

            if key in ["odometer", "price_cash", "price_financed"]:
                item[key] = int(get_only_numbers(value))

            if key == "transmission":
                item[key] = item[key].split(' ')[0]

            if key == "hp":
                if len(value.split()) > 2:
                    item[key] = int(get_only_numbers(value.split()[2]))
                else:
                    item[key] = int(get_only_numbers(value))

            if key == "registration_date" and '/' in value:
                item[key] = int(value.split('/')[1].strip())

            if (key == "location") and (len(value.split(',')) == 2):
                item[key] = value.split(',')[0].title()

        return item
