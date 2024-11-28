import ellipsis as el
import sys

#parameter indicating the raster layer with a time series of NDVI's
pathId = sys.argv[1]
#parameter indicating the layer with plots of interest
plot_pathId = sys.argv[2]
#parameter with the extent of interest
extent = sys.argv[2]


info = el.path.get(pathId = pathId)



plot_info = el.path.get(pathId = plot_pathId)
plot_timestampId = plot_info['vector']['timestamps'][0]['id']

sh = el.path.vector.timestamp.getFeaturesByExtent(pathId = plot_pathId, timestampId=plot_timestampId, extent = extent)['result']

for g in sh['geometry'].values:

    timestampIds = [t['id'] for t in info['raster']['timestamps']]

    timeSeries = el.path.raster.timestamp.analyse(pathId=pathId, timestampIds=timestampIds, geometry=g)

    values = [v['result'][0]['statistics']['mean'] for v in timeSeries]
    values = [v for v in values if v != None]
    print(g['id'], values)




