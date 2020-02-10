#if statement
age = 17
if age >= 18:
    print("age > or = 18")
else:
    print("age < 18")


if age >= 18:
    print(">18")
elif age >= 16:
    print(">16")

#shorthand if age >18 then set message = Eligible else set message = not eligible
message = "Eligible" if age >= 18 else "Not eligible"
print(message)
