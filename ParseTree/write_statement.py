# Li, Kaite
# kxl5704
# 2019-04-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class write_statement() :
  def __init__( self, lineNum, expression, block_statement) :
    self.m_NodeType = 'while_statement'
    self.m_LineNum = lineNum
    self.m_expression = expression
    self.m_block_statement = block_statement

    self.content = 'STATEMENT(WHILE)'
#---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine(indent, self.m_LineNum,self.content, fp)
    self.m_expression.dump(indent+1, fp=fp)
    self.m_block_statement.dump(indent+1, fp=fp)

#---------#---------#---------#---------#---------#--------#
