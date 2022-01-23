from gens.base_gen import BaseGen

class Test:#(BaseGen):
  def __init__(self):
    description="this is a test"
    params=['de']
    super().__init__(description,params)
  
  def handle(self,adv):
    print(f'{self.__name__} says {input()}')