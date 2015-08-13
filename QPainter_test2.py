# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 16:38:28 2014

@author: Seyed Iman Mirzaei
"""


from PySide.QtCore import *
from PySide.QtGui import *


#class DrawCircles(QWidget):
#    def __init__(self, parent=None):
#        QWidget.__init__(self, parent)
#        # setGeometry(x_pos, y_pos, width, height)
#        self.setGeometry(300, 300, 350, 350)
#        self.setWindowTitle('Draw circles')
#    def paintEvent(self, event):
#        paint = QPainter()
#        paint.begin(self)
#        # optional
#        paint.setRenderHint(QPainter.Antialiasing)
#        # make a white drawing background
#        paint.setBrush(Qt.white)
#        paint.drawRect(event.rect())
#        # for circle make the ellipse radii match
#        radx = 100
#        rady = 100
#        # draw red circles
#        paint.setPen(Qt.red)
#        for k in range(125, 220, 10):
#            center = QPoint(k, k)
#            # optionally fill each circle yellow
#            paint.setBrush(Qt.yellow)
#            paint.drawEllipse(center, radx, rady)
#        paint.end()
        

class schematic(QWidget):
    
    # Frame dimensions 
    x0_f = 300; y0_f = 300; w0_f = 500; h0_f = 350;   
    
    # Absolute dimensions
    x0 = 0
    y0 = h0_f
    
    # Substrate dimensions 
    sub_h = -50
    sub_w = w0_f
    
    # Under layer dimensions
    ul_w = 50
    ul_h = -100
    
    # Undercut depth
    uc_d = 80    
    
    # Over layer dimensions
    ol_w = ul_w + uc_d
    ol_h = -20
    
    
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        # setGeometry(x_pos, y_pos, width, height)
        
        self.setGeometry(self.x0_f, self.y0_f, self.w0_f, self.h0_f)
        self.setWindowTitle('Structure cross-section')
        
    def paintEvent(self, event):
        p = QPainter()
        p.begin(self)
        
        # optional
        p.setRenderHint(QPainter.Antialiasing)
        
        # make a white drawing background
        p.setBrush(Qt.white)
        p.drawRect(event.rect())
        
        
        # Construct substrate
        subst = QRectF(self.x0, self.y0, self.sub_w, self.sub_h )
        
        # Construct underlayer
        ul = QRectF(self.x0, self.y0 + self.sub_h, self.ul_w, self.ul_h)
        
        # Constructing over layer
        ol = QRectF(self.x0, self.y0 + self.sub_h + self.ul_h, self.ol_w, self.ol_h)
        
        
        rects = [subst, ul, ol]
        colors = [QColor('black'),QColor('red'),QColor('green')]
        
        for i in range(len(rects)):
            p.drawRect(rects[i])
            p.fillRect(rects[i],colors[i])
        
        
        
        p.end()



#%%

app = QApplication([])
schematics = schematic()
schematics.show()


#%%
#circles = DrawCircles()
#circles.show()
app.exec_()



