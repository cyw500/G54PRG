class Expr:
    pass
         
class Not(Expr):
     
    def __init__(self, var):
        self.var = var

    def __str__(self) :
        if isinstance(self.var, And) or isinstance(self.var, Or):
            return  "!(" + str(self.var) + ")" 
        else:
            return "!" + str(self.var)

    
class And(Expr):
    
    def __init__(self, p, q):
        self.p = p
        self.q = q
        
    def __str__(self):

        if isinstance(self.p, Or):
            return  "(" + str(self.p) + ")&" + str(self.q)
        if isinstance(self.q, Or):
            return  str(self.p) + "&(" + str(self.q) + ")"
        else:
            return  str(self.p) + "&" + str(self.q) 
        
class Or(Expr):
    
    def __init__(self, p, q):
        self.p = p
        self.q = q     

    def __str__(self):
            return   str(self.p) + "|" + str(self.q)
        
        
class Var(Expr):
    
    def __init__(self, var):
        self.var = var

    def __str__(self):
        return self.var

def Equiv(p,q) :
    return Or(And(p,q),And(Not(p),Not(q)))

e1 = Or(Var("x"),Not(Var("x")))
e2 = Equiv(Var("x"),Not(Not(Var("x"))))
e3 = Equiv(Not(And(Var("x"),Var("y"))),Or(Not(Var("x")),Not(Var("y"))))
e4 = Equiv(Not(And(Var("x"),Var("y"))),And(Not(Var("x")),Not(Var("y"))))



