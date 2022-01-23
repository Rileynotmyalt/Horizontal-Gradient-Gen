from gens.base_gen import BaseGen
from ops import chooseColor,choosePoint
from PIL import Image
import numpy

class Reverse_Quad(BaseGen):
  def __init__(self):
    description='Advanced: advanced third point input\n | y=ax^2+bx+c\n | Given: <x> <y> <c>'
    params=["Starting Color","Ending Color","Third Color","Point"]
    super().__init__(description,params)

  def handle(self,adv):
    while 1:
      try:
        im=Image.new("RGB",(int(input('Width:  ')),int(input('Height: '))))
        pix=im.load()
        break
      except ValueError:
        print('Unexpected Value Try Again\n')
    scol=list(chooseColor(input("\nStarting Color: ")) )
    ecol=list(  chooseColor(input("Ending Color:   ")) )
    tcol=list(  chooseColor(input('Third Color:    ')) )
    tpnt=[]
    if adv:
      tpnt=list(choosePoint(input('Point(10,10,10):'),im))
    else:
      while 1:
        if 1:
          st=input('Point(100):')
          if st == '':
            [tpnt.append(int(im.width/2)) for i in range(3)]
            break
          else:
            [tpnt.append(int(st)) for i in range(3)]
            break
        '''except ValueError:
          print('Unexpected Value Try Again')'''
            
    print('\nGenerating Image...')

    acol=[]
    bcol=[]

    for i in range(len(scol)):
      ac,bc= numpy.linalg.inv( numpy.array([[(im.width-1)**2,(im.width-1)],[tpnt[i]**2,tpnt[i]]]) ) @ numpy.array([ecol[i]-scol[i],tcol[i]-scol[i]])
      acol.append(ac)
      bcol.append(bc)
    
    for j in range(im.height):
      for i in range(im.width):
        if j==0:
          col=[]
          for c in range(len(scol)):
            col.append( int(acol[c]*(i**2)+(bcol[c]*i)+scol[c] ) )
          pix[i,0]=tuple(col)
        else:
          pix[i,j]=pix[i,0]
    
    im.save('Image.png')
    print('\nImage Generated')   