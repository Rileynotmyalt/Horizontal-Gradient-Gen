import random

nl="\n"

colorsDict = {
  'black':(0,0,0),
  'white':(255,255,255),
  'red':(255,0,0),
  'brown':(153,102,51),
  'gold':(204,153,51),
  'orange':(255,165,0),
  'peach':(255,153,102),
  'yellow':(255,255,0),
  'green':(0,255,0),
  'turquoise':(64,224,208),
  'aqua':(0,255,255),
  'aquamarine':(127,255,212),
  'teal':(0,128,128),
  'blue':(0,0,255),
  'violet':(204,102,204),
  'purple':(127,0,255),
  'pink':(255,153,204)
}

def chooseColor(choice):
  try:
    if True in [char.isdigit() for char in choice]:
      choice=choice.replace('(','')
      choice=choice.replace(')','')
      if ',' in choice:
        choice=choice.replace(' ','')
        sr,sg,sb=choice.split(',',3)
      else:
        sr,sg,sb=choice.split(' ',3)
      srgb=[int(sr),int(sg),int(sb)]
      for i in srgb:
        if i>255:
          i=255
        elif i<0:
          i=0
      sr,sg,sb=srgb[0],srgb[1],srgb[2]

    elif choice.lower() in colorsDict:
      sr,sg,sb=colorsDict[choice.lower()]
    
    elif choice=='':
      sr,sg,sb=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    else:
      raise

  except:
    print('Invalid input, try \'red\' or \'255,0,0\'')
    sr,sg,sb=chooseColor(input('Pick a color: '))
  
  return(sr,sg,sb)

def choosePoint(choice,im):
  if True in [char.isdigit() for char in choice]:
    choice=choice.replace('(','')
    choice=choice.replace(')','')
    if ',' in choice:
      choice=choice.replace(' ','')
      sr,sg,sb=choice.split(',',3)
    else:
      sr,sg,sb=choice.split(' ',3)
  
  elif choice=='':
    sr,sg,sb=(random.randint(0,im.width),random.randint(0,im.width),random.randint(0,im.width))

  else:
    print('Invalid input, try \'red\' or \'255,0,0\'')
    sr,sg,sb=chooseColor(input('Pick a color: '))
  
  return(int(sr),int(sg),int(sb))

#ask for 2 inputs
#if one input ==''
  #Fwd
  #ask for equation
#else:
  #Reverse
  #Lin or Quad?

  #if Quad
    #3rd point
  #else:
    #lin

#eval('1+2')
#https://stackoverflow.com/a/9686094