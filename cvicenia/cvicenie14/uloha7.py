class Zlomok:

    def __init__(self, citatel, menovatel):
        self.citatel = citatel
        self.menovatel = menovatel

    def vypis(self):
        print(f"zlomok je {self.citatel}/{self.menovatel}")

    def str(self):
        return f"{str(self.citatel)}/{str(self.menovatel)}"

    def float(self):
        return self.citatel/self.menovatel


z = Zlomok(3, 8)
print('z je', z.str())
print('z je', z.float())
