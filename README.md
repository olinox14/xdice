**pydice**

*pydice* is a lightweight python library for managing dice, scores, and dice-notation patterns.

It allows to easily interpret literal expressions as rolls of dice ('1d6', '3d4+3', '12d6+1d4'...etc.), then manipulate the results.

#### Python Versions

DiceRollParser has been tested with python 3.3+

### Documentation

See the full documentation at [...]()

#### Examples:  

	import dice

	## Roll simple dices with **rolldice()**
	
	score = rolldice(6, amount=2)
	
	# manipulates score as an integer
	
	print( score, score * 2, score == 11 )
	>> 11		22		True
	
	
	# Iterates over the results
	
	for result in score:
		print(result)
	>> 5
	>> 6

	# Parse patterns with **roll()**
	
	ps = roll("2d6+18")
	
	print( ps, ps.format() )
	>> 28		'[5,6]+18'


#### CLI

Run `python roll.py [options] <expr>`
	
	Usage:
	    roll [options] <expr>
	
	Options:
	    -s               Numeric score only
	
	    -h --help        Displays help message
	    --version        Displays current pydice version


#### CONTRIBUTION

Any opinion / contribution is welcome, please contact us.

#### TO INSTALL

	pip install pydice

#### License

*pydice* is under GNU License

#### Author

Olivier Massot, 2017, with *Cro-ki Lab*