Introduction
============


Presentation
------------

*xdice* is a dice library for Python that provides the main functionality 
for managing dice, scores, and dice notation patterns.

DiceRollParser has been tested with python 3.9+.
*xdice* is under GNU License

To install:

::

    pip install xdice

What can it do?
---------------

* Parse most of common dice notations: '1d6+1', 'd20', '3d%', '1d20//2 - 2*(6d6+2)', 'max(1d4+1,1d6)', '3D6L2', 'R3(1d6+1)'...etc.
* Manipulate Dice, Pattern, and Score as objects.
* Roll trough command-line or API
* Understand any mathematical expression


Examples
~~~~~~~~

::

    import dice

    score = dice.roll("2d6+18")

    print(score)
    >> 28
    print(score*2)
    >> 56
    print(score.format())
    >> '[5,6]+18'

    score = dice.roll("6D%L2")
    
    print(ps, ps.format(verbose=True))
    >> 315	'6D%L2(scores:[80, 70, 76, 89], dropped:[2, 49])'
