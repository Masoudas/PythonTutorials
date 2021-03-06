"""
The enum module defines four enumeration classes that can be used to define unique sets of names and values: Enum, 
IntEnum, Flag, and IntFlag. It also defines one decorator, unique(), and one helper, auto.

	-	class enum.Enum¶
	Base class for creating enumerated constants. See section Functional API for an alternate construction syntax.

	-	class enum.IntEnum
	Base class for creating enumerated constants that are also subclasses of int.

	-	class enum.IntFlag
	Base class for creating enumerated constants that can be combined using the bitwise operators without losing 
	their IntFlag membership. IntFlag members are also subclasses of int.

	-	class enum.Flag
	Base class for creating enumerated constants that can be combined using the bitwise operations without losing 
	their Flag membership.

	-	enum.unique()
	Enum class decorator that ensures only one name is bound to any one value.

	-	class enum.auto
	Instances are replaced with an appropriate value for Enum members. By default, the initial value starts at 1.
"""