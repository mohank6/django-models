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
`OR`
```python
    # person -> Person()
    # Change a persons name
    person.update(name="John Doe")
```

**5. Delete**
```python
    # person -> Person()
    # Delete a person
    person.delete()
```
- This will also delete the assocaited passport since, Cascade it set on delete.