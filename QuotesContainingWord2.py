input_word = input("Enter word to search: ")
def getQuotesContainingWord(input_word):
    quotes_list = open("QuotesList.txt","r")
    count = 1
    L=quotes_list.readlines()
    for i in L:
        L2 = i.split()
        count += 1
        if input_word in L2:
            print("Line Number",count,":",i)

getQuotesContainingWord(input_word)