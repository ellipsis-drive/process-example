import ellipsis as el
from io import BytesIO
import sys

#parameter indicating the raster layer to analyse
pathId = sys.argv[1]
#parameter indicating the extent of the area of interest
extent = sys.argv[2]
#parameter indicating in which folder to add the resulting raster
folderId = sys.argv[3]


info = el.path.get(pathId = pathId)
timestamp = info['raster']['timestamps'][0]
timestampId = timestamp['id']

r = el.path.raster.timestamp.getRaster(pathId = pathId, timestampId=timestampId, extent = extent, epsg = 4326)['raster']
ndci = r[4,:,:] - r[3,:,:]/(r[4,:,:] + r[3,:,:])

layerId = el.path.raster.add(name = 'Chlorophyl', token = token, folderId=folderId)['id']
timestampId = el.path.raster.timestamp.add(pathId = layerId, token = token)['id']

memfile = el.util.saveRaster(r=r, epsg = 4326,targetFile=BytesIO(), extent = extent)

el.path.raster.timestamp.file.add(pathId=layerId, timestampId=timestampId, token = token,memFile=memfile, fileFormat='tif', name ='out.tif')

