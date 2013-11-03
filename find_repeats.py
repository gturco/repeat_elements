from pyfasta import Fasta
import numpy as np
import re
from collections import defaultdict
### open fastafile...
### find Ns in fastafile
### get diff using numpy between one fasta and other

def find_Ns(fastafile):
    f = Fasta(fastafile)
    d = defaultdict(list)
    for chrm in f:
        chrm_str = f[chrm][:]
        #print chrm_str
        ### match as many repeats get as many as possible lower or upper
        #repeat_reagions = re.finditer("X{1,}",chrm_str, flags=re.IGNORECASE)
        repeat_reagions = re.finditer("[a-z]{1,}",chrm_str)
        rep_pos = [repeat.span() for repeat in repeat_reagions]
        d[chrm].append(rep_pos)
        #return rep_pos
        #pos = np.array(rep_pos, dtype = ('int16','int16'))
    return d

#first remove all ranges that are the same using intersect
#sec remove all ranges within
#(10-14)
#if (10-14) in list (10-21),(11,22),(12,40)
#[fun(s,e) for s,e in cord]
#map()
#function(s,e):
#    for s,e
#    start looping based on 10 int
#    10 in range new end = 15-21

#find_Ns("sorgtest.fasta")
if __name__ == '__main__':
    import optparse
    parser = optparse.OptionParser("usage: %prog [options] ")
    parser.add_option("--RMfasta", dest="fastafile", help="repeatmask fasta file")
    (options, _) = parser.parse_args()

    find_Ns(options.fastafile)
