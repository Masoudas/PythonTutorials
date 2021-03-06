"""
		-Class variables
One of two places where dataclass() actually inspects the type of a field is to determine if a field is a class 
variable as defined in PEP 526. It does this by checking if the type of the field is typing.ClassVar. If a field 
is a ClassVar, it is excluded from consideration as a field and is ignored by the dataclass mechanisms. Such 
ClassVar pseudo-fields are not returned by the module-level fields() function.

	-	Init-only variables
The other place where dataclass() inspects a type annotation is to determine if a field is an init-only variable. 
It does this by seeing if the type of a field is of type dataclasses.InitVar. If a field is an InitVar, it is 
considered a pseudo-field called an init-only field. As it is not a true field, it is not returned by the 
module-level fields() function. Init-only fields are added as parameters to the generated __init__() method, and 
are passed to the optional __post_init__() method. They are not otherwise used by dataclasses.

For example, suppose a field will be initialized from a database, if a value is not provided when creating the 
class:

@dataclass
class C:
    i: int
    j: int = None
    database: InitVar[DatabaseType] = None

    def __post_init__(self, database):
        if self.j is None and database is not None:
            self.j = database.lookup('j')

c = C(10, database=my_database)

In this case, fields() will return Field objects for i and j, but not for database.
"""