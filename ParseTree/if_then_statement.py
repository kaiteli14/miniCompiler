# Li, Kaite
# kxl5704
# 2019-04-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class if_then_statement() :
  def __init__( self, lineNum, expression, block_statement) :
    self.m_NodeType = 'if_then_statement'
    self.m_LineNum = lineNum
    self.m_expression = expression
    self.m_block_statment = block_statement
    self.content = 'STATEMENT (IF-THEN)'
#---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine(indent, self.m_LineNum,self.content, fp)
    self.m_expression.dump(indent+1, fp=fp)
    self.m_block_statment.dump(indent+1, fp=fp)

#---------#---------#---------#---------#---------#--------#
