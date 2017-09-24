## Dice Notation

*Dice notation* is nearly fully understood by pydice.

### Dice

> Patterns describes here can be passed to the Dice.parse() class method, and will then return the corresponding Dice object.

**[See Wikipedia for a complete definition.](https://en.wikipedia.org/wiki/Dice_notation)**

#### Bases

Die rolls are given in the form AdX. A (amount) and X (sides) are variables, separated by the letter "d", which stands for die or dice.

* A is the number of dice to be rolled (1 if omitted).
* X is the number of faces of each die.

If the final number is omitted, it is assumed to be a twenty. (This can be changed trough the class property Dice.DEFAULT_SIDES)

> For example, if a game would call for a roll of d4 or 1d4 this would mean, "roll one 4-sided die."
> `3d6` would mean, "roll three six-sided dice"

Note: the `D%` notation is read as `D100`

#### Selective results

The `AdX` pattern can be followed by `Ln` and/or `Hn` ('L' and 'H' respectively stand for lowest and highest).

In this case, the lowest/highest n scores will be discard when the dice will be rolled.

*Eg: `3D6L1` will roll three 6-sided dice, and drop the lowest, while `3D6H1` will roll three 6-sided dice, and drop the highest.*

Notes:
* If no number follow the 'L' or 'H', it is assumed to be a 1.
* 'L' and 'H' can be combined inside a single pattern.


### Patterns

> Patterns describes here can be passed to the Pattern.parse() class method.

`AdX` notations can be integrated in complex expressions.

Any mathematical expression is allowed:

	>> 1d10+1d5+1
	>> 1d20-6
	>> 1d6*2
	>> 2d20//4
	>> 1d6*(1d4**2)
	
#### Builtin python functions

Currently, the following python functions are allowed: `abs`, `max`, `min`

#### Repeat

The `Rn(AdX)` notation can be used to repat n times the `AdX` command.

For example, the pattern `R3(2d6+2)` will roll `2d6+2` three times.

### Examples

* `1d6` 					> Roll a 6-sided die
* `1d6+3` 				> Roll a 6-sided die, then add 3
* `2*(1d6+3)`			> Roll a 6-sided die, add 3, then multiply by 2
* `3d6L2`				> Roll three 6-sided dice, and drop the two lowest.
* `R2(1d6+3)`			> Similar to `1d6+3+1d6+3`
* `1d%`					> Similar to `1d100`
* `d6`					> Similar to `1d6`
* `min(1d6+10,3d6)`	> Keep the minimal score between `1d6+10` and `3d6`