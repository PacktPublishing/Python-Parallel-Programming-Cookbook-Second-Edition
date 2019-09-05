import unittest

class OutcomesTest(unittest.TestCase):
		def testPass(self):
			return
		def testFail(self):
			self.failIf(True)
		def testError(self):
			raise RuntimeError('test error!')
			
if __name__ == '__main__':
	unittest.main()