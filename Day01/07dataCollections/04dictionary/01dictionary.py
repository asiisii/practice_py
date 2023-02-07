# Ordered
# changeable
# do not allow duplicates

# Syntax
person = {
  'name': 'John Doe',
  'age': 30,
  'country': 'USA'
}

#  if there's duplicates key then the last one from the list will overwrite it previous key value

# Python - Access Dictionary Items
person['city']
person.get('city')
person.keys()
person.values()
person.items() #

person = {'name': 'John Doe', 'age': 30, 'country': 'USA'}
person_items = person.items()
print(person_items) #dict_items([('name', 'John Doe'), ('age', 30), ('country', 'USA')])
for key, value in person_items:
    print(f"{key}: {value}")    #name: John Doe
                                #age: 30
                                #country: USA


if 'name' in person:
  print('name exists')
