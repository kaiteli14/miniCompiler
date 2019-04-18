# Li, Kaite
# kxl5704
# 2019-04-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class lvalue() :
  def __init__( self, lineNum, identifier) :
    self.m_NodeType = 'lvalue'

    self.m_LineNum  = lineNum
    self.m_ID    = identifier.m_ID

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine(indent, self.m_LineNum,
      f'LVALUE(NAME) ID({self.m_ID!r})', fp)

#---------#---------#---------#---------#---------#--------#
