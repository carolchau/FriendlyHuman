from clarifai import rest
from PIL import Image
import requests
from StringIO import StringIO
import io
from pprint import pprint
import pdb

api = rest.ApiClient(client_id='secret', client_secret='secret')

mattz_url = ['http://cliqueimg.com/cache/posts/171539/tk-young-entrepreneurs-share-their-1-career-tip-1518659.640x0c.jpg', 'https://media.licdn.com/mpr/mpr/shrinknp_200_200/p/1/000/120/0b1/301ad2d.jpg', 'https://pbs.twimg.com/profile_images/614168515839434752/8pyJYNtl.jpg', 'https://www.clarifai.com/static/images/team/matthew.jpg','http://bigdata-madesimple.com/wp-content/uploads/2015/09/Matthew-Zeiler.jpg', 'http://vlg.cs.nyu.edu/uploads/People/matthew.jpg', 'http://1u88jj3r4db2x4txp44yqfj1.wpengine.netdna-cdn.com/wp-content/uploads/2015/03/clarifai.jpg', 'https://s3.amazonaws.com/re-work-production/avatars/87/original.png?1446178599', 'http://www.enews.engineering.utoronto.ca/june10_09/images/grad_zeiler_sm.jpg','http://i2.cdn.turner.com/money/dam/assets/150610153029-upstarts-clarifai-1100x619.jpg']



mattz1 = rest.Image(url=mattz_url[0],
             labels=['matthew zeiler', 'clarifai', 'machine learning', 'artificial intelligence', 'deep learning', 'computer vision', 'human', 'male'], not_labels=["female"])
mattz2 = rest.Image(url=mattz_url[1],
             labels=['matthew zeiler', 'clarifai', 'machine learning', 'artificial intelligence', 'deep learning', 'computer vision', 'human', 'male'], not_labels=["female"])
mattz3 = rest.Image(url=mattz_url[2], labels=['matthew zeiler', 'clarifai', 'machine learning', 'artificial intelligence', 'deep learning', 'computer vision', 'human', 'male'], not_labels=["female"])
mattz4 = rest.Image(url=mattz_url[3], labels=['matthew zeiler', 'clarifai', 'machine learning', 'artificial intelligence', 'deep learning', 'computer vision', 'human', 'male'], not_labels=["female"])
mattz5 = rest.Image(url=mattz_url[4], labels=['matthew zeiler', 'clarifai', 'machine learning', 'artificial intelligence', 'deep learning', 'computer vision', 'human', 'male'], not_labels=["female"])
mattz6 = rest.Image(url=mattz_url[5], labels=['matthew zeiler', 'clarifai', 'machine learning', 'artificial intelligence', 'deep learning', 'computer vision', 'human', 'male'], not_labels=["female"])
mattz7 = rest.Image(url=mattz_url[6], labels=['matthew zeiler', 'clarifai', 'machine learning', 'artificial intelligence', 'deep learning', 'computer vision', 'human', 'male'], not_labels=["female"])
mattz8 = rest.Image(url=mattz_url[7], labels=['matthew zeiler', 'clarifai', 'machine learning', 'artificial intelligence', 'deep learning', 'computer vision', 'human', 'male'], not_labels=["female"])
mattz9 = rest.Image(url=mattz_url[8], labels=['matthew zeiler', 'clarifai', 'machine learning', 'artificial intelligence', 'deep learning', 'computer vision', 'human', 'male'], not_labels=["female"])
mattz10 = rest.Image(url=mattz_url[9], labels=['matthew zeiler', 'clarifai', 'machine learning', 'artificial intelligence', 'deep learning', 'computer vision', 'human', 'male'], not_labels=["female"])

mattz_arr = [mattz1, mattz2, mattz3, mattz4, mattz5, mattz6, mattz7, mattz8, mattz9, mattz10]


davef_url = ['https://www.bupipedream.com/wp-content/uploads/2013/02/9-N-JH-TEDx-David-Ferrucci-WEB-1024x682.jpg', 'http://www-07.ibm.com/innovation/in/watson/images/img-overview-david-ferrucci.jpg', 'http://www-03.ibm.com/innovation/us/watson/images/what-is-watson/research-team/img-video-david-ferruci.jpg', 'http://curation.cs.manchester.ac.uk/Turing100/www.turing100.manchester.ac.uk/files/gallery-invited/speakers/12.jpg', 'http://www.pmwired.com/wp-content/uploads/2012/02/ferrucci.jpg', 'http://www.computerhope.com/people/pictures/david_ferrucci.jpg', 'https://www.singularityweblog.com/wp-content/uploads/2014/01/David-Ferrucci-271x3001.jpg', 'http://www.cccblog.org/wp-content/uploads/2012/04/daveferrucci.jpg', 'http://www.compustory.com/_Media/david-ferrucci_med_hr.jpeg', 'https://media.npr.org/assets/img/2011/02/11/dave-ferrucci_wide-d19cb997478416b5cbeef88c93f6749784a5814a.jpg?s=1400']

davef1 = rest.Image(url=davef_url[0],labels=['dave ferrucci', 'IBM', 'researcher', 'human', 'male', 'artificial intelligence'], not_labels=["female"])
davef2 = rest.Image(url=davef_url[1],labels=['dave ferrucci', 'IBM', 'researcher', 'human', 'male', 'artificial intelligence'] , not_labels=["female"])
davef3 = rest.Image(url=davef_url[2],labels=['dave ferrucci', 'IBM', 'researcher', 'human', 'male', 'artificial intelligence'] , not_labels=["female"])
davef4 = rest.Image(url=davef_url[3],labels=['dave ferrucci', 'IBM', 'researcher', 'human', 'male', 'artificial intelligence'] , not_labels=["female"])
davef5 = rest.Image(url=davef_url[4],labels=['dave ferrucci', 'IBM', 'researcher', 'human', 'male', 'artificial intelligence'] , not_labels=["female"])
davef6 = rest.Image(url=davef_url[5],labels=['dave ferrucci', 'IBM', 'researcher', 'human', 'male', 'artificial intelligence'] , not_labels=["female"])
davef7 = rest.Image(url=davef_url[6],labels=['dave ferrucci', 'IBM', 'researcher', 'human', 'male', 'artificial intelligence'] , not_labels=["female"])
davef8 = rest.Image(url=davef_url[7],labels=['dave ferrucci', 'IBM', 'researcher', 'human', 'male', 'artificial intelligence'] , not_labels=["female"])
davef9 = rest.Image(url=davef_url[8],labels=['dave ferrucci', 'IBM', 'researcher', 'human', 'male', 'artificial intelligence'] , not_labels=["female"])
davef10 = rest.Image(url=davef_url[9],labels=['dave ferrucci', 'IBM', 'researcher', 'human', 'male', 'artificial intelligence'] , not_labels=["female"])

davef_arr = [davef1, davef2, davef3, davef4, davef5, davef6, davef7, davef8, davef9, davef10]

def convert_bbox(w, h, pos): #bbox = bounding box
    bottomRow = int(pos['bottomRow'] * h)
    leftCol = int(pos['leftCol'] * w)
    rightCol = int(pos['rightCol'] * w)
    topRow = int(pos['topRow'] * h)
    
    print bottomRow, leftCol, rightCol, topRow
    
    return (leftCol, topRow, rightCol, bottomRow)

for i in range(len(mattz_url)):
    response = requests.get(mattz_url[i])
    
    try:
        pil_img = Image.open(StringIO(response.content))
        img = StringIO(response.content)
    except Exception as e:
        continue
        
    width, height = pil_img.size
    #print 'dimensions: ', width, " x ", height
    
    #outputs = api.PredictFaces([ mattz_arr[i] ])
    outputs = api.predictFaces([mattz_arr[i]])
    if len(outputs['outputs'][0]['data']['tags']) == 0:
        continue
        
    dimensions = outputs['outputs'][0]['data']['tags'][0]['detection']
    
    imgCrop = pil_img.crop(convert_bbox(width, height, dimensions))
    
    imgByteArr = io.BytesIO()
    imgCrop.save(imgByteArr, format='PNG')
    
    temp = rest.Image(file_obj=imgByteArr,labels=['matthew zeiler', 'clarifai', 'machine learning', 'artificial intelligence', 'deep learning', 'computer vision', 'human', 'male'], not_labels=["female"] )
    api.addInputs([temp]) #add input here
    
for i in range(len(davef_url)):
    response = requests.get(davef_url[i])
    
    try:
        pil_img = Image.open(StringIO(response.content))
        img = StringIO(response.content)
    except Exception as e:
        continue
        
    width, height = pil_img.size
    #print 'dimensions: ', width, " x ", height
    
    #outputs = api.PredictFaces([ mattz_arr[i] ])
    outputs = api.predictFaces([davef_arr[i]])
    if len(outputs['outputs'][0]['data']['tags']) == 0:
        continue
        
    dimensions = outputs['outputs'][0]['data']['tags'][0]['detection']
    
    imgCrop = pil_img.crop(convert_bbox(width, height, dimensions))
    
    imgByteArr = io.BytesIO()
    imgCrop.save(imgByteArr, format='PNG')
    
    temp = rest.Image(file_obj=imgByteArr,labels=['dave ferrucci', 'IBM', 'researcher', 'human', 'male', 'artificial intelligence'] , not_labels=["female"])
    api.addInputs([temp]) #add input here
    

    


res = api.createModel(model_name='targethumans', concept_ids=['dave ferrucci', 'matthew zeiler'])
#print 'res: ', res
model_id = res['model']['id']
#print model_id

api.trainModel(model_id=model_id)

murl = open("matthew.jpg").read()

try:
    pil_img = Image.open(StringIO(murl))
    img = StringIO(response.content)
except Exception as e:
    pass

width, height = pil_img.size

whatever = rest.Image(file_obj= open("matthew.jpg"))

outputs = api.predictFaces([whatever])

dimensions = outputs['outputs'][0]['data']['tags'][0]['detection']

imgCrop = pil_img.crop(convert_bbox(width, height, dimensions))

imgCrop.save("temp.png", format='PNG')

res = api.predictModel(model_id="secret", objs=[rest.Image(file_obj=open("temp.png"))] )
pprint(res)
