Command-Line
------------

Run ``python roll.py [options] <expr>``

::

    Usage:
        roll [options] <expr>

    Options:
        -s               Numeric score only
        -v               Verbose result

        -h --help        Displays help message
        --version        Displays current xdice version
        

-  Basic use

   ``python roll 1d6+1`` ``>> 2       ([1]+1)``

-  Numeric score only (-s)

   ``python roll -s 1d6+1`` ``>> 2``

-  Verbose (-v)

   ``python roll -v 2*(3D6L1+2D4)+R3(1d4+2)``
   ``>> (2*(3d6l1(scores:[5, 6], dropped:[3])+2d4(scores:[2, 1]))+(1d4(scores:[4])+2+1d4(scores:[1])+2+1d4(scores:[4])+2))``