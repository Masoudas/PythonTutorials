"""
	-	Frozen instances
It is not possible to create truly immutable Python objects. However, by passing frozen=True to the dataclass() 
decorator you can emulate immutability. In that case, dataclasses will add __setattr__() and __delattr__() methods 
to the class. These methods will raise a FrozenInstanceError when invoked.

There is a tiny performance penalty when using frozen=True: __init__() cannot use simple assignment to initialize 
fields, and must use object.__setattr__().

"""