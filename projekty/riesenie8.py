# 8. zadanie: stvorce
# autor: Patrik Jakab
# datum: 25.11.2020

class Stvorce:

    def __init__(self, n):
        self.tabulka = []
        self.nuly = 0
        self.jednotky = 0
        for i in range(2 ** n):
            self.tabulka.append([0] * (2 ** n))
        self.original_velkost = len(self.tabulka)
        self.velkost_tab = len(self.tabulka)
        self.prev_quadrant = []
        self.quadrant_load()

    def quadrant_load(self):
        self.prev_quadrant.clear()
        self.velkost_tab = self.original_velkost
        for i in range(int(self.original_velkost ** (1 / 2))):
            self.prev_quadrant.append([])
            for j in range(2):
                self.prev_quadrant[i].append([])

    def write_item(self, a, i, j, add=False):
        if add:
            if self.tabulka[i][j] == 0:
                self.tabulka[i][j] = 1
            elif self.tabulka[i][j] == 1:
                self.tabulka[i][j] = 0

        self.prev_quadrant[a][0].append(i)
        self.prev_quadrant[a][1].append(j)

    def check_write_first(self, index, a, i, j):
        if len(index) == 1:
            self.write_item(a, i, j, True)
        else:
            self.write_item(a, i, j)

    def check_write_other(self, index, a, i, j):
        if a == len(index) - 1:
            self.write_item(a, i, j, True)
        else:
            self.write_item(a, i, j)

    def urob(self, index):
        self.quadrant_load()
        if index == "":
            for i in range(len(self.tabulka)):
                for j in range(len(self.tabulka[i])):
                    if self.tabulka[i][j] == 0:
                        self.tabulka[i][j] = 1
                    else:
                        self.tabulka[i][j] = 0
        else:
            for a in range(len(index)):
                for i in range(len(self.tabulka)):
                    for j in range(len(self.tabulka[i])):
                        if int(index[a]) == 1:
                            if a == 0:
                                if i < self.velkost_tab // 2 and j < self.velkost_tab // 2:
                                    self.check_write_first(index, a, i, j)
                            else:
                                if i in self.prev_quadrant[a - 1][0] and j in self.prev_quadrant[a - 1][1]:
                                    if self.prev_quadrant[a - 1][0][0] <= i <= \
                                            self.prev_quadrant[a - 1][0][-1] - self.velkost_tab // 2 and \
                                            self.prev_quadrant[a - 1][1][0] <= j <= self.prev_quadrant[a - 1][1][-1] \
                                            - self.velkost_tab // 2:
                                        self.check_write_other(index, a, i, j)

                        elif int(index[a]) == 2:
                            if a == 0:
                                if i < self.velkost_tab // 2 <= j:
                                    self.check_write_first(index, a, i, j)
                            else:
                                if i in self.prev_quadrant[a - 1][0] and j in self.prev_quadrant[a - 1][1]:
                                    if self.prev_quadrant[a - 1][0][0] <= i <= \
                                            self.prev_quadrant[a - 1][0][-1] - self.velkost_tab // 2 and \
                                            self.prev_quadrant[a - 1][1][0] + self.velkost_tab // 2 <= j <= \
                                            self.prev_quadrant[a - 1][1][-1]:
                                        self.check_write_other(index, a, i, j)

                        elif int(index[a]) == 3:
                            if a == 0:
                                if i >= self.velkost_tab // 2 > j:
                                    self.check_write_first(index, a, i, j)
                            else:
                                if i in self.prev_quadrant[a - 1][0] and j in self.prev_quadrant[a - 1][1]:
                                    if self.prev_quadrant[a - 1][0][0] + self.velkost_tab // 2 <= i <= \
                                            self.prev_quadrant[a - 1][0][-1] and \
                                            self.prev_quadrant[a - 1][1][0] <= j <= self.prev_quadrant[a - 1][1][-1] \
                                            - self.velkost_tab // 2:
                                        self.check_write_other(index, a, i, j)

                        elif int(index[a]) == 4:
                            if a == 0:
                                if i >= self.velkost_tab // 2 and j >= self.velkost_tab // 2:
                                    self.check_write_first(index, a, i, j)
                            else:
                                if i in self.prev_quadrant[a - 1][0] and j in self.prev_quadrant[a - 1][1]:
                                    if self.prev_quadrant[a - 1][0][0] + self.velkost_tab // 2 <= i <= \
                                            self.prev_quadrant[a - 1][0][-1] and \
                                            self.prev_quadrant[a - 1][1][0] + self.velkost_tab // 2 <= j <= \
                                            self.prev_quadrant[a - 1][1][-1]:
                                        self.check_write_other(index, a, i, j)
                self.velkost_tab //= 2

    def pocet(self):
        self.nuly = 0
        self.jednotky = 0
        for i in range(len(self.tabulka)):
            for j in range(len(self.tabulka[i])):
                if self.tabulka[i][j] == 0:
                    self.nuly += 1
                else:
                    self.jednotky += 1
        vys = (self.nuly, self.jednotky)
        return vys

    def vypis(self):
        konecny_vypis = ""
        for i in range(len(self.tabulka)):
            for j in range(len(self.tabulka[i])):
                if self.tabulka[i][j] == 0:
                    konecny_vypis += "-"
                else:
                    konecny_vypis += "X"
            konecny_vypis += "\n"
        print(konecny_vypis)


# s = Stvorce(6)
# for i in ['2', '23224', '2411', '24123', '24131', '24132', '2422', '24223', '2444', '24441',
# '212', '21412', '21421', '21422', '211', '2113', '21132', '21143', '22', '2233',
# '2234', '22342', '14', '14111', '14113', '1433', '14332', '132', '1322', '13223',
# '134', '1344', '13441', '1312', '13142', '13144', '13322', '13324', '1334', '1134',
# '11341', '11333', '11334', '11433', '1224', '12243', '12344', '124', '1241', '12421',
# '12423', '12431', '3112', '31123', '31111', '31112', '31211', '32122', '322', '3223',
# '32213', '3224', '32242', '411', '412', '4124', '41241', '41234', '4211', '42121',
# '42122', '42211', '4131', '413114', '41321']:
#     s.urob(i)
# s.vypis()
