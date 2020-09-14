import os, time
from datetime import datetime
import sys
print (os.path.abspath(__file__))
print (os.path.dirname(__file__))
print (os.pardir)

now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
now1 = datetime.now().strftime("%Y")
# print (now)
# print (now1)

path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
print (path)
# path1 = sys.path()
# print (os.pardir)