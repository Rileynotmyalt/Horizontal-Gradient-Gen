from gens.base_gen import BaseGen
from ops import chooseColor
from PIL import Image

class Reverse_Lin(BaseGen):
  def __init__(self):
    description="y=mx+b\n | Given: <y> <x> <b>"
    params=["Starting Color","Ending Color"]
    super().__init__(description,params)

  def handle(self,adv):
    while 1:
      try:
        im=Image.new("RGB",(int(input('Width:  ')),int(input('Height: '))))
        pix=im.load()
        break
      except ValueError:
        print('Unexpected Value Try Again\n')
    scol=list( chooseColor(input("\nStarting Color: ")) )
    ecol=list(   chooseColor(input("Ending Color:   ")) ) 
    print('\nGenerating Image...')

    mcol=[]
    col=[]

    for i in range(len(scol)):
      mcol.append( (ecol[i]-scol[i])/(im.width-1) )

    for j in range(im.height):
      for i in range(im.width):
        if j==0:
          col=[]
          for c in range(len(scol)):
            col.append( int( mcol[c]*i + scol[c] ) )
          pix[i,0]=tuple(col)
        else:
          pix[i,j]=pix[i,0]
    
    im.save('Image.png')
    print("\nImage Generated")