class Expr:
    
    def isTauto(self):
        for x in [True,False]:
            for y in [True,False]:
                if not self.eval({"x":x,"y":y}) :
                    return False
        return True

         
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
        return not self.Expr.eval(d)

    def checkvar(self):
        pass

    
class And(Expr):
    
    def __init__(self, LeftExpr, RightExpr):
        self.LeftExpr = LeftExpr
        self.RightExpr = RightExpr
        
    def __str__(self):
        if isinstance(self.LeftExpr, Or):  # As And bind stronger than Or
            return "(" + str(self.LeftExpr) + ")&" + str(self.RightExpr)
        if isinstance(self.RightExpr, Or):  # As And bind stronger than Or
            return str(self.LeftExpr) + "&(" + str(self.RightExpr) + ")"
        if isinstance(self.LeftExpr, And):  # As And are right associative
            return "(" + str(self.LeftExpr) + ")&" + str(self.RightExpr)
        else:
            return str(self.LeftExpr) + "&" + str(self.RightExpr)

    def eval(self,d):
        return self.LeftExpr.eval(d) and self.RightExpr.eval(d)
        
class Or(Expr):
    
    def __init__(self, LeftExpr, RightExpr):
        self.LeftExpr = LeftExpr
        self.RightExpr = RightExpr     

    def __str__(self):
        if isinstance(self.LeftExpr, Or):  # As Or are right associative
            return "(" + str(self.LeftExpr) + ")&" + str(self.RightExpr)
        else:
            return str(self.LeftExpr) + "|" + str(self.RightExpr)

    def eval(self,d):
        return self.LeftExpr.eval(d) or self.RightExpr.eval(d)
            # calling the things(left and right expressions) recursively untill it reach the var.eval(e?)

    def checkvar():
        pass
        
class Var(Expr):
    
    def __init__(self, Var):
        self.Var = Var

    def __str__(self):
        return self.Var

    def eval(self,d):
        return d[self.Var]

    def checkvar(self):
        pass 

def Equiv(p,q) :
    return Or(And(p,q),And(Not(p),Not(q)))


e000 = Var("x")
e00 = Not(Var("x"))
e0 = Not(Not(Var("x")))
e = And(Var("x"),Not(Var("y")))

e1 = Or(Var("x"),Not(Var("x")))
e2 = Equiv(Var("x"),Not(Not(Var("x"))))
e3 = Equiv(Not(And(Var("x"),Var("y"))),Or(Not(Var("x")),Not(Var("y"))))
e4 = Equiv(Not(And(Var("x"),Var("y"))),And(Not(Var("x")),Not(Var("y"))))

t1= And(Var("x"),And(Var("y"),Var("z")))
t2= And(And(Var("x"),Var("y")),Var("z"))



