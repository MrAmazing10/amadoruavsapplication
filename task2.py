import numpy as np # did not finish with adding this
import shapely as sh
import shapely.ops as ops
import json # did not finish adding this

geopoints = []
waypoints = []  # initialize global empty list of points


def getpoints(geopoints, waypoints):
    with open("navigate.txt", "r") as file:
        for i, line in enumerate(file):
            if i == 0:
                geofencenum, waypointnum = map(
                    int, line.split()
                )  # Splitting the first line to get counts
                continue
            elif i <= geofencenum:  # Read geofence points
                lat, lon = map(
                    float, line.strip().split()
                )  # Convert lat and lon to float
                geopoints.append([lat, lon])
            elif (
                i > geofencenum and i <= geofencenum + waypointnum
            ):  # Read waypoint points
                lat, lon = map(
                    float, line.strip().split()
                )  # Convert lat and lon to float
                waypoints.append([lat, lon])
    return geopoints, waypoints


def fitpath(geopoints, waypoints):
    pathpoints = waypoints.copy()  # creating copy of waypoints
    geofence = sh.Polygon(geopoints)  # creating geofence polygon
    limit = geofence.buffer(
        -0.00000274
    )  # create inside buffer of geofence of 25ft; converted from degrees to ft

    # assumes buffer list is not empty(if buffer value > geofence's, then it is empty)

    for i, waypoint in enumerate(
        waypoints
    ):  # adjusting waypoints if they are outside buffered geofence
        point = sh.Point(waypoint)  # creating a point from waypoint
        # checking if point is outside buffer
        if not limit.contains(point):
            # Find the nearest point on buffer and update pathpoints to match
            pathpoint = ops.nearest_points(point, limit)[1]
            pathpoints[i] = [
                pathpoint.x,
                pathpoint.y,
            ]  # replaces old waypoint(waypoint) with new waypoint(pathpoint)

    return pathpoints  # return adjusted pathpoints
    # what I planned to add next if I was able to: potential next to add?: if line intersects buffered geofence, adjust points again, move both points along line inside until no longer intersecting buffer


geopoints, waypoints = getpoints(geopoints, waypoints)
pathpoints = fitpath(geopoints, waypoints)
print(
    f"path:{pathpoints}"
)  # this is used for testing output as I did not finish creating method for JSON output:
