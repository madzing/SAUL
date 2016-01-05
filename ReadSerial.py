#!/usr/bin/python3
# get lines of text from serial port, save them to a file

import serial, io
import threading
class ReadSerial(threading.Thread):
    def __init__(self,addr,baud,fname,fmode):
        super(ReadSerial,self).__init__()
        self._end = threading.Event()
        self.addr  = addr  # serial port to read data from
        self.baud  = baud            # baud rate for serial port
        self.fname = fname   # log file to save data in
        self.fmode = fmode             # log file mode = append

    def run(self):
        with serial.Serial(self.addr,self.baud) as pt, open(self.fname,self.fmode) as outf:
            spb = io.TextIOWrapper(io.BufferedRWPair(pt,pt,1),
                encoding='ascii', errors='ignore', newline='\r',line_buffering=True)
            spb.readline()  # throw away first line; likely to start mid-sentence (incomplete)

            while (not self._end.isSet()):
                x = spb.readline()      # read one line of text from serial port
                if '$GPRMC' in x:
                    x = x.strip('\r\n')
                    #print (x)           # echo line of text on-screen
                    outf.write(x)       # write line of text to file
                    outf.flush()        # make sure it actually gets written out

    def stop(self):
        self._end.set()
