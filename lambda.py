#Python Lambda Function Declaration
#lambda argument(s) : expression 
#Example: Python Lambda Function
# declare a lambda function
greet = lambda : print('Hello World')

# call lambda function
greet()

# Output: Hello World

#Python lambda Function with an Argument

# lambda that accepts one argument
greet_user = lambda name : print('Hey there,', name)

# lambda call
greet_user('Jalal')

# Output: Hey there, Delilah

people = [
    {"name":"Jahin","house":"USA 2"},
    {"name":"Aifa","house":"USA"},
    {"name":"Jalal","house":"New Yourk"},
    {"name":"Dolon","house":"Clifornia"}
]

def f(person):
    return person["name"]
people.sort(key=f)
people.sort(key=lambda person:person["name"])
print(people)

