# Li, Kaite
# kxl5704
# 2019-04-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class decl() :
  def __init__( self, lineNum, ID, type, init, number):
    self.m_NodeType = 'decl'
    self.m_LineNum = lineNum
    self.ID = ID
    self.content = 'DECLARATION ' + init + ' ID(\'' + self.ID + '\')'
    self.type = type
    self.number = number

#---------------------------------------
  def dump(self, indent=0, fp=sys.stdout):
    dumpHeaderLine(indent, self.m_LineNum, self.content, fp)
    self.type.dump(indent+1, fp=fp)
    self.number.dump(indent+1, fp=fp)
#---------#---------#---------#---------#---------#--------#
