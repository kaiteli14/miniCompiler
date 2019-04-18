# Li, Kaite
# kxl5704
# 2019-04-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class write_statement() :
  def __init__( self, lineNum, string_list) :
    self.m_NodeType = 'write_statement'
    self.m_LineNum = lineNum
    self.m_string_list = string_list
    self.m_string_list_size = len(string_list)

#---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine(indent, self.m_LineNum,
    f'STATEMENT(WRITE)<{self.m_string_list_size!r}>', fp)
    for m in self.m_string_list:
      m.dump(indent+1, fp=fp)

#---------#---------#---------#---------#---------#--------#
