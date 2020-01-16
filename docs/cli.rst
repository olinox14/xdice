Command-Line
------------

Run ``python roll.py [options] <expr>``

::

	usage: roll [-h] [-V] [-n] [-v] expression [expression ...]
	
	Command Line Interface for the xdice library
	
	positional arguments:
	  expression      mathematical expression(s) containing dice <n>d<s> patterns
	
	optional arguments:
	  -h, --help      show this help message and exit
	  -V, --version   print the xdice version string and exit
	  -n, --num_only  print numeric result only
	  -v, --verbose   print a verbose result
        

-  Basic use

::

   python roll.py 1d6+1
   >> 4       ([3]+1)
   
-  Multiple expressions

::

   python roll.py 1d6+1 2d8
   >> 6       ([5]+1)
   >> 9       ([3, 6])

-  Numeric score only (-n)

::

   python roll.py -n 1d6+1
   >> 2

-  Verbose (-v)

::

   python roll.py -v 2*(3D6L1+2D4)+R3(1d4+2)
   >> 32      (2*(3d6l1(scores:[1, 3], dropped:[1])+2d4(scores:[1, 4]))+(1d4(scores:[2])+2+1d4(scores:[2])+2+1d4(scores:[4])+2))