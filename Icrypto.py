#Program for generating the Crypto Quote

# Import String to generate Alphabet Characters
import string

# Import Random to shuffle the List
import random

#Import Pretty Printing
import pprint
pp = pprint.PrettyPrinter(indent=4)

#Importing webbrowser module to open the html page from a browser
import webbrowser
import urllib


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
        id = str(self.id)
        return "ID: " + id + " Quote: " + self.quote + " Author: " + self.author + " Submitted by: " + self.submitted_by    
   
    def writeToHTML(self):
        current_quote = self.quote
        file = open("random_quote.html", "w", encoding='iso-8859-15')
        file.write(current_quote)
        file.close()

        

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
    # this method imports CSV module to ensure that we are processing the CSV correctly
    # as some quotes may contain commas.
    @classmethod
    def createWithFileName(cls, file_name):
        # create an empty list of quotes
        quotes_list = [ ]

        # now process the file
        file = open(file_name)
        import csv
        reader = csv.reader(file)
        for fields in reader:
            quote = Quote(fields[0], fields[1], fields[2], fields[3])
            quotes_list.append(quote)
        file.close()
        
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

    # ============= Method No: 2 (Nikhitha Gollamudi) ===============
    # Purpose: This method returns how many students (submitted_by) there are in the quotes collection 
    def getStudentCount(self):
        students = set()
        
        for x in self.quotes_list:
            students.add(x.submitted_by)
        return len(students)

    # ============= Method No: 3 (Nikhitha Gollamudi) ===============
    # Purpose: This method returns the student with the most quotes submitted 
    def getStudentWithMostQuotes(self):
        students_list = []
        student = ""
        count = 0
        for x in self.quotes_list:
            students_list.append(x.submitted_by)
            for x in students_list:
                freq = students_list.count(x)
                if freq > count:
                    count = freq
                    student = x
        return student
   

    # ============= Method No: 4 (Anjneya Kumar) ===============
    # Purpose: The method returns a mini-collection of quotes by a certain author (given by the user)
    #TODO: 1. you need to take the author as the input parameter to the method
    #TODO: 2. You need to build a mini collection and return it
    def getQuotesByAuthor(self):
        pass



    # ============= Method No: 5 (Arjun) ===============
    # Given a student name, return a mini collection of all the quotes
    def getQuotesByStudent(student_name):
        pass

     
    # ============= Method No: 6 (Eshaan Dhavala) ===============
    # Purpose: This method returns dictionary
    #  with author as the key, and count as the value
    def getAuthorAndQuoteCount(self):
        author_count_dict = {}       
        for x in self.quotes_list:
            author_name = x.author
            author_name = author_name.strip()
            
            if author_name in author_count_dict:
                current_count = author_count_dict[author_name]
                author_count_dict[author_name] = current_count + 1
            else:
                author_count_dict[author_name] = 1
            
            
        return author_count_dict


    # ============= Method No: 7 (Girish)===============
    # Given a quotes collection, generate Crypto puzzle collection
    def generateCryptoQuoteList():
        pass


    # ============= Method No: 8 (Ishana Didwania) ===============
    # Purpose: This method returns a random crypto quote and hint.
    
    def showRandomCryptoInHTML(self):

        # generate a random quote
        print(self.len())
        quote_index = random.randint(1, self.len())
        print(quote_index)
        #random_quote = quotes_list.at(quote_index)
        random_quote_object = self.quotes_list[quote_index]
        print(random_quote_object)
        random_quote = random_quote_object.quote

        # print the random quote (testing purposes)
        print(random_quote)

        # generate a list of all the letters from the input quote
        random_quote = str(random_quote)
        quote_upper = random_quote.upper()
        quote_list = list(quote_upper)
        quote_list_temp = list(quote_list)
        #print(quote_list_temp)

        # generate an ordered alphabet list
        ordered_list = [] 
        ordered_list = list(string.ascii_uppercase) 
        #print(ordered_list)

        # generate a randomized alphabet list
        random_list = list(ordered_list);
        random.shuffle(random_list);
        #print(random_list)

        # generate the cryptoquote (do the swapping here)
        q_pos = -1

        for x in quote_list:
            q_pos = q_pos + 1
        
            if (x in ordered_list):
                x_pos = ordered_list.index(x)
                y_char = random_list[x_pos]
                quote_list_temp[q_pos] = y_char
            
        #print(quote_list_temp)

        # convert the temporary quote list into a string
        crypto = ""
        crypto = crypto.join(quote_list_temp)
        print(crypto)

        # generate a hint for the cryptoquote
        hint = quote_list_temp[0] + "=" + quote_list[0]

        print(hint)

        # upload the cryptoquote and the hint to the html page
        a_file = open("cryptoquote.html", "r")
        list_of_lines = a_file.readlines()
        list_of_lines[44] = "Cryptoquote: " + crypto + '\n'
        list_of_lines[48] = "Hint: " + hint + '\n'
        a_file.close()

        a_file = open("cryptoquote.html", "w")
        a_file.writelines(list_of_lines)
        a_file.close()
        

        return "Cryptoquote is created in randomcrypto.html"
    

    # ============= Method No: 9 (Jaya Varanasi) ===============
    # Purpose: This method displays a random quote as HTML
    def showRandomQuoteInHTML(self):
        length_of_list = len(self.quotes_list)
        quote_index = random.randint(1, length_of_list)
        print(quote_index)
        random_quote_object = self.quotes_list[quote_index]
        print(random_quote_object)
        random_quote = random_quote_object.quote
        random_quote = random_quote.upper()
        print(random_quote)
        
        #Check if the file exists
        import os
        fileName = os.getcwd() + "/" + "RandomQuote.html"
        if os.path.isfile(fileName):
           file1 = open(fileName,'r')
           list_of_lines = file1.readlines()
           file1.close()
           
           for itr in range(0,len(list_of_lines)):
              line = list_of_lines[itr]
              if( '<div class="quote_box">' in line):
                  print("I am here")
                  list_of_lines[itr] = '<div class="quote_box"> Random Quote :' + random_quote + '</div>'
                  break
           file1 = open(fileName,'w')
           file1.writelines(list_of_lines)
           file1.close()
        else:
            print("Error: RandomQuote.html does not exist. Contact Hiranmayi for the starter file.")
            

        
    # ============= Method No: 10 (Girish Kumar Sure) ===============
    # Purpose: This method returns the list of "Submitted_By" (name of the students) in sorted order
    def sortBySubmittedBy(self):
        submittedby_list = []
        for quote_row in self.quotes_list:
            submittedby = quote_row.submitted_by
            submittedby_list.append(submittedby)

        #print(submittedby_list)
        submittedby_list.sort()
        
        return submittedby_list
    
    # ============= Method No: 11 (Karthik Uppala) ===============
    # Purpose: This method returns the list of "author"
    # (name of the authors) in sorted order
    def getSortedAuthors(self):
        # you have to operate on this variable self.quotes_list

        authors_list = [ ]

        for x in self.quotes_list:
            author_name = x.author
            #author_name = author_name.strip()
            authors_list.append(author_name)

        authors_list.sort()         

        return authors_list

    

    

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

    # ============= Method No: 14 (Shekar Motukuri) ===============
    # Purpose: This method returns count of Quotes submitted by students(him/her)
    
    def getCountOfQuotesByStudent(self, student_name):
        student_count = 0
        student_string=""
        student_name=""
        print('testing')
             
        for x in self.quotes_list:
            current_student = x.submitted_by
            student_string+=current_student+" ";
        #print('testing'+student_string)
        for x in self.quotes_list:
            current_student = x.submitted_by
            student_count1=student_string.count(current_student)
            if(student_count1>=student_count):
              student_count=student_count1
              student_name=current_student    
        print('testing'+student_name)
        print(student_count)  
        return student_name


    # ============= Method No: 15 (Pranav Manikonda) ===============
    # Purpose: This method returns a random quote from the collection of quotes
    def getRandomQuote(self):
        random_quote_object = random.choice(self.quotes_list)
        random_quote_str = random_quote_object.quote
        return random_quote_str



    # ============= Method No: 16 (Pranav Mukkara) ===============
    # Purpose: This method returns the count of quotes submitted by the author
    def getCountOfQuotesByAuthor(self, author_name):
        quote_count = 0
        for x in self.quotes_list:
            p = x.author.strip()
            q = author_name.strip()
            if p==q:
                quote_count = quote_count + 1
        return quote_count


    # ============= Method No: 17 (Pravallika Sunkara) ===============
    # Purpose: This method returns the author who authored the least amount of quotes
    def getAuthorWithLessQuotes(self):
        ## Calling method 4
        author_count_dictionary = self.getAuthorAndQuoteCount()
        ## Find the min key from the dictionary    
        min_key = min(author_count_dictionary, key=author_count_dictionary.get)
        ## Return the min key
        return min_key

            
    # ============= Method No: 18 (Nikhitha Gollamudi) ===============
    # Purpose: This method deletes a quote given the id
    #          This method also updates the source file after the deletion
    def deleteQuote(self, ID):
        for x in self.quotes_list:
            if (x.id == ID):
                self.quotes_list.remove(x)
                return "Quote is deleted"
  
        return "Quote not found"
        



    # ============= Method No: 19 (Sahasra Tummala) ===============
    # Purpose: This method returns shortest quote in the quotes collection
    def getShortestQuote(self):
        shortest_quote = "abcdedfghijklmnopqrstuvwxyz"
        shortest_quote = shortest_quote * 100
        for x in self.quotes_list:
            current_quote = x.quote
            if len(current_quote) < len(shortest_quote):
                shortest_quote = current_quote  
        return shortest_quote


    # ============= Method No: 20 (Sai Akaksha Josylua) ===============
    # Purpose: This method returns the count of Authors in the quotes collection
    def getAuthorCount(self):
        authors = set()
        
        for x in self.quotes_list:
            current_author = x.author
            authors.add(current_author)

        count_of_authors = len(authors)
        return count_of_authors


    # ============= Method No: 21 (Shekar Motukuri) ===============
    # Purpose: This method returns longest quote in the quotes collection 
    def getLongestQuote(self):
        longest_quote = ""
             
        for x in self.quotes_list:
            current_quote = x.quote
            if len(current_quote) > len(longest_quote):
                longest_quote = current_quote         
                
        return longest_quote

    # ========= Sravamti Manikonda: Method # 22 ========================
    # Purpose: This method returns the single author who authored the most quotes
    def getAuthorWithMostQuotes(self):
        ## Call eshan's method to get author - count dictionary
        author_count_dictionary = self.getAuthorAndQuoteCount()
        ## Find the max key from the dictionary    
        max_key = max(author_count_dictionary, key=author_count_dictionary.get)
        ## Return the max key
        return max_key

    


    # ============= Method No: 23 (Sreya Andalkovil) ===============
     #purpose: this method returns dictionary with submitted by as key and count as value
    def getSubmittedByAndQuoteCount (self) :
        submittedby_count_dictionary = {}
        for x in self.quotes_list:
            student_name = x.submitted_by
            student_name = student_name.strip()
    
            if student_name in submittedby_count_dictionary:
                count = submittedby_count_dictionary[student_name]
                submittedby_count_dictionary[student_name] = count + 1
        
            else:
                submittedby_count_dictionary[student_name] = 1
        
        return submittedby_count_dictionary


    # ============= Method No: 24 (Sumedh Ghatti) ===============
    # Purpose: This method returns the quotes containing the word given
    def getQuotesContainingWord(self, given_word):
        # converting to small case and stripping the spaces
        given_word = given_word.lower()
        given_word = given_word.strip()

        # this is the mini collection we want to return
        quotes_list_containing_the_given_word = []
        for x in self.quotes_list:
            current_quote_str = x.quote
            if given_word in current_quote_str:
                quotes_list_containing_the_given_word.append(x)
                    
        # create a mini quotes collection 
        quotes_mini_collection = QuotesList(quotes_list_containing_the_given_word)
        return quotes_mini_collection;

    # ============= Method No: 25 (Udbhav Narani) ===============
     #purpose: this method adds a new quote to the collection
     #         and returns the new Quote object created
    def addQuote(self,quote, author,submitted_by):

         # find the maximum ID in the quotes list and increment the ID by 1
        if len(self.quotes_list) ==0:
            id = 1
        else:
            last_quote = self.quotes_list[-1]
            id = int(last_quote.id) + 1
        
        # create a new quote
        new_quote = Quote(id,quote,author,submitted_by)

        #add this quote to the collection
        self.quotes_list.append(new_quote)

        return new_quote;
        

    
    # ============= Method No: 26 (Vikranth Datta) ===============
    # Purpose: This method returns a list of students with no quotes
    # Algorithm:
    # 1. Get the set of students from the file (x)
    # 2. Get the set of students from the quotes_list (y)
    # 3. Find the difference (x) and (y) to find out the students who did not submit the quotes.
    # 4. Convert this difference set into list and return the list.
    def getStudentListWithNoQuotes(self):
        file=open("students_list.txt")
        lists=file.readlines()

        #create an empty set. we can not use { } because it will be treated as empty dictionary
        all_students_set = set()
        
        for i in range(len(lists)):
            student_name = lists[i].rstrip('\n')
            all_students_set.add(student_name)
        #print(all_students_set)

        students_with_quotes_set = set()
        for x in self.quotes_list:
             students_with_quotes_set.add(x.submitted_by)

        # find the intersection
        students_with_no_quotes_set = all_students_set.difference(students_with_quotes_set)

        # since the method contract says that we should return a list,
        # convert the set to a list and return it
        students_with_no_quotes_list = list(students_with_no_quotes_set)
        
        return students_with_no_quotes_list;


    # ========= Girish Kumar Sure: Method # 27 ========================
    # Purpose: This method returns the single author who authored the most quotes
    def getStudentWithLeastQuotes(self):
        ## Call getSubmittedByAndQuoteCount() method to get submitted_by - count dictionary
        submittedby_count_dict = self.getSubmittedByAndQuoteCount()
        ## Find the max key from the dictionary    
        max_key = max(submittedby_count_dict, key=submittedby_count_dict.get)
        ## Return the max key
        return max_key

    # ============= Method No: 28 (Vishnu Vundamati) ===============
    # Purpose: The method allows you to update a quote in the collection/file
    def updateQuote(self, id, quote, author, submitted_by):

        #default
        updated_status = "The id you entered does not exist in the collection"

        #sorting through each quote to find the quote with the id the user entered
        for x in self.quotes_list:
            current_id = x.id
            current_quote = x.quote
            current_author = x.author
            current_submitted_by = x.submitted_by

            #updates the quote with user input values
            if (current_id == id):
                x.quote = quote
                x.author = author
                x.submitted_by = submitted_by
                #proof of update
                updated_status = "The quote has successfully been updated"

                #exiting loop
                break
        return updated_status

    # ============= Method No: 29 (Nikhita Gollamudi) ===============
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
        for x in self.quotes_list:
            file.write(x.id + "," + x.quote+ "," + x.author + "," + x.submitted_by)
        file.close()

    
        

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

# ============= Method No: 12 (Keertan Chennupati) ===============
# Purpose: Integrate all the functions by providing the user with a menu of actions to choose from
def presentInterface():
    quotes_list_object = QuotesList.createWithFileName("quotes_in_excel.csv") 

    print("Actions:\n 0: Quit program\n 1: getStudentCount\n 2: getStudentWithMostQuotes\n 3: getQuotesByAuthor\n 4: getQuotesByStudent\n 5: getAuthorAndQuoteCount\n 6: generateCryptoQuoteList")
    print(" 7: showRandomCryptoInHTML\n 8: showRandomQuoteInHTML\n 9: sortBySubmittedBy\n 10: getSortedAuthors\n 11: presentInterface\n 12: getWordListByFrequency\n 13: getCountOfQuotesByStudent")
    print(" 14: getRandomQuote\n 15: getQuotesCountByAuthor\n 16: getAuthorWithLessQuotes\n 17: deleteQuote\n 18: getShortestQuote\n 19: getAuthorCount\n 20: getLongestQuote\n 21: getAuthorWithMostQuotes")
    print(" 22: getQuotesContainingWord\n 23: addQuote\n 24: getStudentListWithNoQuotes\n 25: getStudentWithLeastQuotes\n 26: updateQuote\n 27: getQuotesContainingBadWords\n 28: saveToFile\n 29: getQuotesContainingGoodWords")

    response = input("Select the method you would like to run\n")

    if response == 0:
        exit()
    if response == 1:
        pass
    if response == 2:
        #output = getStudentCount()
        print("=== Method #2 (Nikhitha Gollamudi) getStudentCount( ) method ====")
        student_count = quotes_list_object.getStudentCount()
        print(student_count)
    if response == 3: 
        #output = getStudentWithMostQuotes()
        print("=== Method #2 (Nikhitha Gollamudi) getStudentCount( ) method ====")
        student_with_most_quotes = quotes_list_object.getStudentWithMostQuotes()
        print(student_with_most_quotes)
    if response == 4:
        #output = getQuotesByAuthor()
        print("=== Method #4 (Anjneya Kumar) def getQuotesByAuthor( ) method ====")
        mini_quote_collection = quotes_list_object.getQuotesByAuthor()
        #mini_quote_collection.printQuotes()
    if response == 5:
        #output = getQuotesByStudent()
        pass
    if response == 6: 
        #output = getAuthorAndQuoteCount()
        print("=== Method #6 (Eshaan Dhavala) def getAuthorAndQuoteCount( ) method ====")
        author_count_dictionary = quotes_list_object.getAuthorAndQuoteCount()
        pp.pprint(author_count_dictionary)
    if response == 7:
        #output = showRandomCryptoInHTML()
        pass
    if response == 8:
        pass
    if response == 9:
        #output = showRandomQuoteInHTML()
        print("=== Method #9 (Jaya Varanasi) def showRandomQuoteInHTML( )method ====")
        quotes_list_object.showRandomQuoteInHTML( )
    if response == 10:
        #output = sortBySubmittedBy()
        print("=== Method #10 (Girish Kumar Sure) def sortBySubmittedBy( ) method ====")
        sorted_submittedby_list = quotes_list_object.sortBySubmittedBy()
        print(sorted_submittedby_list)
    if response == 11:
        #output = getSortedAuthors()
        print("=== Method #11.1 (Karthik Uppala) def getSortedAuthors( )method ====")
        sorted_authors_list_x = quotes_list_object.getSortedAuthors( )
        #print(sorted_authors_list_x)

        print("=== Method #11.2 (Karthik Uppala) def getSortedAuthors( )method ====")
        q1 = Quote(1, "Hello", "A1", "S1")
        q2 = Quote(2, "How are you?", "X", "S1")
        q3 = Quote(3, "OK", "A1", "S1")
        q4 = Quote(4, "Great", "B3", "S1")
        q5 = Quote(5, "Good to know", "A1", "S1")
        q6 = Quote(6, "TTYL", "A1", "S1")
        q7 = Quote(7, "Bye now", "Y", "S1")
        q8 = Quote(8, "See ya!", "A1", "S1")
        q9 = Quote(9, "Bye Bye!", "P2", "S2")
        quotes_list = [q1,q2,q3,q4,q5,q6,q7,q8, q9]
        uppala_QuotesList_object = QuotesList(quotes_list)
        sorted_authors_list_x = uppala_QuotesList_object.getSortedAuthors()
        print(sorted_authors_list_x)
    if response == 12:
        pass
    if response == 13:
        #output = getWordListByFrequency()
        print("=== Method #13 (Nikhita Gollamudi) getWordListByFrequency( ) method ====")
        word_frequency = quotes_list_object.getWordListByFrequency()
        print(word_frequency)

        print("=== Method #13.2 (Nikhita Gollamudi) getWordListByFrequency( ) method ====")
        q1 = Quote(1, "Hello", "A1", "S1")
        q2 = Quote(2, "How are you?", "A1", "S1")
        q3 = Quote(3, "OK", "A1", "S1")
        q4 = Quote(4, "Great", "A1", "S1")
        q5 = Quote(5, "Good to know", "A1", "S1")
        q6 = Quote(6, "TTYL", "A1", "S1")
        q7 = Quote(7, "Bye now", "A1", "S1")
        q8 = Quote(8, "See ya!", "A1", "S1")
        q9 = Quote(9, "Bye Bye!", "A2", "S2")
        quotes_list = [q1,q2,q3,q4,q5,q6,q7,q8, q9]
        nikhita_QuotesList_object = QuotesList(quotes_list)
        word_frequency = nikhita_QuotesList_object.getWordListByFrequency()
        pp.pprint(word_frequency)
    if response == 14:
        #output = getCountOfQuotesByStudent()
        print("=== Method #14.1 (Soma Modukuri) getCountOfQuotesByStudent(student_name)method ====")
        student_name = "Jasthi"
        quote_count = quotes_list_object.getCountOfQuotesByStudent(student_name)
        print(quote_count)

        print("=== Method #14.2 (Soma Modukuri) getCountOfQuotesByStudent(student_name)method ====")
        q1 = Quote(1, "Hello", "A1", "S1")
        q2 = Quote(2, "How are you?", "A1", "S1")
        q3 = Quote(3, "OK", "A2", "S2")
        q4 = Quote(4, "Great", "A3", "S2")
        q5 = Quote(5, "OK", "A2", "S3")
        q6 = Quote(6, "OK", "A2", "S4")
        quotes_list = [q1,q2,q3,q4,q5, q6]
        soma_QuotesList_object = QuotesList(quotes_list)
        quote_count = quotes_list_object.getCountOfQuotesByStudent("S1")
        print("Count of quotes submitted by S1 : " + quote_count)
    if response == 15:
        #output = getRandomQuote()
        print("=== Method #15.1 (Pranav Manikonda) getRandomQuote method ====")
        random_quote_1 = quotes_list_object.getRandomQuote()
        print(random_quote_1)

        print("=== Method #15.2  (Pranav Manikonda) getRandomQuote method ====")
        q1 = Quote(1, "Hello", "A1", "S1")
        q2 = Quote(2, "How are you?", "A1", "S1")
        q3 = Quote(3, "OK", "A1", "S1")
        q4 = Quote(4, "Great", "A1", "S1")
        q5 = Quote(5, "Good to know", "A1", "S1")
        q6 = Quote(6, "TTYL", "A1", "S1")
        q7 = Quote(7, "Bye now", "A1", "S1")
        q8 = Quote(8, "See ya!", "A1", "S1")
        quotes_list = [q1,q2,q3,q4,q5,q6,q7,q8]
        pranav_QuotesList_object = QuotesList(quotes_list)
        random_quote_2 = pranav_QuotesList_object.getRandomQuote()
        print(random_quote_2)
    if response == 16:
        #output = getQuotesCountByAuthor()
        print("=== Method #16.1 (Pranav mukkara) getCountOfQuotesByAuthor(author_count)method ====")
        author_name = "unknown"
        quote_count = quotes_list_object.getCountOfQuotesByAuthor(author_name)
        print(quote_count)

        print("=== Method #16.2 (Pranav mukkara) getCountOfQuotesByAuthor(author_count)method ====")
        q1 = Quote(1, "Hello", "A1", "S1")
        q2 = Quote(2, "How are you?", "A1", "S1")
        q3 = Quote(3, "OK", "A2", "S1")
        q4 = Quote(4, "Great", "A2", "S1")
        q5 = Quote(5, "Good to know", "A3", "S1")
        q6 = Quote(6, "TTYL", "A3", "S1")
        q7 = Quote(7, "Bye now", "A1", "S1")
        q8 = Quote(8, "See ya!", "A1", "S1")
        quotes_list = [q1,q2,q3,q4,q5,q6,q7,q8]
        mukkara_QuotesList_object = QuotesList(quotes_list)
        quote_count = quotes_list_object.getCountOfQuotesByAuthor("A1")
        print(quote_count)
    if response == 17:
        #output = getAuthorWithLessQuotes()
        print("=== Method #17 (Pravallika Sunkara); getAuthorWithLessQuotes() method ====")
        author_with_less_quotes = quotes_list_object.getAuthorWithLessQuotes()    
        print(author_with_less_quotes)
    if response == 18:
        #output = deleteQuote()
        print("=== Method #18.2 (Nikhitha Gollamudi)  deleteQuote( ) method ====")
        q1 = Quote(1, "Hello", "A1", "S1")
        q2 = Quote(2, "How are you?", "A1", "S1")
        q3 = Quote(3, "OK", "A1", "S1")
        q4 = Quote(4, "Great", "A1", "S1")
        quotes_list = [q1,q2,q3,q4]
        nikhitha_QuotesList_object = QuotesList(quotes_list)
        nikhitha_QuotesList_object.printQuotes()
        quote_deleted = nikhitha_QuotesList_object.deleteQuote(1)
        print(quote_deleted)
        nikhitha_QuotesList_object.printQuotes()
    if response == 19:
        #output = getShortestQuote()
        print("=== Method #19.1  (Sahasra Tummala) getShortestQuote( ) method ====")
        shortest_quotation = quotes_list_object.getShortestQuote( )
        print(shortest_quotation)

        print("=== Method #19.2  (Sahasra Tummala) getShortestQuote( ) method ====")
        q1 = Quote(1, "Hello", "A1", "S1")
        q2 = Quote(2, "How are you?", "A1", "S1")
        q3 = Quote(3, "OK", "A1", "S1")
        q4 = Quote(4, "Great", "A1", "S1")
        quotes_list = [q1,q2,q3,q4]
        my_own_QuotesList_object = QuotesList(quotes_list)
        #my_own_QuotesList_object.printQuotes()
        shortest_quotation = my_own_QuotesList_object.getShortestQuote( )
        print(shortest_quotation)
    if response == 20:
        #output = getAuthorCount()
        print("=== Method #20  (Happy Josyula) getAuthorCount( ) method ====")
        author_count = quotes_list_object.getAuthorCount( )
        print(author_count)
    if response == 21:
        #output = getLongestQuote()
        print("=== Method #21.1  (Soma Modukuri) getLongestQuote( ) method ====")
        longest_quote = quotes_list_object.getLongestQuote( )
        print(longest_quote)

        print("=== Method #21.2  (Soma Modukuri) getLongestQuote( ) method ====")
        q1 = Quote(1, "Hello", "A1", "S1")
        q2 = Quote(2, "How are you?", "A1", "S1")
        q3 = Quote(3, "OK", "A1", "S1")
        q4 = Quote(4, "Great", "A1", "S1")
        quotes_list = [q1,q2,q3,q4]
        my_own_QuotesList_object = QuotesList(quotes_list)
        longest_quotation = my_own_QuotesList_object.getLongestQuote( )
        print(longest_quotation)
    if response == 22:
        #output = getAuthorWithMostQuotes()
        print("=== Method #22.1 (Sravamti Manikonda) getAuthorWithMostQuotes( ) method ====")
        author_with_most_quotes = quotes_list_object.getAuthorWithMostQuotes()    
        print(author_with_most_quotes)

        print("=== Method #22.2  (Sravamti Manikonda) getAuthorWithMostQuotes( ) method ====")
        q1 = Quote(1, "Hello", "A1", "S1")
        q2 = Quote(2, "How are you?", "A1", "S1")
        q3 = Quote(3, "OK", "A2", "S1")
        q4 = Quote(4, "Great", "A3", "S1")
        q5 = Quote(5, "OK", "A2", "S1")
        q6 = Quote(6, "OK", "A2", "S1")
        quotes_list = [q1,q2,q3,q4,q5, q6]
        sravanti_QuotesList_object = QuotesList(quotes_list)
        author_with_most_quotes = sravanti_QuotesList_object.getAuthorWithMostQuotes( )
        print(author_with_most_quotes)
    if response == 23: 
        #output = getSubmittedByAndQuoteCount()
        print("=== Method #23.1 (Sreya Andalkovil) def getSubmittedByAndQuoteCount ( ) method ====")
        submittedby_count_dictionary = quotes_list_object.getSubmittedByAndQuoteCount()
        pp.pprint(submittedby_count_dictionary)

        print("=== Method #23.2  (Sreya Andalkovil) def getSubmittedByAndQuoteCount ( ) method ====")
        q1 = Quote(1, "Hello", "A1", "S1")
        q2 = Quote(2, "How are you?", "A1", "S1")
        q3 = Quote(3, "OK", "A2", "S2")
        q4 = Quote(4, "Great", "A3", "S2")
        q5 = Quote(5, "OK", "A2", "S3")
        q6 = Quote(6, "OK", "A2", "S4")
        quotes_list = [q1,q2,q3,q4,q5, q6]
        shreya_QuotesList_object = QuotesList(quotes_list)
        submittedby_count_dictionary = shreya_QuotesList_object.getSubmittedByAndQuoteCount()
        pp.pprint(submittedby_count_dictionary)
    if response == 24:
        #output = getQuotesContainingWord()
        print("=== Sumedh Ghatti: Method #24; def getQuotesContainingWord(input_word) method ====")
        print("Searching for the quotes containing LOVE")
        word_to_find = "Love"
        quotes_mini_collection = quotes_list_object.getQuotesContainingWord(word_to_find)
        uotes_mini_collection.printQuotes()

        print("Searching for the quotes containing ONE")
        word_to_find = "One"
        quotes_mini_collection = quotes_list_object.getQuotesContainingWord(word_to_find)
        quotes_mini_collection.printQuotes()
    if response == 25:
        #output = addQuote()
        print("=== Udbhav Narani: Method #25; def addQuote(quote, author,submitted_by) method ====")
        quote_to_be_added = quotes_list_object.addQuote("All is well", "Author 1", "Student 1");
        print(quote_to_be_added)
        quote_to_be_added = quotes_list_object.addQuote("All is well That ends well!", "Author 1", "Student 1");
        print(quote_to_be_added)
        quote_to_be_added = quotes_list_object.addQuote("All is well That ends well!", "Author 1", "Student 1");
        print(quote_to_be_added)
    if response == 26:
        #output = getStudentListWithNoQuotes()
        print("===  Method #26 (Vikrant Datta) def getStudentListWithNoQuotes()  method ====")
        students_list_with_no_quotes = quotes_list_object.getStudentListWithNoQuotes()
        print(students_list_with_no_quotes)
    if response == 27:
        #output = getStudentWithLeastQuotes()
        print("=== Method #27 (Girish Kumar Sure) getStudentWithLeastQuotes( ) method ====")
        student_with_least_quotes = quotes_list_object.getStudentWithLeastQuotes()    
        print(student_with_least_quotes)
    if response == 28:
        #output = updateQuote()
        print("===  Method #28 (Vishnu Vundamati) def updateQuote(self, id, quote, author, submitted_by)  method ====")
        update_status = quotes_list_object.updateQuote(2, "test_quote", "test_author", "test_submitted_by")
        print(update_status)
    if response == 29:
        #output = getQuotesContainingBadWords()
        print("===  Method #29 (Nikhitha Gollamudi) def getQuotesContainingBadWords()  method ====")
        mini_collection_29 = quotes_list_object.getQuotesContainingBadWords()
        #mini_collection_29.printQuotes()
    if response == 30:
        #output = saveToFile()
        print("=== Nikhita Gollamudi: Method #30; saveToFile( ) method ====")
        #quotes_list_object.saveToFile()
        
    
    

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
quotes_list_object.printQuotes()

# Step 4: Now let us exercise some methods in the QuotesList

loop = 1
while loop == 1:
    out = presentInterface()
    print(out)


# ========= Nikhitha Gollamudi: Method # 2 ========================
print("=== Method #2 (Nikhitha Gollamudi) getStudentCount( ) method ====")
student_count = quotes_list_object.getStudentCount()
print(student_count)

# ========= Nikhitha Gollamudi: Method # 3 ========================
print("=== Method #2 (Nikhitha Gollamudi) getStudentCount( ) method ====")
student_with_most_quotes = quotes_list_object.getStudentWithMostQuotes()
print(student_with_most_quotes)

# ========= Anjneya Kumar: Method # 4 ========================
print("=== Method #4 (Anjneya Kumar) def getQuotesByAuthor( ) method ====")
mini_quote_collection = quotes_list_object.getQuotesByAuthor()
#mini_quote_collection.printQuotes()

     

# ========= Eshaan Dhavala: Method # 6 ========================
print("=== Method #6 (Eshaan Dhavala) def getAuthorAndQuoteCount( ) method ====")
author_count_dictionary = quotes_list_object.getAuthorAndQuoteCount()
pp.pprint(author_count_dictionary)



# ========= Jaya Varanasi: Method # 9 ========================
print("=== Method #9 (Jaya Varanasi) def showRandomQuoteInHTML( )method ====")
quotes_list_object.showRandomQuoteInHTML( )

#Opening a html file directly from a web browser 
#new = 2
#url = "RandomQuote.html"
#webbrowser.open(url,new=new)


# ========= Girish Kumar Sure: Method # 10 ========================
print("=== Method #10 (Girish Kumar Sure) def sortBySubmittedBy( ) method ====")
sorted_submittedby_list = quotes_list_object.sortBySubmittedBy()
print(sorted_submittedby_list)


# ========= Karthik Uppala: Method # 11 ========================
print("=== Method #11.1 (Karthik Uppala) def getSortedAuthors( )method ====")
sorted_authors_list_x = quotes_list_object.getSortedAuthors( )
#print(sorted_authors_list_x)


print("=== Method #11.2 (Karthik Uppala) def getSortedAuthors( )method ====")
q1 = Quote(1, "Hello", "A1", "S1")
q2 = Quote(2, "How are you?", "X", "S1")
q3 = Quote(3, "OK", "A1", "S1")
q4 = Quote(4, "Great", "B3", "S1")
q5 = Quote(5, "Good to know", "A1", "S1")
q6 = Quote(6, "TTYL", "A1", "S1")
q7 = Quote(7, "Bye now", "Y", "S1")
q8 = Quote(8, "See ya!", "A1", "S1")
q9 = Quote(9, "Bye Bye!", "P2", "S2")
quotes_list = [q1,q2,q3,q4,q5,q6,q7,q8, q9]
uppala_QuotesList_object = QuotesList(quotes_list)
sorted_authors_list_x = uppala_QuotesList_object.getSortedAuthors()
print(sorted_authors_list_x)

# ========= Nikhita Gollamudi: Method # 13 ========================
print("=== Method #13.2 (Nikhita Gollamudi) getWordListByFrequency( ) method ====")
word_frequency = quotes_list_object.getWordListByFrequency()
pp.pprint(word_frequency)


print("=== Method #13.2 (Nikhita Gollamudi) getWordListByFrequency( ) method ====")
q1 = Quote(1, "Hello", "A1", "S1")
q2 = Quote(2, "How are you?", "A1", "S1")
q3 = Quote(3, "OK", "A1", "S1")
q4 = Quote(4, "Great", "A1", "S1")
q5 = Quote(5, "Good to know", "A1", "S1")
q6 = Quote(6, "TTYL", "A1", "S1")
q7 = Quote(7, "Bye now", "A1", "S1")
q8 = Quote(8, "See ya!", "A1", "S1")
q9 = Quote(9, "Bye Bye!", "A2", "S2")
quotes_list = [q1,q2,q3,q4,q5,q6,q7,q8, q9]
nikhita_QuotesList_object = QuotesList(quotes_list)
word_frequency = nikhita_QuotesList_object.getWordListByFrequency()
pp.pprint(word_frequency)

# ========= Soma Modukuri: Method # 14 ========================
print("=== Method #14.1 (Soma Modukuri) getCountOfQuotesByStudent(student_name)method ====")
student_name = "Jasthi"
quote_count = quotes_list_object.getCountOfQuotesByStudent(student_name)
print(quote_count)
 


print("=== Method #14.2 (Soma Modukuri) getCountOfQuotesByStudent(student_name)method ====")
q1 = Quote(1, "Hello", "A1", "S1")
q2 = Quote(2, "How are you?", "A1", "S1")
q3 = Quote(3, "OK", "A2", "S2")
q4 = Quote(4, "Great", "A3", "S2")
q5 = Quote(5, "OK", "A2", "S3")
q6 = Quote(6, "OK", "A2", "S4")
quotes_list = [q1,q2,q3,q4,q5, q6]
soma_QuotesList_object = QuotesList(quotes_list)
quote_count = quotes_list_object.getCountOfQuotesByStudent("S1")
print("Count of quotes submitted by S1 : " + quote_count)


# =================pranav manikonda #15======================
print("=== Method #15.1 (Pranav Manikonda) getRandomQuote method ====")
random_quote_1 = quotes_list_object.getRandomQuote()
print(random_quote_1)


print("=== Method #15.2  (Pranav Manikonda) getRandomQuote method ====")
q1 = Quote(1, "Hello", "A1", "S1")
q2 = Quote(2, "How are you?", "A1", "S1")
q3 = Quote(3, "OK", "A1", "S1")
q4 = Quote(4, "Great", "A1", "S1")
q5 = Quote(5, "Good to know", "A1", "S1")
q6 = Quote(6, "TTYL", "A1", "S1")
q7 = Quote(7, "Bye now", "A1", "S1")
q8 = Quote(8, "See ya!", "A1", "S1")
quotes_list = [q1,q2,q3,q4,q5,q6,q7,q8]
pranav_QuotesList_object = QuotesList(quotes_list)
random_quote_2 = pranav_QuotesList_object.getRandomQuote()
print(random_quote_2)

# =================pranav mukkara #16======================
print("=== Method #16.1 (Pranav mukkara) getCountOfQuotesByAuthor(author_count)method ====")
author_name = "unknown"
quote_count = quotes_list_object.getCountOfQuotesByAuthor(author_name)
print(quote_count)

print("=== Method #16.2 (Pranav mukkara) getCountOfQuotesByAuthor(author_count)method ====")
q1 = Quote(1, "Hello", "A1", "S1")
q2 = Quote(2, "How are you?", "A1", "S1")
q3 = Quote(3, "OK", "A2", "S1")
q4 = Quote(4, "Great", "A2", "S1")
q5 = Quote(5, "Good to know", "A3", "S1")
q6 = Quote(6, "TTYL", "A3", "S1")
q7 = Quote(7, "Bye now", "A1", "S1")
q8 = Quote(8, "See ya!", "A1", "S1")
quotes_list = [q1,q2,q3,q4,q5,q6,q7,q8]
mukkara_QuotesList_object = QuotesList(quotes_list)
quote_count = quotes_list_object.getCountOfQuotesByAuthor("A1")
print(quote_count)

# =================Pravallika Sunkara #17======================
print("=== Method #17 (Pravallika Sunkara); getAuthorWithLessQuotes() method ====")
author_with_less_quotes = quotes_list_object.getAuthorWithLessQuotes()    
print(author_with_less_quotes)


# ========== Nikhitha Gollamudi: Method #18 =================
print("=== Method #18.2 (Nikhitha Gollamudi)  deleteQuote( ) method ====")
q1 = Quote(1, "Hello", "A1", "S1")
q2 = Quote(2, "How are you?", "A1", "S1")
q3 = Quote(3, "OK", "A1", "S1")
q4 = Quote(4, "Great", "A1", "S1")
quotes_list = [q1,q2,q3,q4]
nikhitha_QuotesList_object = QuotesList(quotes_list)
nikhitha_QuotesList_object.printQuotes()
quote_deleted = nikhitha_QuotesList_object.deleteQuote(1)
print(quote_deleted)
nikhitha_QuotesList_object.printQuotes()



# ========== Sahasra Tummala: Method #19 =================
print("=== Method #19.1  (Sahasra Tummala) getShortestQuote( ) method ====")
shortest_quotation = quotes_list_object.getShortestQuote( )
print(shortest_quotation)

print("=== Method #19.2  (Sahasra Tummala) getShortestQuote( ) method ====")
q1 = Quote(1, "Hello", "A1", "S1")
q2 = Quote(2, "How are you?", "A1", "S1")
q3 = Quote(3, "OK", "A1", "S1")
q4 = Quote(4, "Great", "A1", "S1")
quotes_list = [q1,q2,q3,q4]
my_own_QuotesList_object = QuotesList(quotes_list)
#my_own_QuotesList_object.printQuotes()
shortest_quotation = my_own_QuotesList_object.getShortestQuote( )
print(shortest_quotation)

# ========== Happy Josyula: Method #20 =================
print("=== Method #20  (Happy Josyula) getAuthorCount( ) method ====")
author_count = quotes_list_object.getAuthorCount( )
print(author_count)



# ========== Soma MOdukuri: Method #21 =================
print("=== Method #21.1  (Soma Modukuri) getLongestQuote( ) method ====")
longest_quote = quotes_list_object.getLongestQuote( )
print(longest_quote)


print("=== Method #21.2  (Soma Modukuri) getLongestQuote( ) method ====")
q1 = Quote(1, "Hello", "A1", "S1")
q2 = Quote(2, "How are you?", "A1", "S1")
q3 = Quote(3, "OK", "A1", "S1")
q4 = Quote(4, "Great", "A1", "S1")
quotes_list = [q1,q2,q3,q4]
my_own_QuotesList_object = QuotesList(quotes_list)
longest_quotation = my_own_QuotesList_object.getLongestQuote( )
print(longest_quotation)


# ========== Sravamti Manikonda: Method #22 =================
print("=== Method #22.1 (Sravamti Manikonda) getAuthorWithMostQuotes( ) method ====")
author_with_most_quotes = quotes_list_object.getAuthorWithMostQuotes()    
print(author_with_most_quotes)

print("=== Method #22.2  (Sravamti Manikonda) getAuthorWithMostQuotes( ) method ====")
q1 = Quote(1, "Hello", "A1", "S1")
q2 = Quote(2, "How are you?", "A1", "S1")
q3 = Quote(3, "OK", "A2", "S1")
q4 = Quote(4, "Great", "A3", "S1")
q5 = Quote(5, "OK", "A2", "S1")
q6 = Quote(6, "OK", "A2", "S1")
quotes_list = [q1,q2,q3,q4,q5, q6]
sravanti_QuotesList_object = QuotesList(quotes_list)
author_with_most_quotes = sravanti_QuotesList_object.getAuthorWithMostQuotes( )
print(author_with_most_quotes)

# ========== Sreya Andalkovil: Method #23 =================
print("=== Method #23.1 (Sreya Andalkovil) def getSubmittedByAndQuoteCount ( ) method ====")
submittedby_count_dictionary = quotes_list_object.getSubmittedByAndQuoteCount()
pp.pprint(submittedby_count_dictionary)


print("=== Method #23.2  (Sreya Andalkovil) def getSubmittedByAndQuoteCount ( ) method ====")
q1 = Quote(1, "Hello", "A1", "S1")
q2 = Quote(2, "How are you?", "A1", "S1")
q3 = Quote(3, "OK", "A2", "S2")
q4 = Quote(4, "Great", "A3", "S2")
q5 = Quote(5, "OK", "A2", "S3")
q6 = Quote(6, "OK", "A2", "S4")
quotes_list = [q1,q2,q3,q4,q5, q6]
shreya_QuotesList_object = QuotesList(quotes_list)
submittedby_count_dictionary = shreya_QuotesList_object.getSubmittedByAndQuoteCount()
pp.pprint(submittedby_count_dictionary)

# ========= Sumedh Ghatti: Method # 24 ========================
print("=== Sumedh Ghatti: Method #24; def getQuotesContainingWord(input_word) method ====")
print("Searching for the quotes containing LOVE")
word_to_find = "Love"
quotes_mini_collection = quotes_list_object.getQuotesContainingWord(word_to_find)
quotes_mini_collection.printQuotes()

print("Searching for the quotes containing ONE")
word_to_find = "One"
quotes_mini_collection = quotes_list_object.getQuotesContainingWord(word_to_find)
quotes_mini_collection.printQuotes()


# ========= Udhban Narani: Method # 25 ========================
print("=== Udbhav Narani: Method #25; def addQuote(quote, author,submitted_by) method ====")
quote_to_be_added = quotes_list_object.addQuote("All is well", "Author 1", "Student 1");
print(quote_to_be_added)
quote_to_be_added = quotes_list_object.addQuote("All is well That ends well!", "Author 1", "Student 1");
print(quote_to_be_added)
quote_to_be_added = quotes_list_object.addQuote("All is well That ends well!", "Author 1", "Student 1");
print(quote_to_be_added)

# ========= Vishnu Vundamati: Method # 26 ========================
print("===  Method #26 (Vikrant Datta) def getStudentListWithNoQuotes()  method ====")
students_list_with_no_quotes = quotes_list_object.getStudentListWithNoQuotes()
print(students_list_with_no_quotes)


# ========== Girish Kumar Sure: Method #27 =================
print("=== Method #27 (Girish Kumar Sure) getStudentWithLeastQuotes( ) method ====")
student_with_least_quotes = quotes_list_object.getStudentWithLeastQuotes()    
print(student_with_least_quotes)


# ========= Vishnu Vundamati: Method # 28 ========================
print("===  Method #28 (Vishnu Vundamati) def updateQuote(self, id, quote, author, submitted_by)  method ====")
update_status = quotes_list_object.updateQuote(2, "test_quote", "test_author", "test_submitted_by")
print(update_status)

# ========= Nikhitha Gollamudi: Method # 29 ========================
print("===  Method #29 (Nikhitha Gollamudi) def getQuotesContainingBadWords()  method ====")
mini_collection_29 = quotes_list_object.getQuotesContainingBadWords()
#mini_collection_29.printQuotes()


# ========= Nikhita Gollamudi: Method # 30 ========================
print("=== Nikhita Gollamudi: Method #30; saveToFile( ) method ====")
#quotes_list_object.saveToFile()

    
