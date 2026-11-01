"""Fixed arithmetic worker. Never eval/exec arbitrary source."""
import ast,operator,sys
try:
 import resource
 resource.setrlimit(resource.RLIMIT_CPU,(1,1))
 resource.setrlimit(resource.RLIMIT_AS,(128*1024*1024,128*1024*1024))
 resource.setrlimit(resource.RLIMIT_FSIZE,(0,0))
except ImportError:pass
expression=sys.stdin.read(201)
if len(expression)>200:raise ValueError('too long')
tree=ast.parse(expression,mode='eval')
if len(list(ast.walk(tree)))>50:raise ValueError('too complex')
ops={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv}
def visit(node):
 if isinstance(node,ast.Expression):return visit(node.body)
 if isinstance(node,ast.Constant) and type(node.value) in (int,float):result=node.value
 elif isinstance(node,ast.UnaryOp) and isinstance(node.op,(ast.UAdd,ast.USub)):result=visit(node.operand)*(-1 if isinstance(node.op,ast.USub) else 1)
 elif isinstance(node,ast.BinOp) and type(node.op) in ops:result=ops[type(node.op)](visit(node.left),visit(node.right))
 else:raise ValueError('unapproved arithmetic')
 if not -1e12<=result<=1e12:raise ValueError('magnitude exceeded')
 return result
print(visit(tree))
