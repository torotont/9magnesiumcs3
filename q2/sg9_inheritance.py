
# defining publication class 
class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)


# defining book class 
class Book(Publication):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.__pages = 1
        self.set_number_of_pages(pages)

    def get_number_of_pages(self):
        return self.__number_pages

    def set_number_of_pages(self, pages):
        if pages > 0:
            self.__number_pages = pages
        else:
            print("Number of pages must be positive.")

    def display_info(self):
        super().display_info()
        print("Number of pages:", self.__pages)


# defining magazine class
class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = 1
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("Issue number must be positive.")

    def display_info(self):
        super().display_info()
        print("Issue number:", self.__issue_number)


# creating two pub objects
pub1 = Publication("Journal of Experimental Psychology",
                   "Ratchiff, R. & Van Dongen, H.")
pub2 = Publication("Science Today", "John Smith")

# creating two book objects
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 350)

# creating two magazine objects
mag1 = Magazine("National Geographic", "Various Authors", 202)
mag2 = Magazine("Time Magazine", "Time Editors", 15)


# displaying of the information
print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()

print("\nMagazine Information:")
mag1.display_info()
