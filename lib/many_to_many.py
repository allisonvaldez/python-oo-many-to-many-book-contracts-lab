#!/usr/bin/env python3

# This file holds the classes for Author, Book, and Contract

# Book class for books in the system
class Book:

    # Store all the books
    all = []

    # Constructor for the books
    def __init__(self, title):
        self.title = title
        # Make sure to add the book to the class level for the list
        Book.all.append(self)

        # Create a function to return all the contract for the book
        def contracts(self):
            return [contract for contact in Contract.all if contract.book == self]
        
        # Create a function to return all authors for a book
        def authors(self):
            return [contact.author for contract in self.contracts()]


# Author class for the books 
class Author:

    # Store all authors at the class level 
    all = []

    # Contructor for authors
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    # Create a function to return all contracts for an author
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    # Create a function to return all books for an author
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    # Create a function to return new contracts for an author
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    # Create a function to return total royalties for author
    def total_royalties(self):
        return sum(contact.royalties for contract in self.contracts())
    

# Contract for the Author of the book
class Contract:
    # Store all contracts at the class level 
    all = []

    # Constructor
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    # Property getter for author
    @property
    def author(self):
        return self._author

    # Property setter for author (raise an exception if not an Author instance)
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            # raise Exception stops the program and signals invalid input
            raise Exception("author must be an instance of Author")
        self._author = value

    # Property getter for book
    @property
    def book(self):
        return self._book

    # Property setter for book (raise an exception if not a Book instance)
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be an instance of Book")
        self._book = value

    # Property getter for date
    @property
    def date(self):
        return self._date

    # Property setter for date (raise an exception if not a string)
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string")
        self._date = value

    # Property getter for royalties
    @property
    def royalties(self):
        return self._royalties

    # Property setter for royalties (raise exception if not an integer)
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("royalties must be an integer")
        self._royalties = value

    # Create a function to return all contracts that match a given date
    @classmethod
    def contracts_by_date(cls, date):
        # filters Contract.all keeping only contracts where date matches
        return [contract for contract in cls.all if contract.date == date]