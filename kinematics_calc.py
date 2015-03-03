from __future__ import division
from sympy import *
import sys


# Change the variables that aren't the "?" character to floats
def toFloat(first, second, third, fourth):
    ansList = [first, second, third, fourth]
    for i in xrange(4):
        if ansList[i] != '?':
            ansList[i] = float(ansList[i])
    return ansList

# Find the irrelevant/missing variable to determine which kinematic equation to use
def findExVar(a, x, v0, v, t):
    if a == 'x':
        return 'a'
    elif x == 'x':
        return 'x'
    elif v0 == 'x':
        return 'v0'
    elif v == 'x':
        return 'v'
    elif t == 'x':
        return 't'


def questionA(x, v0, v, t):
    givens = toFloat(x, v0, v, t)
    varList = list(enumerate(['x', 'v0', 'v', 't']))

    # Finds which variable that we're trying to solve for
    for term in varList:
        if givens[term[0]] == '?':
            unknownVar = term[1]

    x = givens[0]
    v0 = givens[1]
    v = givens[2]
    t = givens[3]

    if unknownVar == 'x':
        x = symbols('x')
        x = solve((2*x)/t-v-v0, x)
        return "The value of x is %.3f" % x[0]
    elif unknownVar == 'v0':
        v0 = symbols('v0')
        v0 = solve((2*x)/t-v-v0, v0)
        return "The value of v0 is %.3f" % v0[0]
    elif unknownVar == 'v':
        v = symbols('v')
        v = solve((2*x)/t-v-v0, v)
        return "The value of v is %.3f" % v[0]
    elif unknownVar == 't':
        t = symbols('t')
        t = solve((2*x)/t-v-v0, t)
        return "The value of t is %.3f" % t[0]


def questionX(a, v0, v, t):
    givens = toFloat(a, v0, v, t)
    varList = list(enumerate(['a', 'v0', 'v', 't']))

    # Finds which variable that we're trying to solve for
    for term in varList:
        if givens[term[0]] == '?':
            unknownVar = term[1]

    a = givens[0]
    v0 = givens[1]
    v = givens[2]
    t = givens[3]

    if unknownVar == 'v0':
        v0 = symbols('v0')
        v0 = solve(v-v0-a*t, v0)
        return "The value of v0 is %.3f" % v0[0]
    elif unknownVar == 'v':
        v = symbols('v')
        v = solve(v-v0-a*t, v)
        return "The value of v is %.3f" % v[0]
    elif unknownVar == 't':
        t = symbols('t')
        t = solve(v-v0-a*t, t)
        return "The value of t is %.3f" % t[0]
    elif unknownVar == 'a':
        a = symbols('a')
        a = solve(v-v0-a*t, a)
        return "The value of a is %.3f" % a[0]


def questionVKnot(a, x, v, t):
    givens = toFloat(a, x, v, t)
    varList = list(enumerate(['a', 'x', 'v', 't']))

    # Finds which variable that we're trying to solve for
    for term in varList:
        if givens[term[0]] == '?':
            unknownVar = term[1]

    a = givens[0]
    x = givens[1]
    v = givens[2]
    t = givens[3]

    if unknownVar == 'x':
        x = symbols('x')
        x = solve(x-(v*t)+(a*(t**2))/2, x)
        return "The value of x is %.3f" % x[0]
    elif unknownVar == 'v':
        v = symbols('v')
        v = solve(x-(v*t)+(a*(t**2))/2, v)
        return "The value of v is %.3f" % v[0]
    elif unknownVar == 't':
        t = symbols('t')
        t = solve(x-(v*t)+(a*(t**2))/2, t)
        return "The value of t is %.3f" % t[0]
    elif unknownVar == 'a':
        a = symbols('a')
        a = solve(x-(v*t)+(a*(t**2))/2, a)
        return "The value of a is %.3f" % a[0]


def questionV(a, x, v0, t):
    givens = toFloat(a, x, v0, t)
    varList = list(enumerate(['a', 'x', 'v0', 't']))

    # Finds which variable that we're trying to solve for
    for term in varList:
        if givens[term[0]] == '?':
            unknownVar = term[1]

    a = givens[0]
    x = givens[1]
    v0 = givens[2]
    t = givens[3]

    if unknownVar == 'x':
        x = symbols('x')
        x = solve(x-(v0*t)-(a*(t**2))/2, x)
        return "The value of x is %.3f" % x[0]
    elif unknownVar == 'v0':
        v0 = symbols('v0')
        v0 = solve(x-(v0*t)-(a*(t**2))/2, v0)
        return "The value of v0 is %.3f" % v0[0]
    elif unknownVar == 't':
        t = symbols('t')
        t = solve(x-(v0*t)-(a*(t**2))/2, t)
        return "The value of t is %.3f" % t[0]
    elif unknownVar == 'a':
        a = symbols('a')
        a = solve(x-(v0*t)-(a*(t**2))/2, a)
        return "The value of v is %.3f" % a[0]


def questionT(a, x, v0, v):
    givens = toFloat(a, x, v0, v)
    varList = list(enumerate(['a', 'x', 'v0', 'v']))

    # Finds which variable that we're trying to solve for
    for term in varList:
        if givens[term[0]] == '?':
            unknownVar = term[1]

    a = givens[0]
    x = givens[1]
    v0 = givens[2]
    v = givens[3]

    if unknownVar == 'x':
        x = symbols('x')
        x = solve(v**2-v0**2-2*a*x, x)
        return "The value of x is %.3f" % x[0]
    elif unknownVar == 'v0':
        v0 = symbols('v0')
        v0 = solve(v**2-v0**2-2*a*x, v0)
        return "The value of v0 is %.3f" % v0[0]
    elif unknownVar == 'v':
        v = symbols('v')
        v = solve(v**2-v0**2-2*a*x, v)
        return "The value of v is %.3f" % v[0]
    elif unknownVar == 'a':
        a = symbols('a')
        a = solve(v**2-v0**2-2*a*x, a)
        return "The value of t is %.3f" % a[0]


def findSol(a, x, v0, v, t):
    exVar = findExVar(a, x, v0, v, t)
    if exVar == 'a':
        ansString = questionA(x, v0, v, t)
    elif exVar == 'x':
        ansString = questionX(a, v0, v, t)
    elif exVar == 'v0':
        ansString = questionVKnot(a, x, v, t)
    elif exVar == 'v':
        ansString = questionV(a, x, v0, t)
    elif exVar == 't':
        ansString = questionT(a, x, v0, v)
    return ansString
