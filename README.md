# [Github Repo](https://github.com/mohank6/django-models/tree/dev)
# Object Relational Mapping (ORM)

ORM, is a programming technique that allows developers to interact with a relational database using an object-oriented programming language. It simplifies database interactions.

## Pros of ORM

- Abstraction
- Database Independence
- Code Reusability
- Security

## Cons of ORM:

- Performance Overhead
- Learning Curve
- Limited Optimization Control
- Complex Queries

![](./images/orm.jpg)

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

# Note:
```python
    class Books:
        library = models.ForeignKey(Library, on_delete=models.CASCADE)
        ...
```
`on_delete` attribute is used to determine what shall be done when a record of parent model is deleted.
### **Available options in django.models**
### 1. CASCADE
- In this case, if an library instance is deleted, all related Book instances will be deleted as well.

### 2. SET_NULL
- When an Library instance is deleted, the library field in all related Book instances will be set to NULL(requires `null=True`).

### 3. SET_DEFAULT
- When an Library instance is deleted, the library field in all related Book instances will be set to its default value(requires `default=value`).

### 4. PROTECT
- If an attempt is made to delete an Library instance with related Book instances, a ProtectedError will be raised.

### 5. RESTRICT
- Similar to PROTECT, but raises RestrictedError.

### 6. DO_NOTHING
-  This will do nothing when an Library instance is deleted. 