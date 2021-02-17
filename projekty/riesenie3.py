# 3. zadanie: kalendár
# autor: Patrik Jakab
# datum: 21.10.2020


def pocet_dni_v_mesiaci(mesiac, priestupny=False):
    if mesiac == "jan" or mesiac == 1:
        return 31
    elif mesiac == "feb" or mesiac == 2:
        if priestupny:
            return 29
        else:
            return 28
    elif mesiac == "mar" or mesiac == 3:
        return 31
    elif mesiac == "apr" or mesiac == 4:
        return 30
    elif mesiac == "maj" or mesiac == 5:
        return 31
    elif mesiac == "jun" or mesiac == 6:
        return 30
    elif mesiac == "jul" or mesiac == 7:
        return 31
    elif mesiac == "aug" or mesiac == 8:
        return 31
    elif mesiac == "sep" or mesiac == 9:
        return 30
    elif mesiac == "okt" or mesiac == 10:
        return 31
    elif mesiac == "nov" or mesiac == 11:
        return 30
    elif mesiac == "dec" or mesiac == 12:
        return 31


def cislo_mesiaca(mesiac):
    if mesiac == "jan":
        return 1
    elif mesiac == "feb":
        return 2
    elif mesiac == "mar":
        return 3
    elif mesiac == "apr":
        return 4
    elif mesiac == "maj":
        return 5
    elif mesiac == "jun":
        return 6
    elif mesiac == "jul":
        return 7
    elif mesiac == "aug":
        return 8
    elif mesiac == "sep":
        return 9
    elif mesiac == "okt":
        return 10
    elif mesiac == "nov":
        return 11
    elif mesiac == "dec":
        return 12


def pekny_datum(datum):
    if len(datum) > 8:
        mesiac = datum[:len(datum) - 5]
        novy_mesiac = mesiac[:3]
        krajsi_datum = novy_mesiac + datum[len(datum) - 5:]
    else:
        return datum
    return krajsi_datum


def pocet_dni_medzi(datum1, datum2):
    datum1, datum2 = pekny_datum(datum1), pekny_datum(datum2)
    start_mes = datum1[:3]
    start_rok = int(datum1[4:])
    end_mes = datum2[:3]
    end_rok = int(datum2[4:])
    mesiac1 = cislo_mesiaca(start_mes)
    mesiac2 = cislo_mesiaca(end_mes)
    celkovy_pocet_dni = 0
    if start_rok == end_rok:
        if start_rok % 4 == 0:
            if mesiac1 < mesiac2:
                for i in range(mesiac1, mesiac2):
                    celkovy_pocet_dni += pocet_dni_v_mesiaci(i, True)
            elif mesiac1 > mesiac2:
                for i in range(mesiac1, 12):
                    celkovy_pocet_dni += pocet_dni_v_mesiaci(i, True)
            else:
                celkovy_pocet_dni = 0
        else:
            for i in range(mesiac1, mesiac2):
                celkovy_pocet_dni += pocet_dni_v_mesiaci(i, False)

        return celkovy_pocet_dni

    else:
        for i in range(start_rok, end_rok + 1):
            if i % 4 == 0:
                if i == start_rok:
                    for j in range(mesiac1, 12 + 1):
                        celkovy_pocet_dni += pocet_dni_v_mesiaci(j, True)
                elif i == end_rok:
                    for j in range(1, mesiac2):
                        celkovy_pocet_dni += pocet_dni_v_mesiaci(j, True)
                else:
                    for j in range(1, 12 + 1):
                        celkovy_pocet_dni += pocet_dni_v_mesiaci(j, True)
            else:
                if i == start_rok:
                    for j in range(mesiac1, 12 + 1):
                        celkovy_pocet_dni += pocet_dni_v_mesiaci(j, False)
                elif i == end_rok:
                    for j in range(1, mesiac2):
                        celkovy_pocet_dni += pocet_dni_v_mesiaci(j, False)
                else:
                    for j in range(1, 12 + 1):
                        celkovy_pocet_dni += pocet_dni_v_mesiaci(j, False)

        return celkovy_pocet_dni


def den_v_tyzdni(datum):
    cut_den = datum.find('.')
    den = int(datum[:cut_den])
    datum = datum[cut_den + 1:]
    datum = pekny_datum(datum)
    pocet_ubeh_dni = pocet_dni_medzi("jan.1901", datum)
    pocet_ubeh_dni += den + 1
    if pocet_ubeh_dni % 7 == 1:
        return "pon"
    elif pocet_ubeh_dni % 7 == 2:
        return "uto"
    elif pocet_ubeh_dni % 7 == 3:
        return "str"
    elif pocet_ubeh_dni % 7 == 4:
        return "stv"
    elif pocet_ubeh_dni % 7 == 5:
        return "pia"
    elif pocet_ubeh_dni % 7 == 6:
        return "sob"
    elif pocet_ubeh_dni % 7 == 0:
        return "ned"


# print(pocet_dni_medzi("jan.1901", "oktober.2020"))
# print(den_v_tyzdni("21.oktober.2020"))
