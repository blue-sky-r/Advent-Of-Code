import sys
import random

class Animation:
    " very simple helper class to show animation for longer running tasks "

    anim_symbols = '_x*+.!~'

    def __init__(self, pswdlen=8, slowdown=1000):
        self.anim = self.anim_symbols
        self.set(pswdlen, slowdown)

    def set(self, pswdlen=None, slowdown=None, anim=None):
        if pswdlen:     self.pswdlen     = pswdlen
        if slowdown:    self.slowdown    = slowdown
        if anim:        self.anim        = anim
        self.update([])

    def update(self, pswd):
        if type(pswd) is list:
            self.pswd = dict( [ (k,v) for k,v in enumerate(pswd) ] )
        if type(pswd) is dict:
            self.pswd  = pswd

    def animate(self):
        d = dict([(i,random.choice(self.anim)) for i in range(self.pswdlen)])
        #print 'd:',d
        d.update(self.pswd)
        #print 'd:',d.values()
        return ''.join(d.values())

    def searching(self, idx):
        " animate searching for 1 character "
        if idx % self.slowdown: return
        #
        sys.stdout.write(self.animate())
        #
        sys.stdout.flush()
        # back to the starting position
        sys.stdout.write('\b' * self.pswdlen)

