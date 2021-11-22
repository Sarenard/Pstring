class I:
    MUL = "mul"
    ADD = "add"
    PRINT = "print"
    TPRINT = "tprint"
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
    DEFINE_STR = "define_str"
    STR = "str"
    COPY_VAR = "copy_var"
    STR_INPUT = "str_input"
    INT_INPUT = "int_input"
    PRINT_RAW = "print_raw"

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
                        if self.memoire[store][1] != I.INT:
                            raise Exception("Erreur : la variable de stockage doit être un entier")
                        self.memoire[store] = [self.memoire[var1][0] + self.memoire[var2][0], I.INT]
                    if self.memoire[var1][1] == self.memoire[var2][1] == I.STR:
                        if self.memoire[store][1] != I.STR:
                            raise Exception("Erreur : la variable de stockage doit être une chaine de caractères")
                        self.memoire[store] = [self.memoire[var1][0] + self.memoire[var2][0], I.STR]
                    if self.memoire[var1][1] == self.memoire[var2][1] == I.STR:
                        raise Exception("Multiplication d'un string par un string")
                case I.MUL, var1, var2, store:
                    if self.memoire[var1][1] == self.memoire[var2][1] == I.INT:
                        if self.memoire[store][1] != I.INT:
                            raise Exception("Erreur : la variable de stockage doit être un entier")
                        self.memoire[store] = [self.memoire[var1][0] * self.memoire[var2][0], I.INT]
                    if self.memoire[var1][1] == I.STR and self.memoire[var2][1] == I.INT:
                        if self.memoire[store][1] != I.STR:
                            raise Exception("Erreur : la variable de stockage doit être une chaine de caractères")
                        self.memoire[store] = [self.memoire[var1][0] * self.memoire[var2][0], I.STR]
                    if self.memoire[var1][1] == self.memoire[var2][1] == I.STR:
                        raise Exception("Multiplication d'un string par un string")
                case I.PRINT, id_memoire:
                    print(self.memoire[id_memoire][0])
                case I.TPRINT, id_memoire:
                    print(self.memoire[id_memoire])
                case I.PRINT_RAW, autre:
                    print(autre)
                case I.DEFINE_INT, id_memoire, value:
                    if not isinstance(value, int):
                        raise Exception("Erreur : la valeur doit être un entier")
                    self.memoire[id_memoire] = [value, I.INT]
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
                            if self.memoire[var1][1] == self.memoire[var2][1] == I.STR:
                                if self.memoire[var1][0] == self.memoire[var2][0]:
                                    self.run(code)
                        case I.NOT_EQUAL, var1, var2:
                            if self.memoire[var1][1] == self.memoire[var2][1] == I.INT:
                                if self.memoire[var1][0] != self.memoire[var2][0]:
                                    self.run(code)
                            if self.memoire[var1][1] == self.memoire[var2][1] == I.STR:
                                if self.memoire[var1][0] != self.memoire[var2][0]:
                                    self.run(code)
                        case I.LESS, var1, var2:
                            if self.memoire[var1][1] == self.memoire[var2][1] == I.INT:
                                if self.memoire[var1][0] < self.memoire[var2][0]:
                                    self.run(code)
                            if self.memoire[var1][1] == I.STR or self.memoire[var2][1] == I.STR:
                                raise Exception("Les variables ne sont pas des entiers")
                        case I.LESS_EQUAL, var1, var2:
                            if self.memoire[var1][1] == self.memoire[var2][1] == I.INT:
                                if self.memoire[var1][0] <= self.memoire[var2][0]:
                                    self.run(code)
                            if self.memoire[var1][1] == I.STR or self.memoire[var2][1] == I.STR:
                                raise Exception("Les variables ne sont pas des entiers")
                        case I.GREATER, var1, var2:
                            if self.memoire[var1][1] == self.memoire[var2][1] == I.INT:
                                if self.memoire[var1][0] > self.memoire[var2][0]:
                                    self.run(code)
                            if self.memoire[var1][1] == I.STR or self.memoire[var2][1] == I.STR:
                                raise Exception("Les variables ne sont pas des entiers")
                        case I.GREATER_EQUAL, var1, var2:
                            if self.memoire[var1][1] == self.memoire[var2][1] == I.INT:
                                if self.memoire[var1][0] >= self.memoire[var2][0]:
                                    self.run(code)
                            if self.memoire[var1][1] == I.STR or self.memoire[var2][1] == I.STR:
                                raise Exception("Les variables ne sont pas des entiers")
                case I.POW, var1, var2, store:
                    if self.memoire[var1][1] == self.memoire[var2][1] == I.INT:
                        self.memoire[store] = [self.memoire[var1][0] ** self.memoire[var2][0], I.INT]
                    if self.memoire[var1][1] == I.STR or self.memoire[var2][1] == I.STR:
                        raise Exception("Les variables ne sont pas des entiers")
                case I.LOOP, nb, code:
                    if self.memoire[nb][1] != I.INT:
                        raise Exception("La variable n'est pas un entier")
                    else:
                        for _ in range(self.memoire[nb][0]-1):
                            self.run(code)
                case I.DEFINE_STR, id_memoire, value:
                    if not isinstance(value, str):
                        raise Exception("Erreur : la valeur doit être une chaine de caractères")
                    self.memoire[id_memoire] = [value, I.STR]
                case I.COPY_VAR, var1, var2:
                    self.memoire[var1] = self.memoire[var2]
                case I.STR_INPUT, var, texte:
                    self.memoire[var] = [input(texte), I.STR]
                case I.INT_INPUT, var, texte:
                    try:
                        self.memoire[var] = [int(input(texte)), I.INT]
                    except:
                        raise Exception("Erreur : la valeur entrée n'est pas un entier")

# code = [(I.INT_INPUT, "a", "Calculer 2**"),
#         (I.DEFINE_INT, "nb", 2),
#         (I.DEF_FUNCTION, "double", [(I.ADD, "nb", "nb", "nb")]),
#         (I.LOOP, "a", [(I.FUNCTION, "double")]),
#         (I.PRINT, "nb"),
#         ]
      

if __name__ == "__main__":
    code = [(I.INT_INPUT, "x", "Nb de fois a run : "),
            (I.DEFINE_INT, "var", 0),
            (I.DEFINE_INT, "1", 1),
            (I.ADD, "x", "1", "x"),
            (I.LOOP, "x", [(I.ADD, "var", "1", "var"), (I.PRINT, "var")]),
            ]
    Interpretor(debug_mode=False).run(code)