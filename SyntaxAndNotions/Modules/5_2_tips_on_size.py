"""
	-	You can use the -O or -OO switches on the Python command to reduce the size of a compiled module. The -O 
		switch removes assert statements, the -OO switch removes both assert statements and __doc__ strings. Since 
		some programs may rely on having these available, you should only use this option if you know what you’re 
		doing. “Optimized” modules have an opt-tag and are usually smaller. Future releases may change the effects 
		of optimization.

	-	A program doesn’t run any faster when it is read from a .pyc file than when it is read from a .py file; the 
		only thing that’s faster about .pyc files is the speed with which they are loaded.

	-	The module compileall can create .pyc files for all modules in a directory.
"""