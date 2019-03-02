import gzip
import numpy as np
import matplotlib.pyplot as plt

def dispatch_idx(gz_file):
    arr = np.arange(0)
    with gzip.open(gz_file,'rb') as f:
        magic = int.from_bytes(f.read(4),byteorder='big')
        size = int.from_bytes(f.read(4),byteorder='big')
        if magic==0x803:
            rows = int.from_bytes(f.read(4),byteorder='big')
            columns = int.from_bytes(f.read(4),byteorder='big')
            arr = np.frombuffer(f.read(),dtype='u1').reshape(size,rows*columns)
        elif magic==0x801:
            arr = np.frombuffer(f.read(),dtype='u1')
    return arr
	
def show_digit(set, pos):
    plt.gray()
    plt.imshow(set[pos,].reshape(28,28))