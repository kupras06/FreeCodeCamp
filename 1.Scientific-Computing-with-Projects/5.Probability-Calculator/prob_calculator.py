import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**kwargs):
    self.contents = []
    for i , j in kwargs.items():
      temp = [i]*j
      self.contents.extend(temp)
    #print(self.contents)
  def draw(self,trials):
    cur_content = self.contents
    if trials>=len(self.contents):
      return self.contents
    sample = []
    for i in range(trials):
      limit = len(cur_content)
      idx = random.randrange(limit)
      sample.append(cur_content[idx])
      cur_content = cur_content[:idx]+cur_content[idx+1:]
    self.contents = cur_content
    return sample

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments):
    values = copy.copy(hat)
    sample = values.draw(num_balls_drawn)
    flag = True
    for key in expected_balls:
      if sample.count(key) < expected_balls[key]:
        flag = False
        break
    if flag:  count+=1
      
  return count/num_experiments

