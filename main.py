class Interpreteur:
    def __init__(self, code, debug_mode=False):
        self.code = code
        self.stack = []
        self.debug_mode = debug_mode
    def load(self, nb):
        self.stack.append(nb)
    def add(self):
        self.stack.append(self.stack.pop() + self.stack.pop())
    def sub(self):
        self.stack.append(self.stack.pop() - self.stack.pop())
    def mul(self):
        self.stack.append(self.stack.pop() * self.stack.pop())
    def div(self):
        self.stack.append(self.stack.pop() // self.stack.pop())
    def mod(self):
        self.stack.append(self.stack.pop() % self.stack.pop())
    def print(self):
        print(self.stack.pop())
    def debug(self):
        self.debug_mode = True
    def run(self):
        for commande in self.code:
            if isinstance(commande, str):
                commande = (commande, )
            if self.debug_mode:
                print(f"stack : {self.stack} commande : {commande}")
            if commande[0] == "load":
                self.stack.append(int(commande[1]))
            elif commande[0] == "add":
                self.add()
            elif commande[0] == "sub":
                self.sub()
            elif commande[0] == "mul":
                self.mul()
            elif commande[0] == "div":
                self.div()
            elif commande[0] == "mod":
                self.mod()
            elif commande[0] == "print":
                self.print()
            elif commande[0] == "debug":
                self.debug()
            else:
                pass
code = [("load", "2"    ), ("load", "3"), ("add"), ("print")]
interpreteur = Interpreteur(code, debug_mode=False)
interpreteur.run()
#print 5