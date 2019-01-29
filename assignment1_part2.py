#! /usr/bin/env
# -*- coding: utf-8 -*-
"""Duke Phung assignment 1 part 2."""


class Book(object):
    """Object that stores book data.

    """

    def __init__(self, author, title):
        """Constructor for the Book class

        Args:
            author (str): name of the author
            title (str): title of the book

        """
        self.author = author
        self.title = title

    def display(self):
        """Displays the book author and title information

        Returns:
            mixed: the data of the parameters"""

        print(self.title, 'written by', self.author)

book1 = Book("John Steinbeck", "of Mice and Men")
book2 = Book("Harper Lee", "To Kill a Mockingbird")

book1.display()
book2.display()
