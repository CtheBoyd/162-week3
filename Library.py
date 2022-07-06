# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 7/5/2022
# Description: Library simulator, finds library items by item number, shows item location, items show on hold or out with patrons, shows and amends late fees.
#

class LibraryItem:
    """Items in the library"""
    def __init__(self, library_item_id, title):
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = 0

    """get methods for library item attributes."""
    def get_library_item_id (self):
        return self._library_item_id

    def get_title(self):
        return self._title

    def get_checked_out_by(self):
        return self._checked_out_by

    def get_requested_by(self):
        return self._requested_by

    def set_checked_out_by(self, pat_out):
        self._checked_out_by = pat_out

    def set_requested_by(self, pat_out):
        self._requested_by = pat_out

    def set_date_checked_out(self, current_date):
        self._date_checked_out = current_date

    def get_date_checked_out(self, current_date):
        self._date_checked_out = current_date



class Book(LibraryItem):
    """Child class of Library items of each attribute"""


    def __init__(self, library_item_id, title, author):
        super().__init__(library_item_id, title)
        self._author = author
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None

    """get and set methods for book attributes"""
    def set_author(self, author):
        self._author = author

    def get_check_out_length(self):
        return 21

    def get_author(self):
        return self._author

    def get_location(self):
        return self._location


class Album(LibraryItem):
    """Child class of Library items of each attribute"""

    def __init__(self, library_item_id, title, artist):
        super().__init__(library_item_id, title)
        self._artist = artist
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None

    """get and set methods for album attributes"""
    def set_artist(self, library_item_id, title, artist):
        super().__init__(library_item_id, title)
        self._artist = artist

    def get_check_out_length(self):
        return 14

    def get_artist(self):
        return self._artist

    def get_location(self):
        return self._location

class Movie(LibraryItem):
    """Child class of Library items of each attribute"""

    def __init__(self, library_item_id, title, director):
        super().__init__(library_item_id, title)
        self._director = director
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None

        """get and set methods for movie attributes"""
    def set_director(self, library_item_id, title, director):
        super().__init__(library_item_id, title)
        self._director = director

    def get_check_out_length(self):
        return 7

    def get_director(self):
        return self._director

    def get_location(self):
        return self._location

class Patron :
    """class for patron attributes"""

    def __init__(self, patron_id, name):
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0.10

    """get and set methods for patron class attributes"""
    def get_name(self):
        return self._name

    def get_patron_id(self):
        return self._patron_id

    def get_checked_out_items(self):
        return self._checked_out_items

    def get_fine_amount(self):
        return self._fine_amount

    def set_fine_amount(self, fine):
        self._fine_amount = fine

    def add_library_item(self, lib_item):
        """adds library item to patron"""
        self._checked_out_items.append(lib_item)

    def remove_library_item(self,lib_item):
        """removes library item from patron"""
        self._checked_out_items.remove(lib_item)

    def amend_fine(self, amount):
        """changes patron fine for late items"""
        self._fine_amount += amount

class Library:
    """class for the library simulator"""

    def __init__(self):
        self._holdings = []
        self._members = []
        self._current_date = 0

    def get_holdings(self):
        """a collection of the LibraryItems that belong to the Library"""
        return self._holdings

    def get_members(self):
        """a collection of the Patrons who are members of the Library"""
        return self._members

    def get_current_date(self):
        """stores the current date represented as an integer number of "days" since the Library object was created"""
        return self._current_date

    def lookup_library_item_from_id(self, library_item_id):
        """returns the LibraryItem object corresponding to the ID parameter, or None if no such LibraryItem is in the holdings"""
        for item in self._holdings:
            if item.get_library_item_id() == library_item_id:
                return item
            else:
                return None

    def lookup_patron_from_id(self, patron_id):
        """returns the Patron object corresponding to the ID parameter, or None if no such Patron is a member"""
        for patron in self._members:
            if patron.get_patron_id() == patron_id:
                return patron
            else:
                return None

    def add_library_item(self, add_item):
        """takes a LibraryItem object as a parameter and adds it to the holdings"""
        self._holdings.append(add_item)

    def add_patron(self, add_pat):
        """takes a Patron object as a parameter and adds it to the members"""
        self._holdings.append(add_pat)

    def check_out_library_item(self, patron_id, library_item_id):
        """takes as parameters a patron ID and a library item ID, in that order, update the Patron's checked_out_items"""
        for patron in self._members:
            if patron.get_patron_id() == patron_id:
                for item in self._holdings:
                    if item.get_library_item_id() == library_item_id:
                        if item.get_location() == "CHECKED_OUT":
                            return "item checked out"

                        elif item.get_location() == "ON_HOLD_SHELF":
                            return "item on hold "
                        else:
                            item.set_checked_out_by(patron)
                            item.set_date_checked_out(self._current_date)
                            item.set_location("CHECKED_OUT")
                            if item.get_requested_by() == patron:
                                item.set_requested_by(None)
                                patron.add_library_item(item)
                    return "check out successful"

            return "item not found"

        return "patron not found"

    def return_library_item(self, library_item_id):
        """takes as its parameter a library item ID, update the LibraryItem's checked_out_by"""
        for item in self._holdings:
            if item.get_library_item_id() == library_item_id:
                if item.get_location() == "CHECKED_OUT":
                    patron = item.get_checked_out_by()
                    patron.remove_library_item(item)
                if item.get_requested_by() != None:
                    item.set_location("ON_HOLD_SHELF")
                    item.set_location("ON_SHELF")
                    item.set_checked_out_by(None)
                return "return successful"
            return "item in library"
        return "item not found"

    def request_library_item(self, patron_id, library_item_id):
        """takes as parameters a patron ID and a library item ID, in that order, if the LibraryItem is on the shelf, update its location to on hold"""
        for patron in self._members:
            if patron.get_patron_id() == patron_id:
                for item in self._holdings:
                    if item.get_library_item_id() == library_item_id:
                        if item.get_requested_by() != None:
                            return "item on hold"
                        item.set_requested_by(patron)
                        if item.get_location() == "ON_SHELF":
                            item.set_location("ON_HOLD_SHELF")
                        return "request successful"
                return "item not found"
            else:
                return "patron not found"

    def pay_fine(self, library_item_id, amount):
        """takes as parameters a Patron ID and the amount (in dollars) being paid (in that order), use amend_fine to update the Patron's fine; return "payment successful"""
        for patron in self._members:
            if patron.get_patron_id() == library_item_id:
                patron.amend_fine(-amount)
                return "payment successful"
            else:
                return "patron not found"

    def increment_current_date(self):
        """increment current date, increase each Patron's fines by 10 cents for each overdue LibraryItem they have checked out (by calling amend_fine)"""
        self._current_date += 1
        for patron in self._members:
            for item in patron.get_checked_out_items():
                if (self._current_date - item.get_date_checked_out()) > item.get_check_out_length():
                    patron.amend_fine(0.10)











