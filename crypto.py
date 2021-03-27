#Program for generating the Crypto Quote

# Import String to generate Alphabet Characters
import string

# Import Random to shuffle the List
import random


#======= Class Quote =============================
# Class for representing a single QUOTE
# id, quote, author, submitted_by
# _repr__ and __str__
class Quote:
    
    def __init__(self, id, quote, author, submitted_by):
        self.id = id
        self.quote = quote
        self.author = author
        self.submitted_by = submitted_by

    def __repr__(self):
        return "ID: " + self.id + " Quote: " + self.quote + " Author: " + self.author + " Submitted by: " + self.submitted_by

    def __str__(self):
        return "ID: " + self.id + " Quote: " + self.quote + " Author: " + self.author + " Submitted by: " + self.submitted_by    
   


#======= Class QuotesList =============================
#Class for representing all the quotes (quotes collection).
# This class represents a collection of quotes
# _repr__ and __str__
class QuotesList:


    # constructor method for creating a QuotesList object
    # The list of quotes should be constructed outside of the class
    def __init__(self, some_list_of_quotes):
        self.quotes_list = some_list_of_quotes
        

   
    # Another method for creating the  Quote object
    # This method takes the file name as the input
    # See https://stackoverflow.com/questions/44726196/how-to-implement-multiple-constructors-in-python
    @classmethod
    def createWithFileName(cls, file_name):
        # create an empty list of quotes
        quotes_list = [ ]

        # now process the file
        file = open(file_name)
        lines_list = file.readlines()
        for x in lines_list:
            fields = x.split(',')
            quote = Quote(fields[0], fields[1], fields[2], fields[3])
            #print(quote)
            quotes_list.append(quote)
        file.close()

        #print("printing the collection")
        #print(quotes_list_from_file)
        # now, return this 
        return cls(quotes_list)



    # We will now have a getMethod for other classes to get the quotes_list variable
    # from QuotesList object
    def getQuotesList(self):
         return self.quotes_list

    # This is a useful function to print the quotes_list
    # Can be called by different methods to validate that their methods are working
    def printQuotes(self):
        for x in self.quotes_list:
            print(x)
        


    # We will now have methods for __str, __ repr, and __ iter
    # these are the standard methods to print and iterate the object
    def __str__(self):
        return quotes_list.__str()

    def __repr__(self):
        return quotes_list.__str()

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if (self.x < len(self.quotes_list)):
            current_quote = self.quotes_list[self.x]
            self.x = self.x+1
            return current_quote
        else:
            raise StopIteration

    #================= PLEASE READ ======================================
    # All the student's methods start here.
    # Please write the method number and your name as the first line comment
    # Proive the "purpose" of the function
    # Make sure that you are adding your method at the respective sequence
    # Please ensure that you are always working with the latest version of crypto.py
    # So please sync with the UPSTREAM every week
    #=====================================================================

    # ============= Method No: 3 (Achuyuth Madhavan) ===============
    # Purpose: This method returns the name of the student
    #          who submitted the most number of quotes
    def getStudentWithMostQuotes(self):
        # TODO
        student_name = "TODO first name last name"
        return student_name


    # ============= Method No: 11 (Karthik Uppala) ===============
    # Purpose: This method returns provide the list of "author"
    # (name of the authors) in sorted order
    def getSortedAuthors(self):
        # TODO
        # you have to operate on this variable self.quotes_list

        sorted_authors_list = ["a", "bx", "c", "jasthi"]
        return sorted_authors_list
    

    # ============= Method No: 13 (Nikhitha Gollamudi) ===============
    # Purpose: This method returns the words in the quotes sorted by frequency 
    def getWordListByFrequency(self):
        words_list = []
        word_dict = {}

        for x in self.quotes_list:
            quote_str = x.quote
            words_list = words_list + quote_str.split(" ")
          
        for word in words_list:
            if word != "":
                if word not in word_dict.keys():
                   word_dict[word] = 1
                else:
                    word_dict[word] = word_dict.get(word) + 1
        sorted_dict = {}
        sorted_keys = sorted(word_dict, key=word_dict.get, reverse=True)  

        for w in sorted_keys:
            sorted_dict[w] = word_dict[w]

        return sorted_dict
    # ============= Method No: 16 (Pranav) ===============
    # Purpose: This method returns the count of quotes submitted by the author

    def getCountOfQuotesByAuthor(self, author_name):
        quote_count = 0
        for x in self.quotes_list:
            p = x.author.strip()
            q = author_name.strip()
            if p == q:
                quote_count = quote_count + 1
        return quote_count

        # TODO
        return quote_count



    # ============= Method No: 14 (Om Rege) ===============
    # Purpose: This method returns the count of quotes submitted by him/her 
    def getCountOfQuotesByStudent(self, some_student_name):
        quote_count = 0
        # TODO
        return quote_count
   


    # ============= Method No: 20 (Sai Akaksha Josylua) ===============
    # Purpose: This method returns the count of Authors in the quotes collection
    def getAuthorCount(self):
        # this is the quotes_list variable
        #e need to operat on this one
        author_count = 30
        #for x in self.quotes_list:

        return author_count   
    

    # ============= Method No: 29 (Siva Jasthi) ===============
    # Purpose: The method returns a mini-collection of quotes containing the bad words
    # Reference: https://www.geeksforgeeks.org/python-test-if-string-contains-element-from-list/
    def getQuotesContainingBadWords(self):
        bad_word = ["heck", "damn"]
        #this need to be calculated
        quotes_list_containing_bad_words = []
        y = ""
        for x in self.quotes_list:
            for y in bad_word:
                word = " " + y.lower() + " "
                if word in str(x).lower():
                    quotes_list_containing_bad_words.append(x)
                    break

        # create a mini quotes collection 
        quotes_mini_collection = QuotesList(quotes_list_containing_bad_words)
        return quotes_mini_collection;
        



    # ============= Method No: 30 (Nikhitha Gollamudi) ===============
    # Purpose: The quotes collection may have been changed by add, update and delete methods.
    #          This method writes the contents of the quotes_list into the file
    def saveToFile(self):
        file = open("quotes_in_excel.csv", "w", encoding='iso-8859-15')
        file.write(str(self.quotes_list))
        file.close()
    
        
  

    # For adding a quote to the collection
    def add(self, quote):
        self.quotes_list.append(quote)
        
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

#========================= STARTING POINT ==========================
# All the testing happens here
# Please ensure that you print some info about the method invocation and the results
# Please ensure that you put the method number, your name and method name in the print
#================= Starting Point ===============================
# This is the starting point for the program execution
#
# Step 1:  Create a QuotesList object from the input file
quotes_list_object = QuotesList.createWithFileName("quotes_in_excel.csv")

# Step 2:  Now, ask the quotes_list_object for its variable quotes_list
# quotes_list_x = quotes_list_object.getQuotesList()

# Step 3: Just for debugging, iterate through the quotes collection and print it
# We will comment it this line out during the demo
# for x in quotes_list_x:
#    print(x)

# Step 3: Invoke the helper function to print the quotes
print("=== Printing all the quotes:  printQuotes() method ========")
#quotes_list_object.printQuotes()

# Step 4: Now let us exercise some methods in the QuotesList

# ========= Achyuth Madhavan: Method # 3 ========================
print("=== Method #3 (Achyuth Madhavan) def getStudentWithMostQuotes( ) method ====")
student_name = quotes_list_object.getStudentWithMostQuotes()
print(student_name)


# ========= Karthik Uppala: Method # 11 ========================
print("=== Method #11 (Karthik Uppala) def getSortedAuthors( )method ====")
sorted_authors_list_x = quotes_list_object.getSortedAuthors( )
print(sorted_authors_list_x)

# ========= Nikhita Gollamudi: Method # 13 ========================
print("=== Method #13 (Nikhita Gollamudi) getWordListByFrequency( ) method ====")
word_frequency = quotes_list_object.getWordListByFrequency()
#print(word_frequency)

# ========= Om Rege: Method # 14 ========================
print("=== Method #14 (Om Rege) getCountOfQuotesByStudent(student_name)method ====")
student_name = "Jasthi"
quote_count = quotes_list_object.getCountOfQuotesByStudent(student_name)
print(quote_count)

student_name = "ABC"
quote_count = quotes_list_object.getCountOfQuotesByStudent(student_name)
print(quote_count)


# ========== Happy Josyula: Method #20 =================
print("=== Method #20  (Happy Josyula) getAuthorCount( ) method ====")
quotes_list_object = QuotesList.createWithFileName("method_20.csv")
author_count = quotes_list_object.getAuthorCount( )
print(author_count)

# =================pranav mukkara #16======================
print("=== Method #16 (Pranav mukkara) getCountOfQuotesByauthor(author_count)method ====")
author_name = "Harvey Specter"
quote_count = quotes_list_object.getCountOfQuotesByAuthor(author_name)
print(quote_count)

# ========= Nikhitha Gollamudi: Method # 29 ========================
print("===  Method #29 (Nikhitha Gollamudi) def getQuotesContainingBadWords()  method ====")
mini_collection_29 = quotes_list_object.getQuotesContainingBadWords()
#mini_collection_29.printQuotes()


# ========= Nikhita Gollamudi: Method # 30 ========================
print("=== Nikhita Gollamudi: Method #30; saveToFile( ) method ====")
#quotes_list_object.saveToFile()


    
