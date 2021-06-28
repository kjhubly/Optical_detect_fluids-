#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 09:31:37 2021

@author: kadenhubly
"""

from PIL import Image
from matplotlib import pyplot as plt
import argparse
import numpy 

if __name__ == "__main__":
    

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,description= 'help message')

#Adding the Argument 
parser.add_argument('cap_coor', nargs =4 , type = int, help='number of images to analyze')

#defining arguments
arg_in = parser.parse_args()

x_tl = arg_in.cap_coor[0]
y_tl = arg_in.cap_coor[1]
x_br = arg_in.cap_coor[2]
y_br = arg_in.cap_coor[3]

#opening image
a = Image.open(r"/Users/kadenhubly/Desktop/Capillary images (1)/w_07A_I187_0_003.jpg")

#creating array for the image
b = numpy.array(a)


b[y_tl:y_br, x_tl:x_br, 1:3] =0


#showing image on the plot 
plt.imshow (b)
plt.show()
