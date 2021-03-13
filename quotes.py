#Program for generating the Crypto Quote

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


# Method for creating the  Quote object
def process_file(file_name):

    quotes_list = QuotesList();
    file = open(file_name)

    for x in file.readlines():
        fields = x.split(';')
        quote = Quote(fields[0], fields[1], fields[2], fields[3])
        quotes_list.add(quote)
    
    file.close()
    return quotes_list
        
# Program execution
quotes_list = process_file("Quotes_excel_hiranmayi.txt")
print(quotes_list)
    
