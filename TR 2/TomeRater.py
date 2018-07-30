#USERS
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return "The email address has been updated for {}".format(self.name)

    def __repr__(self):
        return "User: {}, Email: {}, Digests: {}".format(self.name, self.email, len(self.books)) 

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        return sum(self.books.values()) / len(self.books.values())

    def __hash__(self):
        return hash((self.name, self.email))
        
        
#BOOKS
class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn

    def add_rating(self, rating):
        if 0 <= rating <= 4:
            self.ratings.append(rating)
        else:
            return "Invalid Rating"
        
    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.title:
            return True

    def __repr__(self):
        return "Book: {}, ISBN: {}".format(self.title, self.isbn)

    def get_average_rating(self):
        return sum(self.ratings) / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))


#FICTION BOOKS (BOOKS SUBCLASS)
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{} by {}".format(self.title, self.author)

#NON-FICTION BOOKS (BOOKS SUBCLASS)
class NonFiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{}, a {} manual on {}".format(self.title, self.level, self.subject)

#######################################################################################################

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}


    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return NonFiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            return "No user with {} exists".format(email)

    def add_user(self, name, email, books=None):
        user = User(name, email)
        self.users[email] = user
        for book in self.books:
            if book != None:
                self.add_book_to_user(book, email)

#ANALYSIS METHODS
    def print_catalog(self):
        for book in self.books.keys():
            print(book)
        
    def print_users(self):
        for user in self.users.values():
            print(user)
        
    def most_read_book(self):
        max_read = max(self.books.values())
        for key, value in self.books.items():
            if value == max_read:
              return key 

    def highest_rated_book(self):
        for title in self.books.keys():
            avg_rate = title.get_average_rating()
            self.books[title] = avg_rate   
        max_rating = max(self.books.values())
        for key, value in self.books.items():
            if value == max_rating:
                return key
       
            
    def most_positive_user(self):
        m_pos = {}
        for name in self.users.values():
            avg_rate = name.get_average_rating()
            m_pos[name] = avg_rate
        max_rating = max(m_pos.values()) 
        for key, value in m_pos.items():
            if value == max_rating:
                return key
            
          
          
        
        

