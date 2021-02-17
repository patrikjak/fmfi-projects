class Subor:

    def __init__(self, meno_suboru):
        self.meno_suboru = meno_suboru

    def pripis(self, text):
        subor = open(self.meno_suboru, 'a')
        subor.write(text+"\n")

    def vypis(self):
        subor = open(self.meno_suboru, 'r')
        print(subor.read())


s = Subor('text.txt')
s.pripis("Prvy riadok")
s.pripis("Druhy riadok")
s.vypis()
s.pripis("Posledny riadok")
s.vypis()
