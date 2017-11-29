class Expr:
    
    def all_instantiations(self, all_vars):
      if all_vars == []:
          return [{}]
      else:
          return [dict(i, **{all_vars[-1]:True}) for i in self.all_instantiations(all_vars[:-1])] + [dict(i, **{all_vars[-1]:False}) for i in self.all_instantiations(all_vars[:-1])]

    def isTauto(self):
        all_vars = self._collect_vars()
        all_instantiations = self.all_instantiations(list(all_vars))
        for instantiation in all_instantiations:
            if not self.eval(instantiation):
                return False  
        return True
         
class Var(Expr):
    def __init__(self, var):
        self.var = var

    def __str__(self):
        return self.var

    def eval(self, instantiation):
        # No check to ensure that the variable is actually instantiated.
        return instantiation[self.var]

    def _collect_vars(self):
        return set(self.var)

class Not(Expr):
    def __init__(self, expr):
        self.expr = expr

    def __str__(self) :
        if isinstance(self.expr, And) or isinstance(self.expr, Or):
            # Sine NOT bind stronger than both AND and OR the self.expr need brackets() around it
            return  f"!({self.expr})" 
        else:  # When type(self.expr) is NOT or VAR
            return f"!{self.expr}"

    def eval(self, instantiation):
        return not self.expr.eval(instantiation)

    def _collect_vars(self):
        return self.expr._collect_vars()

class TwoExpr(Expr):
    def __init__(self, l_expr, r_expr):
        self.l_expr = l_expr
        self.r_expr = r_expr

    def eval(self, instantiation):
        return self.operation(self.l_expr.eval(instantiation), self.r_expr.eval(instantiation))
    
    def _collect_vars(self):
        return self.l_expr._collect_vars() | self.r_expr._collect_vars()

class And(TwoExpr):
    def __str__(self):
        if (isinstance(self.l_expr, Or) or isinstance(self.l_expr, And)) and isinstance(self.r_expr, Or):
            return f"({self.l_expr})&({self.r_expr})"
        elif isinstance(self.l_expr, Or) or isinstance(self.l_expr, And):
            # As AND bind stronger than OR , and AND are right associative
            return f"({self.l_expr})&{self.r_expr}"
        elif isinstance(self.r_expr, Or):  # As AND bind stronger than OR
            return f"{self.l_expr}&({self.r_expr})"
        else:
            return f"{self.l_expr}&{self.r_expr}"

    def operation(self, l, r):
        return l and r

class Or(TwoExpr):
    def __str__(self):
        if isinstance(self.l_expr, Or):
        # Since OR are right associative it need () when left side of the branch
            return f"({self.l_expr})|{self.r_expr}"
        else:
            return f"{self.l_expr}|{self.r_expr}"

    def operation(self, l, r):
        return l or r


e000 = Var("x")
e00 = Not(Var("x"))
e0 = Not(Not(Var("x")))
e = And(Var("x"),Not(Var("y")))

e1 = Or(Var("x"),Not(Var("x")))
def Equiv(p,q) :
    return Or(And(p,q),And(Not(p),Not(q)))
e2 = Equiv(Var("x"),Not(Not(Var("x"))))
e3 = Equiv(Not(And(Var("x"),Var("y"))),Or(Not(Var("x")),Not(Var("y"))))
e4 = Equiv(Not(And(Var("x"),Var("y"))),And(Not(Var("x")),Not(Var("y"))))

t1= And(Var("x"),And(Var("y"),Var("z")))
t2= And(And(Var("x"),Var("y")),Var("z"))

# Test printing.
print("\nPrinting Tests")
print("e1: ",e1)
print("e2: ",e2)
print("e3: ",e3)
print("e4: ",e4)

# Test evaluating.
print("\nEval Tests")
print("e2: ",e2.eval({"x" : True}))
print("e3: ",e3.eval({"x" : True, "y" : True}))
print("e4: ",e4.eval({"x" : False, "y" : True}))

# Test tautology.
print("\nTautology Tests")
print("e1: ",e1.isTauto())
print("e2: ",e2.isTauto())
print("e3: ",e3.isTauto())
print("e4: ",e4.isTauto())



