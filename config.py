#-*- coding: utf-8 -*-

VERSION_NAME = "1.0Beta"
VERSION_CODE = 1
ABOUT_MESSAGE = u"""
版本号: %s\n2017/11/22
Apaserial 是 Aparobot 开源项目的串口调试工具
-------------------------------------------------------------------------
Aparobot是一款基于FreeRTOS的开源平衡小车
由几个科技从业爱好者利用周末时间合作开发
产品代码整洁，抽象层次良好，质量较高
通过BLE蓝牙与手机通信
手机APP开源
上位机程序使用Python开发，跨平台运行(windows, linux, mac)，代码开源
-----------------------【QQ交流群: 206772276】---------------------------

""" % VERSION_NAME

GITHUB_HOME = "https://github.com/aparobot/apaserial"
HEX_TYPE = "HEX"
PROTO_TYPE = "PB-PROTO"
ASCII_TYPE = "ASCII"

CR = "\r"
LF = "\n"
CR_LF = CR + LF
NONE = ""

SEND_DATA_TYPES = [ASCII_TYPE, HEX_TYPE, PROTO_TYPE]
RECV_DATA_TYPES = SEND_DATA_TYPES

ASCII_TAIL = [CR_LF, LF, CR, NONE]

SIGNAL_PROTO_TEMPL_SELECTED = "PROTO_TEMPL_SELECTED"

YES = "YES"
NO = "NO"

CONFIG_FILE_PATH = ".config"
PB_TEMPL_FILE    = "pbtempl.txt"
PB_SOURCE_FILE   = "proto/control_pb2.py"

DEFAULT_BAUD     = 9600
DEFAULT_BYTESIZE = 8
DEFAULT_PARTITY  = "无"
DEFAULT_STOPBITS = 1

DEFAULT_MERGE_INTERVAL = 0

DEFAULT_AUTOLINEFEED  = NO
DEFAULT_HIDERSFLAG    = YES
DEFAULT_CLEARSENTTEXT = YES
DEFAULT_SHOWSENT      = NO
DEFAULT_SENDINTERVAL  = 1000

COMSETTINGS_KEY  = "com-settings"
RECVSETTINGS_KEY = "recv-settings"
SENDSETTINGS_KEY = "send-settings"
PORT_KEY         = "port"
BAUD_KEY         = "baud"
BYTESIZE_KEY     = "bytesize"
PARITY_KEY       = "parity"
STOPBITS_KEY     = "stopbits"
RECVTYPE_KEY     = "recvtype"
AUTOLINEFEED_KEY = "autolinefeed"
HIDERSFLAG_KEY   = "hidersflag"
SENDTYPE_KEY     = "sendtype"
CLEARSENTTEXT_KEY= "clearsenttext"
SHOWSENT_KEY     = "showsent"
SENDINTERVAL_KEY = "sendinterval"
MERGE_INTERVAL_KEY = "merge-interval"

DEFAULT_CONFIG   = {
    COMSETTINGS_KEY:
    {
        PORT_KEY:     "",
        BAUD_KEY:     DEFAULT_BAUD,
        BYTESIZE_KEY: DEFAULT_BYTESIZE,
        PARITY_KEY:   DEFAULT_PARTITY,
        STOPBITS_KEY: DEFAULT_STOPBITS
    },
    RECVSETTINGS_KEY:
    {
        RECVTYPE_KEY:     ASCII_TYPE,
        AUTOLINEFEED_KEY: DEFAULT_AUTOLINEFEED,
        HIDERSFLAG_KEY:   DEFAULT_HIDERSFLAG,
        MERGE_INTERVAL_KEY: DEFAULT_MERGE_INTERVAL
    },
    SENDSETTINGS_KEY:
    {
        SENDTYPE_KEY:      ASCII_TYPE,
        CLEARSENTTEXT_KEY: DEFAULT_CLEARSENTTEXT,
        SHOWSENT_KEY:      NO,
        SENDINTERVAL_KEY:  DEFAULT_SENDINTERVAL
    }
}

import os
import json

def getConfigDict():
    if not os.path.exists(CONFIG_FILE_PATH):
        return DEFAULT_CONFIG
    
    configDict = DEFAULT_CONFIG
    try:
        jsonstr = open(CONFIG_FILE_PATH, "r").read()
        configDict = json.loads(jsonstr)
    except:
        pass
        
    return configDict
    
    
def saveSettings(configDict):
    if not isinstance(configDict, dict):
        return
    
    try:
        jsonstr = json.dumps(configDict, indent=4)
        open(CONFIG_FILE_PATH, "w").write(jsonstr)
        
    except:
        pass
        
mergeInterval = getConfigDict()[RECVSETTINGS_KEY].get(MERGE_INTERVAL_KEY, DEFAULT_MERGE_INTERVAL)
try:
    mergeInterval = int(mergeInterval)
except:
    mergeInterval = DEFAULT_MERGE_INTERVAL

