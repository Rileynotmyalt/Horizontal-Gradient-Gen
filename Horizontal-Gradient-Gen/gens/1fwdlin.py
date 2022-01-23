from gens.base_gen import BaseGen
from ops import chooseColor
from PIL import Image

class Forward_Lin(BaseGen):
  def __init__(self):
    description="Advanced: slopes for each channel\n | y=mx+b\n | Given: <m> <b>"
    params=["Starting Color","Slope"]
    super().__init__(description,params)
  
  def handle(self,adv):
    while 1:
      try:
        im=Image.new("RGB",(int(input('Width:  ')),int(input('Height: '))))
        pix=im.load()
        break
      except ValueError:
        print('Unexpected Value Try Again\n')
    scol=list(chooseColor(input('Starting Color: ')))

    mcol=[]
    while 1:
      try:
        if adv:
          mcol=[float(input('R Slope: ')),
                float(input('G Slope: ')),
                float(input('B Slope: '))]
        else:
          sm=float(input('Slope: '))
          [mcol.append(sm) for i in range(3)]
        break
      except ValueError:
        print('Unexpected Value Try Again')
      
    
    print('\nGenerating Image...')

    for j in range(im.height):
      for i in range(im.width):
        if j==0:
          col=[]
          for c in range(len(scol)):
            col.append( int(mcol[c]*i + scol[c]) )
          pix[i,0]=tuple(col)
        else:
          pix[i,j]=pix[i,0]
      
    im.save('Image.png')
    print('\nImage Generated')