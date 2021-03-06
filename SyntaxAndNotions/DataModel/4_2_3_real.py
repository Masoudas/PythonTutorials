"""
	-	numbers.Real (float)
These represent machine-level double precision floating point numbers. You are at the mercy of the underlying 
machine architecture (and C or Java implementation) for the accepted range and handling of overflow. Python 
does not support single-precision floating point numbers; the savings in processor and memory usage that are 
usually the reason for using these are dwarfed by the overhead of using objects in Python, so there is no 
reason to complicate the language with two kinds of floating point numbers.
"""
if type(12.1) is float:
	print("This is a float type")