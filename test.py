#!/usr/bin/env python
import unittest

from d20_ai.tests.test_directories import TestDirectories
from d20_ai.tests.test_example import TestExample
from d20_ai.tests.test_stat_roller import TestAbilityScoreRoller


class CountSuite(object):
    def __init__(self):
        self.count = 0
        self.s = unittest.TestSuite()

    def add(self, tests):
        self.count += 1
        print("%d: %s" % (self.count, tests.__name__))
        self.s.addTest(unittest.makeSuite(tests))


def suite():
    s = CountSuite()

    s.add(TestDirectories)
    s.add(TestExample)
    s.add(TestAbilityScoreRoller)

    return s.s


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
