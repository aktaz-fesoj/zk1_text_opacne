def otoc_seznam(seznam):
    novy_seznam = seznam[::-1]
    return novy_seznam

def konec_vety_nebo_carka(li):
    novy_li = []
    for a in li:
        i = list(a)
        if i[-1] == "." or i[-1] == "!" or i[-1] == "?" or i[-1] == ",":
            i.insert(0, i[-1])
            del i[-1]
            a = ''.join(i)
        novy_li.append(a)
    return(novy_li)

def velke_pismeno(li):
    novy_li = []
    for a in li:
        i = list(a)
        if i[0].isupper() == True:
            i[0] = i[0].lower()
            i[-1] = i[-1].upper()
            a = ''.join(i)
        novy_li.append(a)
    return(novy_li)

def nacti_data(adresa):
    with open(adresa, encoding = "utf-8") as vstupni_text:
        text_read = vstupni_text.read()
    return(text_read)

def zapis_text(adresa, text_k_zapsani):
    with open(adresa, "w", encoding = "utf-8") as vystupni_text:
        vystupni_text.write(text_k_zapsani)
    return(f"Úspěšně uložen soubor {adresa} s textem s obráceným pořadím slov.")


try:
    text = nacti_data("text.txt")
except:
    text = input("Soubor text.txt nebyl nalezen ve stejné složce, ze které spouštíte tento program. Můžete vložit text ručně:")
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