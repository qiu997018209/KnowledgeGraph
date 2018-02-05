# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from app import app
from conf import *

if __name__ == '__main__':
    args=get_args()
    print('\nhttp_host:{},http_port:{}'.format('0.0.0.0',args.http_port))
    app.run(debug=True, host='0.0.0.0', port=args.http_port)
