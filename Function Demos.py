"""
CTEC 121
<Stephen Guild>
<Module 5 Lab 2>
<Function Demos>
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

#practice 1
def finger(name):
    print("\n",name,"finger,",name,"finger where are you?")
    print("Here I am, here I am. How do you do?\n")

def fingerFamily():
    '''
    finger("Daddy")
    finger("Mommy")
    finger("Brother")
    finger("Sister")
    finger("Baby")
    '''

    for name in ["Daddy", "Mommy","Brother", "Sister","Baby"]:
        finger(name)

def main():
    fingerFamily()
#main()

#practice 2

def AgeClassification(age):
    if age <2:
        return 'I'
    elif age <13:
        return 'C'
    elif age <18:
        return 'T'
    elif age <=125:
        return 'A'
    else:
        return 'U'

def testAgeClassification():
    print()
    print(AgeClassification(-1), "expect U: -1 input")
    print(AgeClassification(0),"expect I: 0 input")
    print(AgeClassification(1),"expect I: 1 input")
    print(AgeClassification(2),"expect C: 2 input")
    print(AgeClassification(12),"expect C: 12 input")
    print(AgeClassification(13),"expect T: 13 input")
    print(AgeClassification(17),"expect T: 17 input")
    print(AgeClassification(18),"expect A: 18 input")
    print(AgeClassification(100),"expect A: 100 input")
    print(AgeClassification(125),"expect A: 125 input")
    print(AgeClassification(126),"expect U: 126 input")

    print()

testAgeClassification()