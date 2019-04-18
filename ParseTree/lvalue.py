# Li, Kaite
# kxl5704
# 2019-04-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class lvalue() :
  def __init__( self, lineNum, lvalue) :
    self.m_NodeType = 'Lvalue'

    self.m_LineNum  = lineNum
    self.m_lvalue    = lvalue

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine(indent, self.m_LineNum,
      f'LVALUE(NAME) ID({self.m_ID!r})', fp)

#---------#---------#---------#---------#---------#--------#
