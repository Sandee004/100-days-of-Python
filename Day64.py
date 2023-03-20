class Job:
    name= None
    salary= None
    hrsWorked= None

    def __init__(self, name, salary, hrsWorked):
        self.name= name 
        self.salary= salary
        self.hrsWorked= hrsWorked

class Teacher(Job):
    def __init__(self, subject, position):
        self.name = "Teacher"
        self.salary = "$Nowhere near enough"
        self.hrsWorked = "All of them"
        self.subject = subject
        self.position = position

class Doctor(Job):
    def __init__(self, specialty, exp):
        self.name = "Doctor"
        self.salary = "$ Doing very nicely thank you"
        self.hrsWorked = "50"
        self.specialty = specialty
        self.exp = exp

prof= Job("Lawyer", "$Squillions", "60hrs")
print(f"Profession: {prof.name}\nSalary: {prof.salary}\nHours Worked: {prof.hrsWorked}")
print()

teach= Teacher("Computer Science", "Classroom Teacher")
print(f"Profession: {teach.name}\nSalary: {teach.salary}\nHours Worked: {teach.hrsWorked}\nSubject: {teach.subject}\nPosition: {teach.position}")
print()

doc= Doctor("Pediatric consultant", "7")
print(f"Profession: {doc.name}\nSalary: {doc.salary}\nHours Worked: {doc.hrsWorked}\nSpecialty: {doc.specialty}\nExperience: {doc.exp}")
print()