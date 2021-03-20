# a_string = "tova e string"

# print(a_string)

# if a_string == "tova e string":
#     print('dobre e')
# print('not in if')
    
# class Main: 
#     def __init__ (self):
#         self.a = 15

# a = Main()

# print(a.a);

# for i in range(20):
#     print(i)

# if True:
#     print("this is true")
# elif True:
#     print("this is sparta")
# else:
#     pass

languages = []
xs = [1,2,3]
xss = [1,2,3,4,5]

languages.append("ASD")
languages.append("ASD2")
languages.append("ASD3")
languages.append("ASD4")    

# Lenght of array 
print(len(languages))

# Boolean value of array

print(bool(xs))

# Iterate over indecies

for i in range(0, len(xs)):
    print(i, xs[i])

# Compare lists 

print(xs == xss)

# Out of bound index - exception - the program stops and it blows up

# print(xs[400])

# Concationation of lists

print(xs + xss + languages)

# Element belongs in list

print(1 in xs)