def otoc_seznam(seznam):
    novy_seznam = seznam[::-1]
    return novy_seznam

def konec_vety(li):
    novy_li = []
    for a in li:
        i = list(a)
        if i[-1] == "." or i[-1] == "!" or i[-1] == "?":
            i.insert(0, i[-1])
            del i[-1]
            a = ''.join(i)
        novy_li.append(a)
    return(novy_li)

text = input("Vložte text:")
print(text)
text_list = text.split()
print(text_list)
text_list_opacne = otoc_seznam(text_list)
print(text_list_opacne)
text_list_opacne_konce = konec_vety(text_list_opacne)
print(text_list_opacne_konce)