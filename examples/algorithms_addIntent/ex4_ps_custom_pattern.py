"""
FCA - Python libraries to support FCA tasks
Copyright (C) 2017  Victor Codocedo

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
# Kyori code.
import argparse
from fca.algorithms import dict_printer
from fca.algorithms.addIntent import AddIntent
from fca.defs.patterns import IntervalPattern
from fca.io import read_representations
from fca.io.transformers import List2IntervalsTransformer



class MaxLengthIntervalPattern(IntervalPattern):
    """
    In this example we make a custom pattern structure by modifying
    an existing one
    Particularly, we modify the IntervalPattern intersection
    to allow for a similarity thresholding of each individual interval
    """
    THETA = 0

    @classmethod
    def intersection(cls, desc1, desc2):
        """
        Each interval should be at most of length THETA
        if not, the intersection is the bottom
        """
        new_interval = []
        bottom = False
        for i, j in zip(desc1, desc2):
            new_interval.append((min(i[0], j[0]), max(i[1], j[1])))
            if max(i[1], j[1]) - min(i[0], j[0]) > cls.THETA:
                bottom = True
        if bottom:
            bot = MaxLengthIntervalPattern.bottom(new_interval)
            return bot
        return new_interval


def exec_ex4(filepath, theta_value):
    """
    Execute this example
    """
    MaxLengthIntervalPattern.THETA = int(theta_value)
    # AddIntent(read_representations(filepath, transformer=List2IntervalsTransformer(int)), pattern=MaxLengthIntervalPattern, lazy=False, silent=False)
    dict_printer(AddIntent(read_representations(filepath, transformer=List2IntervalsTransformer(int)), pattern=MaxLengthIntervalPattern, lazy=False, silent=False).lat)


if __name__ == '__main__':
    __parser__ = argparse.ArgumentParser(description='Example 4 - Custom Pattern Structure with AddIntent: Interval with theta value')
    __parser__.add_argument('context_path', metavar='context_path', type=str, help='path to the formal context')
    __parser__.add_argument('-t', '--theta', metavar='theta', type=int, help='Maximal length for intervals [0,inf]', default=0)
    __args__ = __parser__.parse_args()
    exec_ex4(__args__.context_path, __args__.theta)
# okay decompiling ex4_ps_custom.pyc
