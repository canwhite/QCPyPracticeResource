#test_count.py
#通过unittest单元测试框架编写测试用例

import unittest

from count import Calculator


#括号里边是继承内容
# class CountTest(unittest.TestCase):
# 	"""docstring for CountTest"""
# 	def setup(self):

class CountTest(unittest.TestCase):
		"""docstring for CountTest"""

	# 初始化计算器
		def setUp(self):
			self.cal = Calculator(8,4)

		def tearDown(self):
			pass

		def test_add(self):
			result = self.cal.add()
			self.assertEqual(result,12)

		def test_sub(self):
			result = self.cal.sub()
			self.assertEqual(result,4)

		def test_mul(self):
			result = self.cal.mul()
			self.assertEqual(result,32)

		def test_div(self):
			result = self.cal.div()
			self.assertEqual(result,2)


if __name__ == "__main__":
	#unittest.main()
	#构建测试集
	suite = unittest.TestSuite()
	suite.addTest(CountTest('test_add'))
	suite.addTest(CountTest('test_sub'))
	suite.addTest(CountTest('test_mul'))
	suite.addTest(CountTest('test_div'))
	#执行测试
	runner = unittest.TextTestRunner()
	runner.run(suite)



				
		
















