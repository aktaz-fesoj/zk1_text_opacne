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

text = input("Vložte text:")
print(text)
vp = input("Přejete se upravit velikost písmen pro čtení zprava doleva? Zadejte 1 pro volbu ANO.")
text_list = text.split()
text_f = otoc_seznam(text_list)
text_f = konec_vety_nebo_carka(text_f)
if vp == "1":
    text_f = velke_pismeno(text_f)
text_f_spojeny = ' '.join(text_f)
print(text_f_spojeny)