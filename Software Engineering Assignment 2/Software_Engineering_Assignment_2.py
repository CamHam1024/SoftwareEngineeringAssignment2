import csv

# Format I used here (do feel free to tweak) ModuleName, ModID, Students[StudentIDs], ModuleGrades[ModGrades]
# Similarly as above students are in numerical order with their grades :
# eg. Visual Data has an ID of 10 and has registered:
ModuleList = [ 
    {'ModuleName': "Visual Data",           'ModID': 10, 'registeredStudentsID': [0, 3, 5], 'moduleGrades': [44, 55, 58]},
    {'ModuleName': "Comp Sciance",          'ModID': 20, 'registeredStudentsID': [0, 1, 4], 'moduleGrades': [68, 42, 57]},
    {'ModuleName': "Software Engineering",  'ModID': 30, 'registeredStudentsID': [1, 2, 3], 'moduleGrades': [60, 51, 64]},
    {'ModuleName': "Network Security",      'ModID': 40, 'registeredStudentsID': [2, 3, 4], 'moduleGrades': [61, 61, 70]},
    {'ModuleName': "Working with Hardware", 'ModID': 50, 'registeredStudentsID': [1, 4, 5], 'moduleGrades': [70, 45, 48]},
    {'ModuleName': "Professional Skills",   'ModID': 60, 'registeredStudentsID': [0, 2, 5], 'moduleGrades': [64, 62, 48]},
]
  
#Student Data
StudentList = [
    {'studentName': "Ella Thompson", 'studentID': 0, 'registeredModulsID': [10, 20, 60], 'myGrades': [44, 68, 64]},
    {'studentName': "Liam Carter",   'studentID': 1, 'registeredModulsID': [20, 30, 50], 'myGrades': [42, 60, 70]},
    {'studentName': "Sofia Ramirez", 'studentID': 2, 'registeredModulsID': [30, 40, 60], 'myGrades': [51, 61, 62]},
    {'studentName': "Noah Patel",    'studentID': 3, 'registeredModulsID': [10, 30, 40], 'myGrades': [55, 61, 64]},
    {'studentName': "Maya Chen",     'studentID': 4, 'registeredModulsID': [20, 40, 50], 'myGrades': [57, 70, 45]},
    {'studentName': "Ethan Brooks",  'studentID': 5, 'registeredModulsID': [10, 50, 60], 'myGrades': [58, 48, 48]},
] #An empty list for where all the students will be placed into.

#The Student Class, here is where a student object can be created apon making a new student they will be added to the list automatically.
class Student: 
    def __init__(self, name, studentID, modules, modgrades):
        #The individual attributes for the students: Name, Student ID, Modules attending and Modual grades
        self.name = name 
        self.studentID = studentID 
        self.modules = modules #modules can be done using a list
        self.modgrades = modgrades #modgrades should also be using a list in the same order as in modules for simplicity
        
        #Appends the newly created student into the "StudentList" list
        StudentList.append({'StudentName': name,  'studentID': studentID, 'registeredModulsID': modules, 'myGrades': modgrades})

#Module class for makign a new Module.
class module:
    def init(self, ModuleName, ModID, studentID, moduleGrades):
        # The individual attributes for the module: Name, module ID, registered Student ID and module grades
        self.ModuleName = ModuleName
        self.ModID = ModID
        self.registeredStudentsID = registeredStudentsID
        self.moduleGrades = moduleGrades

        # Appends the newly created student into the "StudentList" list
        ModuleList.append({'ModuleName': ModuleName, 'ModID': ModID, 'registeredStudentsID': registeredStudentsID, 'moduleGrades': modgrades})

#A Function for creating and adding a student to the list.
def create_student(Name: str, StudentID: int, ModuleIDs: list, ModuleGrades: list):     
    #print(f"Current Students: {StudentList}") #Prints the student List before adding an entry
    newStudent = Student(Name, StudentID, ModuleIDs, ModuleGrades)

    print(f"Student: {newStudent.name} Added!") #confirmation of addition
    
#Function that Takes Student ID As input, Prints all modules student is part of, and grades.
def module_finder():
    studId = input("Module Finder: Input student's ID (type 'exit' to exit): ") #This variable takes User input asking for the desired Student ID.
    GradeIter = 0 #This variable is for use in iterating through the Grades.
    
    if (studId != "exit"): # if you type "Exit" you will close the function.
        
        for S in StudentList: #This loop cycles through the list of registered students.
            if (S['studentID'] != int(studId)): #If the Student ID Isn't the desired Student ID It will Skip this iteration.
                continue
            else: #if it is the desired ID then execute the following.
                #Print the student name.
                print(f"=====\nStudent Name: {S['studentName']}")
                
                #Getting the module Names and grades are alil more complex.
                for Stu, Mod in S.items(): #Loop through the dictonary of the Student's records to find their Modules.
                    if (Stu != 'registeredModulsID'): #If it isnt the Modules key. Skip.
                        continue
                    else: #If it is Modules
                        for modules in Mod: #Loop through the modules.
                            for M in ModuleList: 
                                if(M['ModID'] != modules): #If the Student isnt registered for this module ID then Skip.
                                    continue
                                else: #If the Module IS one the Student is registered.
                                    print(f"Module Name: {M['ModuleName']}") #Print module name.
                                    print(f"Module Grade: {S['myGrades'][GradeIter]}/100\n") #print Module Grade.
                                    GradeIter += 1
                                
                        break

                break
        # Calls itself in order for you to continue looking up students until you type "Exit"
        module_finder()
    
#Function that finds students in a module
def student_finder():
    ModuleID = input("Student Finder: Input module ID (type 'exit' to exit) ")
    GradeIter = 0
    
    if (ModuleID != "exit"):
        for M in ModuleList:
            if (M['ModID'] != int(ModuleID)):
                continue
            else:
                print(f"Module name: {M['ModuleName']} ")
                
                for Mod, Stu in M.items():
                    if (Mod != 'registeredStudentsID'):
                        continue
                    else:
                        for students in Stu:
                            for S in StudentList:
                                if (S['studentID'] != students):
                                    #print(f"Student: {S['StudentId']} : {students}")
                                    continue
                                else:
                                    print(f"Student Name: {S['studentName']}") #Print module name.
                                    print(f"Student Grade: {M['moduleGrades'][GradeIter]}/100\n") #print Module Grade.
                                    GradeIter += 1   
        #Function calls itself to enable multiple searches (recursion)
        student_finder()                   

#Function that prints Students andn their average grades.
def student_adverage():
    print("Student Averages: ")
    # Inital Loop to go though entrys
    for S in StudentList:
        for Stu, Key in S.items():
            if (Stu != 'myGrades'): #if the key isnt 'myGrades' skip the iteration.
                continue
            else:
                #We set it to 0 here so that each loop the variables reset for the next student.
                ScoreTotal = 0 #Container variable for addign the grades together.
                NoOfModules = 0 #container variable for counting the modules.
                
                for G in Key: 
                    #for each grade a Student has add it to ScoreTotal and increase the modules by one.
                    ScoreTotal += G
                    NoOfModules += 1
                
                # Print the adverage of each student, using round() to round them to 2 decimal palces.
                print(f"Student: {S['studentName']}, Adv: {round(ScoreTotal/NoOfModules, 2)}")
    print("\n")

#Function that Takes Modules and modules adverage.
def module_adverage():
    # Inital Loop to go though entrys
    print("Module Averages: ")
    for M in ModuleList:
        for Mod, Key in M.items():
            if (Mod != 'moduleGrades'): #if the key isnt 'myGrades' skip the iteration.
                continue
            else:
                #We set it to 0 here so that each loop the variables reset for the next student.
                ScoreTotal = 0 #Container variable for addign the grades together.
                NoOfModules = 0 #container variable for counting the modules.
                
                for G in Key: 
                    #for each grade a Student has add it to ScoreTotal and increase the modules by one.
                    ScoreTotal += G
                    NoOfModules += 1
                
                # Print the adverage of each student, using round() to round them to 2 decimal palces.
                print(f"Module: {M['ModuleName']},  Adv: {round(ScoreTotal/NoOfModules, 2)}")
    print("\n")
      
# initial execution of Student_finder.
student_finder()

# Initial execution of Module_Finder. (comment this out if you dont need it.)
module_finder()

# Initial execution of Student_adverage. (comment this out if you dont need it.)
student_adverage()

# Execution of Module_adverage. (comment this out if you dont need it.)
module_adverage()

