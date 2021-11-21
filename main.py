class I:
    MUL = "mul"
    ADD = "add"
    PRINT = "print"
    STORE = "store"
    LOAD = "load"
    DEBUG = "debug"
    DEFINE_INT = "define_int"
    INT = "int"
    DEF_FUNCTION = "def_function"
    FUNCTION = "function"
    IF = "if"
    EQUAL = "equal"
    NOT_EQUAL = "not_equal"
    LESS = "less"
    LESS_EQUAL = "less_equal"
    GREATER = "greater"
    GREATER_EQUAL = "greater_equal"

class Interpreteur:
    def __init__(self, debug_mode=False):
        self.memoire = {}
        self.debug_mode = debug_mode
    def run(self, code):
        for commande in code:
            if self.debug_mode:
                print(f"MEMOIRE = {self.memoire} COMMANDE : {commande}")
            match commande:
                case I.ADD, var1, var2, store: 
                    self.memoire[store] = [self.memoire[var1][0] + self.memoire[var2][0], I.INT]
                case I.MUL, var1, var2, store:
                    self.memoire[store] = [self.memoire[var1][0] * self.memoire[var2][0], I.INT]
                case I.PRINT, id_memoire:
                    print(self.memoire[id_memoire])
                case I.DEBUG:
                    self.debug_mode = True
                case I.DEFINE_INT, id_memoire, value:
                    self.memoire[id_memoire] = [int(value), I.INT]
                case I.DEF_FUNCTION, name, code:
                    self.memoire[name] = [code, I.FUNCTION]
                case I.FUNCTION, name:
                    self.run(self.memoire[name][0])
                case I.IF, condition, code:
                    match condition:
                        case I.EQUAL, var1, var2:
                            if self.memoire[var1][0] == self.memoire[var2][0]:
                                self.run(code)
                        case I.NOT_EQUAL, var1, var2:
                            if self.memoire[var1][0] != self.memoire[var2][0]:
                                self.run(code)
                        case I.LESS, var1, var2:
                            if self.memoire[var1][0] < self.memoire[var2][0]:
                                self.run(code)
                        case I.LESS_EQUAL, var1, var2:
                            if self.memoire[var1][0] <= self.memoire[var2][0]:
                                self.run(code)
                        case I.GREATER, var1, var2:
                            if self.memoire[var1][0] > self.memoire[var2][0]:
                                self.run(code)
                        case I.GREATER_EQUAL, var1, var2:
                            if self.memoire[var1][0] >= self.memoire[var2][0]:
                                self.run(code)

code = [(I.DEFINE_INT, "a", "4"), 
        (I.DEFINE_INT, "b", "8"), 
        (I.DEF_FUNCTION, "doubler", [(I.ADD, "a", "a", "a"), (I.PRINT, "a")]),
        (I.FUNCTION, "doubler"),
        (I.IF, [I.EQUAL, "a", "b"], [(I.FUNCTION, "doubler"), (I.PRINT, "a")]),
        (I.FUNCTION, "doubler"),
        ]
Interpreteur(debug_mode=True).run(code)