Title: Notes on data science from Data Smart
Date: 2016-12-26
Category: Notes
Tags: datasci
Slug: 
Authors: Amit
Status: draft

# Cluster analysis

Cluster analysis is partitioning a large data set into a number of clusters. Essentially, the data lives in an *n*-dimensional space, and we want to come up with a number of artificial points that represent the centre of clusters of data. The data are assigned to clusters by measuring the distance of the data from the centroid points. Another way of visualising this is segmenting a space by a Voronoi diagram.

To do this, we need a measure of distance:

1. Eucledian distance (i.e. Pythagoras in n-dimensions) - this would be the simplest and most intuitive measure to take.

2. Hamming distance (or Manhattan distance) - this is a more straightforward measure of the degree of mismatch between the idealised point and the actual data points.

3. Cosine distance. The problem with the fist two distance measures is that where binary data exists, a data match is weighted the same as a data mismatch. The cosine distance is a asymmetric measure that measures the distances based on the matched parameters, and normalises by the number of dimensions in the vector. It is the cosine of the subtended angle of the vectors of two points in space.

## Testing the clustering

A silhouette can be used to test the clustering: the average distance of a data point from the data points in an adjacent cluster is compared to the distance of the data point from the points in its own assigned cluster. If these are comparable, then the data point might not be in the correct cluster.

In practice, this is a common step, since we don't know how many clusters we'll find in any given data set, so we might iterate until we have a suitable number of optimised clusters. 

## Normalising data

Working with n-dimensional data means that our dimensions won't have similar units. As a result, any distance measure might be skewed by the size of the units (or the spread of the data in any one dimension). So, in practice, the data can be normalised to give a value in the range $-1 \le x \le 1$.
