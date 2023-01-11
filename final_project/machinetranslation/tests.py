import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def testEnglish(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour" )
        self.assertNotEqual(english_to_french(""),"")
    
    

class TestFrenchToEnglish(unittest.TestCase):
    def testFrench(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertNotEqual(french_to_english(""),"")

unittest.main()

