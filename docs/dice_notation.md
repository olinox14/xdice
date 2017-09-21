# Dice Notation

*Dice notation* is fully understood by pydice.

### Dice

Die rolls are given in the form AdX. A (amount) and X (sides) are variables, separated by the letter "d", which stands for die or dice.

* A is the number of dice to be rolled (usually omitted if 1).
* X is the number of faces of each die.

If the final number is omitted, it is typically assumed to be a six, but in some contexts, other defaults are used.

> For example, if a game would call for a roll of d4 or 1d4 this would mean, "roll one 4-sided die."
> `3d6` would mean, "roll three six-sided dice"

**[See Wikipedia for a complete definition.](https://en.wikipedia.org/wiki/Dice_notation)**


### Patterns

`AdX` notations can be integrated in complex expressions: the resulting scores will then behave like integers.

Any mathematical expression is allowed:

	>> 1d10+1d5+1
	>> 1d20-6
	>> 1d6*2
	>> 2d20//4
	>> 1d6*(1d4**2)

...Etc
	
### Builtin python functions

Currently, the following python functions are allowed: `abs`, `max`, `min`






