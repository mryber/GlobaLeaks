# -*- coding: utf-8 -*-
import base64
import os

from globaleaks.models import Config


def db_fix_salt(session):
    items = session.query(Config).filter(Config.var_name == u'receipt_salt')
    for item in items:
        try:
            if len(base64.b64decode(item.value)) != 16:
                item.value = base64.b64encode(os.urandom(16)).decode()
        except:
            item.value = base64.b64encode(os.urandom(16)).decode()


def db_fix_config(session):
    db_fix_salt(session)
