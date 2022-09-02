# Create an empty dictionary called dog
dog = {}
print(dog)
# Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "ROLEX"
dog["color"] = "BROWN"
dog["breed"] = "HUSKEY"
dog["legs"] = "LONG"
dog["age"] = "10"
print(dog)
# Create a student dictionary and add first_name, last_name, gender, age, marital status,
# skills, country, city and address as keys for the dictionary
student = {}
student["first_name"] = "RAHUL"
student["last_name"] = "SAGAR"
student["gender"] = "MALE"
student["age"] = "24"
student["martial_status"] = "I AM SINGLE"
student["skills"] = ['PYTHON', 'JAVA']
student["country"] = "INDIA"
student["city"] = "HYDERABAD"
student["address"] = "NEAR TO CHARMINAR"
print(student)
# Get the length of the student dictionary
print(f'length of student dictonary: {len(student)}')

# Get the value of skills and check the data type, it should be a list
skills = student.get('skills')
print(f'skills in student dictonary: {skills}, type of skills: {type(skills)}')
student['skills'] += ['javascript', 'sql']
print(f"new skills added: {student['skills']}")
print(f"dictonary keys as list: {list(student.keys())}")
print(f"dictonary values as list: {list(student.values())}")