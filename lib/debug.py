from classes.many_to_many import Author, Magazine, Article

# Create sample data
author1 = Author("Alice")
author2 = Author("Bob")

magazine1 = Magazine("Tech Today", "Technology")
magazine2 = Magazine("Health Weekly", "Health")

article1 = author1.add_article(magazine1, "AI is the Future")
article2 = author1.add_article(magazine2, "Nutrition and Wellness")
article3 = author2.add_article(magazine1, "Quantum Computing Explained")

print("Author Articles:", author1.articles())
print("Author Magazines:", author1.magazines())
print("Magazine Contributors:", magazine1.contributors())
