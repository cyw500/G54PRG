class Expr:
    
    def isTauto():
        pass
         
class Not(Expr):
     
    def __init__(self, Expr):
        self.Expr = Expr

    def __str__(self) :
        if isinstance(self.Expr, And) or isinstance(self.Expr, Or):
            # As Not bind stronger than both And and Or
            return  "!(" + str(self.Expr) + ")" 
        else:
            return "!" + str(self.Expr)

    def eval(self,d):
            return not d[str(self.Expr)]

    
class And(Expr):
    
    def __init__(self, LeftExpr, RightExpr):
        self.LeftExpr = LeftExpr
        self.RightExpr = RightExpr
        
    def __str__(self):
        if isinstance(self.LeftExpr, Or):  # As And bind stronger than Or
            return  "(" + str(self.LeftExpr) + ")&" + str(self.RightExpr)
        if isinstance(self.RightExpr, Or):  # As And bind stronger than Or
            return  str(self.LeftExpr) + "&(" + str(self.RightExpr) + ")"
        if isinstance(self.LeftExpr, And):  # As And are right associative
            return  "(" + str(self.LeftExpr) + ")&" + str(self.RightExpr)
        else:
            return  str(self.LeftExpr) + "&" + str(self.RightExpr)
        
class Or(Expr):
    
    def __init__(self, LeftExpr, RightExpr):
        self.LeftExpr = LeftExpr
        self.RightExpr = RightExpr     

    def __str__(self):
        if isinstance(self.LeftExpr, Or):  # As Or are right associative
            return  "(" + str(self.LeftExpr) + ")&" + str(self.RightExpr)
        else:
            return   str(self.LeftExpr) + "|" + str(self.RightExpr)        
        
class Var(Expr):
    
    def __init__(self, Var):
        self.Var = Var

    def __str__(self):
        return self.Var

    def eval(self,d):
        return d[self.Var]

def Equiv(p,q) :
    return Or(And(p,q),And(Not(p),Not(q)))

e00 = Var("x")
e0 = Not(Var("x"))
e = And(Var("x"),Not(Var("y")))
e1 = Or(Var("x"),Not(Var("x")))
e2 = Equiv(Var("x"),Not(Not(Var("x"))))
e3 = Equiv(Not(And(Var("x"),Var("y"))),Or(Not(Var("x")),Not(Var("y"))))
e4 = Equiv(Not(And(Var("x"),Var("y"))),And(Not(Var("x")),Not(Var("y"))))


