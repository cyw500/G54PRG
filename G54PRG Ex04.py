class Expr:
    def allInstantiations(self, allVars):
        # creat a list containing dictionaries with all variable with all combination of True & False
        if allVars == []:
            return [{}]
        else:
            return [dict(i, **{allVars[-1]:True}) for i in self.allInstantiations(allVars[:-1])] + [dict(i, **{allVars[-1]:False}) for i in self.allInstantiations(allVars[:-1])]

    def isTauto(self):
        for instantiation in self.allInstantiations(list(self.collectVars())):
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

    def collectVars(self):
        return set(self.var)

class Not(Expr):
    def __init__(self, expr):
        self.expr = expr

    def __str__(self) :
        if isinstance(self.expr, TwoExpr):
            # Since NOT bind stronger than both And and Or the self.expr need brackets() around them
            return f"!({self.expr})" 
        else:  # When type(self.expr) is Not or Var
            return f"!{self.expr}"

    def eval(self, instantiation):
        return not self.expr.eval(instantiation)

    def collectVars(self):
        return self.expr.collectVars()

class TwoExpr(Expr):
    def __init__(self, l_expr, r_expr):
        self.l_expr = l_expr
        self.r_expr = r_expr
 
    def collectVars(self):
        return self.l_expr.collectVars() | self.r_expr.collectVars()

class And(TwoExpr):
    def __str__(self):
        if isinstance(self.l_expr, TwoExpr) and isinstance(self.r_expr, Or):
            return f"({self.l_expr})&({self.r_expr})"
        elif isinstance(self.l_expr, TwoExpr):
            # As AND bind stronger than OR , and AND are right associative
            return f"({self.l_expr})&{self.r_expr}"
        elif isinstance(self.r_expr, Or):  # As AND bind stronger than OR
            return f"{self.l_expr}&({self.r_expr})"
        else:
            return f"{self.l_expr}&{self.r_expr}"

    def eval (self, instantiation):
        return self.l_expr.eval(instantiation) and self.r_expr.eval(instantiation)

class Or(TwoExpr):
    def __str__(self):
        if isinstance(self.l_expr, Or):
        # Since OR are right associative it need () when left side of the branch
            return f"({self.l_expr})|{self.r_expr}"
        else:
            return f"{self.l_expr}|{self.r_expr}"

    def eval (self, instantiation):
        return self.l_expr.eval(instantiation) or self.r_expr.eval(instantiation)




e1 = Or(Var("x"),Not(Var("x")))
def Equiv(p,q) :
    return Or(And(p,q),And(Not(p),Not(q)))
e2 = Equiv(Var("x"),Not(Not(Var("x"))))
e3 = Equiv(Not(And(Var("x"),Var("y"))),Or(Not(Var("x")),Not(Var("y"))))
e4 = Equiv(Not(And(Var("x"),Var("y"))),And(Not(Var("x")),Not(Var("y"))))

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



