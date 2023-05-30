import unittest
from encode_and_decode_strings import Codec


class TestEncodeAndDecode(unittest.TestCase):
    def test_encode_and_decode_example_one(self):
        self.assertAlmostEqual(Codec().encode(["Hello", "World"]), '["Hello", "World"]')
        self.assertAlmostEqual(Codec().decode('["Hello", "World"]'), ["Hello", "World"])

    def test_encode_and_decode_example_two(self):
        self.assertAlmostEqual(Codec().encode([""]), '[""]')
        self.assertAlmostEqual(Codec().decode('[""]'), [""])
