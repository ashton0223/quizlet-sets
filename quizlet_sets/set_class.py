from . import export

#Term class
class Term:
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition

class TermList:
    def __init__(self, tlist):
        self.tlist = tlist
    
    def xls(self, name):
        export.write_xls(self.tlist, name)
    
    def txt(self, name):
        export.write_txt(self.tlist, name)

    def csv(self, name):
        export.write_csv(self.tlist, name)
    
    def anki(self, deck_name, name):
        export.write_anki(term_list, deck_name, name)