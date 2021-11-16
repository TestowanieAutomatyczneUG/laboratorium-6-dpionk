import unittest

class Song:
	def getSong(self, arg):
		song = ["On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree./n",
"On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree./n",
"On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n",
"On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n",
"On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n",
"On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n",
"On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n",
"On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n",
"On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n",
"On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n",
"On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n",
"On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"]
		songToGet = ""
		if isinstance(arg, list) and (len(arg) != 2 or arg[1] <= arg[0] or arg[0] < 1):
			raise ValueError("Zły argument")
		if isinstance(arg, str) and arg != "whole":
			raise ValueError("Zły argument")
		if isinstance(arg, int):
			songToGet = song[arg-1]
		if isinstance(arg,list):
			for i in range(arg[0], arg[1] + 1):
				songToGet += song[i - 1]
		if arg == "whole":
			for i in song:
				songToGet += i		
		return songToGet

getSong=Song().getSong

class SongTest(unittest.TestCase):
	def test_wholeSong(self):
		self.assertEqual(getSong("whole"), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree./n"+
"On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n")

	def test_single_verse_first(self):
		self.assertEqual(getSong(1), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree./n")

	def test_single_verse_last(self):
		self.assertEqual(getSong(12),"On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n")

	def test_single_verse_middle(self):
		self.assertEqual(getSong(6),"On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n")
	def test_multipleVerses_1_to_12(self):
		self.assertEqual(getSong([1,12]), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree./n"+
"On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n")

	def test_multipleVerses_1_to_3(self):
		self.assertEqual(getSong([1,3]),  "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree./n"+
"On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n" )

	def test_multipleVerses_3_to_8(self):
		self.assertEqual(getSong([3,8]),  "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n")

	def test_multipleVerses_8_to_12(self):
		self.assertEqual(getSong([8,12]), "On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n"+
"On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree./n")

	def test_disallow_any_other_string_than_whole(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong("wholp")

	def test_disallow_any_other_string_than_whole(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong("gsdfs")
	def test_disallow_start_higher_than_stop(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong([12,3])
	def test_disallow_start_equal_to_stop(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong([10,10])
	def test_disallow_start_lower_than_1(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong([0,3])
	def test_disallow_start_lower_than_1_2(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong([-20,3])
	def test_disallow_only_one_value_in_array(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong([-20])
	def test_disallow_only_one_value_in_array_2(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong([3])
	def test_disallow_multiple_values_in_array(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong([3,5,45645,True, "sdfsdf", None])
	def test_disallow_one_value_in_array(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong([3])
	@unittest.skip("Not done")
	def test_disallow_start_higher_than_11(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong([12,12])
	@unittest.skip("Not done")
	def test_disallow_stop_higher_than_12(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong([3,14])
	@unittest.skip("Not done")
	def test_disallow_stop_higher_than_12_2(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong([4,1212])
	@unittest.skip("Not done")
	def test_disallow_start_and_stop_incorrect(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong([-345,1212435435])
	@unittest.skip("Not done")
	def test_disallow_start_and_stop_incorrect_2(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong([150, -45645])
	@unittest.skip("Not done")
	def test_disallow_start_and_stop_incorrect_3(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong([150, {}])
	@unittest.skip("Not done")
	def test_disallow_start_and_stop_incorrect_4(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong([150, {}])
	@unittest.skip("Not done")
	def test_disallow_start_and_stop_incorrect_5(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong([[], ()])
	@unittest.skip("Not done")
	def test_disallow_start_and_stop_incorrect_6(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong([4.5, 4564564564.120])
	@unittest.skip("Not done")
	def test_disallow_start_ok_and_stop_incorrect(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong([3, True])
	@unittest.skip("Not done")
	def test_disallow_stop_ok_and_start_incorrect_2(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong([None, 11])
	@unittest.skip("Not done")
	def test_disallow_stop_ok_and_start_incorrect_3(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong([3.5, 11])
	@unittest.skip("Not done")
	def test_disallow_verse_lower_than_1(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong(0)
	@unittest.skip("Not done")
	def test_disallow_verse_lower_than_1_2(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong(-345345)
	@unittest.skip("Not done")
	def test_disallow_verse_higher_than_12(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong(13)
	@unittest.skip("Not done")
	def test_disallow_verse_higher_than_12_2(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong(343453453455)
	@unittest.skip("Not done")
	def test_disallow_verse_notInt(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong([])
	@unittest.skip("Not done")
	def test_disallow_verse_notInt_2(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong(3.45656776575)
	@unittest.skip("Not done")
	def test_disallow_verse_notInt_3(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong({})
	@unittest.skip("Not done")
	def test_disallow_verse_notInt_4(self):
		with self.assertRaisesWithMessage(ValueError):
			getSong(True)

	def setUp(self):
		try:
			self.assertRaisesRegex
		except AttributeError:
			self.assertRaisesRegex = self.assertRaisesRegexp
	def assertRaisesWithMessage(self, exception):
		return self.assertRaisesRegex(exception, r".+")

if __name__ == "__main__":
    unittest.main()