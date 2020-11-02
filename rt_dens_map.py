from fortranfile import *
import numpy as np
from matplotlib import pyplot as plt

from optparse import OptionParser

# Parse command line arguments
parser = OptionParser()
parser.usage = "%prog [options] map_file"
parser.add_option('-i','--iter',dest='iter', \
	help='File iterator', default=1)
parser.add_option('-d','--dir',dest='dir', \
	help='Directory', default=1)
(opts,args)=parser.parse_args()

# Getting the input file
infile = '%s/dens_%05d.map' % (opts.dir,int(opts.iter))

# Reading data in
f = FortranFile(infile)
_ = f.readInts()
[nx,ny] = f.readInts()
data = f.readReals()

# You should start from here and either save data to an ASCII file and use your favourite programming language to analyse it or develop this code further to obtained desired answers
data = np.array(data).reshape(nx,ny)

# Plotting
plt.imshow(data,interpolation='none')
plt.savefig(infile+'.png')
