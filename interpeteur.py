class I:
    MUL = "mul"
    ADD = "add"
    PRINT = "print"
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
    POW = "pow"
    LOOP = "loop"

class Interpretor:
    def __init__(self, debug_mode=False):
        self.memoire = {}
        self.debug_mode = debug_mode
    def run(self, code):
        for commande in code:
            if self.debug_mode:
                print(f"MEMOIRE = {self.memoire} COMMANDE : {commande}")
            match commande:
                case I.ADD, var1, var2, store: 
                    if self.memoire[var1][1] == self.memoire[var2][1] == I.INT:
                        self.memoire[store] = [self.memoire[var1][0] + self.memoire[var2][0], I.INT]
                case I.MUL, var1, var2, store:
                    if self.memoire[var1][1] == self.memoire[var2][1] == I.INT:
                        self.memoire[store] = [self.memoire[var1][0] * self.memoire[var2][0], I.INT]
                case I.PRINT, id_memoire, end:
                    print(self.memoire[id_memoire], end=end)
                case I.PRINT, id_memoire:
                    print(self.memoire[id_memoire])
                case I.DEFINE_INT, id_memoire, value:
                    self.memoire[id_memoire] = [int(value), I.INT]
                case I.DEF_FUNCTION, name, code:
                    self.memoire[name] = [code, I.FUNCTION]
                case I.FUNCTION, name:
                    self.run(self.memoire[name][0])
                case I.IF, condition, code:
                    match condition:
                        case I.EQUAL, var1, var2:
                            if self.memoire[var1][1] == self.memoire[var2][1] == I.INT:
                                if self.memoire[var1][0] == self.memoire[var2][0]:
                                    self.run(code)
                        case I.NOT_EQUAL, var1, var2:
                            if self.memoire[var1][1] == self.memoire[var2][1] == I.INT:
                                if self.memoire[var1][0] != self.memoire[var2][0]:
                                    self.run(code)
                        case I.LESS, var1, var2:
                            if self.memoire[var1][1] == self.memoire[var2][1] == I.INT:
                                if self.memoire[var1][0] < self.memoire[var2][0]:
                                    self.run(code)
                        case I.LESS_EQUAL, var1, var2:
                            if self.memoire[var1][1] == self.memoire[var2][1] == I.INT:
                                if self.memoire[var1][0] <= self.memoire[var2][0]:
                                    self.run(code)
                        case I.GREATER, var1, var2:
                            if self.memoire[var1][1] == self.memoire[var2][1] == I.INT:
                                if self.memoire[var1][0] > self.memoire[var2][0]:
                                    self.run(code)
                        case I.GREATER_EQUAL, var1, var2:
                            if self.memoire[var1][1] == self.memoire[var2][1] == I.INT:
                                if self.memoire[var1][0] >= self.memoire[var2][0]:
                                    self.run(code)
                case I.POW, var1, var2, store:
                    if self.memoire[var1][1] == self.memoire[var2][1] == I.INT:
                        self.memoire[store] = [self.memoire[var1][0] ** self.memoire[var2][0], I.INT]
                case I.LOOP, nb, code:
                    if self.memoire[nb][1] == I.INT:
                        for _ in range(self.memoire[nb][0]-1):
                            self.run(code)
if __name__ == "__main__":
    code = [(I.DEFINE_INT, "a", "2"), 
            (I.DEFINE_INT, "b", "6"),
            (I.DEF_FUNCTION, "double", [(I.ADD, "a", "a", "a")]),
            (I.LOOP, "b", [(I.FUNCTION, "double")]),
            (I.PRINT, "a"),
            ]
    Interpretor(debug_mode=False).run(code)