import unittest

class TruthTest(unittest.TestCase):

	def testFailUnless(self):
		self.failUnless(True)
	def testAssertTrue(self):
		self.assertTrue(True)
	def testFailIf(self):
		self.assertFalse(False)
	def testAssertFalse(self):
		self.assertFalse(False)
if __name__ == '__main__':
	unittest.main()