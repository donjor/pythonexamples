#function
def increment(number, by):
    return (number, number + by) #returning multiple values

#calling function
increment(2,3)
result = increment(number=2, by=3)

print(result)
print("Orginal Number = ", result[0], " | New Number ", result[1])



print("Function V2")

#function

def incrementV2(number, by=1):#add a default value
    orginal_number = number
    new_number = number + by
    return (orginal_number, new_number) #returning multiple values by name

#calling function storing values
orginal_number, new_number = increment(number=5, by=10)

print("Orginal Number = ", orginal_number, " | New Number ", new_number)
