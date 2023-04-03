import random
name= input("Name: ")
url= input("URL: ")
desc= input("Description: ")
rating= random.randint(1,5)

summary= {"name": name,"url":url,"desc":desc,"rating":rating}
print("\nURL Summary")
for name,value in summary.items():
  print(f"{name}:{value}")
