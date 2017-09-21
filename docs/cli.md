# XDice Command-Line

Run `python roll.py [options] <expr>`
	
	Usage:
	    roll [options] <expr>
	
	Options:
	    -s               Numeric score only
	
	    -h --help        Displays help message
	    --version        Displays current xdice version
	    
### Examples

* Basic use

	python roll 1d6+1
	
	>> 2       ([1]+1)
	
* Numeric score only

	python roll -s 1d6+1
	
	>> 2
