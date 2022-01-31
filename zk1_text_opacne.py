def otoc_seznam(seznam):
    """Funkce obrátí pořádí prvků seznamu.

        Parameters:
                    seznam(list): Vstupní seznam, který bude otočen
                    novy_seznam(list): Výstupní seznam s opačným pořadím prvků oproti seznamu vstupnímu
    """
    novy_seznam = seznam[::-1]      # Step parameter -1 docílí "braní" prvků v opačném pořadí
    return novy_seznam

def konec_vety_nebo_carka(li):
    """Funkce upraví položky v seznamu. Pokud se na konci řetězce nachází alespoň jeden ze znaků .,;?! bude tento znak(y) převeden na druhou stranu textového řetězce (pokud se zde nachází znaků více, budou převedeny v opačném pořadí).

        Parameters:
                    li(list): Vstupní seznam, který bude upraven
                    novy_li(list): Výstupní upravený seznam
    """
    novy_li = []
    for a in li:
        i = list(a)                 #Rozdělení slova na znaky
        znovu = True
        while znovu == True:        #Následující část se opakuje dokud na konci slova není žádný "nevhodný" znak
            if i[-1] == "." or i[-1] == "!" or i[-1] == "?" or i[-1] == "," or i[-1] == ";":
                i.insert(0, i[-1])  #Vložení daného znaku na první pozici řetězce (=před řetězec)
                del i[-1]           #Pdstranění znaku z konce řetězce
                a = ''.join(i)      #Opětovné spojení znaků do slova
            else:
                znovu = False

        novy_li.append(a)
    return novy_li

def velke_pismeno(li):
    """Funkce upraví položky v seznamu. Začíná-li textový řetězec velkým písmenem, bude toto písmeno zmenšeno a naopak zvětšen bude poslední znak řetězce.

        Parameters:
                    li(list): Vstupní seznam, ve kterém budou upravena počáteční velká písmena
                    novy_li(list): Výstupní upravený seznam
    """
    novy_li = []
    for a in li:
        i = list(a)
        if i[0].isupper() == True:
            i[0] = i[0].lower()
            i[-1] = i[-1].upper()
            a = ''.join(i)
        novy_li.append(a)
    return novy_li

def nacti_data(adresa):
    """Funkce načte textový řetězec ze souboru a uloží ho do proměnné.

        Parameters:
                    adresa(str): Absolutní či relativní cesta k zdrojovému textovému souboru
                    text_read(str): Textový řetězec obsahující text ze vstupního textového souboru
    """
    with open(adresa, encoding = "utf-8") as vstupni_text:
        text_read = vstupni_text.read()
    return(text_read)

def zapis_text(adresa, text_k_zapsani):
    """Funkce uloží text do textového souboru.

        Parameters:
                    adresa(str): Absolutní či relativní cesta k souboru, do kterého má být text zapsán
                    text_k_zapsani(str): Text, který bude do výstupního souboru zapsán
    """
    with open(adresa, "w", encoding = "utf-8") as vystupni_text:
        vystupni_text.write(text_k_zapsani)
    return(f"Úspěšně uložen soubor {adresa} s textem s obráceným pořadím slov.")


try:
    text = nacti_data("text.txt")
except:
    text = input("Soubor text.txt nebyl nalezen ve stejné složce, ze které spouštíte tento program, nebo se ho nepodařilo úspěšně spustit. Můžete vložit text ručně:")
print(text)
vel_pismena_ano = input("Přejete si upravit velikost písmen pro čtení zprava doleva? Zadejte 1 pro volbu ANO.")
text_list = text.split()
text_f = otoc_seznam(text_list)
text_f = konec_vety_nebo_carka(text_f)
if vel_pismena_ano == "1":
    text_f = velke_pismeno(text_f)
text_f_spojeny = ' '.join(text_f)
print(text_f_spojeny)
zapis_ano = input("Přejete si zapsat upravený výsledný text do nového textového souboru? Zadejte 1 pro volbu ANO.")
if zapis_ano == "1":
    zapis_text("obraceno.txt", text_f_spojeny)