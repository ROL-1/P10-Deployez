#! /usr/bin/env python3
# coding: utf-8
"""Custom command to clear and fill database from api datas."""

# loggings (for Sentry)
import logging
logger = logging.getLogger(__name__)


from django.core.management.base import BaseCommand

from product.offapi.apirequests import ApiRequests
from product.offapi.insertdb import deletedata, insertdb
from product.offapi.charmax import Charmax


class Command(BaseCommand):
    """Custom command to clear and fill database from api datas."""

    def databasefill(self):
        """Command to clear and fill database from api datas."""
        try:
            logger.info('run : manage.py database', exc_info=True)
            # Retrieves the maximum number of characters for the fields.
            Fields_charmax = Charmax.characters_max()
            # Retrives datas from Api and reject unsuitable datas.
            Api_data = ApiRequests().api_get_data(Fields_charmax)
            # Clear products data (not users and favorites)
            deletedata()
            # Insertion in database.
            Insert = insertdb(Api_data)
            logger.info('success : manage.py database', exc_info=True)
            print("Database installed.")

        except DatabaseError:
            print("Error while updating database")
            logger.error("error : manage.py database", exc_info=True)

    def handle(self, *args, **options):
        """Call customs commands."""
        self.databasefill()
        return
