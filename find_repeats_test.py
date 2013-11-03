import unittest
import sys
from pyfasta import Fasta
#sys.path.append("../scripts")
from find_repeats import find_Ns

class TestFindReapeats(unittest.TestCase):
    def setUp(self):
        self.fastafile = "sorgtest.fasta"
        self.fasta = Fasta(self.fastafile)

    def test_findNs(self):
        repeats = find_Ns(self.fastafile)
        sort_repreats = repeats['3'][0].sort()
        first = repeats['3'][0][0]
        last = repeats['3'][0][-1]
        print first
        print self.fasta['3'][first[0]-1:first[1]+1]
        print last
        print self.fasta['3'][last[0]-1:last[1]+1]
       
        
if __name__ == '__main__':
    unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)
