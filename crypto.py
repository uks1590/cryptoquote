#Program for generating the Crypto Quote

# Import String to generate Alphabet Characters
import string

# Import Random to shuffle the List
import random

# Method for Integrating all functions
# Author: Keertan 
print("Functions: getStudentWithMostQuotes, getQuotesByAuthor, getQuotesByStudent, getAuthorAndQuoteCount, generateCryptoQuoteList, 
getSortedAuthors, getWordListByFrequency, getQuotesCountByAuthor, getAuthorWithLessQuotes, getShortestQuote, getAuthorCount, 
getLongestQuote, getAuthorWithMostQuotes, getSubmittedByAndQuoteCount, getQuotesContainingWord, getStudentListWithNoQuotes")
Function_Menu = input("Choose and type which function to run on the cryptoquote generated")

if Function_Menu == "":
    pass

if Function_Menu: 
    pass

#1. Class for representing a single QUOTE
# id, quote, author, submitted_by
# _repr__ and __str__
class Quote:
    
    def __init__(self, id, quote, author, submitted_by):
        self.id = id
        self.quote = quote
        self.author = author
        self.submitted_by = submitted_by

    def __repr__(self):
        return 'Quote(id=%s, quote=%s, author=%s, submitted_by=%s)' % (self.id, self.quote, self.author, self.submitted_by)
    
    def __str__(self):
        return 'Quote(id=%s, quote=%s, author=%s, submitted_by=%s)' % (self.id, self.quote, self.author, self.submitted_by)


#2. Class for representing all the quotes (quotes collection).
# This class represents a collection of quotes
# _repr__ and __str__
class QuotesList:

    def __init__(self):
        self.quotes_list = []
        
    def __str__(self):
        return 'QuotesList(quotes_list=%s)' % (self.quotes_list)

    def __repr__(self):
        return 'QuotesList(quotes_list=%s)' % (self.quotes_list)

    def add(self, quote):
        self.quotes_list.append(quote)
        
        
        
     # Karthik,s code for sorting based on author
        #Method used inside sorting authors in quotes
def mysort(line):
  return line.split(",")[2]
     # Karthik,s code for sorting based on author

#Method for sorting the quotes based on author names
def getSortedAuthors(file_name): 
    
      file = open(file_name)
      lines_data = file.readlines()

      for line in sorted(lines_data, key=mysort):
       print(line)

      file.close()
      return sorted(lines_data, key=mysort)

        
# This method chooses a random quote from the collection
# The quote is converted to the crypto quote
# The crypto quote is shown on the HTML page
# Author : Ishana D
    def showRandomCryptoInHTML(self):
        return self
        



# Generates Crypto Quote for the input Quote
def generateCryptoQuote(quote):
    upper_quote = quote.upper()
    quote_list = list(upper_quote)
    quote_list_temp = list(upper_quote)
    
    list_of_alphabets = []
    list_of_alphabets = list(string.ascii_uppercase)
    
    random_list_of_alphabets = list(list_of_alphabets)
    random.shuffle(random_list_of_alphabets)

    output_queue_pos = -1
    for quote_char in quote_list:
        output_queue_pos += 1
        if quote_char in list_of_alphabets:
            quote_char_alphbt_pos = list_of_alphabets.index(quote_char)
            replace_char = random_list_of_alphabets[quote_char_alphbt_pos]
            quote_list_temp[output_queue_pos] = replace_char

    cryptoquote = ''.join(quote_list_temp)

    return cryptoquote

    #author:vikranth
    #this method returns all the students who did not submit 
    #any quotes to the collection
    def getStudentListWithNoQuotes():
        pass

# Method for creating the  Quote object
def process_file(file_name):

    quotes_list = QuotesList();
    file = open(file_name)

    for x in file.readlines():
        fields = x.split(',')
        quote = Quote(fields[0], fields[1], fields[2], fields[3])
        quotes_list.add(quote)

        crypto_quote = generateCryptoQuote(fields[1])
    
    file.close()
    return quotes_list
        
# Program execution
quotes_list = process_file("quotes_in_excel.csv")
print(quotes_list)
    
    
    quoteslist_sort_author = getSortedAuthors("quotes_in_excel.csv")
print(quoteslist_sort_author) 
