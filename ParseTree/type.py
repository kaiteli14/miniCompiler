# Li, Kaite
# kxl5704
# 2019-04-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class type() :
  def __init__( self, lineNum):
    self.m_NodeType = 'TYPE'
    self.m_LineNum = lineNum
    self.content = 'TYPE (NAME)'+ '\'int\''


#---------------------------------------
  def dump(self, indent=0, fp=sys.stdout):
    dumpHeaderLine(indent, self.m_LineNum, self.content, fp)


#---------#---------#---------#---------#---------#--------#
