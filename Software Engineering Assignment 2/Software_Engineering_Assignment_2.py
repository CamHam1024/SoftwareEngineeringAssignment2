import csv

# This should be the list used for the functions, Maybe someone could translate it into a CSV file?

# Format I used here (do feel free to tweak) StudentName, StudentID, Modules[ModIDs], ModuleGrades[int]
# students and their grades are in order of their student ID:
# eg. Luci has studentID of 5, her modules are: 
# Visual Data - Grade 55, Soft Engin - Grade 64, Network Security - Grade 61
StudentList = [ 
    {'StudentName': "Kamiel",  'StudentId': 0, 'Modules': [10,20,60], 'ModGrades': [44,68,64]},
    {'StudentName': "Evan",    'StudentId': 1, 'Modules': [20,30,50], 'ModGrades': [42,60,70]},
    {'StudentName': "Rebecca", 'StudentId': 2, 'Modules': [30,40,60], 'ModGrades': [51,61,62]},
    {'StudentName': "Luci",    'StudentId': 3, 'Modules': [10,30,40], 'ModGrades': [55,64,61]},
    {'StudentName': "Jack",    'StudentId': 4, 'Modules': [20,40,50], 'ModGrades': [57,70,45]},
    {'StudentName': "Sally",   'StudentId': 5, 'Modules': [10,50,60], 'ModGrades': [58,44,48]},
]

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