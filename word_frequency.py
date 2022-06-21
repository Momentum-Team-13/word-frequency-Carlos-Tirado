STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]



def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""

    print(f'Your file is:{file}')

    with open(file) as open_file:
        word_dictionary = {} # contains all of the words as key value pairs
        words_list = [] # contains all of the words in the text file
        #read_file = open_file.read()
        for line in open_file.readlines():
        #lowercase_line = line.lower().replace(',','').replace('.','').replace('?','') #short way
            lowercase_line = line.lower()
            remove_comas = lowercase_line.replace(',','')
            remove_dots = remove_comas.replace('.','')
            remove_questionmark = remove_dots.replace('?','') #just an example if a I need to remove question marks
            # print(f'This is a line: {remove_questionmark}')
            # putting the words in a dictionary
            # print (remove_questionmark.split())

            for worditem in remove_questionmark.split(): #we are looping each word in the list
                #print("word", worditem)         #printing list word item
                words_list.append(worditem)

        #print(words_list) #
        for worditem in words_list:
            #print(worditem) #
            word_dictionary[worditem] = words_list.count(worditem)
            # print(worditem, words_list.count(worditem))#

        # print(word_dictionary)#
        new_copy = word_dictionary.copy()
        for word in word_dictionary:
            if word in STOP_WORDS:
                # print(word)#
                del new_copy[word]
        #print(new_copy)#
        
        final_list = sorted(new_copy.items(), key=lambda item: item[1], reverse=True)
        # print(new_copy.items()[0])#
        # print(final_list)#
        for item in final_list:
            print(item[0], item[1], "*"*item[1])





if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
