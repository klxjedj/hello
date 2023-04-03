import json
data={}
viewData=[]
compData=[]

for compId in range(1,25):
    comp={
        "compId":compId,
        "compColorOptions":[],
        "defaultColorChoice":'',
        "compIconImgName":'comp{}.png'.format(compId)
    }
    compData.append(comp)


for viewIndex in range(1,8):
    compList=[]
    for compId in range(1,25):
        compViewData={
            "viewIndex":viewIndex,
            "compId":compId,
            "defautChoice":'',
            "imgFileName":"v{}_sg{}.png".format(viewIndex,compId)
        }
        compList.append(compViewData)
    viewData.append(compList)
data['viewData']=viewData
data['compData']=compData

json.dump(data,open('nikeShoe.json','w'))