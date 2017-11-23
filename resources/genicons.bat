@echo off
genqrc.py
pyrcc4 -py2 tmp.qrc -o ../icons.py
del tmp.qrc