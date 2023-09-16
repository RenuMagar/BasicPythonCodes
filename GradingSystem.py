""" A school has following rules for grading system:
1.below 35-Fail
2.35 to 50 -D
3.50 to 65 -C
4.65 to 75- B
75 to 90 -A
90 to 100 -Firstclass"""
marks=int(input("enter your marks"))
if marks<=100 and marks>=90:
    print("Firstclass")
elif marks<90 and marks>=75:
    print("A grade")
elif marks<75 and marks>=65:
    print("B grade")
elif marks<65 and marks>=50:
    print("c grade")
elif marks<50 and marks>=35:
    print("D grade")
else:
    print("fail")
