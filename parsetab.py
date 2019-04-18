
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programrightEQUALSleftORleftANDleftIS_EQNOT_EQleftLESSLESS_EQGREATERGREATER_EQleftPLUSMINUSleftTIMESDIVIDEMODULUSrightEXPONENTleftUMINUSNOTAND COLON DIVIDE EQUALS EXPONENT GREATER GREATER_EQ ID IF INT INT_LITERAL IS_EQ LBRACE LESS LESS_EQ LPAREN MINUS MODULUS NOT NOT_EQ OR PLUS RBRACE RPAREN SEMICOLON TIMESprogram : block_statementsemicolon_opt : epsilon\n                     | SEMICOLONblock_statement : LBRACE statement_decl_list semicolon_opt RBRACEstatement : expressionstatement : block_statement\n                 | if_then_statementstatement_decl_list : statement_decl_list SEMICOLON statement_declstatement_decl_list : statement_declstatement_decl_list : epsilonstatement_decl : statement\n                      | decldecl : ID COLON type InitiationInitiation : EQUALS expressionInitiation : epsilonif_then_statement : IF expression block_statementidentifier : IDtype : INTexpression : PLUS expression %prec UMINUS\n                  | MINUS expression %prec UMINUS\n                  | NOT expressionexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression EXPONENT expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression MODULUS expression\n                  | expression LESS expression\n                  | expression LESS_EQ expression\n                  | expression GREATER expression\n                  | expression GREATER_EQ expression\n                  | expression IS_EQ expression\n                  | expression NOT_EQ expression\n                  | expression AND expression\n                  | expression OR expression\n                  | identifier EQUALS expressionexpression : LPAREN expression RPARENexpression : INT_LITERALlvalue : identifierexpression : lvalueepsilon :'
    
_lr_action_items = {'LBRACE':([0,3,16,18,19,22,39,40,41,42,45,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,],[3,3,-39,-38,-40,3,-19,-17,-20,-21,3,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,]),'$end':([1,2,46,],[0,-1,-4,]),'SEMICOLON':([3,4,5,6,7,8,9,10,11,12,16,18,19,39,40,41,42,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,],[-41,22,-9,-10,-11,-12,-5,-6,-7,-17,-39,-38,-40,-19,-17,-20,-21,-4,-8,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-41,-18,-36,-37,-16,-13,-15,-14,]),'RBRACE':([3,4,5,6,7,8,9,10,11,12,16,18,19,21,22,23,39,40,41,42,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,],[-41,-41,-9,-10,-11,-12,-5,-6,-7,-17,-39,-38,-40,46,-3,-2,-19,-17,-20,-21,-4,-8,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-41,-18,-36,-37,-16,-13,-15,-14,]),'ID':([3,13,14,15,17,20,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,43,68,],[12,40,40,40,40,40,12,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'PLUS':([3,9,12,13,14,15,16,17,18,19,20,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40,41,42,43,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,68,70,],[13,24,-17,13,13,13,-39,13,-38,-40,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,-19,-17,-20,-21,13,24,24,-22,-23,-24,-25,-26,-27,24,24,24,24,24,24,24,24,24,-37,13,24,]),'MINUS':([3,9,12,13,14,15,16,17,18,19,20,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40,41,42,43,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,68,70,],[14,25,-17,14,14,14,-39,14,-38,-40,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,-19,-17,-20,-21,14,25,25,-22,-23,-24,-25,-26,-27,25,25,25,25,25,25,25,25,25,-37,14,25,]),'NOT':([3,13,14,15,17,20,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,43,68,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'LPAREN':([3,13,14,15,17,20,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,43,68,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'INT_LITERAL':([3,13,14,15,17,20,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,43,68,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'IF':([3,22,],[20,20,]),'EXPONENT':([9,12,16,18,19,39,40,41,42,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,70,],[26,-17,-39,-38,-40,-19,-17,-20,-21,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-37,26,]),'TIMES':([9,12,16,18,19,39,40,41,42,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,70,],[27,-17,-39,-38,-40,-19,-17,-20,-21,27,27,27,27,-24,-25,-26,-27,27,27,27,27,27,27,27,27,27,-37,27,]),'DIVIDE':([9,12,16,18,19,39,40,41,42,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,70,],[28,-17,-39,-38,-40,-19,-17,-20,-21,28,28,28,28,-24,-25,-26,-27,28,28,28,28,28,28,28,28,28,-37,28,]),'MODULUS':([9,12,16,18,19,39,40,41,42,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,70,],[29,-17,-39,-38,-40,-19,-17,-20,-21,29,29,29,29,-24,-25,-26,-27,29,29,29,29,29,29,29,29,29,-37,29,]),'LESS':([9,12,16,18,19,39,40,41,42,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,70,],[30,-17,-39,-38,-40,-19,-17,-20,-21,30,30,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,30,30,30,30,30,-37,30,]),'LESS_EQ':([9,12,16,18,19,39,40,41,42,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,70,],[31,-17,-39,-38,-40,-19,-17,-20,-21,31,31,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,31,31,31,31,31,-37,31,]),'GREATER':([9,12,16,18,19,39,40,41,42,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,70,],[32,-17,-39,-38,-40,-19,-17,-20,-21,32,32,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,32,32,32,32,32,-37,32,]),'GREATER_EQ':([9,12,16,18,19,39,40,41,42,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,70,],[33,-17,-39,-38,-40,-19,-17,-20,-21,33,33,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,33,33,33,33,33,-37,33,]),'IS_EQ':([9,12,16,18,19,39,40,41,42,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,70,],[34,-17,-39,-38,-40,-19,-17,-20,-21,34,34,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,34,34,34,-37,34,]),'NOT_EQ':([9,12,16,18,19,39,40,41,42,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,70,],[35,-17,-39,-38,-40,-19,-17,-20,-21,35,35,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,35,35,35,-37,35,]),'AND':([9,12,16,18,19,39,40,41,42,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,70,],[36,-17,-39,-38,-40,-19,-17,-20,-21,36,36,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,36,36,-37,36,]),'OR':([9,12,16,18,19,39,40,41,42,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,70,],[37,-17,-39,-38,-40,-19,-17,-20,-21,37,37,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,37,-37,37,]),'COLON':([12,],[38,]),'EQUALS':([12,16,40,62,63,],[-17,43,-17,68,-18,]),'RPAREN':([16,18,19,39,40,41,42,44,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,],[-39,-38,-40,-19,-17,-20,-21,65,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,]),'INT':([38,],[63,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'block_statement':([0,3,22,45,],[2,10,10,66,]),'statement_decl_list':([3,],[4,]),'statement_decl':([3,22,],[5,47,]),'epsilon':([3,4,62,],[6,23,69,]),'statement':([3,22,],[7,7,]),'decl':([3,22,],[8,8,]),'expression':([3,13,14,15,17,20,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,43,68,],[9,39,41,42,44,45,9,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,70,]),'if_then_statement':([3,22,],[11,11,]),'identifier':([3,13,14,15,17,20,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,43,68,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'lvalue':([3,13,14,15,17,20,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,43,68,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'semicolon_opt':([4,],[21,]),'type':([38,],[62,]),'Initiation':([62,],[67,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> block_statement','program',1,'p_program','miniFrontEnd.py',132),
  ('semicolon_opt -> epsilon','semicolon_opt',1,'p_semicolon_opt','miniFrontEnd.py',137),
  ('semicolon_opt -> SEMICOLON','semicolon_opt',1,'p_semicolon_opt','miniFrontEnd.py',138),
  ('block_statement -> LBRACE statement_decl_list semicolon_opt RBRACE','block_statement',4,'p_block_statement','miniFrontEnd.py',145),
  ('statement -> expression','statement',1,'p_statement_expr','miniFrontEnd.py',150),
  ('statement -> block_statement','statement',1,'p_statement_A','miniFrontEnd.py',154),
  ('statement -> if_then_statement','statement',1,'p_statement_A','miniFrontEnd.py',155),
  ('statement_decl_list -> statement_decl_list SEMICOLON statement_decl','statement_decl_list',3,'p_statement_decl_list_A','miniFrontEnd.py',164),
  ('statement_decl_list -> statement_decl','statement_decl_list',1,'p_statement_decl_list_B','miniFrontEnd.py',169),
  ('statement_decl_list -> epsilon','statement_decl_list',1,'p_statement_decl_list_C','miniFrontEnd.py',173),
  ('statement_decl -> statement','statement_decl',1,'p_statement_decl','miniFrontEnd.py',178),
  ('statement_decl -> decl','statement_decl',1,'p_statement_decl','miniFrontEnd.py',179),
  ('decl -> ID COLON type Initiation','decl',4,'p_decl','miniFrontEnd.py',184),
  ('Initiation -> EQUALS expression','Initiation',2,'p_with_initiation','miniFrontEnd.py',191),
  ('Initiation -> epsilon','Initiation',1,'p_no_initiation','miniFrontEnd.py',195),
  ('if_then_statement -> IF expression block_statement','if_then_statement',3,'p_if_then_statement_A','miniFrontEnd.py',199),
  ('identifier -> ID','identifier',1,'p_identifier','miniFrontEnd.py',207),
  ('type -> INT','type',1,'p_type','miniFrontEnd.py',211),
  ('expression -> PLUS expression','expression',2,'p_expression_uniop','miniFrontEnd.py',220),
  ('expression -> MINUS expression','expression',2,'p_expression_uniop','miniFrontEnd.py',221),
  ('expression -> NOT expression','expression',2,'p_expression_uniop','miniFrontEnd.py',222),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','miniFrontEnd.py',228),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','miniFrontEnd.py',229),
  ('expression -> expression EXPONENT expression','expression',3,'p_expression_binop','miniFrontEnd.py',230),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','miniFrontEnd.py',231),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','miniFrontEnd.py',232),
  ('expression -> expression MODULUS expression','expression',3,'p_expression_binop','miniFrontEnd.py',233),
  ('expression -> expression LESS expression','expression',3,'p_expression_binop','miniFrontEnd.py',234),
  ('expression -> expression LESS_EQ expression','expression',3,'p_expression_binop','miniFrontEnd.py',235),
  ('expression -> expression GREATER expression','expression',3,'p_expression_binop','miniFrontEnd.py',236),
  ('expression -> expression GREATER_EQ expression','expression',3,'p_expression_binop','miniFrontEnd.py',237),
  ('expression -> expression IS_EQ expression','expression',3,'p_expression_binop','miniFrontEnd.py',238),
  ('expression -> expression NOT_EQ expression','expression',3,'p_expression_binop','miniFrontEnd.py',239),
  ('expression -> expression AND expression','expression',3,'p_expression_binop','miniFrontEnd.py',240),
  ('expression -> expression OR expression','expression',3,'p_expression_binop','miniFrontEnd.py',241),
  ('expression -> identifier EQUALS expression','expression',3,'p_expression_binop','miniFrontEnd.py',242),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','miniFrontEnd.py',248),
  ('expression -> INT_LITERAL','expression',1,'p_expression_int_literal','miniFrontEnd.py',254),
  ('lvalue -> identifier','lvalue',1,'p_lvalue','miniFrontEnd.py',259),
  ('expression -> lvalue','expression',1,'p_expression_lvalue','miniFrontEnd.py',264),
  ('epsilon -> <empty>','epsilon',0,'p_epsilon','miniFrontEnd.py',274),
]
