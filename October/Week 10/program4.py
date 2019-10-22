# -------------------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 4: Advising System
# Anthony Louis Rosenblum
# Last Modified: 
# -------------------------------------------------
# A brief overview of the program.
# -------------------------------------------------

class Generic_Major:

    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.major_troubles = False
        self.math_troubles = False
    def get_major(self):
        return "Generic"
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_math_troubles(self):
        return self.math_troubles
    def get_major_troubles(self):
        return self.major_troubles
    def set_math_troubles(self,math_troubles):
        self.math_troubles = math_troubles
    def set_major_troubles(self,major_troubles):
        self.major_troubles = major_troubles
    def major_advising(self):
        if self.major_troubles == True:
            print("because you are having troubles with your major:")
            print("--> visit your professor during office hours")
            print("--> visit your academic advisor")
        else:
            pass
    def math_advising(self):
        if self.math_troubles == True:
            print("because you are having troubles with math:")
            print("--> visit the Math Learning Center in Wilson 1-112")
        else:
            pass

class CLS_Major:

    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.major_troubles = False
        self.math_troubles = False
    def get_major(self):
        return "College of Letters and Sciences"
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_math_troubles(self):
        return self.math_troubles
    def get_major_troubles(self):
        return self.major_troubles
    def set_math_troubles(self,math_troubles):
        self.math_troubles = math_troubles
    def set_major_troubles(self,major_troubles):
        self.major_troubles = major_troubles
    def major_advising(self):
        if self.major_troubles == True:
            print("because you are having troubles with your major:")
            print("--> visit your professor during office hours")
            print("--> visit your academic advisor")
        else:
            pass
    def math_advising(self):
        if self.math_troubles == True:
            print("because you are having troubles with math:")
            print("--> visit the Math Learning Center in Wilson 1-112")
        else:
            pass

class COE_Major:

    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.major_troubles = False
        self.math_troubles = False
    def get_major(self):
        return "College of Engineering"
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_math_troubles(self):
        return self.math_troubles
    def get_major_troubles(self):
        return self.major_troubles
    def set_math_troubles(self,math_troubles):
        self.math_troubles = math_troubles
    def set_major_troubles(self,major_troubles):
        self.major_troubles = major_troubles
    def major_advising(self):
        if self.major_troubles == True:
            print("because you are having troubles with your major:")
            print("--> visit the EMPower Student Center in Roberts 313")
            print("--> visit your professor during office hours")
            print("--> visit your academic advisor")
        else:
            pass
    def math_advising(self):
        if self.math_troubles == True:
            print("because you are having troubles with math:")
            print("--> visit the Math Learning Center in Wilson 1-112")
        else:
            pass

class Physics_Major:

    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.major_troubles = False
        self.math_troubles = False
    def get_major(self):
        return "Physics"
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_math_troubles(self):
        return self.math_troubles
    def get_major_troubles(self):
        return self.major_troubles
    def set_math_troubles(self,math_troubles):
        self.math_troubles = math_troubles
    def set_major_troubles(self,major_troubles):
        self.major_troubles = major_troubles
    def major_advising(self):
        if self.major_troubles == True:
            print("because you are having troubles with your major:")
            print("--> visit the Physics Learning Center in Barnard Hall 230")
            print("--> visit your professor during office hours")
            print("--> visit your academic advisor")
        else:
            pass
    def math_advising(self):
        if self.math_troubles == True:
            print("because you are having troubles with math:")
            print("--> visit the Math Learning Center in Wilson 1-112")
        else:
            pass

class Computer_Engineering_Major:

    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.major_troubles = False
        self.math_troubles = False
    def get_major(self):
        return "Computer Engineering"
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_math_troubles(self):
        return self.math_troubles
    def get_major_troubles(self):
        return self.major_troubles
    def set_math_troubles(self,math_troubles):
        self.math_troubles = math_troubles
    def set_major_troubles(self,major_troubles):
        self.major_troubles = major_troubles
    def major_advising(self):
        if self.major_troubles == True:
            print("because you are having troubles with your major:")
            print("--> visit the EMPower Student Center in Roberts 313")
            print("--> visit your professor during office hours")
            print("--> visit your academic advisor")
        else:
            pass
    def math_advising(self):
        if self.math_troubles == True:
            print("because you are having troubles with math:")
            print("--> visit the Math Learning Center in Wilson 1-112")
        else:
            pass

class Computer_Science_Major:

    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.major_troubles = False
        self.math_troubles = False
    def get_major(self):
        return "Computer Science"
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_math_troubles(self):
        return self.math_troubles
    def get_major_troubles(self):
        return self.major_troubles
    def set_math_troubles(self,math_troubles):
        self.math_troubles = math_troubles
    def set_major_troubles(self,major_troubles):
        self.major_troubles = major_troubles
    def major_advising(self):
        if self.major_troubles == True:
            print("because you are having troubles with your major:")
            print("--> visit the CS Student Success Center in Barnard Hall 259")
            print("--> visit a CS professional advisor in Barnard Hall 357")
            print("--> visit the EMPower Student Center in Roberts 313")
            print("--> visit your professor during office hours")
            print("--> visit your academic advisor")
        else:
            pass
    def math_advising(self):
        if self.math_troubles == True:
            print("because you are having troubles with math:")
            print("--> visit the Math Learning Center in Wilson 1-112")
        else:
            pass
    

# -------------------------------------------------
# Do not change anything below this line
# -------------------------------------------------

def advise(student):
    print("Student:", student.get_first_name(), student.get_last_name())
    print("Major: " + student.get_major() + ", Major Troubles: " +
          str(student.get_major_troubles()) + ", Math Troubles: " +
          str(student.get_math_troubles()))
    print()
    if not student.get_math_troubles() and not student.get_major_troubles():
        print("No advising is necessary.  Keep up the good work!")
    else:
        student.major_advising()
        student.math_advising()
    print("------------------------------")

# -------------------------------------------------

def process(student):
    advise(student)
    student.set_major_troubles(True)
    student.set_math_troubles(True)
    advise(student)

# -------------------------------------------------

def main():

    # Every student has a major, even if it is "undeclared"
    msu_student = Generic_Major("jalen", "nelson")
    process(msu_student)

    msu_student.set_math_troubles(False)
    advise(msu_student)

    msu_student.set_math_troubles(True)
    msu_student.set_major_troubles(False)
    advise(msu_student)

    # A CLS (College of Letters and Science) major is a subclass of a Generic major
    msu_student = CLS_Major("emma", "phillips")
    process(msu_student)

    # A COE (College of Engineering) major is a subclass of a Generic major
    msu_student = COE_Major("camden", "miller")
    process(msu_student)

    # A Computer Engineering major is a subclass of a COE major
    msu_student = Computer_Engineering_Major("gabriel", "smith")
    process(msu_student)

    # A Physics major is a subclass of a CLS major
    msu_student = Physics_Major("lena", "hamilton")
    process(msu_student)

    # A Computer Science major is a subclass of a COE major
    msu_student = Computer_Science_Major("halley", "jones")
    process(msu_student)

    msu_student.set_math_troubles(False)
    advise(msu_student)

    msu_student.set_math_troubles(True)
    msu_student.set_major_troubles(False)
    advise(msu_student)

# -------------------------------------------------

main()


