import ipdb

class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

    @property
    def title (self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if hasattr(self, "title"):
            raise AttributeError ("Title cannot be changed")
        else:
            if isinstance(new_title, str):
                if 5 <= len(new_title) <= 50:
                    self._title = new_title
                else:
                    raise ValueError("Title must be between 5 and 50 characters")
            else:
                raise TypeError("Title must be a string")
            

        
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name (self, new_name):
        if hasattr(self, "name"):
            raise AttributeError("Name cannot be changed")
        else:
            if isinstance(new_name, str):
                if len(new_name):
                    self._name = new_name
                else:
                    raise ValueError("Name must be longer than 0 characters")
            else:
                raise TypeError("Name must be a string")

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            # ipdb.set_trace()
            if 2 <= len(new_name) <= 16:
                self._name = new_name
            else: 
                raise ValueError("Name must be between 2 and 16 characters")
        else:
            raise TypeError("Name must be a string")   
        
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str):
            if len(new_category):
                self._category = new_category
            else:
                raise ValueError("Category must be longer than 0 characters")
        else:
            raise TypeError("Category must be a string")   

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass