"""
Called by built-in function hash() and for operations on members of hashed collections including set, frozenset, and 
dict. __hash__() should return an integer. The only required property is that objects which compare equal have the 
same hash value; it is advised to mix together the hash values of the components of the object that also play a 
part in comparison of objects by packing them into a tuple and hashing the tuple. Example:

def __hash__(self):
    return hash((self.name, self.nick, self.color))

Note that hash() truncates the value returned from an object's custom __hash__() method to the size of a Py_ssize_t. 
This is typically 8 bytes on 64-bit builds and 4 bytes on 32-bit builds. If an object's __hash__() must interoperate 
on builds of different bit sizes, be sure to check the width on all supported builds. An easy way to do this is 
with python -c "import sys; print(sys.hash_info.width)".

If a class does not define an __eq__() method it should not define a __hash__() operation either; if it defines 
__eq__() but not __hash__(), its instances will not be usable as items in hashable collections. If a class defines 
mutable objects and implements an __eq__() method, it should not implement __hash__(), since the implementation of 
hashable collections requires that a key's hash value is immutable (if the object's hash value changes, it will be 
in the wrong hash bucket).

User-defined classes have __eq__() and __hash__() methods by default; with them, all objects compare unequal 
(except with themselves) and x.__hash__() returns an appropriate value such that x == y implies both that x is y 
and hash(x) == hash(y).

A class that overrides __eq__() and does not define __hash__() will have its __hash__() implicitly set to None. 
When the __hash__() method of a class is None, instances of the class will raise an appropriate TypeError when a 
program attempts to retrieve their hash value, and will also be correctly identified as unhashable when checking 
isinstance(obj, collections.abc.Hashable).

If a class that does not override __eq__() wishes to suppress hash support, it should include __hash__ = None in 
the class definition. A class which defines its own __hash__() that explicitly raises a TypeError would be 
incorrectly identified as hashable by an isinstance(obj, collections.abc.Hashable) call.
"""
import sys
# print(sys.hash_info.width)

class hashable:
	def __init__(self):
		self.x = 10

	def __hash__(self):
		return hash((self.x))	


