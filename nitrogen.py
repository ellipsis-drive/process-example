import ellipsis as el
import sys

#parameter indicating the deposit raster layer
pathId = sys.argv[1]
#parameter indicating the timestamp in the deposit layer to use
timestampId = sys.argv[2]
#parameter indicating the extent of interest
extent = sys.argv[3]




sh = el.path.vector.timestamp.getFeaturesByExtent(pathId=pathId, timestampId=timestampId,  extent = {'xMin':-180, 'xMax':180,'yMin':-85, 'yMax':85})['result']


for g in sh['geometry'].values:
    g = g.simplify(tolerance=1)
    result = el.path.raster.timestamp.analyse(pathId = pathId, timestampIds=[timestampId], geometry=g)
    print(result[0]['result'][0]['statistics']['percentiles'])





