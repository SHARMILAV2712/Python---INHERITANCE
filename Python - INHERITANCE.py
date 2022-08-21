#A code with Hospital theme that explains inheritance
# BY: V.SHARMILA_SIST

hospital = "CMC - Vellore"
print(hospital)
print("The departments are:\nCardio\nNeuro\nOrtho\nOpthal\nDerma\nGyno\nOnco\nHemato")
a = input("Enter the department:")
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
class Doctor(Person):
    consulting_fee = 100
    def __init__(self,name,age,gender,degree,speciality):
        super().__init__(name,age,gender)
        self.degree = degree
        self.speciality = speciality
    def ddetails(self):
        doc = f"Doctor Name:{self.name}\nAge:{self.age}\
        \nGender:{self.gender}\nDegree:{self.degree}\nSpeciality:{self.speciality}"
        return doc
    
class Patient(Person):
     def __init__(self,name,age,gender,place,disease,cd):
        super().__init__(name,age,gender)
        self.disease = disease
        self.place = place
        self.cd =cd
     def p(self):
         pat = f"Patient Name:{self.name}\nAge:{self.age}\
        \nGender:{self.gender}\nPlace:{self.place}\nDisease:{self.disease}\nConsulted with:{self.cd} "
         return pat
p1 = Patient("Max",55,"Male","Chennai","Anemia","Dr.Pal")
p2 = Patient("Ameed",65,"Male","TVM","Leukoderma","Dr.Lakshmi")
p3 = Patient("Priya",26,"Female","Vellore","Labour","Dr.Vanitha")
if a == "Cadio":
    d = Doctor("Dr.Sathish",48,"Male","M.s","Open heart Surgeon")
    print(d.ddetails())
    print("Fees:",d.consulting_fee)
    print("Patient Details:No Patient")
elif a == "Neuro":
    d = Doctor("Dr.Rajesh",36,"Male","M.s","Neurologist(Cerebrovascular)")
    print(d.ddetails())
    print("Fees:",d.consulting_fee)
    print("Patient Details:No Patient")
elif a == "Ortho":
    d = Doctor("Dr.Emily",40,"FeMale","M.s","Rheumatology")
    print(d.ddetails())
    print("Fees:",d.consulting_fee)
    print("Patient Details:No Patient")
elif a == "Derma":
    d = Doctor("Dr.Lakshmi",45,"FeMale","MBBS","Procedural Dermatologist")
    print(d.ddetails())
    print("Fees:",d.consulting_fee)
    print("Patient Details:\n",p2.p())
elif a == "Gyno":
    d = Doctor("Dr.Vanitha",40,"FeMale","M.s","Pediatric and Adolescent Gynacology")
    print(d.ddetails())
    print("Fees:",d.consulting_fee)
    print("Patient Details:\n",p3.p())
elif a == "Onco":
    d = Doctor("Dr.John",56,"Male","M.s","Radiation Oncology")
    print(d.ddetails())
    print("Fees:",d.consulting_fee)
    print("Patient Details:No Patient")
elif a == "Hemato":
    d = Doctor("Dr.Pal",40,"Male","M.s","Clinical Hematology")
    print(d.ddetails())
    print("Fees:",d.consulting_fee)
    print("Patient Details:\n",p1.p())
    
else:
    print("None")