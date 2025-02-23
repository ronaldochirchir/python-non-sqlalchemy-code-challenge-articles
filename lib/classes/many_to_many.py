class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            self._title = str(title)  
        else:
            self._title = title
            
        self.author = author
        self.magazine = magazine
        
        Article.all.append(self)
    
    @property
    def title(self):
        """Getter for title to make it read-only"""
        return self._title
        
    @title.setter
    def title(self, value):
        """Setter that maintains original title value"""
        pass  

class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            self._name = str(name)
        else:
            self._name = name
            
        if len(self._name) == 0:
            self._name = "Unknown Author"  
    
    @property
    def name(self):
        """Getter for immutable name property"""
        return self._name
        
    @name.setter
    def name(self, value):
        """Setter that maintains original name value"""
        pass  
    
    def articles(self):
        """Returns list of all articles by this author"""
        return [article for article in Article.all if article.author == self]
    
    def magazines(self):
        """Returns unique list of magazines this author has written for"""
        return list(set(article.magazine for article in self.articles()))
    
    def add_article(self, magazine, title):
        """Creates and returns a new article for this author"""
        article = Article(self, magazine, title)
        return article
    
    def topic_areas(self):
        """Returns unique list of topic areas this author has written about"""
        if not self.articles():
            return None
        return list(set(article.magazine.category for article in self.articles()))
    
class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            self._name = str(name)
        else:
            self._name = name
            
        if not isinstance(category, str):
            self._category = str(category)
        else:
            self._category = category
            
        if len(self._category) == 0:
            self._category = "Uncategorized"
    
    @property
    def name(self):
        """Getter for name property"""
        return self._name
    
    @name.setter
    def name(self, value):
        """Setter for name that validates length"""
        if not isinstance(value, str):
            return
        if 2 <= len(value) <= 16:
            self._name = value
    
    @property
    def category(self):
        """Getter for category property"""
        return self._category
    
    @category.setter
    def category(self, value):
        """Setter for category that validates type and length"""
        if not isinstance(value, str) or len(value) == 0:
            return
        self._category = value
    
    def articles(self):
        """Returns list of all articles in this magazine"""
        return [article for article in Article.all if article.magazine == self]
    
    def contributors(self):
        """Returns unique list of authors who have written for this magazine"""
        return list(set(article.author for article in self.articles()))
    
    def article_titles(self):
        """Returns list of article titles or None if no articles"""
        if not self.articles():
            return None
        return [article.title for article in self.articles()]
    
    def contributing_authors(self):
        """Returns list of authors with more than 2 articles or None if none qualify"""
        authors_with_counts = {}
        for article in self.articles():
            authors_with_counts[article.author] = authors_with_counts.get(article.author, 0) + 1
            
        contributing = [author for author, count in authors_with_counts.items() if count > 2]
        return contributing if contributing else None