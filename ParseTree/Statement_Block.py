# Dalio, Brian A.
# dalioba
# 2019-02-27
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Statement_Block() :
  def __init__( self, lineNum, statementList) :
    self.m_NodeType = 'Statement_Block'
    self.m_LineNum  = lineNum
    # self.m_Expr     = expr
    self.m_StatementList = statementList
    self.content = 'STATEMENT (BLOCK) <'+str(len(statementList))+'>'
#---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,self.content, fp)
    for m_Expr in self.m_StatementList:
      m_Expr.dump(indent+1, fp=fp)

#---------#---------#---------#---------#---------#--------#
