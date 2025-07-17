from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model) :
    tittle = models.CharField(max_length=225)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self) :
        return self.tittle


class Library(models.Model) :
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name
    

class Librarian(models.Model) :
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='ribrarian')

    def __str__(self):
        return self.name