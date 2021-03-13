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
    def __init__(self, ID, quote, author, submitted_by):
        self.ID = ID
        self.quote = quote
        self.author = author
        self.submitted_by = submitted_by

    def __repr__(self):
        return "ID: " + self.ID + " Quote: " + self.quote + " Author: " + self.author + " Submitted by: " + self.submitted_by

    def __str__(self):
        return "ID: " + self.ID + " Quote: " + self.quote + " Author: " + self.author + " Submitted by: " + self.submitted_by    

#2. Class for representing all the quotes (quotes collection).
# This class represents a collection of quotes
# _repr__ and __str__
# TODO: ________
class QuotesList:
    def __init__(self, quotes):
        self.quotes = quotes

    def __str__(self):
        return quotes.__str()

    def __repr__(self):
        return quotes.__str()

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if (self.x < len(self.quotes)):
            current_quote = self.quotes[self.x]
            self.x = self.x+1
            return current_quote
        else:
            raise StopIteration


# Method for creating the  Quote object
# INPUT: one line of string
# OUTPUT: the quotes object
# Assume file_name is quotes_in_excel.csv
# And further assume that the file is in the same directory as python file
    #this method reads the file
    # creates a list of lines
    # where each line represents a quote
    # each line is split into four fields
    # and a quote object is created
    # then the created object is added to QuotesList
    # by the time, the process_file method is done, we will have a QuotesList collection
def process_file(file_name):
    file = open("/Users/nikhitha/Documents/SILC-Python/cryptoquote/quotes_in_excel.csv", encoding='iso-8859-15')
    lines_list = file.readlines()
    list_of_quotes = []
    for x in lines_list:
        y = x.split(",")
        quote = Quote(y[0], y[1], y[2], y[3])
        list_of_quotes.append(quote)
    qlist = QuotesList(list_of_quotes)
    return qlist
    



# Program execution
quotes_list = process_file("quotes_in_excel.csv")
for x in quotes_list:
    print(x)
#print(quotes_list)
