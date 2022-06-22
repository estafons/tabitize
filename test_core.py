import unittest
from tabitize.core import Tab, TabFromListList
from tabitize.models import Pitch, Octave, Accidental
class TestNote(unittest.TestCase):

    def testTabFromList(self):
        t = TabFromListList([('C', 'one', 'perfect'),[Pitch('D'), Octave('two'), Accidental('perfect')]])
        p = TabFromListList([('C', 'one', 'perfect'),(Pitch('D'), Octave('two'), Accidental('perfect'))])
        s = TabFromListList([('C', 'one', 'perfect'),(Pitch('D'), Octave('two'), Accidental('flat'))])
        self.assertEqual(t,p)
        self.assertIsNot(t,s)
        self.assertIsInstance(t, Tab)
        self.assertIsInstance(t, TabFromListList)
        self.assertNotEqual(t,s)

if __name__ == "__main__":
    unittest.main()