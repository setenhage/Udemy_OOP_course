# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 09:53:50 2020

OOP - Assignment 2 - Inheritance
@author: Suzanne
"""

import abc
import datetime

class WriteFile(object):
    __metaclass__ = abc.ABCMeta #make this class an abstract class
    
    def __init__(self, filename):
        self.fname = filename
        
    @abc.abstractmethod
    def write (self):
        return
    
    def write_line(self, text):
        fh = open(self.fname, 'a')
        fh.write(text + '\n')
        fh.close()

class LogFile(WriteFile): 

    def write(self, mystring):
        #Create log message with time stamp 
        dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        self.write_line('{0}    {1}'.format(dt_str, mystring))

class DelimFile(WriteFile):
    def __init__(self, filename, delim): 
        #super is used for inheritence of the constructor
        super(DelimFile, self).__init__(filename)
        self.delim = delim
    
    def write(self, mylist):
        #create line with list content seperated by delim
        this_line = self.delim.join(mylist)
        self.write_line(this_line)


#Test code
log = LogFile('log.txt')
mydelim = DelimFile('data.csv',',')

log.write('this is a log message')
log.write('this is another log message')

mydelim.write(['a','b','c','d'])
mydelim.write(['1','2','3','4'])
