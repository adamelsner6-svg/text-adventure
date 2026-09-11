import random

enemies = [
    {"jmeno": "Skeleton", "min_dmg": 5, "max_dmg": 15, "hp": 105, "armor": 1},
    {"jmeno": "Stříbrný rytíř", "min_dmg": 10, "max_dmg": 22, "hp": 120, "armor": 0.9},
    {"jmeno": "Nemrtvý strážce", "min_dmg": 20, "max_dmg": 35, "hp": 200, "armor": 0.8},
    {"jmeno": "Padlý král", "min_dmg": 25, "max_dmg": 50, "hp": 350, "armor": 0.7}
]

inventar = [
    {"nazev": "Ruce","vis": "visible","typ": "zbran","min_dmg": 0, "max_dmg": 5, "popis": "Tvé holé ruce. Dokážeš udělit od 0 - 5 dmg", "pocet": 1},
    {"nazev": "Bez zbroje","vis": "no","typ": "armor","armor": 1 ,"popis": "armor", "pocet": 1},
    {"nazev": "Groše","vis": "visible","typ": "coin","popis": "Tvé drahocené penízky. Co si za ně koupíš?", "pocet": 0}   
]

poloha = 0
hp = 100
max_hp = 100
game_on = True
global aktualni_zbran
global aktualni_armor
odmena_chodba = True
odmena_park = True
odmena_dum = True
odmena_spiz = True
fontana1 = True
fontana2 = True

def uvod():
    print("Prolog")
    print("")
    print("Přicházíš do téměř opuštěného městečka, které kdysi prosperovalo.")
    print("Po smrti starého krále usedl na trůn nový panovník, který se ukázal být tyranem.")
    print("Lidé kvůli jeho vládě uprchli a v městečku zůstalo jen několik přeživších a jeho věrných stoupenců.")
    print("")
    print("Přicházíš jim na pomoc.")
    print("Tvým úkolem je porazit krále a ukončit jeho vládu, aby se lidé mohli vrátit do svých domovů.")
    print("")
    print("Tvé dobrodružství právě začíná...")
    print("")
    input("Pro pokračování stiskněte ENTER")


def mapa():
    print("__________________________________________________________________________________")
    print("|                                                                                |")
    print("|[Zbrojírna]      [Hřbitov]                [Obchodník]     [Skleník]             |")
    print("|     |               |                         |              |                 |")
    print("|   [Park] ------ [Náměstí] --- [Dům]     [Levé křídlo] --- [Kaple]              |")
    print("|     |               |                         |              |                 |")
    print("| [Brána do] ----- [Ulice] --- [Brána] ---- [Zahrada] ---- [Předsíň] ---- [Síň]  |")
    print("|  [města]                                      |              |                 |")
    print("|                                         [Pravé křídlo]     [Spíž]              |")
    print("|________________________________________________________________________________|")

def menu(hp,max_hp):
    while True:
        print("1 - Mapa")
        print("2 - Inventář")
        print("3 - Vypít lektvar")
        print("4 - Vybrat zbraň")
        print("5 - Vybrat zbroj")
        print("6 - Konec hry")
        print("0 - Zpět do hry")

        volba = ziskat_volbu()
        if volba == 1:
            mapa()
            return hp, True
        elif volba == 2:
            zobrazit_inventar()
        elif volba == 3:
            hp = vypit_lektvar(hp,max_hp)
        elif volba == 4:
            vybrat_zbrane()
            return hp, True
        elif volba == 5:
            vybrat_zbroje()
            return hp, True
        elif volba == 6:
            return hp, False
        elif volba == 0:
            return hp, True

def ziskat_moznost():
    while True:
        try:
            return int(input("Volba: ")) 
        except ValueError:
            print("Musíš zadat číslo!")

def ziskat_volbu():
    volba = ziskat_moznost()
    print("_____________________________________________")
    return volba

def zobrazit_inventar():
    if inventar:
        print("Inventář: ")
        for predmet in inventar:
            if predmet.get("vis") == "visible":
                print(predmet["pocet"],predmet["nazev"],"-", predmet["popis"])
        print("_____________________________________________")
    else:
        print("Inventář je prázdný.")

def vypit_lektvar(hp,max_hp):
    while True:
        lektvary = []
        
        maly_lektvar = najdi_predmet("Malý lektvar")
        str_lektvar = najdi_predmet("Střední lektvar")
        vel_lektvar = najdi_predmet("Velký lektvar")
        if maly_lektvar:
            lektvary.append(maly_lektvar)
        if str_lektvar:
            lektvary.append(str_lektvar)
        if vel_lektvar:
            lektvary.append(vel_lektvar)
        if not lektvary:
            print("Nemáš žádný lektvar!")
            return hp
        
        print("Vyber lektvar:")

        for i,lektvar in enumerate(lektvary, start = 1):
            print(f"{i} - {lektvar['nazev']} ({lektvar['pocet']}x)")
        print("0 - Zpět")
        volba = ziskat_volbu()
        if volba == 0:
            return hp
        if 1 <= volba <= len(lektvary):
            lektvar = lektvary[volba - 1]
            lektvar["pocet"] -= 1
            hp += lektvar["hp"]
            if hp > max_hp:
                zisk = lektvar["hp"] - (hp - max_hp)
                hp = max_hp
            else:
                zisk = lektvar["hp"]
            print(f"Napil ses lektvaru, získal jsi {zisk} HP")
            if lektvar["pocet"] == 0:
                inventar.remove(lektvar)
            return hp
        else:
            print("Neplatná možnost!")

def zobraz_moznosti(poloha):
    print("HP -",f"{hp:.1f}")
    if poloha == 0: #Brána do města
        print("Můžeš jít:")
        print("1 - Ulice")
        print("2 - Park")
        print("0 - Možnosti")
    elif poloha == 1: #Ulice
        print("Můžeš jít:")
        print("1 - Brána do města")
        print("2 - Náměstí")
        print("3 - Brána do hradu")
        print("0 - Možnosti")
    elif poloha == 2: #Hrob
        print("Můžeš jít:")
        print("1 - Náměstí")
        print("2 - Prohledat hrob")
        print("0 - Možnosti")
    elif poloha == 3: #Brána
        print("Můžeš jít:")
        print("1 - Ulice")
        print("2 - Projít bránou")
        print("0 - Možnosti")
    elif poloha == 5: #Park
        print("Můžeš jít:")
        print("1 - Brána do města")
        print("2 - Náměstí")
        print("3 - Zbrojnice")
        print("0 - Možnosti")
    elif poloha == 4: #Zbrojírna
        print("Můžeš jít:")
        print("1 - Park")
        print("0 - Možnosti")
    elif poloha == 6: #Dům
        print("1 - Odejít")
        print("2 - Přijmout")
        print("0 - Možnosti")
    elif poloha == 7: #Náměstí
        print("Můžeš jít:")
        print("1 - Ulice")
        print("2 - Park")
        print("3 - Hřbitov")
        print("4 - Dům")
        print("0 - Možnosti")
    elif poloha == 8: #Zahrada
        print("Můžeš jít:")
        print("1 - Brána")
        print("2 - Předsíň")
        print("3 - Levé křídlo")
        print("4 - Pravé křídlo")
        print("5 - Vyléčit se")
        print("0 - Možnosti")
    elif poloha == 9: #Pravé křídlo
        print("Můžeš jít:")
        print("1 - Zahrada")
        print("0 - Možnosti")
    elif poloha == 10: #Levé křídlo
        print("Můžeš jít:")
        print("1 - Zahrada")
        print("2 - Kaple")
        print("3 - Obchodník")
        print("0 - Možnosti")
    elif poloha == 11: #Obchodník
        print("Můžeš jít:")
        print("1 - Levé křídlo")
        print("2 - Obchodovat")
        print("0 - Možnosti")
    elif poloha == 12: #Předsíň
        print("Můžeš jít:")
        print("1 - Zahrada")
        print("2 - Spíž")
        print("3 - Kaple")
        print("4 - Síň")
        print("0 - Možnosti")
    elif poloha == 13: #Spíž
        print("Můžeš jít:")
        print("1 - Předsíň")
        print("0 - Možnosti")
    elif poloha == 14: #Kaple
        print("Můžeš jít:")
        print("1 - Předsíň")
        print("2 - Levé křídlo")
        print("3 - Skleník")
        print("0 - Možnosti")
    elif poloha == 15: #Skleník
        print("Můžeš jít:")
        print("1 - Kaple")
        print("2 - Vyléčit se")
        print("0 - Možnosti")
    elif poloha == 16: #Síň
        print("Můžeš jít:")
        print("1 - Odejít")
        print("2 - Předsíň")
        print("0 - Možnosti")
    print("_____________________________________________")
    if inventar:
        print("Inventář: ")
        for predmet in inventar:
            if predmet.get("vis") == "visible":
                print("-", predmet["nazev"],"(",predmet["pocet"],")")
    else:
        print("Inventář je prázdný.")


def utok_hrac():
    sance = random.randint(0,10)
    utok = random.randint(aktualni_zbran["min_dmg"], aktualni_zbran["max_dmg"]) * enemy["armor"]
    if sance == 1:
        utok *= 2
        print("Udělil jsi kritický zásah! ", f"{utok:.1f}","poškození")
    else:
        print("Udělil jsi ",f"{utok:.1f}","poškození")
    return utok

def utok_enemy(enemy):
    sance = random.randint(0,10)
    utok = random.randint(enemy["min_dmg"], enemy["max_dmg"]) * aktualni_armor["armor"]
    if sance == 1:
        utok = 0
        print("Nepřítel minul!")
    return utok

def souboj(hp,enemy,poloha,max_hp):
    while hp > 0 and enemy["hp"] > 0:
        aktualni_pozice = poloha
        print("Vyber akci proti nepříteli.")
        print("1 - Útok")
        print("2 - Obrana")
        print("3 - Lektvar")
        print("0 - Utéct z boje")
        print("HP -",f"{hp:.1f}")
        print("Nepřítelovi HP -",f"{enemy['hp']:.1f}")
        maly_lektvar = najdi_predmet("Malý lektvar")
        str_lektvar = najdi_predmet("Střední lektvar")
        vel_lektvar = najdi_predmet("Velký lektvar")
        if maly_lektvar:
            print("Malý lektvar", maly_lektvar["pocet"],"x")
        if str_lektvar:
            print("Střední lektvar", str_lektvar["pocet"],"x")
        if vel_lektvar:
            print("Velký lektvar", vel_lektvar["pocet"],"x")
        akce = ziskat_volbu()
        if akce == 1:
            utok = utok_hrac()
            enemy["hp"] -= utok
            if enemy["hp"] <= 0:
                print(enemy["jmeno"]," padnul!")
                print("_____________________________________________")
                break
            print("_____________________________________________")
            print("Nepřítel na tebe útočí!")
            utok_e = utok_enemy(enemy)
            hp -= utok_e
            print(enemy["jmeno"]," ti udělil ", f"{utok_e:.1f}","poškození")
            if hp <= 0:
                print("Padnul jsi!")
                print("_____________________________________________")
                break
            print("_____________________________________________")
        elif akce == 2:
            sance = random.randint(1,2)
            utok_e = utok_enemy(enemy)
            if sance == 1:
                if utok_e == 0:
                    print("")
                else:
                    dmg = utok_e * 0.75
                    hp -= dmg
                    print("Obrana ti nevyšla! Nepřítel ti udělil", f"{dmg:.1f}", "poškození")
                    if hp <= 0:
                        print("Padnul jsi!")
                        print("_____________________________________________")
                        break
            else:
                if utok_e == 0:
                    print("")
                else:
                    dmg = utok_e * 0.9
                    enemy["hp"] -= dmg
                    print("Odrazil jsi útok a ubral tak nepříteli", f"{dmg:.1f}", "poškození")
                    if enemy["hp"] <= 0:
                        print(enemy["jmeno"]," padnul!")
                        print("_____________________________________________")
                        break
        elif akce == 3:
            if maly_lektvar or str_lektvar or vel_lektvar:
                utok_e = utok_enemy(enemy) / 2
                hp = vypit_lektvar(hp,max_hp)
                hp -= utok_e
                print("Při pití lektvaru obdržíš o polovinu menší poškození. ",enemy["jmeno"],"ti udělil", f"{utok_e:.1f}","poškození")
            else:
                print("Nemáš žádný lektvar!")
        elif akce == 0:
            print("Utíkáš z boje.")
            poloha = aktualni_pozice - 2
            break
        else:
            print("Neplatná možnost!")
    return hp, poloha

def vytvor_mec():
    return {
        "nazev": "Krátký meč",
        "vis": "visible",
        "typ": "zbran",
        "min_dmg": 10,
        "max_dmg": 25,
        "popis": "Poškozený starý meč, který dává požkození od 10 - 25 dmg",
        "pocet": 1
    }

def pridat_maly_lektvar():
    return {
        "nazev": "Malý lektvar",
        "vis": "visible",
        "typ": "lektvar",
        "hp": 20,
        "pocet": 1,
        "popis": "Lektvar, který doplní 20 HP"
    }

def pridat_str_lektvar():
    return {
        "nazev": "Střední lektvar",
        "vis": "visible",
        "typ": "lektvar",
        "hp": 40,
        "pocet": 1,
        "popis": "Lektvar, který doplní 40 HP"
    }

def pridat_vel_lektvar():
    return {
        "nazev": "Velký lektvar",
        "vis": "visible",
        "typ": "lektvar",
        "hp": 70,
        "pocet": 1,
        "popis": "Lektvar, který doplní 70 HP"
    }

def pridat_klic():
    return{
        "nazev": "Starý klíč",
        "vis": "visible",
        "typ": "item",
        "popis": "Klíč od hlavní brány hradu.",
        "pocet": 1
    }

def pridat_zbroj():
    return{
        "nazev": "Zašlá zbroj",
        "vis": "visible",
        "typ": "armor",
        "armor": 0.75,
        "popis": "Špinavá a některých místech díravá zbroj, ale i tak poslouží. Budeš dostávat o 20% menší poškození",
        "pocet": 1
    }

def pridat_stribrny_mec():
    return {
            "nazev": "Stříbrný meč",
            "vis": "visible",
            "typ": "zbran",
            "min_dmg": 25,
            "max_dmg": 40,
            "popis": "Dlouhý stříbrný meč, který dává poškození od 25 - 40 dmg.",
            "pocet": 1
        }

def pridat_srdce():
    return{
        "nazev": "Srdce strážce",
        "vis": "visible",
        "typ": "item",
        "popis": "Srdce, které patří strážci tohoto hradu. Zvyšuje tvé maximální životy na 200",
        "pocet": 1
    }

def pridat_zlaty_klic():
    return{
        "nazev": "Zlatý klíč",
        "vis": "visible",
        "typ": "item",
        "popis": "Klíč od královi síně.",
        "pocet": 1
    }

def pridat_stribrna_zbroj():
    return{
        "nazev": "Stříbrná zbroj",
        "vis": "visible",
        "typ": "armor",
        "armor": 0.5,
        "popis": "Nepoužitá nablýskaná stříbrná zbroj, která tě v boji zaručeně ochrání. Poškození od nepřátel se snižuje o 50%",
        "pocet": 1
    }

def pridat_zlatý_mec():
    return {
            "nazev": "Zlatý meč",
            "vis": "visible",
            "typ": "zbran",
            "min_dmg": 50,
            "max_dmg": 70,
            "popis": "Dlouhý zlatý meč. Vypadá, že patřil samotnému králi. Dává poškození od 50 - 70 dmg.",
            "pocet": 1
        }

def vypsat_zbroj():
    zbroje = []
    for predmet in inventar:
        if predmet.get("typ") == "armor":
            zbroje.append(predmet)
    return zbroje

def vypsat_zbrane():
    zbrane = []
    for predmet in inventar:
        if predmet.get("typ") == "zbran":
            zbrane.append(predmet)
    return zbrane

def vybrat_zbroje():
    while True:
        global aktualni_armor
        zbroje = vypsat_zbroj()
        print("Jsi vybaven:", aktualni_armor["nazev"])
        print("Vyber zbroj:")
        for i,zbroj in enumerate(zbroje, start = 1):
            print(f"{i} - {zbroj['nazev']}")
        print("0 - Zpět")
        volba = ziskat_volbu()
        if volba == 0:
            break
        if 1 <= volba <= len(zbroje):
            aktualni_armor = zbroje[volba - 1]
            print("Vybral jsi:", aktualni_armor["nazev"])
            break
        else:
            print("Neplatná možnost!")

def vybrat_zbrane():
    while True:
        global aktualni_zbran
        zbrane = vypsat_zbrane()
        print("Jsi vybaven:", aktualni_zbran["nazev"])
        print("Vyber zbraň:")
        for i,zbran in enumerate(zbrane, start = 1):
            print(f"{i} - {zbran['nazev']}")
        print("0 - Zpět")
        volba = ziskat_volbu()
        if volba == 0:
            break
        if 1 <= volba <= len(zbrane):
            aktualni_zbran = zbrane[volba - 1]
            print("Vybral jsi:", aktualni_zbran["nazev"])
            break
        else:
            print("Neplatná možnost!")

def najdi_predmet(nazev):
    for predmet in inventar:
        if predmet["nazev"] == nazev:
            return predmet
    return None

def najdi_enemy(jmeno):
    for nepritel in enemies:
        if nepritel["jmeno"] == jmeno:
            return nepritel
    return None

def pocet_ml_lektvar():
    lektvar = najdi_predmet("Malý lektvar")
    if lektvar:
        lektvar["pocet"] += 1
    else:
        inventar.append(pridat_maly_lektvar())

def pocet_str_lektvar():
    lektvar = najdi_predmet("Střední lektvar")
    if lektvar:
        lektvar["pocet"] += 1
    else:
        inventar.append(pridat_str_lektvar())

def pocet_vel_lektvar():
    lektvar = najdi_predmet("Velký lektvar")
    if lektvar:
        lektvar["pocet"] += 1
    else:
        inventar.append(pridat_vel_lektvar())

uvod()
mapa()
print("Přicházíš k hlavní bráně městečka. V pozadí vidíš velký hrad se dvěmi věžemi.")
aktualni_zbran = najdi_predmet("Ruce")
aktualni_armor = najdi_predmet("Bez zbroje")
while hp > 0 and game_on:
    if poloha == 0:
        print("Došel jsi k hlavní bráně.")
        zobraz_moznosti(poloha)
        volba = ziskat_volbu()
        if volba == 0:
            hp, game_on = menu(hp,max_hp)
        elif volba == 1:
            poloha = 1
        elif volba == 2:
            poloha = 5
        else:
            print("Neplatná možnost!")
            
    elif poloha == 1:
        print("Procházíš ulicí.")
        if odmena_chodba:
            print("Našel jsi malý lektvar!")
            pocet_ml_lektvar()
            odmena_chodba = False
        zobraz_moznosti(poloha)
        volba = ziskat_volbu()
        if volba == 0:
            hp, game_on = menu(hp,max_hp)
        elif volba == 1:
            poloha = 0
        elif volba == 2:
            poloha = 7
        elif volba == 3:
            poloha = 3
        else:
            print("Neplatná možnost!")
    elif poloha == 2:
        print("Přicházíš na hřbitov. Vidíš krásný zdobený hrob. Je to hrob posledního krále.")
        klic = najdi_predmet("Starý klíč")
        zobraz_moznosti(poloha)
        volba = ziskat_volbu()
        if volba == 0:
            hp, game_on = menu(hp,max_hp)
        elif volba == 1:
            poloha = 7
        elif volba == 2:
            if not klic:
                print("Našel jsi starý klíč!")
                inventar.append(pridat_klic())
            else:
                print("Hrob je prázdný.")
        else:
            print("Neplatná možnost!")
            
    elif poloha == 3:
        print("Přišel jsi k bráně hradu.")
        klic = najdi_predmet("Starý klíč")
        zobraz_moznosti(poloha)
        volba = ziskat_volbu()
        if volba == 0:
            hp, game_on = menu(hp,max_hp)
        elif volba == 1:
            poloha = 1
        elif volba == 2:
            if not klic:
                print("Brána je zamčená.")
            else:
                print("Odemkl jsi bránu!")
                klic["vis"] = "no"
                poloha = 8
        else:
            print("Neplatná možnost!")

    elif poloha == 5:
        print("Vstoupil si do parku.")
        if odmena_park:
            gros = najdi_predmet("Groše")
            gros["pocet"] += 20
            print("Našel jsi 20 grošů")
            odmena_park = False
        zobraz_moznosti(poloha)
        volba = ziskat_volbu()
        if volba == 0:
            hp, game_on = menu(hp,max_hp)
        elif volba == 1:
            poloha = 0
        elif volba == 2:
            poloha = 7
        elif volba == 3:
            poloha = 4
        else:
            print("Neplatná možnost!")
    elif poloha == 4:
        print("Vstoupil si do zbrojnice.")
        mec = najdi_predmet("Krátký meč")
        if not mec:
            print("Získal si krátký meč.")
            inventar.append(vytvor_mec())
            aktualni_zbran = najdi_predmet("Krátký meč")
            print("Vybavil ses Krátkým mečem.")
        else:
            print("Zbrojnice je prázdná.")  
        zobraz_moznosti(poloha)
        volba = ziskat_volbu()
        if volba == 0:
            hp, game_on = menu(hp,max_hp)
        elif volba == 1:
            poloha = 5
        else:
            print("Neplatná možnost!")
    elif poloha == 6:
        if odmena_dum:
            print("Vešel jsi do domu. Vidíš před sebou starce, který tě žádá o tvou krev. Naoplátku ti chce dát 40 grošů")
            print("Bude tě to stát 40 HP")
            zobraz_moznosti(poloha)
            volba = ziskat_volbu()
            if volba == 0:
                hp, game_on = menu(hp,max_hp)
            elif volba == 1:
                poloha = 7
            elif volba == 2:
                hp -= 40
                if hp <= 0:
                    print("Vykrvácel jsi!")
                else:
                    print("Přišel jsi o 40 HP, ale získal jsi 40 grošů.")
                    print("Stařec utekl pryč s tvou krví.")
                    gros = najdi_predmet("Groše")
                    gros["pocet"] += 40
                    odmena_dum = False
            else:
                print("Neplatná možnost!")
        else:
            print("Stojíš v prázdném domě.")
            print("HP -",hp)
            print("Můžeš jít:")
            print("1 - Náměstí")
            print("0 - Možnosti")
            volba = ziskat_volbu()
            if volba == 0:
                hp, game_on = menu(hp,max_hp)
            elif volba == 1:
                poloha = 7
            else:
                print("Neplatná možnost!")
    elif poloha == 7:
        print("Přišel jsi na náměstí.")
        enemy = najdi_enemy("Skeleton")
        if enemy["hp"] > 0:
            print("Pozor! Před tebou stojí ",enemy["jmeno"],"!")
            hp, poloha = souboj(hp, enemy, poloha,max_hp)
            if enemy["hp"] <= 0:
                gros = najdi_predmet("Groše")
                gros["pocet"] += 30
                print("Získal jsi 30 grošu!")
        else:
            zobraz_moznosti(poloha)
            volba = ziskat_volbu()
            if volba == 0:
                hp, game_on = menu(hp,max_hp)
            elif volba == 1:
                poloha = 1
            elif volba == 2:
                poloha = 5
            elif volba == 3:
                poloha = 2
            elif volba == 4:
                poloha = 6
            else:
                print("Neplatná možnost!")
    elif poloha == 8:
        print("Došel si do zahrady, uprostřed se nachází fotána s léčivou vodou.")
        zobraz_moznosti(poloha)
        volba = ziskat_volbu()
        if volba == 0:
            hp, game_on = menu(hp,max_hp)
        elif volba == 1:
            poloha = 3
        elif volba == 2:
            poloha = 12
        elif volba == 3:
            poloha = 10
        elif volba == 4:
            poloha = 9
        elif volba == 5:
            if fontana1:
                hp = max_hp
                fontana1 = False
                print("Vyléčil ses na", max_hp,"HP")
            else:
                print("Můžeš se vyléčit pouze jednou!")
        else:
            print("Neplatná možnost!")
    elif poloha == 9:
        print("Došel si do pravého křídla.")
        zbroj = najdi_predmet("Zašlá zbroj")
        if not zbroj:
            print("Našel jsi zašlou zbroj a malý lektvar.")
            inventar.append(pridat_zbroj())
            pocet_ml_lektvar()
            aktualni_armor = najdi_predmet("Zašlá zbroj")
        zobraz_moznosti(poloha)
        volba = ziskat_volbu()
        if volba == 0:
            hp, game_on = menu(hp,max_hp)
        elif volba == 1:
            poloha = 8
        else:
            print("Neplatná možnost!")
    elif poloha == 10:
        print("Došel si do levého křídla.")
        enemy = najdi_enemy("Stříbrný rytíř")
        if enemy["hp"] > 0:
            print("Pozor! Před tebou stojí ",enemy["jmeno"],"!")
            hp, poloha = souboj(hp, enemy, poloha,max_hp)
            if enemy["hp"] <= 0:
                gros = najdi_predmet("Groše")
                gros["pocet"] += 50
                inventar.append(pridat_stribrny_mec())
                aktualni_zbran = najdi_predmet("Stříbrný meč")
                print("Získal jsi od nepřítele jeho stříbrný meč a 50 grošu!")
                print("Vybavil ses Stříbrným mečem.")
        else:
            zobraz_moznosti(poloha)
            volba = ziskat_volbu()
            if volba == 0:
                hp, game_on = menu(hp,max_hp)
            elif volba == 1:
                poloha = 8
            elif volba == 2:
                poloha = 14
            elif volba == 3:
                poloha = 11
            else:
                print("Neplatná možnost!")
    elif poloha == 11:
        print("Došel si za obchodníkem.")
        zobraz_moznosti(poloha)
        volba = ziskat_volbu()
        if volba == 0:
            hp, game_on = menu(hp,max_hp)
        elif volba == 1:
            poloha = 10
        elif volba == 2:
            while True:
                zlaty_mec = najdi_predmet("Zlatý meč")
                brneni = najdi_predmet("Stříbrná zbroj")
                gros = najdi_predmet("Groše")
                print("Máš",gros["pocet"],"grošů.")
                print("Obchodník nabízí:")
                print("1 - Střední lektvar (Doplní až 40 HP.) Cena: 15 grošů")
                if not zlaty_mec:
                    print("2 - Zlatý meč (Udělí 50 až 70 poškození.) Cena: 400 grošů")
                if not brneni:
                    print("3 - Stříbrná zbroj (Sníží poškození až o 50%) Cena: 80 grošů")
                print("0 - Odejít")
                volba = ziskat_volbu()
                if volba == 1:
                    if gros["pocet"] > 15:
                        pocet_str_lektvar()
                        gros["pocet"] -= 15
                        print("Zakoupil jsi 1 střední lektvar.")
                    else:
                        print("Nemáš dostatek grošů.")
                elif volba == 2:
                    if not zlaty_mec:
                        if gros["pocet"] > 400:
                            inventar.append(pridat_zlatý_mec())
                            gros["pocet"] -= 400
                            aktualni_zbran = najdi_predmet("Zlatý meč")
                            print("Vybavil ses Zlatým mečem.")
                        else:
                            print("Nemáš dostatek grošů.")
                    else:
                        print("Neplatná možnost!")
                elif volba == 3:
                    if not brneni:
                        if gros["pocet"] > 80:
                            inventar.append(pridat_stribrna_zbroj())
                            gros["pocet"] -= 80
                            aktualni_armor = najdi_predmet("Stříbrná zbroj")
                            print("Vybavil ses Stříbrnou zbrojí.")
                        else:
                            print("Nemáš dostatek grošů.")
                    else:
                        print("Neplatná možnost!")
                elif volba == 0:
                    break            
                else:
                    print("Neplatná možnost!")

        else:
            print("Neplatná možnost!")
    elif poloha == 12:
        print("Došel si do předsíně.")
        zobraz_moznosti(poloha)
        volba = ziskat_volbu()
        if volba == 0:
            hp, game_on = menu(hp,max_hp)
        elif volba == 1:
            poloha = 8
        elif volba == 2:
            poloha = 13
        elif volba == 3:
            poloha = 14
        elif volba == 4:
            klic = najdi_predmet("Zlatý klíč")
            if not klic:
                print("Dveře do hlavní síně jsou zamčené.")
            else:
                poloha = 16
        else:
            print("Neplatná možnost!")
    elif poloha == 13:
        print("Došel si do spíže.")
        if odmena_spiz:
            pocet_vel_lektvar()
            gros = najdi_predmet("Groše")
            gros["pocet"] += 20
            odmena_spiz = False
            print("Našel jsi velký lektvar a 20 grošů.")
        zobraz_moznosti(poloha)
        volba = ziskat_volbu()
        if volba == 0:
            hp, game_on = menu(hp,max_hp)
        elif volba == 1:
            poloha = 12
        else:
            print("Neplatná možnost!")
    elif poloha == 14:
        print("Došel si do kaple.")
        enemy = najdi_enemy("Nemrtvý strážce")
        if enemy["hp"] > 0:
            print("Pozor! Před tebou stojí ",enemy["jmeno"],"!")
            hp, poloha = souboj(hp, enemy, poloha,max_hp)
            if enemy["hp"] <= 0:
                gros = najdi_predmet("Groše")
                gros["pocet"] += 400
                inventar.append(pridat_srdce())
                inventar.append(pridat_zlaty_klic())
                max_hp = 200
                print("Získal jsi od nepřítele Srdce strážce,které ti zvýší maximální HP na 200, Zlatý klíč a 400 grošu!")
        else:
            zobraz_moznosti(poloha)
            volba = ziskat_volbu()
            if volba == 0:
                hp, game_on = menu(hp,max_hp)
            elif volba == 1:
                poloha = 12
            elif volba == 2:
                poloha = 10
            elif volba == 3:
                poloha = 15
            else:
                print("Neplatná možnost!")
    elif poloha == 15:
        print("Došel si do skleníku, uprostřed vidíš malou kašnu s léčivou vodou.")
        zobraz_moznosti(poloha)
        volba = ziskat_volbu()
        if volba == 0:
            hp, game_on = menu(hp,max_hp)
        elif volba == 1:
            poloha = 14
        elif volba == 2:
            if fontana2:
                hp = max_hp
                fontana2 = False
                print("Vyléčil ses na", max_hp,"HP")
            else:
                print("Můžeš se vyléčit pouze jednou!")
        else:
            print("Neplatná možnost!")
    elif poloha == 16:
        print("Došel si do královské síně.")
        enemy = najdi_enemy("Padlý král")
        if enemy["hp"] > 0:
            print("Pozor! Před tebou stojí ",enemy["jmeno"],"!")
            hp, poloha = souboj(hp, enemy, poloha,max_hp)
            if enemy["hp"] <= 0:
                gros = najdi_predmet("Groše")
                gros["pocet"] += 1000
                print("Porazil jsi samotného krále! Tvůj úkol byl splněn. Jdi! A oslavuj!")
        else:
            zobraz_moznosti(poloha)
            volba = ziskat_volbu()
            if volba == 0:
                hp, game_on = menu(hp,max_hp)
            elif volba == 1:
                print("Dohrál jsi hru. Gratuluji.")
                break
            elif volba == 2:
                poloha = 12
            else:
                print("Neplatná možnost!")


if hp <= 0:
    print("_____________________________________________")
    print("Prohrál jsi!")