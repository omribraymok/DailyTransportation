import math
import sys
from random import shuffle, uniform


# https://www.geeksforgeeks.org/k-means-clustering-introduction/

###_Auxiliary Function_###
def FindColMinMax(items):
    n = len(items[0])
    minima = [sys.maxsize for i in range(n)]
    maxima = [-sys.maxsize - 1 for i in range(n)]

    for item in items:
        for f in range(len(item)):
            if item[f] < minima[f]:
                minima[f] = item[f]

            if item[f] > maxima[f]:
                maxima[f] = item[f]

    return minima, maxima


# We will be using the euclidean distance
# as a metric of similarity for our data set
def EuclideanDistance(x, y):
    S = 0  # The sum of the squared differences of the elements
    for i in range(len(x)):
        S += math.pow(x[i] - y[i], 2)

        # The square root of the sum
    return math.sqrt(S)


def InitializeMeans(items, k, cMin, cMax):
    # Initialize means to random numbers between
    # the min and max of each column/feature
    f = len(items[0]);  # number of features
    means = [[0 for i in range(f)] for j in range(k)]

    for mean in means:
        for i in range(len(mean)):
            # Set value to a random float
            # (adding +-1 to avoid a wide placement of a mean)
            mean[i] = uniform(cMin[i] + 1, cMax[i] - 1)

    return means


#
# To update a mean, we need to find the average value for its feature, for all the items in the mean/cluster.
# We will calculate the new average by doing the following:
# m = (m*(n-1)+x)/n where m is the mean value for a feature, n is the number of items in the cluster and x is the
# feature value for the added item. We do the above for each feature to get the new mean.
def UpdateMean(n, mean, item):
    for i in range(len(mean)):
        m = mean[i]
        m = (m * (n - 1) + item[i]) / float(n)
        mean[i] = round(m, 3)

    return mean


def Classify(means, item):
    # Classify item to the mean with minimum distance
    minimum = sys.maxsize
    index = -1

    for i in range(len(means)):

        # Find distance from item to mean
        dis = EuclideanDistance(item, means[i])

        if dis < minimum:
            minimum = dis
            index = i

    return index


def CalculateMeans(k, items, maxIterations=100000):
    # Find the minima and maxima for columns
    cMin, cMax = FindColMinMax(items)

    # Initialize means at random points
    means = InitializeMeans(items, k, cMin, cMax)

    # Initialize clusters, the array to hold
    # the number of items in a class
    clusterSizes = [0 for i in range(len(means))]

    # An array to hold the cluster an item is in
    belongsTo = [0 for i in range(len(items))]

    # Calculate means
    for e in range(maxIterations):

        # If no change of cluster occurs, halt
        noChange = True
        for i in range(len(items)):

            item = items[i]

            # Classify item into a cluster and update the
            # corresponding means.
            index = Classify(means, item)

            clusterSizes[index] += 1
            cSize = clusterSizes[index]
            means[index] = UpdateMean(cSize, means[index], item)

            # Item changed cluster
            if index != belongsTo[i]:
                noChange = False

            belongsTo[i] = index

            # Nothing changed, return
        if noChange:
            break

    return means


def FindClusters(means, items):
    clusters = [[] for i in range(len(means))]  # Init clusters

    for item in items:
        # Classify item into a cluster
        index = Classify(means, item)

        # Add item to cluster
        clusters[index].append(item)

    return clusters


###_Main_###
def k_means(items, k):
    means = CalculateMeans(k, items)
    clusters = FindClusters(means, items)
    print(means)
    length = len(clusters)
    for i in range(length):
        print("clusters " + str(i) + ":")
        print(clusters[i])
    return clusters, means

