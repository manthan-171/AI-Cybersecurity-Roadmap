dict = { 
    "Name" : "Manthan",
    "Age" : 19,
    "Marks" : 98.09,
    "Subjects" : ["Java", "python" , "JavaScript"],
    "Hobbies" : ("Cricket" , "Gaming" , "Travelling")
}

print(dict["Name"])
print(dict["Hobbies"])

dict["Name"] = "Ethan"
dict["Surname"] = "Patel"

print(dict)

#Methods Of Dictionary
dict1 = { 
    "Name" : "Manthan Patel",
    "Age" : 21,
    "Marks" : 100.0,
    "Subjects" : ["Html", "artificial intelligence" , "machine learning"],
    "Hobbies" : ("Cricket" , "Gaming" , "Travelling")
}

#To Get Keys
print(dict1.keys())
print(len(dict1))

print(list(dict1.keys())) 
print(len(list(dict1.keys())))

#To Get Values
print(dict1.values())
print(len(dict1))

print(list(dict1.values())) 
print(len(list(dict1.values())))

#To Get Keys Items(Gives In A Tuple)
print(dict1.items())
print(len(list(dict1.items())))

#Get The Value From The Key
print(dict1["Name"]) #Returns Error
print(dict1.get("Name")) #Returns None

#Update The Dictionary
dict1.update({"Game" : "BGMI"})
print(dict1)

#By Creating New Dict And Update It in Previous Dict
new_dict  = {
    "City" : "Ahmedabad"
}
dict1.update(new_dict)
print(dict1)