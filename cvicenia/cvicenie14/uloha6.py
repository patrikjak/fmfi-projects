class Zlomok:

    def __init__(self, citatel, menovatel):
        self.citatel = citatel
        self.menovatel = menovatel

    def vypis(self):
        print(f"zlomok je {self.citatel}/{self.menovatel}")


z1 = Zlomok(3, 8)
z2 = Zlomok(2, 4)
z1.vypis()
z2.vypis()
