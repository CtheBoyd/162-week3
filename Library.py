class LibraryItem:
    """class for items in the library"""
    def __init__(self, library_item_id, title, location, checked_out_by, requested_by, date_checked_out):
        self._library_item_id = library_item_id
        self._title = title
        self._location = location
        self._checked_out_by = checked_out_by
        self._requested_by = requested_by
        self._date_checked_out = date_checked_out

    """get methods for library items"""
    def get_library_item_id(self):
        return self._library_item_id

    def get_title(self):
        return self._title

    def get_location(self):
        return self._location

    def get_checked_out_by(self):
        return self._checked_out_by

    def get_requested_by(self):
        return self._requested_by

    def get_date_checked_out(self):
        return self._date_checked_out



class Book(LibraryItem):
    """item book"""
    def __init__(self):
        super().__init__(LibraryItem)
        pass

class Album(LibraryItem):
    """item album"""
    def __init__(self):
        super().__init__(LibraryItem)
        pass

class Movie(LibraryItem):
    """item movie"""
    def __init__(self):
        super().__init__(LibraryItem)
        pass



class Patron:
    """library customer"""

    def __init__(self):
        pass

    def add_patron(self, patron_obj):
        """adds patron"""
        pass


class Library:
    """individual library"""
    pass






b1 = Book("345", "Phantom Tollbooth", "Juster")
a1 = Album("456", "...And His Orchestra", "The Fastbacks")
m1 = Movie("567", "Laputa", "Miyazaki")
print(b1.get_author())
print(a1.get_artist())
print(m1.get_director())

p1 = Patron("abc", "Felicity")
p2 = Patron("bcd", "Waldo")

lib = Library()
lib.add_library_item(b1)
lib.add_library_item(a1)
lib.add_patron(p1)
lib.add_patron(p2)

lib.check_out_library_item("bcd", "456")
for _ in range(7):
    lib.increment_current_date()  # 7 days pass
lib.check_out_library_item("abc", "567")
loc = a1.get_location()
lib.request_library_item("abc", "456")
for _ in range(57):
    lib.increment_current_date()  # 57 days pass
p2_fine = p2.get_fine_amount()
lib.pay_fine("bcd", p2_fine)
lib.return_library_item("456")