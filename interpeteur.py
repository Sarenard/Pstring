class I:
    MUL = "mul"
    ADD = "add"
    PRINT = "print"
    TPRINT = "tprint"
    DEFINE_INT = "define_int"
    INT = "int"
    POW = "pow"
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
    MOD = "mod"
    IFMOD = "ifmod"
    NOTIFMOD = "notifmod"
    PRINT_END = "print_end"
    PRINT_END_RAW = "print_end_raw"

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
                case I.POW, var1, var2, store:
                    if self.memoire[var1][1] == self.memoire[var2][1] == I.INT:
                        if self.memoire[store][1] != I.INT:
                            raise Exception("Erreur : la variable de stockage doit être un entier")
                        self.memoire[store] = [self.memoire[var1][0] ** self.memoire[var2][0], I.INT]
                    if self.memoire[var1][1] == I.STR or self.memoire[var2][1] == I.STR:     
                        raise Exception("Puissance d'un string")
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
                case I.MOD, var1, var2, store:
                    if self.memoire[var1][1] == self.memoire[var2][1] == I.INT:
                        if self.memoire[store][1] != I.INT:
                            raise Exception("Erreur : la variable de stockage doit être un entier")
                        self.memoire[store] = [self.memoire[var1][0] % self.memoire[var2][0], I.INT]
                    else:
                        raise Exception("Modulo d'un non entier par un non entier")
                case I.PRINT, id_memoire:
                    print(self.memoire[id_memoire][0])
                case I.PRINT_END, id_memoire, end:
                    print(self.memoire[id_memoire][0], end=end)
                case I.PRINT_END_RAW, raw, end:
                    print(raw, end=end)
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
                        case I.IFMOD, var1, var2:
                            if self.memoire[var1][1] == self.memoire[var2][1] == I.INT:
                                if self.memoire[var1][0] % self.memoire[var2][0] != 0:
                                    self.run(code)
                            if self.memoire[var1][1] == I.STR or self.memoire[var2][1] == I.STR:
                                raise Exception("Les variables ne sont pas des entiers")
                        case I.NOTIFMOD, var1, var2:
                            if self.memoire[var1][1] == self.memoire[var2][1] == I.INT:
                                if self.memoire[var1][0] % self.memoire[var2][0] == 0:
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
    code = [
        (I.DEFINE_INT, "1", 1),
        (I.DEFINE_INT, "a", 2),
        (I.DEFINE_INT, "0", 0),
        (I.DEFINE_INT, "-1", -1),
        (I.DEFINE_INT, "-1000", -1000),
        (I.DEFINE_INT, "2", 2),
        (I.DEF_FUNCTION, "test_prime", [
            (I.DEFINE_STR, "est_premier", "est premier"),
            (I.COPY_VAR, "input", "valeur"),
            (I.COPY_VAR, "tinput", "input"),
            (I.DEF_FUNCTION, "is_prime", [(I.IF, (I.GREATER_EQUAL, "input", "a"), [
                (I.COPY_VAR, "i", "a"),
                (I.COPY_VAR, "mod", "input"),
                (I.ADD, "input", "-1", "input"),
                (I.ADD, "input", "-1", "input"),
                (I.LOOP, "input", [
                    (I.ADD, "i", "1", "i"),
                    (I.IF, (I.NOTIFMOD, "mod", "i"), [(I.DEFINE_STR, "est_premier", "n'est pas premier")]),])
                ]),
                (I.IF, (I.EQUAL, "input", "2"), [(I.DEFINE_STR, "est_premier", "n'est pas premier")]),
                (I.IF, (I.LESS_EQUAL, "tinput", "1"), [(I.DEFINE_STR, "est_premier", "n'est pas premier")])]
            ),
            (I.FUNCTION, "is_prime"),
            (I.PRINT, "est_premier")
        ]),
        (I.INT_INPUT, "total_max", "Entrez un entier >>> "),
        (I.ADD, "total_max", "1", "total_max"),
        (I.DEFINE_INT, "valeur", 1),
        (I.LOOP, "total_max", [
            (I.PRINT_END_RAW, "Le nombre ", ""),
            (I.PRINT_END, "valeur", ""),
            (I.PRINT_END_RAW, " ", ""),
            (I.FUNCTION, "test_prime"),
            (I.ADD, "valeur", "1", "valeur"),
        ]),
    ]
    Interpretor(debug_mode=False).run(code)