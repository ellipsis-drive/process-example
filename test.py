import ellipsisAI as ai
import ellipsis as el
import numpy as np

import sys

<<<<<<< HEAD
#el.apiManager.baseUrl = 'https://api.esa.ellipsis-drive.com/v3'

=======
el.apiManager.baseUrl = 'https://api.esa.ellipsis-drive.com/v3'
ai.url = 'https://api.esa.ellipsis-drive.com/v3'
>>>>>>> 7c2be7897787b53c0d3fdfb6345a549515d82de1

pathId = 'a479869c-caa6-4b95-acb7-0ce1cfe71828'
timestampId = "Not available, activate first"
targetPathId = "19b30a1c-2ea3-49ca-a859-2ff3bd731abe"



pathId = sys.argv[1]
<<<<<<< HEAD
timestampId =  int(sys.argv[2])
targetPathId = int(sys.argv[3])

=======
timestampId =  sys.argv[2]
targetPathId = sys.argv[3]
try:
    token = sys.argvd[4]
except:
    token = None
>>>>>>> 7c2be7897787b53c0d3fdfb6345a549515d82de1


token = el.auth()

#retrieve the zoom and bounds of the capture you wish to classify
classificationZoom = ai.getReccomendedClassificationZoom(pathId = pathId, timestampId = timestampId, token = token)
bounds = el.path.raster.timestamp.getBounds(pathId, timestampId, token)



#we create a dummy model. We use the identity function mapping an image to itself. We use the getTleData function to retirve the image for the given input tile ofthe model.
def model(tile):
    result = el.getTileData(pathId = pathId, timestampId = timestampId, tile = tile, token  = token)
    if result['status'] == 204:
        output =  np.zeros((1,256,256))
        output[:,:,:] = -1
    else:
        r = result['result']

        output = (r[7,:,:] -r[3,:,:]) / (r[7,:,:] + r[3,:,:])
    return(output)


#apply the model on the given bounds on the given zoomlevel
el.applyModel(model = model, bounds = bounds, targetPathId = targetPathId, classificationZoom = classificationZoom, token=token)

