# Li, Kaite
# kxl5704
# 2019-04-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class if_then_else_statement() :
  def __init__( self, lineNum, expression, block_statement_then, block_statement_else) :
    self.m_NodeType = 'if_then_statement'
    self.m_LineNum = lineNum
    self.m_expression = expression
    self.m_block_statement_then = block_statement_then
    self.m_block_statement_else = block_statement_else
    self.content = 'STATEMENT (IF-THEN)'
#---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine(indent, self.m_LineNum,self.content, fp)
    self.m_expression.dump(indent+1, fp=fp)
    self.m_block_statement_then.dump(indent+1, fp=fp)
    self.m_block_statement_else.dump(indent+1, fp=fp)

#---------#---------#---------#---------#---------#--------#
