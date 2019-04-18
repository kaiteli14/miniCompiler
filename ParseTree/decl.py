# Li, Kaite
# kxl5704
# 2019-04-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class decl() :
  def __init__( self, lineNum, identifier, INT_LITERAL):
    self.m_NodeType = 'decl'
    self.m_LineNum = lineNum
    self.ID = identifier.m_ID
    self.number = str(INT_LITERAL)
    self.content = 'DECLARATION '

#---------------------------------------
  def dump(self, indent=0, fp=sys.stdout):
    dumpHeaderLine(indent, self.m_LineNum, self.content, fp)


#---------#---------#---------#---------#---------#--------#
