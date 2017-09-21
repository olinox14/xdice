'''
Created on 18 nov. 2016

@author: olinox
'''
import unittest

import xdice


class Test(unittest.TestCase):
    """unitests for DiceRollParser"""

    def test_secured_eval(self):
        # refused
        self.assertRaises(TypeError, xdice._secured_eval, "open('foo', 'r')")
        # accepted
        xdice._secured_eval("1 + max([1,2,3])")
        xdice._secured_eval("1 + min([1,2,3])")

    def test_patterns_validation(self):
        """check the with behaviour with valid / invalid patterns"""
        # check valid expressions
        xdice.roll("3")
        xdice.roll("0d6")
        xdice.roll("1d6")
        xdice.roll("1d66")
        xdice.roll("1d4+2")
        xdice.roll("1d4-2")
        xdice.roll("1d4 - 2 ")
        xdice.roll("6d102+123")
        xdice.roll("6d102+123+8d6")
        xdice.roll("6d102+123+8d6+2+1+1-8-6d4+8-2d101+100d2")
        xdice.roll("32+3-0-2")
        xdice.roll("1d1-3")
        xdice.roll("1000d1000")
        xdice.roll("10 d 10")
        xdice.roll("10*1d10/2")
        xdice.roll("1d20**2")
        xdice.roll("abs(1d6-1d10)")
        xdice.roll("max(1d6,2d4)")
        xdice.roll("min(1d6,2d4)")

        # test invalid expressions
        self.assertRaises(SyntaxError, xdice.roll, "1d-8")
        self.assertRaises(SyntaxError, xdice.roll, "1d")
        self.assertRaises(ValueError, xdice.roll, "")
        self.assertRaises(ValueError, xdice.roll, "1d0")
        self.assertRaises(TypeError, xdice.roll, "d6")
        self.assertRaises(TypeError, xdice.roll, "abc")
        self.assertRaises(TypeError, xdice.roll, "1d2,3")

    def test_dice_object(self):

        d = xdice.Dice(6, 6)
        self.assertEqual(d.sides, 6)
        self.assertEqual(d.amount, 6)
        self.assertEqual(d.__repr__(), "<Dice; sides=6; amount=6>")

        self.assertRaises(ValueError, setattr, d, "sides", -1)
        self.assertRaises(ValueError, setattr, d, "sides", "a")
        self.assertRaises(ValueError, setattr, d, "sides", None)
        self.assertRaises(ValueError, setattr, d, "amount", -1)
        self.assertRaises(ValueError, setattr, d, "amount", "a")
        self.assertRaises(ValueError, setattr, d, "amount", None)

        self.assertEqual(xdice.Dice(1, 6).roll(), 6)

        self.assertEqual(xdice.Dice.parse("6d1").roll(), 6)

    def test_score_object(self):

        s = xdice.Score([1, 2, 3])

        self.assertEqual(s, 6)
        self.assertEqual(str(s), "6")
        self.assertEqual(list(s), [1, 2, 3])
        self.assertEqual(s.detail, [1, 2, 3])
        self.assertTrue(1 in s)
        self.assertEqual(s.__repr__(), "<Score; score=6; detail=[1, 2, 3]>")


    def test_pattern_object(self):

        p = xdice.Pattern("6d1+6")

        self.assertEqual(p._normalize("1 D 6"), "1d6")

        p.compile()
        self.assertEqual(p.format_string, "{0}+6")
        self.assertEqual(p.dices, [xdice.Dice(1, 6)])

        self.assertEqual(p.roll(), 12)

    def test_patternscore_objet(self):
        ps = xdice.PatternScore("{0}+6", [xdice.Score([1, 1, 1, 1, 1, 1])])

        self.assertEqual(ps, 12)
        self.assertEqual(ps.score(0), 6)
        self.assertEqual(ps.scores(), [6])
        self.assertEqual(ps.format(), "[1, 1, 1, 1, 1, 1]+6")

    def test_compile(self):
        p1 = xdice.compile("6d1+6")
        p2 = xdice.Pattern("6d1+6")
        p2.compile()

        self.assertEqual(p1.format_string, p2.format_string)
        self.assertEqual(p1.dices, p2.dices)

    def test_roll(self):
        ps1 = xdice.roll("6d1+6")
        ps2 = xdice.PatternScore("{0}+6", [xdice.Score([1, 1, 1, 1, 1, 1])])

        self.assertEqual(ps1, ps2)

    def test_rolldice(self):
        self.assertEqual(xdice.rolldice(1, 6), xdice.Dice(1, 6).roll())

if __name__ == "__main__":
    unittest.main()
