def list_reverse(list1):
    """The function takes in a list and returns the same list in reversed order.

        Parameters:
                    list1(list1): The input list that has to be reversed
        Returns:
                    new_list(list): Output list with elements in reversed order in comparison with the input list.
    """
    # Elements are going to be "taken" in reverse order due to step parameter -1
    new_list = list1[::-1]
    return new_list

def interpunction(li):
    """The function modifies elements in a list. If there is at least one of symbols .,;:?! at end of a string, this symbol is going to be moved to the opposite \
    side of the string (if more than one symbol occures, symbols are gonna be moved in reversed order)

        Parameters:
                    li(list): Input list that is going to be modified
        Returns:
                    new_li(list): Modified list
    """
    new_li = []
    for a in li:
        #Spliting the word to list of single characters
        i = list(a)
        again = True
        #Following section iterates until any "invalid" (as mentioned above) character remains at the end of a string 
        while again == True:
            if i[-1] == "." or i[-1] == "!" or i[-1] == "?" or i[-1] == "," or i[-1] == ";" or i[-1] == ":":
                #Putting the character to the first position in a string (=in front of the string)
                i.insert(0, i[-1])
                #Deleting the invalid character from the end of the string
                del i[-1]
                #Joining the characters into a single string again
                a = ''.join(i)
            else:
                again = False

        new_li.append(a)
    return new_li

def capital_letter(li):
    """The function modifies elements in a list. When on position 0 in a string capital letter is found, \
        the function changes it to small letter and a character on last position in the string is changed to uppercase.

        Parameters:
                    li(list): Input list that is going to be modified
        Returns:
                    new_li(list): Output list with modified capital letters
    """
    new_li = []
    for a in li:
        i = list(a)
        if i[0].isupper() == True:
            i[0] = i[0].lower()
            i[-1] = i[-1].upper()
            a = ''.join(i)
        new_li.append(a)
    return new_li

def load_data(adress):
    """Function loads text string from a file and saves it as a variable.

        Parameters:
                    adress(str): Absolute or relative path of a text file that has to be loaded
        Returns:
                    text_read(str): String containing text from input text file
    """
    with open(adress, encoding = "utf-8") as input_text:
        text_read = input_text.read()
    return(text_read)

def write_text(adress, text_to_be_written):
    """Function saves text to text file

        Parameters:
                    adress(str): Absolute or relative path of a file, where the text should be written
                    text_to_be_written(str): String containing text that is going to be written in the file
    """
    with open(adress, "w", encoding = "utf-8") as output_text:
        output_text.write(text_to_be_written)
    return(f"File {adress} containing text with reverse order of words was successfully saved.")

try:
    text = load_data("text.txt")
except:
    text = input("File text.txt was not found in the same folder from which you are running this program, or it fail to load the file. You can enter text manually:")
print(f"Following text is going to be modified (words are going to be written in reverse order): {text}")
capitals_yes = input("Do you wish to change capital letters in order to make the text readable in right-left direction? Enter 1 for YES.")
#Splits the text by whitespaces (including more whitespaces, including tabs)
text_list = text.split()
text_f = list_reverse(text_list)
text_f = interpunction(text_f)
if capitals_yes == "1":
    text_f = capital_letter(text_f)
text_f_joined = ' '.join(text_f)
print(text_f_joined)
write_yes = input("Do you wish to save generated reversed text to new text file? Enter 1 for YES.")
if write_yes == "1":
    write_text("reversed.txt", text_f_joined)