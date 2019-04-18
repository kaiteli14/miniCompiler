# Li, Kaite
# kxl5704
# 2019-04-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class write_statement() :
  def __init__( self, lineNum, expression_opt) :
    self.m_NodeType = 'write_statement'
    self.m_LineNum = lineNum
    self.m_expression_opt = expression_opt
    self.m_expression_opt_size = len(expression_opt)
    self.content = 'STATEMENT(WRITE)<' + self.m_expression_opt_size +'>'
#---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine(indent, self.m_LineNum,self.content, fp)
    for m in self.m_expression_opt:
      m.dump(indent+1, fp=fp)

#---------#---------#---------#---------#---------#--------#
