from pyfasta import Fasta
import numpy as np
import re
from collections import defaultdict
### open fastafile...
### find Ns in fastafile
### get diff using numpy between one fasta and other

def find_repeats(fastafile,outfile):
    f = Fasta(fastafile)
    d = defaultdict(list)
    out = open(outfile,"wb")
    for chrm in f:
        chrm_str = f[chrm][:]
        ### match as many repeats get as many as possible lower or upper
        #repeat_reagions = re.finditer("X{1,}",chrm_str, flags=re.IGNORECASE)
        repeat_reagions = re.finditer("[a-z]{1,}",chrm_str)
        rep_pos = [repeat.span() for repeat in repeat_reagions]
        d[chrm].append(rep_pos)
        name = "{0}_{1}_{2}".format(chrm,rep_pos[0], rep_pos[1])
        out.write("{0}\t{1}\t{2}\t{4}\t".format(chrm,rep_pos[0],rep_pos[1],name))
    out.close()
    return d

if __name__ == '__main__':
    import optparse
    parser = optparse.OptionParser("usage: %prog [options] ")
    parser.add_option("--RMfasta", dest="fastafile", help="repeatmask fasta file")
    parser.add_option("--out", dest="outfile", help="repeatmask fasta file")
    (options, _) = parser.parse_args()

    find_repeats(options.fastafile, options.outfile)
