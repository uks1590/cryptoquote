#Draft For QuotesContainingWord; Need to get excel.
input_word = input("Enter word to find quotes containing it: ")
def getQuotesContainingWord(input_word):
    quotes_list = open("QuotesList")
    found = False
    for line in quotes_list:
        if input_word in line:
            found = True
            break
    if found == True:
        return True
    else:
        return False
getQuotesContainingWord(input_word)
