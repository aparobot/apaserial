# -*- coding: utf-8 -*-
from icons import *
from PyQt4 import QtGui

def initToolBar(self):
    tb = QtGui.QToolBar(self)
    self.addToolBar(tb)
    
    self.ui.save_action = QtGui.QAction(QtGui.QIcon(":/app/icons/app/save.png"),
        u"保存接收到的数据", self, priority=QtGui.QAction.LowPriority, triggered = self.onSaveData)
    self.ui.about_action = QtGui.QAction(QtGui.QIcon(":/app/icons/app/about.png"),
        u"关于", self, priority=QtGui.QAction.LowPriority, triggered=self.onAbout)
    self.ui.github_action = QtGui.QAction(QtGui.QIcon(":/app/icons/app/github.png"),
        u"github开源地址", self, priority=QtGui.QAction.LowPriority, triggered=self.onOpenGithubProj)

    tb.addAction(self.ui.save_action)
    tb.addAction(self.ui.about_action)
    tb.addAction(self.ui.github_action)