import sys
import os

from AppKit import *
from PyObjCTools import AppHelper
from Foundation import NSLog

class Delegate (NSObject):
    def applicationDidFinishLaunching_(self, aNotification):
        '''Called automatically when the application has launched'''
        print("App did finish launching.")
