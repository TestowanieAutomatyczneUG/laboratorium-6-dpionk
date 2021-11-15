import unittest

class Hamming:
	def distance(self,genotype1,genotype2):
		if len(genotype1) != len(genotype2):
			raise ValueError("Podano złe wartości")
		else:
			distance = 0
			for i in range (0, len(genotype1)):
				if genotype1[i] != genotype2[i]:
					distance += 1
			return distance
hamming = Hamming()


class HammingTest(unittest.TestCase):
	def test_empty_strands(self):
		self.assertEqual(hamming.distance("", ""), 0)
	def test_single_letter_identical_strands(self):
		self.assertEqual(hamming.distance("A", "A"), 0)
	def test_single_letter_different_strands(self):
		self.assertEqual(hamming.distance("G", "T"), 1)
	def test_long_identical_strands(self):
		self.assertEqual(hamming.distance("GGACTGAAATCTG", "GGACTGAAATCTG"), 0)
	def test_long_different_strands(self):
		self.assertEqual(hamming.distance("GGACGGATTCTG", "AGGACGGATTCT"), 9)
	def test_disallow_first_strand_longer(self):
		with self.assertRaisesWithMessage(ValueError):
			hamming.distance("AATG", "AAA")
	def test_disallow_second_strand_longer(self):
		with self.assertRaisesWithMessage(ValueError):
			hamming.distance("ATA", "AGTG")
	def test_disallow_left_empty_strand(self):
		with self.assertRaisesWithMessage(ValueError):
			hamming.distance("", "G")
	def test_disallow_right_empty_strand(self):
		with self.assertRaisesWithMessage(ValueError):
			hamming.distance("G", "")

	# Utility functions
	def setUp(self):
		try:
			self.assertRaisesRegex
		except AttributeError:
			self.assertRaisesRegex = self.assertRaisesRegexp
	def assertRaisesWithMessage(self, exception):
		return self.assertRaisesRegex(exception, r".+")