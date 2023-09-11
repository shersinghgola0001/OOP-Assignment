# Problem Statement 
# Implement the complete Student class by completing the tasks below
# Task # Implement the following properties as private:
#     name
#     RollNumber
# Include the following methods to get and set the private properties above:
#     getName()
#     setName()
#     getRollNumber()
#     setRollNumber()
# Implement this class according to the rules of encapsulation.
class Student:
    def __init__(self):
        self.__name = None
        self.__rollNumber = None
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber
    def getRollNumber(self):
        return self.__rollNumber
student = Student()
student.setName("SherSingh Gola")
student.setRollNumber("010130044221")
name = student.getName()
rollNumber = student.getRollNumber()
print("Name:", name)
print("Roll Number:", rollNumber)
