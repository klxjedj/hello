import os
import re
from PIL import Image
import collections
import json
imgLocation={}
imgValue={}
imgAlpha={}

imgList=[i for i in os.listdir() if i.endswith('.png')]

for imgFilename in imgList:
    im=Image.open(imgFilename)
    
    [(viewIndex,compIndex)]=(re.findall(r'v(\d).sg(\d*).*',imgFilename))
    if not viewIndex in imgLocation:
        imgLocation[viewIndex]={}
    if not viewIndex in imgValue:
        imgValue[viewIndex]={}
    if not viewIndex in imgAlpha:
        imgAlpha[viewIndex]={}
    if not compIndex in imgLocation[viewIndex]:
        imgLocation[viewIndex][compIndex]=[]
    if not compIndex in imgValue[viewIndex]:
        imgValue[viewIndex][compIndex]=[]
    if not compIndex in imgAlpha[viewIndex]:
        imgAlpha[viewIndex][compIndex]=[]
    inside=false
    for (loc,data) in enumerate(im.getdata()):
        if data[0]!=255:
            if inside==false:
                imgLocation[viewIndex][compIndex].append(loc)
                inside=true
            imgValue[viewIndex][compIndex].append(data[0])
            imgAlpha[viewIndex][compIndex].append(data[3])
        else:
            if inside==true:
                imgLocation[viewIndex][compIndex].append(loc)
                inside=false



with open('imgLocation.json','w') as f:
    json.dump(imgLocation,f,indent='')
with open('imgValue.json','w') as f:
    json.dump(imgValue,f,indent='')
with open('imgAlpha.json','w') as f:
    json.dump(imgAlpha,f,indent='')


