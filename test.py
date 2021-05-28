# -*- coding: utf-8 -*-
import unittest
from random import *
from detector import *


class DetectorTestCase(unittest.TestCase):

    def test_detect_language(self):
        with open('fixtures/x_test.txt') as x_test_file:
            x_test_lines = x_test_file.readlines()
        with open('fixtures/y_test.txt') as y_test_file:
            y_test_lines = y_test_file.readlines()

        detector = Detector()

        for i in range(5):
            line_number = randint(0, len(x_test_lines))
            self.assertEqual(
                detector.detect_language(x_test_lines[line_number]),
                y_test_lines[line_number]
            )
