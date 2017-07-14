# -*- coding: utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    app.run()