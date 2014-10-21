import datetime


class RVTPipeline(object):

    def process_item(self, item, spider):
        # Set default values
        item.setdefault('year', None)
        item.setdefault('length', None)
        item.setdefault('main_photo', None)
        item.setdefault('contact_person', None)
        item.setdefault('phone1', None)
        item.setdefault('email', None)
        item.setdefault('created', datetime.datetime.now())
        return item
