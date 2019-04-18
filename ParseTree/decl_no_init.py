# Li, Kaite
# kxl5704
# 2019-04-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class decl_no_init() :
  def __init__( self, lineNum, identifier, type, non_init):
    self.m_NodeType = 'decl'
    self.m_LineNum = lineNum
    self.ID = identifier.m_ID
    self.content = 'DECLARATION ' + non_init + ' ID(\'' + self.ID + '\')'
    self.type = type

#---------------------------------------
  def dump(self, indent=0, fp=sys.stdout):
    dumpHeaderLine(indent, self.m_LineNum, self.content, fp)
    self.type.dump(indent+1, fp=fp)

#---------#---------#---------#---------#---------#--------#
