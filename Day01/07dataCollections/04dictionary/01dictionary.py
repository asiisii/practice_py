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
person['country']
person.get('country')
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


# Python - Change Dictionary Items
person['country'] = 'NP'
person.update({ 'country' : 'NP' })

# and if the key doesn't exist then it will add the key value to the dictionary

# Python - Remove Dictionary Items
person.pop('county') #will remove the key city and its value with it
person.popitem() #will remove the last key value
del person['country'] # will removes the item with the specified key name
del person #will remove the entire variable
person.clear() # person will equal to {} now


# Python - Loop Dictionaries
for key, value in person.items():
  print(key, value)

for key in person.keys():
  print(key)

for value in person.values():
  print(value)


# Python - Copy Dictionaries
person.copy()

dict(person)
