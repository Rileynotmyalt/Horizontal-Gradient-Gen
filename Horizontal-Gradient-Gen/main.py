adv=False

print('Advanced? (y/n)')
if input().lower() == 'y':
  adv=True

from gens.base_gen import BaseGen
from gens import *
generators= {g.__name__.lower(): g() for g in BaseGen.__subclasses__()}

for i in range(len(BaseGen.__subclasses__())):
  print(f'[{i+1}]{BaseGen.__subclasses__()[i].__name__}{BaseGen.__subclasses__()[i]().description if adv else ""}')

while 1:
  try:
    choice=int(input())
    BaseGen.__subclasses__()[choice-1]
    break
  except ValueError:
    print("Invalid Input Try Again")
  except IndexError:
    print('Gen Does Not Exist Try Again')

BaseGen.__subclasses__()[choice-1].handle(BaseGen.__subclasses__()[choice-1],adv)