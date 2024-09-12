#Name: Ryley Ashcraft
#Class: 5th hour
#Assignment: HW4

print("Hello World!")
Dogdict = { "breed":"Australian Shepard",
            "color":"Grey,white & brown",
            "life span":"13-15 years"}
print(Dogdict["breed"])
Dogdict.update({"size":"medium"})
print(Dogdict)
Dogdict.clear()
print(Dogdict)
fifthhour ={
    "student1":{
        "Name":"Zachary",
        "Grade":12,
        "phone":"iphone"
    },
    "student2":{
        "Name":"Dominic",
        "Grade":12,
        "phone":"iphone"
    },
    "student3":{
        "Name":"Gabe",
        "Grade":12,
        "phone":"iphone"

    }
}
print(fifthhour["student1"]["Name"],fifthhour["student2"]["Name"],fifthhour["student3"]["Name"])