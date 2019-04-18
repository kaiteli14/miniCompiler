# Li, Kaite
# kxl5704
# 2019-04-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class type() :
  def __init__(self, lineNum, type):
    self.m_NodeType = 'TYPE'
    self.m_LineNum = lineNum
    self.m_Type = type
    self.content = 'TYPE (NAME)' + f'{self.m_Type!r}'


#---------------------------------------
  def dump(self, indent=0, fp=sys.stdout):
    dumpHeaderLine(indent, self.m_LineNum, self.content, fp)


#---------#---------#---------#---------#---------#--------#
