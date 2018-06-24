|Build Status| |Coverage Status| |Documentation Status|

**xdice**

*xdice* is a lightweight python library for managing dice, scores, and
dice-notation patterns.

- Parse almost any Dice Notation pattern: '1d6+1', 'd20', '3d%', '1d20//2 - 2*(6d6+2)', 'max(1d4+1,1d6)', '3D6L2', 'R3(1d6+1)', '3dF'...etc.
- API help you to easily manipulate dices, patterns, and scores as objects
- A command line tool for convenience


Python Versions
^^^^^^^^^^^^^^^

*xdice* has been tested with **python 3.3+**

Documentation
~~~~~~~~~~~~~

For more, see the Documentation_

Examples:
^^^^^^^^^

::

    import dice

    # Roll simple dices with rolldice()
	# eg: 2d6
	
    score = rolldice(6, amount=2)

    # manipulates the score as an integer

    print(score)
    >> 11
    print(score * 2)
    >> 22
    print(score == 11)
    >> True

    # Or iterates over the results

    for result in score:
        print(result)
    >> 5
    >> 6

    # Parse patterns with roll() and get a PatternScore object

    ps = roll("2d6+18")

    print(ps)
    >> 28
    print(ps.format())
    >> '[5,6]+18'

	# Use special notations, as selective dice
    ps = roll("6D%L2")

    print(ps)
    >> 315
    print(ps.format(verbose=True))
    >> '6D%L2(scores:[80, 70, 76, 89], dropped:[2, 49])'


CLI
^^^

Run ``python roll.py [options] <expr>``

::

	Usage:
	    roll [options] <expr>
	
	Options:
	    -n               Numeric score only
	    -v               Verbose result
	
	    -h --help        Displays help message
	    --version        Displays current xdice version

CONTRIBUTION
^^^^^^^^^^^^

Any opinion / contribution is welcome, please contact us.

TO INSTALL
^^^^^^^^^^

::

    pip install xdice

License
^^^^^^^

*xdice* is under GNU License

Author
^^^^^^

Olivier Massot, 2017, with *Cro-ki Lab*

Tags
^^^^

::

    dice roll d20 game random parser dices role board

.. _Documentation: https://xdice.readthedocs.io/en/latest/

.. |Build Status| image:: https://travis-ci.org/cro-ki/xdice.svg?branch=master
   :target: https://travis-ci.org/cro-ki/xdice
.. |Coverage Status| image:: https://coveralls.io/repos/github/cro-ki/xdice/badge.svg?branch=master
   :target: https://coveralls.io/github/cro-ki/xdice?branch=master
.. |Documentation Status| image:: https://readthedocs.org/projects/xdice/badge/?version=latest
   :target: http://xdice.readthedocs.io/en/latest/?badge=latest