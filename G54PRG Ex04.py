class Expr:
    pass
         
class Not(Expr):
     
    def __init__(self, p):
        self.p = p

    def __str__(self) :
        if type(self.p) == Or:
            return "!(" + str(self.p) + ")"
        else:
            return "!" + str(self.p)

    
class And(Expr):
    
    def __init__(self, p, q):
        self.p = p
        self.q = q
        
    def __str__(self):
        return  str(self.p) + "&" + str(self.q)   
        
class Or(Expr):
    
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __str__(self):
        return  str(self.p) + "|" + str(self.q)
        
class Var(Expr):
    
    def __init__(self, var):
        self.var = var

    def __str__(self):
        return self.var

def Equiv(p , q):    
    return Or(And(str(p) ,str(q)),And(Not(str(p)) ,Not(str(q))))

e1 = Or(Var("x"),Not(Var("x")))
e2 = Equiv(Var("x"),Not(Not(Var("x"))))
e3 = Equiv(Not(And(Var("x"),Var("y"))),Or(Not(Var("x")),Not(Var("y"))))
e4 = Equiv(Not(And(Var("x"),Var("y"))),And(Not(Var("x")),Not(Var("y"))))



