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
StudentList = [] #An empty list for where all the students will be placed into.

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

#A Function for creating and adding a student to the list.
def create_student(Name: str, StudentID: int, ModuleIDs: list, ModuleGrades: list):     
    #print(f"Current Students: {StudentList}") #Prints the student List before adding an entry
    newStudent = Student(Name, StudentID, ModuleIDs, ModuleGrades)

    print(f"Student: {newStudent.name} Added!") #confirmation of addition
    print(f"Registered Students: ") #Prints the resulting List
    for x in StudentList:
        entry = x
        print(x)
    
create_student("Bob", 102, [60,50,40], [10,20,30])
create_student("Larry", 60, [30,20,60], [37,64,55])

#Function that Takes Student ID As input, Prints all modules student is part of, and grades.
def student_finder():
    studId = input("Student Finder: Input student's ID (type 'exit' to exit): ") #This variable takes User input asking for the desired Student ID.
    GradeIter = 0 #This variable is for use in iterating through the Grades.
    
    if (studId != "exit"): # if you type "Exit" you will close the function.
        
        for S in StudentList: #This loop cycles through the list of registered students.
            if (S['StudentId'] != int(studId)): #If the Student ID Isn't the desired Student ID It will Skip this iteration.
                continue
            else: #if it is the desired ID then execute the following.
                
                #Print the student name.
                print(f"=====\nStudent Name: {S['StudentName']}")
                
                #Getting the module Names and grades are alil more complex.
                for Stu, Mod in S.items(): #Loop through the dictonary of the Student's records to find their Modules.
                    if (Stu != 'Modules'): #If it isnt the Modules key. Skip.
                        continue
                    else: #If it is Modules
                        for modules in Mod: #Loop through the modules.
                            for M in ModuleList: 
                                if(M['ModID'] != modules): #If the Student isnt registered for this module ID then Skip.
                                    continue
                                else: #If the Module IS one the Student is registered.
                                    print(f"Module Name: {M['ModuleName']}") #Print module name.
                                    print(f"Module Grade: {S['ModGrades'][GradeIter]}/100\n") #print Module Grade.
                                    GradeIter += 1
                                
                        break

                break
        # Calls itself in order for you to continue looking up students until you type "Exit"
        student_finder()
     
#Function that Takes Student ID As input, Prints the Student's grade average
def student_adverage():
    studId = input("Student adverages: Input student's ID (type 'exit' to exit): ") #This variable takes User input asking for the desired Student ID.
    ScoreTotal = 0 #Container variable for addign the grades together.
    NoOfModules = 0 #container variable for counting the modules.
    
    if (studId != "exit"): # if you type "Exit" you will close the function.
        for S in StudentList: #This loop cycles through the list of registered students.
            if (S['StudentId'] != int(studId)): #If the Student ID Isn't the desired Student ID It will Skip this iteration.
                continue
            else:
                for M in S['ModGrades']: #Loops through the Module Grades for the Student.
                    ScoreTotal += M #Adds each of the scores to a container variable.
                    NoOfModules += 1 #counts each module score accessed.
                #Prints Student name, along with  their Grade Average (ScoreTotal / NoOfModules).
                print(f"=====\nStudent: {S['StudentName']}\nStudent Grade Average: {ScoreTotal/NoOfModules}\n=====")
        student_adverage()

# Initial execution of Student_Finder. (comment this out if you dont need it.)
student_finder()

# Initial execution of Student_adverage. (comment this out if you dont need it.)
student_adverage()

