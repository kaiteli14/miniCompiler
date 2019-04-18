# Li, Kaite
# kxl5704
# 2019-04-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class read_statement() :
  def __init__( self, lineNum, lvalue_list) :
    self.m_NodeType = 'read_statement'
    self.m_LineNum = lineNum
    self.m_lv_list = lvalue_list
    self.m_lv_list_size = len(lvalue_list)

#---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout):
    dumpHeaderLine(indent, self.m_LineNum,
    f'STATEMENT (READ) <{self.m_lv_list_size!r}>', fp)
    for l in self.m_lv_list:
      l.dump(indent+1,fp=fp)


#---------#---------#---------#---------#---------#--------#
