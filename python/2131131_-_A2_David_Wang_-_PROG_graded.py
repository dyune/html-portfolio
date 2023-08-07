"""
DAVID WANG 2131131
420-LCU-05 SECTION 3
PROF J. GULLIFER
ASSIGNMENT 2
"""
stu = '' # Initial variable for part A, this is what we will use to make an individual student entry into a list with.
registry = [] # This is the list of all student records. It will contain nested tuples.
total = 0 #Class average sum.
menuinput='' # How we will navigate through the menus.
stu_grade = 0 # This variable is the sum of a student's grades.
stu_letgrade ='' # Is stu_grade but in letter form.
error='' # Because we'll need to bypass a section of code (check Line 31). Not great but oh well.
fail=0 # For checking duplicate IDs with less for loops. man i probably shouldve used def but its too late for that.
preinput=input("""
HELLO USER, WELCOME TO THE CLASS STUDENT RECORDS DATABSE.
INPUT THE FOLLOWING LETTERS TO ACCESS A FUNCTION:
A - Enter student records.
B - Calculate class average.
C - Display information for a given student.
D - List entire class by name and ID.
X - Exit program.
""")
menuinput=preinput.lower()
while menuinput!='x':
  if menuinput=='a':
    print("""STUDENT RECORDS: Format example: Ann,123,3,4,5,6,7,8""")
    stu=input('Input student information or \'q\' to return to menu: ')
    stud=stu.split(',')
    while stu!='q': #ALL EXITS FOR PART A GO HERE
      error=''#RESET ERROR VALUE, THIS IS USED TO BYPASS THE FACT THAT WHEN WE BREAK FROM THE FOR LOOP LATER AT LINE 50, WE ARE STILL GOING TO EXECUTE THE REMAINDER OF THE CODE
      if len(stud)!=8: #entries need 8 data sets
        print('ERROR: invalid entry format: MISSING DATA OR INCORRECT DATA FORMAT')
        stu=input('Input student information or \'q\' to return to menu: ')
        stud=stu.split(',')
        continue #EXIT HERE
      if len(stud[1])!=3: #student id needs three characters
        print('ERROR: invalid entry format: IMPROPER ID.')
        stu=input('Input student information or \'q\' to return to menu: ')
        stud=stu.split(',')
        continue #EXIT HERE
      elif ' ' in stu or '.' in stu: #cant accept any weird characters either
        print('ERROR: invalid entry format: ILLEGAL CHARACTERS')
        stu=input('Input student information or \'q\' to return to menu: ')
        stud=stu.split(',')
        continue #EXIT HERE
      else: #run if all is ok
        for elem in range(1,8): #to check for appropriate grades, 8c isnt a valid grade but 8 is
          if stud[elem].isdigit():
            stud[elem]=int(stud[elem])
          else:
            print('ERROR: invalid entry format: IMPROPER GRADE FORMAT.')
            error='y'
            break #exit FOR LOOP, SINCE WE CANT EXIT BACK TO THE WHILE LOOP TO RESTART AN INPUT, WE HAVE TO INVALIDATE ALL FURTHER ACTIONS THROUGH THE ERROR VARIABLE
      if not error=='y':
        registry.append(stud) #for now, we will add the entry
        if len(registry)==1: #no such thing as a duplicate when there's only one entry
          print('SUCCESSFUL ENTRY')
        else: #otherwise, we need to check
          for i in range(len(registry)-1):
            fail = 0
            if registry[i][1]==stud[1]:
              fail=1
              break
          if fail==1:
            print('ERROR: Duplicate ID found.')
            registry.pop() #SINCE IT IS A DUPLICATE, WE GET RID OF IT, IT IS THE LAST THING ADDED SO POP'S ARGUMENT CAN BE EMPTY
          else:
            print('SUCCESSFUL ENTRY')
          for index in range(len(registry)): 
            registry[index]=tuple(registry[index])
          registry.sort() 
      stu=input('Input student information or \'q\' to return to menu: ')
      stud=stu.split(',')
  stu=''
  if menuinput=='b':
    if len(registry)==0:
      print('ERROR: Please enter student results first.')
    #0 divided by zero does not occur in everyday mathematics, therefore, if there are no entries, the output will indicate there is no average to calculate yet.
    else:
      for sumelem in range(0, len(registry)):
        for sumelem2 in range (2, 8):
        #Line 40.
          total += registry[sumelem][sumelem2]
      avg = round(total/(len(registry)))
      print(f'The class average is {avg}.')
      total=0
  if menuinput=='c': 
    findstu=input('Enter the ID of the student or \'q\' to return to menu: ')
    if findstu.isdigit():
      match=int(findstu) 
      for entry in registry:
        query = entry[1]
        if query == match:
          stu_grade = sum(entry[2:])
          if stu_grade >= 90:
            stu_letgrade = 'A'
          if stu_grade < 90 and stu_grade >= 80:
            stu_letgrade = 'B'
          if stu_grade < 80 and stu_grade >= 70:
            stu_letgrade = 'C'
          if stu_grade < 70 and stu_grade >= 60:
            stu_letgrade = 'D'
          if stu_grade < 60:
            stu_letgrade = 'F'
          break
      if stu_letgrade=='': #if no match is found, no grade is assigned
        print(f'No student with an ID of {match} was found.')
      else:
        print(f'{str(entry[0])}, {str(entry[1])} has a grade of {stu_grade}, {stu_letgrade}')
      stu_letgrade='' #reset the value so that the conditon for line 107 works
    else:
      print('ERROR: Please enter a valid ID.')
  if menuinput=='d':
    print('Current students in record: ')
    for student in range(0, len(registry)):
      print(str(registry[student][0]), (str(registry[student][1])))
  preinput=input("""
MENU:
A - Enter student records.
B - Calculate class average.
C - Display information for a given student.
D - List entire class by name and ID.
X - Exit program.
""")
  menuinput=preinput.lower()
print('PROGRAM TERMINATED, HAVE A NICE DAY.')

# Grading
# Nice work.
# 20/20