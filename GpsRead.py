#!/usr/bin/python3

###############################################################
# Script written by Jan Metzing
# Kontakt: janmetzing@gmx.de
###############################################################
import os

class GpsRead:
    _logFile = ""
    _fin = os
    _letzteDatenmenge = 0

    def __init__(self,logFile):
        self._logFile = logFile
        self._fin = open(logFile)
        for line in self._fin:
           self._fin.readline()
        statinfo = os.stat(self._logFile)
        self._letzteDatenmenge = statinfo.st_size

    def istNewData(self):
        statinfo = os.stat(self._logFile)
        if self._letzteDatenmenge < statinfo.st_size:
            self._letzteDatenmenge = statinfo.st_size
            return True
        else:
            return False

    def getNewData(self):
        latString = ""
        lonString = ""
        string = self._fin.readline()
        return string
