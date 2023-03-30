class Rectangle:
    def __init__(self, x, y, h, w):
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)
    
    def __str__(self):
        """ this function is intended to find the parameters in a string
        """
        
        return F"x:{self.x} y:{self.y} height:{self.height} width:{self.width}"