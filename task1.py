import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# importing necessary libraries


def main():  # top level function
    points = []  # initialize global empty list
    points = create_list(points)
    centroids = findcentroids(points, cluster(points))
    plot(points)
    with open("centers.txt", "w") as f:
        for centroid in centroids:
            f.write(f"{centroid[0]} {centroid[1]}\n")
            f.close


def create_list(points):
    with open("inferences.txt", "r") as file:  # open file in read
        for i, line in enumerate(file):
            # excludes line 1, as information there(# of lines) is not needed
            if i == 0:
                continue

            values = line.strip()

            lat, long = values.split()  # split into lat + long then adds to 2d list
            points.append([float(lat), float(long)])

    return points


# uses DBSCAN as clustering algorithm to find clusters of points and label them
def cluster(points):
    db = DBSCAN(eps=0.00006, min_samples=50).fit(points)
    # above line:finds clusters with radius of .0001 around each point to find others, with minimum amt of samples in this process being 50(has to find 49 others total)
    labels = db.labels_
    return labels


# note: this was only used for visualization purposes for me, but since it said we could use matplotlib, I left it in in case it may be beneficial in revie
def plot(points):
    x = [i[0] for i in points]  # sets x-values
    y = [j[1] for j in points]  # sets y-values
    df = plt.scatter(x, y)
    plt.savefig("scatter_plot.png")  # saves as file for me to view


def findcentroids(points, labels):
    sortedclusterpts = [
        [],
        [],
        [],
        [],
        [],
    ]  # creating 5 different lists. values inside the list will also be lists, where the clusters' respective points will go
    latpts = []  # creating list for all latitudes
    longpts = []  # creating list for all longitudes
    centroids = []  # creating list for all centroids to go in
    for i in range(len(labels)):
        label = labels[i]
        if label == -1:
            continue
        sortedclusterpts[label].append(points[i])

    for i in range(len(sortedclusterpts)):
        latpts.append(
            [[np.mean(sortedclusterpts[i][0][0])]]
        )  # calculating avg of each cluster for lat and adding them to a list of latitudes
        longpts.append(
            [np.mean(sortedclusterpts[i][0][1])]
        )  # calculating avg of each cluster for long and adding them to a list of longitudes
        latpts.sort()  # sorting the latitudes

        centroids.append(
            [np.mean(sortedclusterpts[i][0][0]), np.mean(sortedclusterpts[i][0][1])]
        )  # calculating avg of each cluster for lat and long, and adding them to a list of centroids
        centroids = sorted(centroids)  # sort centroids by latitudes lowest to highest
    return centroids


if __name__ == "__main__":
    main()
