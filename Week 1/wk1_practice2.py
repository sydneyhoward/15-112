#################################################
# Week1 Practice
#################################################

import cs112_s17_linter
import math

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Tue Lecture
#################################################

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def circlesIntersect(x1, y1, r1, x2, y2, r2):
    if distance(x1,y1,x2,y2) <= r1+r2:
        return True
    else:
        return False

def getInRange(x, bound1, bound2):
    high= max(bound1,bound2)
    low= bound1+bound2 - high
    if x<low:
        return low
    elif x>high:
        return high
    else:
        return x

def eggCartons(eggs):
    return math.ceil(eggs/12)

#################################################
# Wed Recitation
#################################################

def isFactor(f, n):
    if f!=0 and n//f*f==n:
        return True
    elif n==0:
        return True
    else:
        return False

def isMultiple(m, n):
    if m==0:
        return True
    elif isFactor(n,m) == True:
        return True
    else:
        return False

def isLegalTriangle(s1,s2,s3):
    longest= max(s1,s2,s3)
    if s1+s2+s3-longest > longest:
        return True
    else:
        return False

def triangleArea(s1, s2, s3):
    s= (s1+s2+s3)/2
    if isLegalTriangle(s1,s2,s3) == True:
        return math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
    else:
        return 0 

def triangleAreaByCoordinates(x1, y1, x2, y2, x3, y3):
    a= distance(x1,y1,x2,y2)
    b= distance(x2,y2,x3,y3)
    c= distance(x1,y1,x3,y3)
    return triangleArea(a,b,c)

#################################################
# Thu Lecture
#################################################

def isEvenPositiveInt(x):
    if isinstance(x,int)==True:
        if x>0:
            if x%2 ==0:
                return True
            else:
                return False
            return True
        else:
            return False
        return True
    else: 
        return False 

def nearestBusStop(street):
    if street%8 <= 4:
        return street - (street%8)
    else: 
        return street+8-street%8

def lineIntersection(m1, b1, m2, b2):
    if m1==m2:
        return None
    else:
        return (b2-b1)/(m1-m2)

def threeLinesArea(m1, b1, m2, b2, m3, b3):
    x1= lineIntersection(m1,b1,m2,b2)
    if m1==m2: return 0
    x2= lineIntersection(m2,b2,m3,b3)
    if m2==m3: return 0
    x3= lineIntersection(m1,b1,m3,b3)
    if m3==m1: return 0
    
    y1= m1*x1+ b1
    y2=m2*x2+ b2
    y3=m3*x3+ b3
    s1= distance(x1,y1,x2,y2)
    s2= distance(x2,y2,x3,y3)
    s3= distance(x3,y3,x1,y3)
    return triangleArea(s1,s2,s3)

#################################################
# TA-led Small-Group Sessions
#################################################

def numberOfPoolBalls(rows):
    return rows*((rows+1)/2)

def numberOfPoolBallRows(balls):
    return math.ceil((-1+math.sqrt(1+8*balls))/2)

#################################################
# Test Functions
#################################################

def testDistance():
    print('Testing distance()... ', end='')
    assert(almostEqual(distance(0, 0, 3, 4), 5))
    assert(almostEqual(distance(-1, -2, 3, 1), 5))
    assert(almostEqual(distance(-.5, .5, .5, -.5), 2**0.5))
    print('Passed.')

def testCirclesIntersect():
    print('Testing circlesIntersect()... ', end='')
    assert(circlesIntersect(0, 0, 2, 3, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 4, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 5, 0, 2) == False)
    assert(circlesIntersect(3, 3, 3, 3, -3, 3) == True)
    assert(circlesIntersect(3, 3, 3, 3,- 3, 2.99) == False)
    print('Passed.')

def testGetInRange():
    print('Testing getInRange()... ', end='')
    assert(getInRange(5, 1, 10) == 5)
    assert(getInRange(5, 5, 10) == 5)
    assert(getInRange(5, 9, 10) == 9)
    assert(getInRange(5, 10, 10) == 10)
    assert(getInRange(5, 10, 1) == 5)
    assert(getInRange(5, 10, 5) == 5)
    assert(getInRange(5, 10, 9) == 9)
    assert(getInRange(0, -20, -30) == -20)
    assert(almostEqual(getInRange(0, -20.25, -30.33), -20.25))
    print('Passed.')

def testEggCartons():
    print('Testing eggCartons()... ', end='')
    assert(eggCartons(0) == 0)
    assert(eggCartons(1) == 1)
    assert(eggCartons(12) == 1)
    assert(eggCartons(13) == 2)
    assert(eggCartons(24) == 2)
    assert(eggCartons(25) == 3)
    print('Passed.')

def testIsFactor():
    print('Testing isFactor()... ', end='')
    assert(isFactor(1,1) == True)
    assert(isFactor(2,10) == True)
    assert(isFactor(-5,25) == True)
    assert(isFactor(5,0) == True)
    assert(isFactor(0,0) == True)
    assert(isFactor(2,11) == False)
    assert(isFactor(10,2) == False)
    assert(isFactor(0,5) == False)
    print('Passed.')

def testIsMultiple():
    print('Testing isMultiple()... ', end='')
    assert(isMultiple(1,1) == True)
    assert(isMultiple(2,10) == False)
    assert(isMultiple(-5,25) == False)
    assert(isMultiple(5,0) == False)
    assert(isMultiple(0,0) == True)
    assert(isMultiple(2,11) == False)
    assert(isMultiple(10,2) == True)
    assert(isMultiple(0,5) == True)
    assert(isMultiple(25,-5) == True)
    print('Passed.')

def testIsLegalTriangle():
    print('Testing isLegalTriangle()... ', end='')
    assert(isLegalTriangle(3, 4, 5) == True)
    assert(isLegalTriangle(5, 4, 3) == True)
    assert(isLegalTriangle(3, 5, 4) == True)
    assert(isLegalTriangle(0.3, 0.4, 0.5) == True)
    assert(isLegalTriangle(3, 4, 7) == False)
    assert(isLegalTriangle(7, 4, 3) == False)
    assert(isLegalTriangle(3, 7, 4) == False)
    assert(isLegalTriangle(5, -3, 1) == False)
    assert(isLegalTriangle(-3, -4, -5) == False)
    print('Passed.')

def testTriangleArea():
    print('Testing triangleArea()... ', end='')
    assert(almostEqual(triangleArea(3,4,5), 6))
    assert(almostEqual(triangleArea(3,4,0), 0))
    assert(almostEqual(triangleArea(3,4,7), 0))
    assert(almostEqual(triangleArea(-3,-4,-5), 0))
    assert(almostEqual(triangleArea(1,2,2.8), (2.9 * 1.9 * 0.9 * 0.1)**0.5))
    print('Passed.')

def testTriangleAreaByCoordinates():
    print('Testing triangleAreaByCoordinates()... ', end='')
    assert(almostEqual(triangleAreaByCoordinates(1,1,9,1,5,5),16))
    assert(almostEqual(triangleAreaByCoordinates(0,0,10,0,0,50),250))
    assert(almostEqual(triangleAreaByCoordinates(1,3,5,3,3,(3+2*3**.5)),
                                                 4*3**.5))
    assert(almostEqual(triangleAreaByCoordinates(-6,7,-3,20,0,7),39))
    assert(almostEqual(triangleAreaByCoordinates(-2,2,2,-2,5,5),20))
    assert(almostEqual(triangleAreaByCoordinates(-2,2,-2,2,5,5),0))
    print('Passed.')


def testIsEvenPositiveInt():
    print('Testing isEvenPositiveInt()... ', end='')
    assert(isEvenPositiveInt(809) == False)
    assert(isEvenPositiveInt(810) == True)
    assert(isEvenPositiveInt(2389238001) == False)
    assert(isEvenPositiveInt(2389238000) == True)
    assert(isEvenPositiveInt(-2389238000) == False)
    assert(isEvenPositiveInt(0) == False)
    assert(isEvenPositiveInt('do not crash here!') == False)
    print('Passed.')

def testNearestBusStop():
    print('Testing nearestBusStop()... ', end='')
    assert(nearestBusStop(0) == 0)
    assert(nearestBusStop(4) == 0)
    assert(nearestBusStop(5) == 8)
    assert(nearestBusStop(12) == 8)
    assert(nearestBusStop(13) == 16)
    assert(nearestBusStop(20) == 16)
    assert(nearestBusStop(21) == 24)
    print('Passed.')

def testLineIntersection():
    print('Testing lineIntersection()... ', end='')
    assert(lineIntersection(2.5, 3, 2.5, 11) == None)
    assert(lineIntersection(25, 3, 25, 11) == None)
    # y=3x-5 and y=x+5 intersect at (5,10)
    assert(almostEqual(lineIntersection(3,-5,1,5), 5))
    # y=10x and y=-4x+35 intersect at (2.5,25)
    assert(almostEqual(lineIntersection(10,0,-4,35), 2.5))
    assert(almostEqual(lineIntersection(10,0,-4,15), 1.0714285714285714))
    print('Passed.')

def testThreeLinesArea():
    print('Testing threeLinesArea()... ', end='')
    assert(almostEqual(threeLinesArea(1, 2, 3, 4, 5, 6), 0))
    assert(almostEqual(threeLinesArea(0, 7, 1, 0, -1, 2), 36))
    assert(almostEqual(threeLinesArea(0, 3, -.5, -5, 1, 3), 42.66666666666666))
    assert(almostEqual(threeLinesArea(1, -5, 0, -2, 2, 2), 25))
    assert(almostEqual(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21))
    assert(almostEqual(threeLinesArea(1, -5, 0, -2, 2, 25), 272.25))
    print('Passed.')

def testNumberOfPoolBalls():
    print('Testing numberOfPoolBalls()... ', end='')
    assert(numberOfPoolBalls(0) == 0)
    assert(numberOfPoolBalls(1) == 1)
    assert(numberOfPoolBalls(2) == 3)   # 1+2 == 3
    assert(numberOfPoolBalls(3) == 6)   # 1+2+3 == 6
    assert(numberOfPoolBalls(10) == 55) # 1+2+...+10 == 55
    print('Passed.')

def testNumberOfPoolBallRows():
    print('Testing numberOfPoolBallRows()... ', end='')
    assert(numberOfPoolBallRows(0) == 0)
    assert(numberOfPoolBallRows(1) == 1)
    assert(numberOfPoolBallRows(2) == 2)
    assert(numberOfPoolBallRows(3) == 2)
    assert(numberOfPoolBallRows(4) == 3)
    assert(numberOfPoolBallRows(6) == 3)
    assert(numberOfPoolBallRows(7) == 4)
    assert(numberOfPoolBallRows(10) == 4)
    assert(numberOfPoolBallRows(11) == 5)
    assert(numberOfPoolBallRows(55) == 10)
    assert(numberOfPoolBallRows(56) == 11)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testDistance()
    testCirclesIntersect()
    testGetInRange()
    testEggCartons()
    testIsFactor()
    testIsMultiple()
    testIsLegalTriangle()
    testTriangleArea()
    testTriangleAreaByCoordinates()
    testIsEvenPositiveInt()
    testNearestBusStop()
    testLineIntersection()
    testThreeLinesArea()
    testNumberOfPoolBalls()
    testNumberOfPoolBallRows()

def main():
    bannedTokens = (
        #'False,None,True,and,assert,def,elif,else,' +
        #'from,if,import,not,or,return,' +
        'as,break,class,continue,del,except,finally,for,' +
        'global,in,is,lambda,nonlocal,pass,raise,repr,' +
        'try,while,with,yield,' +
        #'abs,all,any,bool,chr,complex,divmod,float,' +
        #'int,isinstance,max,min,pow,print,round,sum,' +
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,input,issubclass,iter,' +
        'len,list,locals,map,memoryview,next,object,oct,' +
        'open,ord,property,range,repr,reversed,set,' +
        'setattr,slice,sorted,staticmethod,str,super,tuple,' +
        'type,vars,zip,importlib,imp,string,[,],{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
