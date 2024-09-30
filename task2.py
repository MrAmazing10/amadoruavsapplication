import numpy as np
import shapely as sh
import json
import matplotlib.pyplot as plt

geopoints = []
waypoints = [] # initialize global empty list of points
def getpoints(geopoints,waypoints):
    with open("navigate.txt","r") as file:
        for i, line in enumerate(file):
            if i == 0:
                geofencenum, waypointnum = line.split() # splitting line to find each value
                geofencenum = int(geofencenum)
                waypointnum = int(waypointnum) # converting to int
                continue
            elif i <= geofencenum: # checking values of i to determine if it is within geofence or waypoint line ranges
                for __ in range(geofencenum):
                    values = line.strip()
                    lat, long = values.split() # getting lat + long values from line and adding to 2d list
                    geopoints.append([float(lat), float(long)])
            elif i > geofencenum and i <= geofencenum + waypointnum:
                for __ in range(waypointnum):
                    values = line.strip()
                    lat, long = values.split() # getting lat + long values from line and adding to 2d list
                    waypoints.append([float(lat), float(long)])
    return geopoints, waypoints


def fitpath(geopoints, waypoints):
   pathpoints = waypoints #currently duplicate of waypoints; will be changed with correct points after
   geofence = sh.Polygon(geopoints) # creating geofence polygon
   limit = geofence.buffer(25)
   for i,waypoint in enumerate(waypoints):
       point = sh.Point(waypoint) # creating point from waypoint
       if not limit.contains(point): # checking if point is within 25 ft limit
           pathpoint = sh.ops.nearest_points(point,limit)[1]
           pathpoints[i] = [pathpoint.x,pathpoint.y]
           xgeo,ygeo = geofence.exterior.xy
           xpath,ypath = limit.exterior.xy
           plt.figure()
           plt.plot(xgeo,ygeo)
           plt.plot(xpath,ypath)
           waypoints_x, waypoints_y = zip(*waypoints)
           pathpoints_x, pathpoints_y = zip(*pathpoints)
           plt.scatter(waypoints_x, waypoints_y, color='blue')
           plt.scatter(pathpoints_x, pathpoints_y, color='red')
           plt.savefig('geofence_path_plot.png')
           plt.show
       else:
           continue
   return pathpoints
geopoints, waypoints = getpoints(geopoints, waypoints)
pathpoints = fitpath(geopoints,waypoints)



