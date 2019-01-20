#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'ybdesire@gmail.com'
__date__ = '2019-01-20'
__version_info__ = (0, 0, 1)
__version__ = '.'.join(str(i) for i in __version_info__)


from math import sqrt
from PIL import Image, ImageDraw


class Bezier(object):
    def __init__(self, draw, points, line_width, line_color):
        self.draw = draw
        self.points = points
        self.line_width = line_width
        self.line_color = line_color
        self.current_point = (0, 0)

    def moveto(self, p):
        self.current_point = p
    
    def lineto(self, p):
        self.draw.line((self.current_point, p), width=self.line_width, fill=self.line_color)
        self.current_point = p

    def render(self):
        NO = 3
        KT = 5
        m = NO - 1
        p = {} # p[3][2]
        for i in range(0, NO, 2):
            p[i] = self.points[i]
        
        l1 = 1.0 * (self.points[0][0] - self.points[1][0])
        ll = 1.0 * (self.points[0][1] - self.points[1][1])
        l1 = sqrt(l1 * l1 + ll * ll)
        
        l2 = 1.0 * (self.points[2][0] - self.points[1][0])
        ll = 1.0 * (self.points[2][1] - self.points[1][1])
        l2 = sqrt(l2 * l2 + ll * ll)
        
        p[1] = (
            ((l1 + l2) * (l1 + l2) * self.points[1][0] - l2 * l2 * self.points[0][0] - l1 * l1 * self.points[2][0]) / (2 * l1 * l2),
            ((l1 + l2) * (l1 + l2) * self.points[1][1] - l2 * l2 * self.points[0][1] - l1 * l1 * self.points[2][1]) / (2 * l1 * l2)
        )
        
        pk = {}  # pk[129][2]
        for i in range(m + 1):
            pk[i] = p[i]
        
        pt = {} # pt[129][2]
        for k in range(KT + 1):
            for i in range(0, m + 1, 2):
                pt[2*i] = pk[i]
            for i in range(m):
                pt[2*i + 1] = (
                    int(pk[i][0] + pk[i+1][0]) >> 1,
                    int(pk[i][1] + pk[i+1][1]) >> 1
                )
            for i in range(1, m):
                pt[2*i] = (
                    int(pt[2*i-1][0] + pt[2*i+1][0]) >> 1,
                    int(pt[2*i-1][1] + pt[2*i+1][1]) >> 1
                )
            for i in range(2*m + 1):
                pk[i] = pt[i]
            
            if k == KT:
                break
            m <<= 1
        self.moveto(pk[0])
        for i in range(1, 2*m + 1):
            self.lineto(pk[i])

if __name__ == '__main__':
    # init figure
    im = Image.new('RGB', (1024,1024), (255,255,255))
    draw = ImageDraw.Draw(im)
    # draw B Curve
    points = ((150,300), (300,200), (485,300))
    b = Bezier(draw, points, 5, (0,0,255))
    b.render()

    im.show()
    im.save('b_curve.jpg')
