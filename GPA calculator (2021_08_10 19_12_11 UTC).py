#A python program to calculate the CGPA of students
def ucc():
        print(
                """
Name of University: University of Cape Coast
Motto: Veritas Nobis Lumen
Est: 1962
""")

def ug():
        print("""
Name of University: University of Ghana
Motto:
Est:

""")


def uew():
        print("""
Name of University: University of Education Winneba
Motto:
Est:

""")


def knust():
        print("""
Name of University: Kwame Nkrumah University of Science and Technology
Motto:
Est:

""")


sch=input('Name of university: ')
##print('                                                               ',sch)
##print('                                                               motto:  veritas nobis lumen                      ')
##print('                                                                         est_1962                                       ')      
##print('_'*167)
##print("Hello, you are welcome to ",sch, "the platform of higher learning.")
##print("We will ask you some few questions to get you signed in.")
##print('_'*167)
if 'ucc' in sch.lower() or sch.lower() in 'university of cape coast':
        ucc()
elif 'ug' in sch.lower() or sch.lower() in 'university of ghana':
        ug()
elif 'uew' in sch.lower() or sch.lower() in 'university of winneba':
        uew()
elif 'knust' in sch.lower() or sch.lower() in 'kwame nkrumah university of science and technology':
        knust()
else:
        print('Invalid input. Enter name of school manually')
        sch=input('Name of University: ')


#Student details
name=input('Enter your name:  ')
age=input('How old are you? ')
level=input('Enter your level:')
pro=input('Which program do you read? ')

print('_'*167)
##print('Your name is ', name)
##print('You are ', age ,'years of age')
##print('You attend ', uni ,'and currently you are in level ', level ,'reading ', pro)
##print()

user=input('Please enter your password: ')
for conf in range(1):
        conf=input('Confirm your password: ')
if user==conf:
          print('Login successful ')
else:
        print('Wrong password ')
        re_enter=input('Please re-enter your password: ')
        if re_enter==user:
                print('Login Successful')
                input('Press Enter to continue')
        else:
                print('Entries exceeded')
                print('Create a new password')
                user=input('Please enter your password: ')
                for conf in range(1):
                        conf=input('Confirm your password: ')
                if user==conf:
                        print('Login successful ')
print()
#Taking inputs for assessment and exams score to compute GPA and CGPA

def GPT():
		if totalMarks >= 80 and totalMarks < 101:
				gPt = 4.0*creditHours
		elif totalMarks >= 75 and totalMarks < 80:
				gPt = 3.5*creditHours
		elif totalMarks >= 70 and totalMarks < 75:
				gPt = 3.0*creditHours
		elif totalMarks >= 65 and totalMarks < 70:
				gPt = 2.5*creditHours
		elif totalMarks >= 60 and totalMarks < 65:
				gpt = 2.0*creditHours
		elif totalMarks >= 55 and totalMarks < 60:
				gPt = 1.5*creditHours
		elif totalMarks >= 50 and totalMarks < 55:
				gPt = 1.0*creditHours
		elif totalMarks == 50:
				gPt = 0.5*creditHours
		else:
				gPt = 0

num_pro=eval(input('Number of courses: '))
overall_Tmarks=0
totalCreHours=0

CGPA=0

for i in range(0,num_pro):
	courseName=input('Name of course: ')
	print('         Taking inputs for ',courseName)
	print('-'*167)
	creditHours=eval(input('Number of credit hours: '))
	totalCreHours=totalCreHours+creditHours
	assessmentScore=eval(input('Score for assessment out of 40: '))
	examsScore=eval(input('Exams score out of 60: '))
	totalMarks=assessmentScore+examsScore
	print('Total= ' , totalMarks)
	

	overall_Tmarks=overall_Tmarks+totalMarks

	
	if totalMarks >= 80 and totalMarks < 101:
		gPt = 4.0*creditHours
		print('GPT = ' ,gPt)
		print()
		CGPA+=gPt
	elif totalMarks >= 75 and totalMarks < 80:
		gPt = 3.5*creditHours
		print('GPT = ' ,gPt)
		print()
		CGPA+=gPt
	elif totalMarks >= 70 and totalMarks < 75:
		gPt = 3.0*creditHours
		print('GPT = ' ,gPt)
		print()
		CGPA+=gPt
	elif totalMarks >= 65 and totalMarks < 70:
		gPt = 2.5*creditHours
		print('GPT = ' ,gPt)
		print()
		CGPA+=gPt
	elif totalMarks >= 60 and totalMarks < 65:
		gpt = 2.0*creditHours
		print('GPT = ' ,gPt)
		print()
		CGPA+=gPt
	elif totalMarks >= 55 and totalMarks < 60:
		gPt = 1.5*creditHours
		print('GPT = ' ,gPt)
		print()
		CGPA+=gPt
	elif totalMarks >= 50 and totalMarks < 55:
		gPt = 1.0*creditHours
		print('GPT = ' ,gPt)
		print()
		CGPA+=gPt
	elif totalMarks == 50:
		gPt = 0.5*creditHours
		print('GPT = ' ,gPt)
		print()
		CGPA+=gPt
	else:
		gPt = 0
		print('GPT = ' ,gPt)
		print()
		CGPA+=gPt

	

print('Cummulative marks =',overall_Tmarks) 
print('Total credit hours = ',totalCreHours)
print('Grade point=',gPt)
print('Total Grade Points = ',CGPA)
print('Cummulative gradepoint average (CGPA) = ',CGPA/totalCreHours)

#Done

