class Rectangle:
  def __init__(self,wid,hht):
    self.width = wid
    self.height = hht
  def set_width(self,wid):
    self.width = wid
  def set_height(self,hht):
    self.height = hht
  def get_area(self):
    return (self.width*self.height)
  def get_perimeter(self):
    return ((2 * self.width + 2 * self.height))
  def get_diagonal(self):
    return  ((self.width ** 2 + self.height ** 2) ** .5)
  def get_picture(self):
    if self.width>50 or self.height>50:
      return "Too big for picture."
    ans = '*'*self.width+'\n'
    ans = ans*self.height
    return ans
  def __repr__(self):
    return "Rectangle(width={}, height={})".format(self.width,self.height)
  def get_amount_inside(self,Shape):
     s1 = self.width // Shape.width
     s2 =  self.height//Shape.height 
     return s1*s2


class Square(Rectangle):
  def __init__(self,wid):
    super().__init__(wid,wid)
  def __repr__(self):
    return "Square(side={})".format(self.width)
  def set_width(self,wid):
    self.width = wid
    self.height = wid
  def set_height(self,hht):
    self.height = hht
    self.width = hht
  def set_side(self,hht):
    self.height = hht
    self.width = hht