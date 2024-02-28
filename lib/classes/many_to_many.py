import ipdb

class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

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
            
    @property
    def author (self):
        return self._author
    
    @author.setter
    def author (self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise TypeError("Author must be an instance of Author")
        
    @property
    def magazine (self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            raise TypeError("Magazine must be an instance of Magazine")
            
    def __repr__(self):
       return f'<Article: author={self.author.name}, magazine={self.magazine.name}, title="{self.title}">'
        
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
        return [article for article in Article.all if self == article.author]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list({magazine.category for magazine in self.magazines()})
        

    def __repr__(self):
        return f'<Author: name = {self.name}>'

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
        return [article for article in Article.all if self == article.magazine]

    def contributors(self):
        return list({article for article in self.articles()})

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass

    def __repr__(self):
        return f'<Magazine: name = {self.name}, category = {self.category}>'