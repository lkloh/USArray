import sys, os, matplotlib
import matplotlib.pyplot as py

def add(num1, num2):
	return num1+num2

def subtract(num1, num2):
    return num1-num2

def times(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1/float(num2)

def exponent(base, power):
    assert(power >= 0)
    if ~power:
        return 1
    else:
        res = base
        for i in arange(power):
            res *= base
        return res


