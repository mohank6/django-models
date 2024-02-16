# Models
**1. Define Models**
- Define your database models in the `<app-name>/models.py` file.

**2. Migrate Models to Database**
```bash
    python manage.py makemigrations
```
```bash
    python manage.py migrate
```

# CRUD (django shell)

```bash
    python manage.py shell
```

## OneToOne Relationship
`Person <-> Passport`

OneToOne relationship is a type of relationship between two models where each record in the first model corresponds to exactly one record in the second model, and vice versa.

**1. Import models**
```python
    from app.models import Person, Passport
```
**2. Create Person and Passport objects**
```python 
    person = Person.objects.create(**kwargs)
    passport = Passport.objects.create(person=person, **kwargs)
``` 
`OR`   
```python 
    person = Person(**kwargs)
    person.save()
    passport = Passport(person=person, **kwargs)
    passport.save()
```    
**3. Read operations**
```python
    # passport -> Passport()
    # Get person from passport
    person = passport.person
    # person -> Person()
    # Get passport of a person
    passport = person.passport
```

**4. Update**
```python
    # person -> Person()
    # Change a persons name
    person.name = "John Doe"
    person.save()
```

**5. Delete**
```python
    # person -> Person()
    # Delete a person
    person.delete()
```
- This will also delete the assocaited passport since, Cascade it set on delete.

## OneToMany Relationship
`Library <-< Book`

In a OneToMany relationship,  each record in the first model can be related to multiple records in the second model, but each record in the second model is related to only one record in the first model.

**1. Import models**
```python
    from app.models import Library, Book
```
**2. Create Library and Book objects**
```python 
    library = Library.objects.create(**kwargs)
    book1 = Book.objects.create(library=library, **kwargs)
    book2 = Book.objects.create(library=library, **kwargs)
``` 
**3. Read operations**
```python
    # book1 -> Book()
    # Get library of  a book
    library = book1.library
    # library -> Library()
    # Get all books from a Library
    books = library.book_set.all()
```
- If `related_name` is set
```python
    # library -> Library()
    # Get all books from a Library
    books = library.related_name.all()
```

**4. Update**
```python
    # library -> library()
    # Change a libraries name
    library.name = "John's Library"
    library.save()
```

**5. Delete**
```python
    # library -> library()
    # Delete a library
    library.delete()
```
- This will also delete all  the assocaited books since, Cascade it set on delete.