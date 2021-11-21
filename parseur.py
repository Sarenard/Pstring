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
                self.code.append((I.DEFINE_INT, var, value))
            case "print", value, end:
                self.code.append((I.PRINT, value, end))
            case "print", value:
                self.code.append((I.PRINT, value))