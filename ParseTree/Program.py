# Dalio, Brian A.
# dalioba
# 2019-02-27
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Program() :
  def __init__( self, lineNum, block ) :
    self.m_NodeType = 'Program'

    self.m_LineNum  = lineNum
    self.m_Block = block

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      'PROGRAM', fp )

    # for s in self.m_StmtList :
    #   s.dump( indent+1, fp = fp )

    # for s in self.m_StmtList :
    self.m_Block.dump( indent+1, fp = fp )


#---------#---------#---------#---------#---------#--------#
