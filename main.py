#the main function, inputs the book, prints the number of words
def main():
    book_path="books/frankenstein.txt"
    text=get_text(book_path)
    word_count=count(text)
    character_count=char_count(text)
    character_count.sort(reverse=True, key=sorting_key_number)
    print(f"--Begin report of {book_path}--")
    print(f"{word_count} words found in the document")
    print(character_count)

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

#the sorting key function, returns a number of appearances of each character, used in dictionary ordering
def sorting_key_number(dict):
    for char in dict:
        return dict[char]


main()








