from peewee import *

db = SqliteDatabase('cats.sqlite')

"""
create the model class to bind data from the database objects

"""

class Cat(Model):
    name = CharField()
    color = CharField()
    age = IntegerField()

    class Meta(Model):
        database = db

        def _str_(self):
            return f'{self.name} is a {self.color} cat and is {self.age} years old'

db.connect()
db.create_tables([Cat])

print('\nCreate and save 3 cats.')
zoe = Cat(name="Zoe",color="Orange",age=7)
zoe.save()

duder = Cat(name="Duder", color="Black",age=9)
duder.save()

tintin = Cat(name="Tintin", color="Grey",age=3)
duder.save()

print('\nFind all cats')

cats = Cat.select()

for cat in cats:
    print(cat)