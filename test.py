import ellipsisAI as ai
import ellipsis as el
import numpy as np

import sys


pathId = '8a502f6b-e599-48ac-85ea-875a87bee2f3'
timestampId = "69991f4b-871a-4bc5-8bd2-b3902c8b4329"
targetPathId = "c75ffc02-ff41-4c46-915c-4705e58d2386"
token = "epat_MCGw1tytB0SIIpAwyB6J8ZCNSxJHAhazsOvPj8XdHCzts84MeSeCi3qFdVmwLYgB"


el.apiManager.baseUrl = 'https://api.esa.ellipsis-drive.com/v3'
ai.url = 'https://api.esa.ellipsis-drive.com/v3'
pathId = sys.argv[1]
timestampId =  sys.argv[2]
targetPathId = sys.argv[3]
token = sys.argv[4]



#retrieve the zoom and bounds of the capture you wish to classify
classificationZoom = ai.getReccomendedClassificationZoom(pathId = pathId, timestampId = timestampId, token = token)
bounds = el.path.raster.timestamp.getBounds(pathId, timestampId, token)


#we create a dummy model. We use the identity function mapping an image to itself. We use the getTleData function to retirve the image for the given input tile ofthe model.
def model(tile):
    result = ai.getTileData(pathId = pathId, timestampId = timestampId, tile = tile, token  = token)
    if result['status'] == 204:
        output =  np.zeros((1,256,256))
        output[:,:,:] = -1
    else:
        r = result['result']

        output = (r[7,:,:] -r[3,:,:]) / (r[7,:,:] + r[3,:,:])
    return(output)


#apply the model on the given bounds on the given zoomlevel
ai.applyModel(model = model, bounds = bounds, targetPathId = targetPathId, classificationZoom = classificationZoom, token=token)

