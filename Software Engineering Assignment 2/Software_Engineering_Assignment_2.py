import csv

# Format I used here (do feel free to tweak) ModuleName, ModID, Students[StudentIDs], ModuleGrades[ModGrades]
# Similarly as above students are in numerical order with their grades :
# eg. Visual Data has an ID of 10 and has registered: Kamiel - Grade 44, Luci - Grade 55, Sally - Grade 58
ModuleList = [ 
    {'ModuleName': "Visual Data",           'ModID':10 , 'Students':[0,3,5], 'StudentGrades':[44,55,58]},
    {'ModuleName': "Comp Sciance",          'ModID':20 , 'Students':[0,1,4], 'StudentGrades':[68,42,57]},
    {'ModuleName': "Software Engineering",  'ModID':30 , 'Students':[1,2,3], 'StudentGrades':[60,51,64]},
    {'ModuleName': "Network Security",      'ModID':40 , 'Students':[2,3,4], 'StudentGrades':[61,61,70]},
    {'ModuleName': "Working with Hardware", 'ModID':50 , 'Students':[1,4,5], 'StudentGrades':[70,45,48]},
    {'ModuleName': "Professional Skills",   'ModID':60 , 'Students':[0,2,5], 'StudentGrades':[64,62,48]},
]
  
#Student Data
StudentList = [] #An empty list for where all the students will be placed into

#The Student Class, here is where a student object can be created apon making a new student they will be added to the list automatically.
class Student: 
    def __init__(self, name, studentID, modules, modgrades):
        #The individual attributes for the students: Name, Student ID, Modules attending and Modual grades
        self.name = name 
        self.studentID = studentID 
        self.modules = modules #modules can be done using a list
        self.modgrades = modgrades #modgrades should also be using a list in the same order as in modules for simplicity
        
        #Appends the newly created student into the "StudentList" list
        StudentList.append({'StudentName': name,  'StudentId': studentID, 'Modules': modules, 'ModGrades': modgrades})

#A Function for creating and adding a student to the list
def create_student(Name: str, StudentID: int, ModualIDs: list, ModuleGrades: list):     
    #print(f"Current Students: {StudentList}") #Prints the student List before adding an entry
    newStudent = Student(Name, StudentID, ModualIDs, ModuleGrades)

    print(f"Student: {newStudent.name} Added!") #confirmation of addition
    print(f"Registered Students: ") #Prints the resulting List
    for x in StudentList:
        entry = x
        print(x)
    
create_student("Bob", 102, [60,50,40], [10,20,30])
create_student("Larry", 60, [30,20,60], [37,64,55])
