def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path) #reads book as string
    words = text.split() #converts string to list on whitespace
    num_of_words = get_num_words(words) 
    num_of_char = get_characters(text) #returns a dictionary
    list_dictionary = list_of_dictionary(num_of_char)
    list_dictionary.sort(reverse = True, key = sort_on)
    #Printing on the screen
    print(f"--- Begin report of {path} ---")
    print(f"{num_of_words} words found in the document")
    for dict in list_dictionary:
        value_1 = dict["char"]
        value_2 = dict["count"]
        print(f"The '{value_1}' character was found {value_2} times")
        


def sort_on(dict):
    return dict["count"]
   
    
def list_of_dictionary(dict):
    list = []
    for key,value in dict.items():
        list.append({"char":key, "count":value})
    return list

def get_num_words(words):
    return len(words)

def get_characters(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()