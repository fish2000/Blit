""" Tests for Blit.

Run as a module, like this:
    python -m Blit.tests
"""
import unittest
import Image

from . import Layer, Color

def _str2img(str):
    """
    """
    return Image.fromstring('RGBA', (3, 3), str)

class Tests(unittest.TestCase):

    def setUp(self):
        """
        """
        # Sort of a sw/ne diagonal street, with a top-left corner halo:
        # 
        # +------+   +------+   +------+   +------+   +------+
        # |\\\\\\|   |++++--|   |  ////|   |    ''|   |\\//''|
        # |\\\\\\| + |++++--| + |//////| + |  ''  | > |//''\\|
        # |\\\\\\|   |------|   |////  |   |''    |   |''\\\\|
        # +------+   +------+   +------+   +------+   +------+
        # base       halos      outlines   streets    output
        #
        # Just trust the tests.
        #
        _fff, _ccc, _999, _000, _nil = '\xFF\xFF\xFF\xFF', '\xCC\xCC\xCC\xFF', '\x99\x99\x99\xFF', '\x00\x00\x00\xFF', '\x00\x00\x00\x00'
        
        self.base = Layer(_str2img(_ccc * 9))
        self.halos = Layer(_str2img(_fff + _fff + _000 + _fff + _fff + (_000 * 4)))
        self.outlines = Layer(_str2img(_nil + (_999 * 7) + _nil))
        self.streets = Layer(_str2img(_nil + _nil + _fff + _nil + _fff + _nil + _fff + _nil + _nil))
    
    def test0(self):
    
        out = self.base
        out = out.blend(self.outlines)
        out = out.blend(self.streets)
        
        img = out.image()

        assert img.getpixel((0, 0)) == (0xCC, 0xCC, 0xCC, 0xFF), 'top left pixel'
        assert img.getpixel((1, 0)) == (0x99, 0x99, 0x99, 0xFF), 'top center pixel'
        assert img.getpixel((2, 0)) == (0xFF, 0xFF, 0xFF, 0xFF), 'top right pixel'
        assert img.getpixel((0, 1)) == (0x99, 0x99, 0x99, 0xFF), 'center left pixel'
        assert img.getpixel((1, 1)) == (0xFF, 0xFF, 0xFF, 0xFF), 'middle pixel'
        assert img.getpixel((2, 1)) == (0x99, 0x99, 0x99, 0xFF), 'center right pixel'
        assert img.getpixel((0, 2)) == (0xFF, 0xFF, 0xFF, 0xFF), 'bottom left pixel'
        assert img.getpixel((1, 2)) == (0x99, 0x99, 0x99, 0xFF), 'bottom center pixel'
        assert img.getpixel((2, 2)) == (0xCC, 0xCC, 0xCC, 0xFF), 'bottom right pixel'
    
    def test1(self):

        out = self.base
        out = out.blend(self.outlines, self.halos)
        out = out.blend(self.streets)
        
        img = out.image()

        assert img.getpixel((0, 0)) == (0xCC, 0xCC, 0xCC, 0xFF), 'top left pixel'
        assert img.getpixel((1, 0)) == (0x99, 0x99, 0x99, 0xFF), 'top center pixel'
        assert img.getpixel((2, 0)) == (0xFF, 0xFF, 0xFF, 0xFF), 'top right pixel'
        assert img.getpixel((0, 1)) == (0x99, 0x99, 0x99, 0xFF), 'center left pixel'
        assert img.getpixel((1, 1)) == (0xFF, 0xFF, 0xFF, 0xFF), 'middle pixel'
        assert img.getpixel((2, 1)) == (0xCC, 0xCC, 0xCC, 0xFF), 'center right pixel'
        assert img.getpixel((0, 2)) == (0xFF, 0xFF, 0xFF, 0xFF), 'bottom left pixel'
        assert img.getpixel((1, 2)) == (0xCC, 0xCC, 0xCC, 0xFF), 'bottom center pixel'
        assert img.getpixel((2, 2)) == (0xCC, 0xCC, 0xCC, 0xFF), 'bottom right pixel'
    
    def test2(self):
    
        out = Color(0xcc, 0xcc, 0xcc)
        out = out.blend(self.outlines, self.halos)
        out = out.blend(self.streets)
        
        img = out.image()
        
        assert img.getpixel((0, 0)) == (0xCC, 0xCC, 0xCC, 0xFF), 'top left pixel'
        assert img.getpixel((1, 0)) == (0x99, 0x99, 0x99, 0xFF), 'top center pixel'
        assert img.getpixel((2, 0)) == (0xFF, 0xFF, 0xFF, 0xFF), 'top right pixel'
        assert img.getpixel((0, 1)) == (0x99, 0x99, 0x99, 0xFF), 'center left pixel'
        assert img.getpixel((1, 1)) == (0xFF, 0xFF, 0xFF, 0xFF), 'middle pixel'
        assert img.getpixel((2, 1)) == (0xCC, 0xCC, 0xCC, 0xFF), 'center right pixel'
        assert img.getpixel((0, 2)) == (0xFF, 0xFF, 0xFF, 0xFF), 'bottom left pixel'
        assert img.getpixel((1, 2)) == (0xCC, 0xCC, 0xCC, 0xFF), 'bottom center pixel'
        assert img.getpixel((2, 2)) == (0xCC, 0xCC, 0xCC, 0xFF), 'bottom right pixel'
    
    def test3(self):
        
        out = Color(0xcc, 0xcc, 0xcc)
        out = out.blend(Color(0x99, 0x99, 0x99), self.halos)
        out = out.blend(self.streets)
        
        img = out.image()
        
        assert img.getpixel((0, 0)) == (0x99, 0x99, 0x99, 0xFF), 'top left pixel'
        assert img.getpixel((1, 0)) == (0x99, 0x99, 0x99, 0xFF), 'top center pixel'
        assert img.getpixel((2, 0)) == (0xFF, 0xFF, 0xFF, 0xFF), 'top right pixel'
        assert img.getpixel((0, 1)) == (0x99, 0x99, 0x99, 0xFF), 'center left pixel'
        assert img.getpixel((1, 1)) == (0xFF, 0xFF, 0xFF, 0xFF), 'middle pixel'
        assert img.getpixel((2, 1)) == (0xCC, 0xCC, 0xCC, 0xFF), 'center right pixel'
        assert img.getpixel((0, 2)) == (0xFF, 0xFF, 0xFF, 0xFF), 'bottom left pixel'
        assert img.getpixel((1, 2)) == (0xCC, 0xCC, 0xCC, 0xFF), 'bottom center pixel'
        assert img.getpixel((2, 2)) == (0xCC, 0xCC, 0xCC, 0xFF), 'bottom right pixel'
    
    def test4(self):

        out = Color(0x00, 0x00, 0x00, 0x00)
        out = out.blend(Color(0x99, 0x99, 0x99), self.halos)
        out = out.blend(self.streets)
        
        img = out.image()
        
        assert img.getpixel((0, 0)) == (0x99, 0x99, 0x99, 0xFF), 'top left pixel'
        assert img.getpixel((1, 0)) == (0x99, 0x99, 0x99, 0xFF), 'top center pixel'
        assert img.getpixel((2, 0)) == (0xFF, 0xFF, 0xFF, 0xFF), 'top right pixel'
        assert img.getpixel((0, 1)) == (0x99, 0x99, 0x99, 0xFF), 'center left pixel'
        assert img.getpixel((1, 1)) == (0xFF, 0xFF, 0xFF, 0xFF), 'middle pixel'
        assert img.getpixel((2, 1)) == (0x00, 0x00, 0x00, 0x00), 'center right pixel'
        assert img.getpixel((0, 2)) == (0xFF, 0xFF, 0xFF, 0xFF), 'bottom left pixel'
        assert img.getpixel((1, 2)) == (0x00, 0x00, 0x00, 0x00), 'bottom center pixel'
        assert img.getpixel((2, 2)) == (0x00, 0x00, 0x00, 0x00), 'bottom right pixel'

class AlphaTests(unittest.TestCase):
    """
    """
    def setUp(self):

        _808f = '\x80\x80\x80\xFF'
        _fff0, _fff8, _ffff = '\xFF\xFF\xFF\x00', '\xFF\xFF\xFF\x80', '\xFF\xFF\xFF\xFF'
        _0000, _0008, _000f = '\x00\x00\x00\x00', '\x00\x00\x00\x80', '\x00\x00\x00\xFF'
        
        # 50% gray all over
        self.gray = Layer(_str2img(_808f * 9))
            
        # nothing anywhere
        self.nothing = Layer(_str2img(_0000 * 9))
            
        # opaque horizontal gradient, black to white
        self.h_gradient = Layer(_str2img((_000f + _808f + _ffff) * 3))
            
        # transparent white at top to opaque white at bottom
        self.white_wipe = Layer(_str2img(_fff0 * 3 + _fff8 * 3 + _ffff * 3))
            
        # transparent black at top to opaque black at bottom
        self.black_wipe = Layer(_str2img(_0000 * 3 + _0008 * 3 + _000f * 3))
    
    def test0(self):
    
        out = self.gray
        out = out.blend(self.white_wipe)
        
        img = out.image()
        
        assert img.getpixel((0, 0)) == (0x80, 0x80, 0x80, 0xFF), 'top left pixel'
        assert img.getpixel((1, 0)) == (0x80, 0x80, 0x80, 0xFF), 'top center pixel'
        assert img.getpixel((2, 0)) == (0x80, 0x80, 0x80, 0xFF), 'top right pixel'
        assert img.getpixel((0, 1)) == (0xC0, 0xC0, 0xC0, 0xFF), 'center left pixel'
        assert img.getpixel((1, 1)) == (0xC0, 0xC0, 0xC0, 0xFF), 'middle pixel'
        assert img.getpixel((2, 1)) == (0xC0, 0xC0, 0xC0, 0xFF), 'center right pixel'
        assert img.getpixel((0, 2)) == (0xFF, 0xFF, 0xFF, 0xFF), 'bottom left pixel'
        assert img.getpixel((1, 2)) == (0xFF, 0xFF, 0xFF, 0xFF), 'bottom center pixel'
        assert img.getpixel((2, 2)) == (0xFF, 0xFF, 0xFF, 0xFF), 'bottom right pixel'
    
    def test1(self):
        
        out = self.gray
        out = out.blend(self.black_wipe)
        
        img = out.image()
        
        assert img.getpixel((0, 0)) == (0x80, 0x80, 0x80, 0xFF), 'top left pixel'
        assert img.getpixel((1, 0)) == (0x80, 0x80, 0x80, 0xFF), 'top center pixel'
        assert img.getpixel((2, 0)) == (0x80, 0x80, 0x80, 0xFF), 'top right pixel'
        assert img.getpixel((0, 1)) == (0x40, 0x40, 0x40, 0xFF), 'center left pixel'
        assert img.getpixel((1, 1)) == (0x40, 0x40, 0x40, 0xFF), 'middle pixel'
        assert img.getpixel((2, 1)) == (0x40, 0x40, 0x40, 0xFF), 'center right pixel'
        assert img.getpixel((0, 2)) == (0x00, 0x00, 0x00, 0xFF), 'bottom left pixel'
        assert img.getpixel((1, 2)) == (0x00, 0x00, 0x00, 0xFF), 'bottom center pixel'
        assert img.getpixel((2, 2)) == (0x00, 0x00, 0x00, 0xFF), 'bottom right pixel'
    
    def test2(self):
    
        out = self.gray
        out = out.blend(self.white_wipe, self.h_gradient)
        
        img = out.image()
        
        assert img.getpixel((0, 0)) == (0x80, 0x80, 0x80, 0xFF), 'top left pixel'
        assert img.getpixel((1, 0)) == (0x80, 0x80, 0x80, 0xFF), 'top center pixel'
        assert img.getpixel((2, 0)) == (0x80, 0x80, 0x80, 0xFF), 'top right pixel'
        assert img.getpixel((0, 1)) == (0x80, 0x80, 0x80, 0xFF), 'center left pixel'
        assert img.getpixel((1, 1)) == (0xA0, 0xA0, 0xA0, 0xFF), 'middle pixel'
        assert img.getpixel((2, 1)) == (0xC0, 0xC0, 0xC0, 0xFF), 'center right pixel'
        assert img.getpixel((0, 2)) == (0x80, 0x80, 0x80, 0xFF), 'bottom left pixel'
        assert img.getpixel((1, 2)) == (0xC0, 0xC0, 0xC0, 0xFF), 'bottom center pixel'
        assert img.getpixel((2, 2)) == (0xFF, 0xFF, 0xFF, 0xFF), 'bottom right pixel'
    
    def test3(self):
        
        out = self.gray
        out = out.blend(self.black_wipe, self.h_gradient)
        
        img = out.image()
        
        assert img.getpixel((0, 0)) == (0x80, 0x80, 0x80, 0xFF), 'top left pixel'
        assert img.getpixel((1, 0)) == (0x80, 0x80, 0x80, 0xFF), 'top center pixel'
        assert img.getpixel((2, 0)) == (0x80, 0x80, 0x80, 0xFF), 'top right pixel'
        assert img.getpixel((0, 1)) == (0x80, 0x80, 0x80, 0xFF), 'center left pixel'
        assert img.getpixel((1, 1)) == (0x60, 0x60, 0x60, 0xFF), 'middle pixel'
        assert img.getpixel((2, 1)) == (0x40, 0x40, 0x40, 0xFF), 'center right pixel'
        assert img.getpixel((0, 2)) == (0x80, 0x80, 0x80, 0xFF), 'bottom left pixel'
        assert img.getpixel((1, 2)) == (0x40, 0x40, 0x40, 0xFF), 'bottom center pixel'
        assert img.getpixel((2, 2)) == (0x00, 0x00, 0x00, 0xFF), 'bottom right pixel'
    
    def test4(self):
        
        out = self.nothing
        out = out.blend(self.white_wipe)
        
        img = out.image()
        
        assert img.getpixel((0, 0)) == (0x00, 0x00, 0x00, 0x00), 'top left pixel'
        assert img.getpixel((1, 0)) == (0x00, 0x00, 0x00, 0x00), 'top center pixel'
        assert img.getpixel((2, 0)) == (0x00, 0x00, 0x00, 0x00), 'top right pixel'
        assert img.getpixel((0, 1)) == (0xFF, 0xFF, 0xFF, 0x80), 'center left pixel'
        assert img.getpixel((1, 1)) == (0xFF, 0xFF, 0xFF, 0x80), 'middle pixel'
        assert img.getpixel((2, 1)) == (0xFF, 0xFF, 0xFF, 0x80), 'center right pixel'
        assert img.getpixel((0, 2)) == (0xFF, 0xFF, 0xFF, 0xFF), 'bottom left pixel'
        assert img.getpixel((1, 2)) == (0xFF, 0xFF, 0xFF, 0xFF), 'bottom center pixel'
        assert img.getpixel((2, 2)) == (0xFF, 0xFF, 0xFF, 0xFF), 'bottom right pixel'

class BlendTests(unittest.TestCase):
    """
    """
    def setUp(self):
    
        _808f = '\x80\x80\x80\xFF'
        _ffff = '\xFF\xFF\xFF\xFF'
        _000f = '\x00\x00\x00\xFF'
        
        # opaque horizontal gradient, black to white
        self.h_gradient = Layer(_str2img((_000f + _808f + _ffff) * 3))
            
        # opaque vertical gradient, black to white
        self.v_gradient = Layer(_str2img(_000f * 3 + _808f * 3 + _ffff * 3))
    
    def test0(self):
        
        out = self.h_gradient
        out = out.blend(self.v_gradient, mode='screen')
        
        img = out.image()
        
        assert img.getpixel((0, 0)) == (0x00, 0x00, 0x00, 0xFF), 'top left pixel'
        assert img.getpixel((1, 0)) == (0x80, 0x80, 0x80, 0xFF), 'top center pixel'
        assert img.getpixel((2, 0)) == (0xFF, 0xFF, 0xFF, 0xFF), 'top right pixel'
        assert img.getpixel((0, 1)) == (0x80, 0x80, 0x80, 0xFF), 'center left pixel'
        assert img.getpixel((1, 1)) == (0xC0, 0xC0, 0xC0, 0xFF), 'middle pixel'
        assert img.getpixel((2, 1)) == (0xFF, 0xFF, 0xFF, 0xFF), 'center right pixel'
        assert img.getpixel((0, 2)) == (0xFF, 0xFF, 0xFF, 0xFF), 'bottom left pixel'
        assert img.getpixel((1, 2)) == (0xFF, 0xFF, 0xFF, 0xFF), 'bottom center pixel'
        assert img.getpixel((2, 2)) == (0xFF, 0xFF, 0xFF, 0xFF), 'bottom right pixel'
    
    def test1(self):
        
        out = self.h_gradient
        out = out.blend(self.v_gradient, mode='multiply')
        
        img = out.image()
        
        assert img.getpixel((0, 0)) == (0x00, 0x00, 0x00, 0xFF), 'top left pixel'
        assert img.getpixel((1, 0)) == (0x00, 0x00, 0x00, 0xFF), 'top center pixel'
        assert img.getpixel((2, 0)) == (0x00, 0x00, 0x00, 0xFF), 'top right pixel'
        assert img.getpixel((0, 1)) == (0x00, 0x00, 0x00, 0xFF), 'center left pixel'
        assert img.getpixel((1, 1)) == (0x40, 0x40, 0x40, 0xFF), 'middle pixel'
        assert img.getpixel((2, 1)) == (0x80, 0x80, 0x80, 0xFF), 'center right pixel'
        assert img.getpixel((0, 2)) == (0x00, 0x00, 0x00, 0xFF), 'bottom left pixel'
        assert img.getpixel((1, 2)) == (0x80, 0x80, 0x80, 0xFF), 'bottom center pixel'
        assert img.getpixel((2, 2)) == (0xFF, 0xFF, 0xFF, 0xFF), 'bottom right pixel'
    
    def test2(self):
        
        out = self.h_gradient
        out = out.blend(self.v_gradient, mode='linear light')
        
        img = out.image()
        
        assert img.getpixel((0, 0)) == (0x00, 0x00, 0x00, 0xFF), 'top left pixel'
        assert img.getpixel((1, 0)) == (0x00, 0x00, 0x00, 0xFF), 'top center pixel'
        assert img.getpixel((2, 0)) == (0x00, 0x00, 0x00, 0xFF), 'top right pixel'
        assert img.getpixel((0, 1)) == (0x01, 0x01, 0x01, 0xFF), 'center left pixel'
        assert img.getpixel((1, 1)) == (0x81, 0x81, 0x81, 0xFF), 'middle pixel'
        assert img.getpixel((2, 1)) == (0xFF, 0xFF, 0xFF, 0xFF), 'center right pixel'
        assert img.getpixel((0, 2)) == (0xFF, 0xFF, 0xFF, 0xFF), 'bottom left pixel'
        assert img.getpixel((1, 2)) == (0xFF, 0xFF, 0xFF, 0xFF), 'bottom center pixel'
        assert img.getpixel((2, 2)) == (0xFF, 0xFF, 0xFF, 0xFF), 'bottom right pixel'
    
    def test3(self):
        
        out = self.h_gradient
        out = out.blend(self.v_gradient, mode='hard light')
        
        img = out.image()
        
        assert img.getpixel((0, 0)) == (0x00, 0x00, 0x00, 0xFF), 'top left pixel'
        assert img.getpixel((1, 0)) == (0x00, 0x00, 0x00, 0xFF), 'top center pixel'
        assert img.getpixel((2, 0)) == (0x00, 0x00, 0x00, 0xFF), 'top right pixel'
        assert img.getpixel((0, 1)) == (0x01, 0x01, 0x01, 0xFF), 'center left pixel'
        assert img.getpixel((1, 1)) == (0x80, 0x80, 0x80, 0xFF), 'middle pixel'
        assert img.getpixel((2, 1)) == (0xFF, 0xFF, 0xFF, 0xFF), 'center right pixel'
        assert img.getpixel((0, 2)) == (0xFF, 0xFF, 0xFF, 0xFF), 'bottom left pixel'
        assert img.getpixel((1, 2)) == (0xFF, 0xFF, 0xFF, 0xFF), 'bottom center pixel'
        assert img.getpixel((2, 2)) == (0xFF, 0xFF, 0xFF, 0xFF), 'bottom right pixel'
    
    def test4(self):
        
        out = self.h_gradient
        out = out.blend(self.v_gradient, opacity=0.5)
        
        img = out.image()
        
        assert img.getpixel((0, 0)) == (0x00, 0x00, 0x00, 0xFF), 'top left pixel'
        assert img.getpixel((1, 0)) == (0x40, 0x40, 0x40, 0xFF), 'top center pixel'
        assert img.getpixel((2, 0)) == (0x80, 0x80, 0x80, 0xFF), 'top right pixel'
        assert img.getpixel((0, 1)) == (0x40, 0x40, 0x40, 0xFF), 'center left pixel'
        assert img.getpixel((1, 1)) == (0x80, 0x80, 0x80, 0xFF), 'middle pixel'
        assert img.getpixel((2, 1)) == (0xC0, 0xC0, 0xC0, 0xFF), 'center right pixel'
        assert img.getpixel((0, 2)) == (0x80, 0x80, 0x80, 0xFF), 'bottom left pixel'
        assert img.getpixel((1, 2)) == (0xC0, 0xC0, 0xC0, 0xFF), 'bottom center pixel'
        assert img.getpixel((2, 2)) == (0xFF, 0xFF, 0xFF, 0xFF), 'bottom right pixel'

if __name__ == '__main__':
    unittest.main()
