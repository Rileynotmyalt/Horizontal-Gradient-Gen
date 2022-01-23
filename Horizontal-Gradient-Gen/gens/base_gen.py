
class BaseGen:
  def __init__(self,description,params):
    self.name=type(self).__name__
    self.params=params
    
    desc= f''
    if self.params:
      desc += " "+" ".join(f"<{p}>" for p in params)
    if description != None:
      desc += f'\n | {description}'
    
    self.description=desc
  
  def handle(self,adv):
    raise NotImplementedError