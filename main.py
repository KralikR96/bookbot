#the main function, inputs the book, prints the number of words
def main():
    book_path="books/frankenstein.txt"
    text=get_text(book_path)
    word_count=count(text)
    character_count=char_count(text)
    character_count_list=dictionary_to_listofdictionaries(character_count)
    character_count_list.sort(reverse=True, key=sorting_key_number)
    print(f"--Begin report of {book_path}--")
    print(f"{word_count} words found in the document")
    alpha_report(character_count_list)

#the read function, returns the book as a string
def get_text(path):
    with open(path) as f:
        file_contents=f.read()
    return(file_contents)


#the count function, returns the number of words in a book
def count(text):
    words=text.split()
    return len(words)

#the character count function, returns a dictionary of character/number of appearances in order of appearance
def char_count(text):
    lowercase_dictionary={}
    lowercase_text=text.lower()
    for char in lowercase_text:
        if char in lowercase_dictionary:
            lowercase_dictionary[char] += 1
        else: lowercase_dictionary[char] = 1
    return lowercase_dictionary

#turn dictionary into a list of dictionaries

def dictionary_to_listofdictionaries(dict):
    turned_list=[]
    sub_dict={}
    for char in dict:
        sub_dict["character"]=char
        sub_dict["count"]=dict[char]
        turned_list.append(sub_dict)
        sub_dict={}
    return turned_list


#the sorting key function, returns a number of appearances of each character, used in dictionary ordering
def sorting_key_number(dict):
    return dict["count"]

#alphabetical characters generating report
def alpha_report(list):
    for dict in list:
        if dict["character"].isalpha()==True:
            print(f"The '{dict["character"]}' character was found {dict["count"]} times")



main()








