# Unsupervised Learning:
Unsupervised learning is when the ML model is trained on unlabeled data. The model tries to find hidden patterns, structures, or relationships in the data without explicit output labels.

## K-Means Clustering Algorithm
K-means clustering is a popular unsupervised machine learning algorithm used for partitioning a dataset into a pre-defined number of clusters. 

The goal is to group similar data points together and discover underlying patterns or structures within the data.

K-Means is a centroid-based clustering algorithm that divides data into K clusters, where each cluster has a central point called a centroid.

Goal of the algorithm:
- Minimize the sum of squared distances between each data point and its cluster centroid.

In simple terms:
- points inside a cluster should be similar and close together
- clusters should be well separated from each other.

### How the K-Means Algorithm Works
Steps of the algorithm:
- Initialization : Randomly choose K data points as initial centroids.
- Assignment Step : Calculate distance from each data point to all centroids and assign the point to the nearest centroid.

- Update Step : Recalculate the centroid of each cluster by taking the mean of all points in the cluster.
- Repeat : Continue assignment and update steps until clusters stabilize.

### Stopping Criteria
The algorithm stops when:
- centroids stop changing
- data points stay in the same clusters
- maximum number of iterations is reached.

### Properties of Good Clusters
Good clustering should have:
- Low intra-cluster distance → points inside a cluster are similar
- High inter-cluster distance → clusters are clearly different.

### Challenges in K-Means
Important issues include:
- Clusters may be unevenly distributed.
- Random centroid initialization can lead to different results each time.
- The algorithm may struggle with spread-out clusters.

### K-Means++
To improve initialization, K-Means++ is used.

It selects centroids more carefully by choosing points that are far from existing centroids, which usually produces better clusters and faster convergence.

### Choosing the Optimal Number of Clusters (K)
The number of clusters must be chosen by the user.

A common technique is the Elbow Method:
1. Train the model with different values of K.
2. Compute an evaluation metric (like inertia).
3. Plot K vs inertia.
4. Choose the K where the curve starts flattening (the “elbow”).

### Advantages of K-Means
- Simple and easy to understand
- Fast and scalable for large datasets
- Works well when clusters are clearly separated.

### Example
```python
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Generate sample dataset
X, y = make_blobs(n_samples=300, centers=3, random_state=42)

# Apply K-Means
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Predicted clusters
labels = kmeans.labels_

# Plot clusters
plt.scatter(X[:,0], X[:,1], c=labels)
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], 
            color='red', marker='X', s=200)

plt.title("K-Means Clustering")
plt.show()
```

---

## PCA (Principal Component Analysis)
Principal Component Analysis (PCA) is an unsupervised learning technique.

It reduces the number of variables in a dataset while preserving most of the information.

It converts correlated features into independent principal components.

### Curse of dimensionality
As number of features increases the accuracy of model decreases.

Two different ways to remove curse of dimensionality : 
- Feature Selection
- Dimensionality Reduction (PCA)

### Why PCA is Needed
Datasets often have many features, which causes:
- Curse of dimensionality
- Overfitting
- Increased training time

### Important terms used in PCA include:
- Variance – amount of spread in data
- Covariance – relationship between variables
- Eigenvectors – directions of maximum variance
- Eigenvalues – amount of variance in those directions. magnitude of eigenvectors
- Principal Components (PCs) – new features formed from original features

### Steps of PCA (workflow):
1. Standardize the data (mean =0, variance =1)
2. Compute the covariance matrix
    
    Formula:
    ```math
    Cov(x,y) = (\sum{(x_i - \bar{x})(y_i - \bar{y})})/n
    ```

3. Calculate eigenvalues and eigenvectors
    
    Formula to calculate eigen value:
    ```math
    det(M - \lambda I)
    ```
    where, M is covariance matrix and I is identity matrix
    
    Formula to calculate eigen vector:
    ```math
    (M - \lambda_i I)U_i = 0
    ```
    where U of i is eigen vector. 

4. Select top principal components
5. Transform the data into a lower-dimensional space

For 2D to 1D conversion, we will have PC1 and PC2. Similarly, For 3D -> 1d, we will also have PC3.

Implementation example:
https://www.analyticsvidhya.com/blog/2022/07/principal-component-analysis-beginner-friendly/


### Advantages
- Reduces dimensionality
- Removes multicollinearity
- Improves training speed
- Helps prevent overfitting

### Disadvantages
- Hard to interpret transformed features
- Works mainly with numerical data

### Applications
- Computer vision
- Bioinformatics
- Image compression
- Data visualization
- Pattern discovery in high-dimensional data

Example:
```python
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

X = load_iris().data

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

print("Original", X.shape)
print("Reduced", X_pca.shape)

plt.scatter(X_pca[:,0], X_pca[:,1])
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA Projection")
plt.show()
```


## Hierarchical Clustering
Hierarchical clustering is an unsupervised machine learning algorithm used to group similar data points into clusters.

It builds a hierarchy (tree structure) of clusters, which is visualized using a **dendrogram** (a tree-like diagram that illustrates the arrangement of clusters produced by hierarchical clustering).

Dendrogram helps to:
- Understand relationships between clusters
- Decide the optimal number of clusters by cutting the tree at a specific height.

Each node in the tree represents a cluster.

The height in the dendrogram shows the distance between clusters.

### Types of Hierarchical Clustering
- Agglomerative Clustering (Bottom-Up)
    - Starts with each data point as a separate cluster.
    - The closest clusters are merged step by step.
    - Process continues until all points become one cluster.

- Divisive Clustering (Top-Down)
    - Starts with all data points in one cluster.
    - The cluster is recursively split into smaller clusters.
    - Continues until each point becomes its own cluster.

### Distance Measures
Clusters are formed based on distance between points or clusters, such as:
- Euclidean distance 
- Manhattan distance
- Chebyshev distance
- Mahalanobis distance


### Evaluation (Silhouette Score)
Clustering quality can be measured using the Silhouette Score, which considers:
- Cohesion – similarity within a cluster
- Separation – difference between clusters

Formula for the Silhouette Score:
```math
s(o) = {b(o) - a(o)} \div {max(a(o), b(o))}
```

### Advantages
- Works with different cluster shapes
- Easy to interpret with dendrogram
- Effective for small datasets

### Disadvantages
- High time complexity
- High memory usage
- Not suitable for large datasets

### k means vs hierarchical clustering
| Feature                            | K-Means                     | Hierarchical                   |
| ---------------------------------- | --------------------------- | ------------------------------ |
| Need number of clusters beforehand | Yes (K)                     | No                             |
| Output                             | Flat clusters               | Tree structure                 |
| Speed                              | Fast                        | Slower                         |
| Dataset size                       | Large datasets              | Small–medium datasets          |
| Cluster shape                      | Best for spherical clusters | Can capture complex structures |
| Visualization                      | Scatter clusters            | Dendrogram                     |


### Example:
```python
from sklearn.datasets import make_blobs # generating synthetic, multi-class datasets
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Generate sample dataset
X, y = make_blobs(n_samples=50, centers=3, random_state=42) 
Z = linkage(X, method="ward")

plt.figure(figsize=(8,5))
dendrogram(Z)
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Data Points")
plt.ylabel("Distance")
plt.show()
```

---

## DBSCAN Clustering 
**Density-Based Spatial Clustering of Applications with Noise**

DBSCAN is an unsupervised clustering algorithm that groups data points based on density.

Clusters are formed where many points are close together, while sparse points are treated as noise (outliers).

Unlike algorithms like K-Means, DBSCAN does not require specifying the number of clusters beforehand.

### Why DBSCAN is Used
Algorithms like K-Means and Hierarchical clustering struggle with:
- clusters of arbitrary shapes
- datasets with noise

DBSCAN can correctly detect irregularly shaped clusters and also identify noisy points in the dataset.

### Important Parameters
DBSCAN mainly uses two parameters:
1. ε (epsilon / eps)
- Radius around a data point
- Determines its neighborhood

2. minPts (min_samples)
- Minimum number of points required in that neighborhood to form a dense region.

### Types of Points in DBSCAN
- Core Point : 
    Has at least minPts neighbors within ε radius
- Border Point : 
    Has fewer neighbors but lies near a core point
- Noise (Outlier) : 
    Does not belong to any cluster.

### Important Concepts
- Density-Reachable :

    A point can be reached from another through a chain of nearby points.

- Density-Connected :

    Two points belong to the same cluster if they are reachable from a common point.

- Density edge : 

    If two points are neighbors then we join them by an edge that
we call a density edge.


### Steps in the DBSCAN algorithm
1. Classify the points.

2. Discard noise.

3. Assign cluster to a core point.

4. Color all the density connected points of a core point.

5. Color boundary points according to the nearest core point.

### How to determine epsilon and z?
Determining Epsilon and Minimum Points (MinPts, or in your prompt) in DBSCAN involves finding the point where cluster density drops, usually via a "k-distance plot."

1. Determine MinPts (Minimum Points/z):
    
    A common rule of thumb is :
    ```math
    MinPoints >= dimensions + 1
    ```
    - For 2D data, a value of 4 is commonly used.
    - Higher values are better for noisy datasets or larger data.

2. Determine Epsilon :
    
    K-distance Graph: Compute the distance to the nearest neighbor (where k = MinPoints) for every point.

    - Sort and Plot: Sort these distances in ascending order and plot them.
    - Find the "Elbow": The optimal is the value where the graph shows the sharpest change, or "knee".
    - Too Small: Most data is classified as noise.
    - Too Large: Clusters merge, and the algorithm fails to distinguish between them.

### Advantages
- Detects arbitrary shaped clusters
- Automatically detects noise
- No need to predefine number of clusters.

### Limitations
- Sensitive to parameter selection (eps and minPts)
- Struggles with high-dimensional data
- Difficult when clusters have similar densities.

### Examples
```python
from sklearn.datasets import make_circles
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# Generate circular dataset
X, y = make_circles(n_samples=300, noise=0.05, factor=0.5)

# Apply DBSCAN
db = DBSCAN(eps=0.2, min_samples=5)
labels = db.fit_predict(X)

# Plot clusters
plt.scatter(X[:,0], X[:,1], c=labels)
plt.title("DBSCAN Clustering (Circular Data)")
plt.show()
```

---

## Silhoutte Clustering (Performance matrix)
The Silhouette Score is a method used to evaluate the quality of clustering. It measures how well each data point fits within its cluster compared to other clusters.

Value range: -1 to +1

Interpretaton : 
| Score  | Meaning                                     |
| ------ | ------------------------------------------- |
| **+1** | Data point is well clustered                |
| **0**  | Data point lies between clusters            |
| **-1** | Data point is probably in the wrong cluster |

### How Silhouette Score is Calculated

For each data point:
- a = Average distance between the point and other points in the same cluster (intra-cluster distance).
- b = Average distance between the point and points in the nearest cluster (inter-cluster distance).

#### Calculating a(i) 
```math
a(i) = (1 / (|C_I| - 1)) \sum_{j \in C_I, i != j} d(i, j) 
```
where, 
- $C_I$ is no of points belonging to cluster i
- d(i, j) is distance between i and j

#### Calculating b(i) 
```math
b(i) = min_{J != I} (1 / |C_J|) \sum_{j \in C_J} d(i, j) 
```
where, 
- $C_J$ is mean distance from i to all points $i \in C_I$
- d(i, j) is distance between i and j

Formula:
```math
𝑆 (Silhouette Score) = 𝑏 − 𝑎 / 𝑚𝑎𝑥(𝑎,𝑏)
```

### Why Silhouette Score is Used
It helps to:
- Evaluate clustering performance
- Find the optimal number of clusters
- Compare clustering algorithms

Commonly used with algorithms like:
- K-Means Clustering
- Hierarchical Clustering
- DBSCAN

### Advantages
- Simple to understand
- Works without labeled data
- Helps choose the best number of clusters

### Limitations
- Computationally expensive for large datasets
- Works best when clusters are well separated

### Example:
```python
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Generate dataset
X, y = make_blobs(n_samples=200, centers=3, random_state=42)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3)
labels = kmeans.fit_predict(X)

# Calculate silhouette score
score = silhouette_score(X, labels)

print("Silhouette Score:", score)
```


## When to use which unsupervised technique:
* K-Means → Fast clustering. Big dataset

* Hierarchical → Cluster tree. Small dataset

* DBSCAN → Noise & irregular clusters.

* PCA → Reduce features