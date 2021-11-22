from interpeteur import I

class Parser:
    def __init__(self, debug_mode=False):
        self.lignes = ""
        self.code = []
        self.debug_mode = debug_mode
    def parse(self, file):
        with open(file, 'r') as f:
            for line in f:
                self.lignes += line
        self.lignes = list(self.lignes.replace("\n", "").split(";"))
        for ligne in self.lignes:
            self.parse_line(ligne)
        if self.debug_mode : print(f"lignes brutes : {self.lignes}\ncode : {self.code}")
        return self.code
    def parse_line(self, ligne):
        match ligne.split():
            case "int", var, value:
                self.code.append((I.DEFINE_INT, var, int(value)))
            case "print", value, end:
                self.code.append((I.PRINT, value, end))
            case "print", value:
                self.code.append((I.PRINT, value))

# code = [(I.DEFINE_INT, "1", 1),(I.DEF_FUNCTION, "test_prime", [(I.DEFINE_INT, "a", 2),(I.DEFINE_INT, "0", 0),(I.DEFINE_INT, "-1", -1),(I.DEFINE_INT, "-1000", -1000),(I.DEFINE_INT, "2", 2),(I.DEFINE_STR, "est_premier", "est premier"),(I.COPY_VAR, "input", "valeur"),(I.COPY_VAR, "tinput", "input"),(I.DEF_FUNCTION, "is_prime", [(I.IF, (I.GREATER_EQUAL, "input", "a"), [(I.COPY_VAR, "i", "a"),(I.COPY_VAR, "mod", "input"),(I.ADD, "input", "-1", "input"),(I.ADD, "input", "-1", "input"),(I.LOOP, "input", [(I.ADD, "i", "1", "i"),(I.IF, (I.NOTIFMOD, "mod", "i"), [(I.DEFINE_STR, "est_premier", "n'est pas premier")]),])]),(I.IF, (I.EQUAL, "input", "2"), [(I.DEFINE_STR, "est_premier", "n'est pas premier")]),(I.IF, (I.LESS_EQUAL, "tinput", "1"), [(I.DEFINE_STR, "est_premier", "n'est pas premier")])]),(I.FUNCTION, "is_prime"),(I.PRINT, "est_premier")]),(I.INT_INPUT, "total_max", "Entrez un entier >>> "),(I.ADD, "total_max", "1", "total_max"),(I.DEFINE_INT, "valeur", 1),(I.LOOP, "total_max", [(I.PRINT_END_RAW, "Le nombre ", ""),(I.PRINT_END, "valeur", ""),(I.PRINT_END_RAW, " ", ""),(I.FUNCTION, "test_prime"),(I.ADD, "valeur", "1", "valeur"),]),]