"""
Default factory functions
If a field() specifies a default_factory, it is called with zero arguments when a default value for the field is 
needed. For example, to create a new instance of a list, use:

mylist: list = field(default_factory=list)
If a field is excluded from __init__() (using init=False) and the field also specifies default_factory, then the 
default factory function will always be called from the generated __init__() function. This happens because there 
is no other way to give the field an initial value.
"""