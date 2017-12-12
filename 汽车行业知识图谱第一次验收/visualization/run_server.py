# -*- coding: utf-8 -*-
# @Author: ioriiod0
# @Date:   2017-07-12 11:47:28
# @Last Modified by:   ioriiod0
# @Last Modified time: 2017-07-14 19:21:37
import sys
sys.path.append("..")

import gevent
from gevent.monkey import patch_all
from conf import *
'''
gevent是第三方库，通过greenlet实现协程，其基本思想是：
当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。
由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。
由于切换是在IO操作时自动完成，所以gevent需要修改Python自带的一些标准库，这一过程在启动时通过monkey patch完成：
'''
patch_all()
from server.app import app

if __name__ == '__main__':
    app.run(debug=True, host=http_host, port=http_port)
