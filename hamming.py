import unittest

class Hamming:
	def distance(self,genotype1,genotype2):
		if genotype1 == genotype2: 
			return 0
		return 1

hamming = Hamming()


class HammingTest(unittest.TestCase):
	def test_empty_strands(self):
		self.assertEqual(hamming.distance("", ""), 0)
	def test_single_letter_identical_strands(self):
		self.assertEqual(hamming.distance("A", "A"), 0)
	def test_single_letter_different_strands(self):
		self.assertEqual(hamming.distance("G", "T"), 1)
	@unittest.skip("Not done")
	def test_long_identical_strands(self):
		self.assertEqual(hamming.distance("GGACTGAAATCTG", "GGACTGAAATCTG"), 0)
	@unittest.skip("Not done")
	def test_long_different_strands(self):
		self.assertEqual(hamming.distance("GGACGGATTCTG", "AGGACGGATTCT"), 9)
	@unittest.skip("Not done")
	def test_disallow_first_strand_longer(self):
		with self.assertRaisesWithMessage(ValueError):
			hamming.distance("AATG", "AAA")
	@unittest.skip("Not done")
	def test_disallow_second_strand_longer(self):
		with self.assertRaisesWithMessage(ValueError):
			hamming.distance("ATA", "AGTG")
	@unittest.skip("Not done")
	def test_disallow_left_empty_strand(self):
		with self.assertRaisesWithMessage(ValueError):
			hamming.distance("", "G")
	@unittest.skip("Not done")
	def test_disallow_right_empty_strand(self):
		with self.assertRaisesWithMessage(ValueError):
			hamming.distance("G", "")

	# Utility functions
	def setUp(self):
		try:
			self.assertRaisesRegex
		except AttributeError:
			self.assertRaisesRegex = self.assertRaisesRegexp
	@unittest.skip("Not done")
	def assertRaisesWithMessage(self, exception):
		return self.assertRaisesRegex(exception, r".+")