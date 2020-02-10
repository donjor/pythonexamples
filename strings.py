#Substrings
str = "Example String"

print(len(str)) #14
print(str[0]) #E
print(str[-1]) #g (loops to end of string)
print(str[0:3]) #Exa
print(str[:3]) #Exa (0 is assumed as frist index)
print(str[8:]) #String (Last index assumed)

print(str.find("Str")) #8 (0 indexed) is case senseitive
print("Example" in str) #True


#Concat/format strings

first = "Jordon"
last = "Retter"

fullname = first + " " + last
print(fullname) #Jordon Retter

fullname = f"{first} {last}"
print(fullname) #Jordon Retter

print(f"{first} {last}") #Jordon Retter

print(f"{len(first)} {len(last * 3)}") #6 18


#String methods
str = "Example String"
print(str.upper()) #EXAMPLE STRING
print(str.lower()) #example string

str = "ExaMPle StriNg"
print(str.title()) #Example String

str = "  Example String  "
print(str.strip()) #Example String
