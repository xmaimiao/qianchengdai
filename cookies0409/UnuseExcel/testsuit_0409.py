import unittest
from UnuseExcel import test_Recharge

suite = unittest.TestSuite()
load = unittest.TestLoader()
suite.addTest(load.loadTestsFromModule(test_Recharge))
runner = unittest.TextTestRunner()
runner.run(suite)