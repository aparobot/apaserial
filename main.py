#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
    Aparobot 串口调试助手
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Aparobot是一款基于FreeRTOS的开源平衡小车
    由几个科技从业爱好者利用周末时间合作开发
    产品代码整洁，抽象层次良好，质量较高
    通过BLE蓝牙与手机通信
    手机APP开源
    上位机程序使用Python开发，跨平台运行(windows, linux, mac)，代码开源
    QQ交流群: 206772276
"""

import sys
sys.dont_write_bytecode = 1
from PyQt4.QtGui import QApplication
from MainWindow import MainWindow

__author__ = "ehcapa"
__version__ = "1.0Beta"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setStyle("CDE")
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
