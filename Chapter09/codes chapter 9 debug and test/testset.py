#testset.py
from nose.tools import eq_
import unittest	


class TestSuite:
	def test_mult(self):
		eq_(2*2,4)
        
	def ignored(self):
		eq_(2*2,3)