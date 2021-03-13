#Program for generating the Crypto Quote

#Read the file
#For each line, construct a “Quote” object
#Add that Quote to a collection
#Create a “CryptoQuote” for each quote in the selection.
#Display all the “CryptoQuotes” as HTML

#============================================================



#1. Class for representing a single QUOTE
# id, quote, author, submitted_by
# _repr__ and __str__
# TODO: ______
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
# TODO: ________
class QuotesList:

    def __init__(self):
        self.quotes_list = []

    def __str__(self):
        return 'QuotesList(quotes_list=%s)' % (self.quotes_list)

    def __repr__(self):
        return 'QuotesList(quotes_list=%s)' % (self.quotes_list)

    def add(self, quote):
        self.quotes_list.append(quote)

    def def deleteQuote(quote_id):
        pass
    
    


# Method for creating the  Quote object
# INPUT: one line of string
# OUTPUT: the quotes object
# Assume file_name is quotes_in_excel.csv
# And further assume that the file is in the same directory as python file
def process_file(quotes_in_excel_anu):
    #this method reads the file
    # creates a list of lines
    # where each line represents a quote
    # each line is split into four fields
    # and a quote object is created
    # then the created object is added to QuotesList
    # by the time, the process_file method is done, we will have a QuotesList collection


    quotes_list = QuotesList();
    file = open("quotes_in_excel_anu.csv")

    for x in file.readlines():
        fields = x.split(',')
        quote = Quote(fields[0], fields[1], fields[2], fields[3])
        quotes_list.add(quote)

    file.close()
    return quotes_list

# Program execution
# quotes_list = process_file("quotes_in_excel.csv")
# print(quotes_list)
quotes_list = process_file("quotes_in_excel_anu.csv")
print(quotes_list, sep = "\n")
