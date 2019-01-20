#!/usr/bin/python
# -*- coding: utf-8 -*-
# install by cmd first: python    -m pip install --upgrade bezier

__author__ = 'ybdesire@gmail.com'
__date__ = '2019-01-20'
__version_info__ = (0, 0, 1)
__version__ = '.'.join(str(i) for i in __version_info__)


import matplotlib.pyplot as plt
import seaborn, bezier
import numpy as np


if __name__ == '__main__':
    # 3 points
    (x1,y1)=(0.2,0.5)
    (x2,y2)=(0.5,3.0)
    (x3,y3)=(1.0,0.0)
    nodes = np.asfortranarray([
        [x1,x2,x3],
        [y1,y2,y3],
    ])
    # 3 points regression by 
    curve = bezier.Curve(nodes, degree=2)
    ax = curve.plot(num_pts=256, color=(1,0,0,1))#  RGBA values should be within 0-1 range
    plt.scatter(x1,y1, s=10, color='blue')
    plt.scatter(x2,y2, s=10, color='blue')
    plt.scatter(x3,y3, s=10, color='blue')
    # display image
    plt.show()