# MatPlotLib

Mathematical Plotting Library

Matplotlib is a low level graph plotting library in python that serves as a visualization utility.

## Pyplot
Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias.

```
import matplotlib.pyplot as plt
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()
```

### Matplotlib Plotting

#### Plotting x and y points
The plot() function is used to draw points (markers) in a diagram. By default, the plot() function draws a line from point to point.

```plt.plot(xpoints, ypoints)```

#### Plotting Without Line
```plt.plot([1,2,3,4,5], [4,4,4,4,4], '*')```

#### Default X-Points
If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 etc., depending on the length of the y-points.



### Matplotlib Markers
You can use the keyword argument marker to emphasize each point with a specified marker. Marking the intersection of axis.

```plt.plot([1,2,3,4,5], [0,0,0,0,0], marker="o")```

-> Marker Reference:
Like 'o' for Circle, '*' for Star, 's' for Square, and etc.

#### Format Strings fmt
You can also use the shortcut string notation parameter to specify the marker. This parameter is also called fmt, and is written with this syntax:
    
    marker|line|color

Example:
```plt.plot(ypoints, 'o:r')```

- Line Reference
    - '-' : Solid line	
    - ':' : Dotted line	
    - '--' : Dashed line	
    - '-.' : Dashed/dotted line

- Color Reference : You can also use Hexadecimal color values.
    - 'r' : Red	
    - 'g' : Green	
    - 'b' : Blue	
    - 'c' : Cyan	
    - 'm' : Magenta	
    - 'y' : Yellow	
    - 'k' : Black	
    - 'w' : White

    - Marker Size
    You can use the keyword argument markersize or the shorter version, ms to set the size of the markers: 
    
        ```plt.plot(ypoints, marker = 'o', ms = 20)```

- Marker Color :
markeredgecolor or the shorter mec to set the color of the edge of the markers: 
    ```plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')```

- Maker face color :
    markerfacecolor or the shorter mfc to set the color inside the edge of the markers: 

    ```plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')```



### Matplotlib Line

- linestyle : to change style of plotted line. Shorthand: ls
    
    ```plt.plot(ypoints, linestyle = 'dotted')```

- color : or the shorter c to set the color of the line:
    
    ```plt.plot(ypoints, color = 'r')```

- linewidth : or the shorter lw to change the width of the line.
    
    ```plt.plot(ypoints, linewidth = '20.5')```

- Multiple Lines: You can plot as many lines as you like by simply adding more plt.plot() functions:
    ```
    plt.plot(y1)
    plt.plot(y2)
    ```


### Matplotlib Labels and Title

- Create Labels for a Plot : use the xlabel() and ylabel() functions.
    ```
    plt.xlabel("Average Pulse")
    plt.ylabel("Calorie Burnage")
    ```

- Create a Title for a Plot : use title(). 

    ```plt.title("Sports Watch Data")```

- Set Font Properties for Title and Labels: You can use the fontdict parameter in xlabel(), ylabel(), and title() to set font properties for the title and labels.
    ```
    font1 = {'family':'serif','color':'blue','size':20}
    plt.title("Sports Watch Data", fontdict = font1)
    ```

- Position the Title: use loc param in title

    ```plt.title("Sports Watch Data", loc = 'left')```

### Matplotlib Adding Grid Lines

- Add Grid Lines to a Plot :

    ```plt.grid()```

- Specify Which Grid Lines to Display : You can use the axis parameter in the grid() function to specify which grid lines to display. Legal values are: 'x', 'y', and 'both'. Default value is 'both'.

    ```plt.grid(axis = 'x')```

- Set Line Properties for the Grid : 

    ```plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)```


## Matplotlib Subplot

With the subplot() function you can draw multiple plots in one figure:
```
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()
```

### subplot() Function
The subplot() function takes three arguments that describes the layout of the figure.

```
plt.subplot(1, 2, 1)
#the figure has 1 row, 2 columns, and this plot is the first plot so 3rd shows index of current plot.
```

You can add a title to each plot with the title() function after calling subplot().

- Super Title : You can add a title to the entire figure with the suptitle() function
    
    ```plt.suptitle("MY SHOP")```


## Matplotlib Scatter
With Pyplot, you can use the scatter() function to draw a scatter plot. The scatter() function plots one dot for each observation.

```
a = np.arange(0,20,2)
b = np.arange(20,0,-2)
plt.scatter(a, b)
```

#### ColorMap
A colormap is like a list of colors, where each color has a value that ranges from 0 to 100.

This colormap is called 'viridis' and as you can see it ranges from 0, which is a purple color, up to 100, which is a yellow color.

##### How to Use the ColorMap?
with the keyword argument cmap with the value of the colormap
You can include the colormap in the drawing by including the plt.colorbar().

```
a = np.arange(0,20,2)
b = np.arange(20,0,-2)
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70])
plt.scatter(a, b, marker='*', c=colors, cmap='viridis')
plt.colorbar()
```

### Other styling :
We can have the styling values in array form to apply to individual points.

- Size : ```plt.scatter(x, y, s=sizes)```
- Alpha : ```plt.scatter(x, y, s=sizes, alpha=0.5)```


## Matplotlib Bars
With Pyplot, you can use the bar() function to draw bar graphs:

```
a = np.arange(0,20,2)
b = np.arange(20,0,-2)
plt.bar(a, b)
```

### Horizontal Bars
use barh()

### params 

- color : 
- width : for bar()
- height : for barh()


## Matplotlib Histograms
A histogram is a graph showing frequency distributions. It is a graph showing the number of observations within each given interval.

```
x = np.random.normal(170, 10, 250)
plt.hist(x)
```

## Matplotlib Pie Charts
With Pyplot, you can use the pie() function to draw pie charts:
```
plt.pie([20, 20, 20, 20, 20])
plt.show()
```

### Params :
- labels : plt.pie(y, labels = mylabels)
- startangle : default start angle is at the x-axis
- explode : Each value represents how far from the center each wedge is displayed

    ```plt.pie([20, 20, 20, 20, 20], startangle=60, explode=[0,0.2,0,0.2,0])```
- shadow : true / false
- colors : 
- legend : To add a list of explanation for each wedge
- Legend With Header : To add a header to the legend, add the title parameter to the legend function.

    ```plt.legend(title = "Four Fruits:")```

## Saving plot to disk
Use savefig()

```
plt.savefig('pie_chart.png', dpi=300, bbox_inches='tight')
```

## Matplotlib Image Tutorial
Using PIL library to open image file. Install using ```pip install pillow```

```
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load the image from a file
img = mpimg.imread('image.png')

# Display the image
plt.imshow(img)

# Turn off axis labels and ticks (optional)
plt.axis('off')

# Show the figure
plt.show()
```

### Importing image data into Numpy arrays
```
from PIL import Image
imp = np.asarray(Image.open('image.png'))
# The img obj has the nd array of image
```

### Plotting numpy arrays as images
```
imgplot = plt.imshow(img)
```

#### Random image using random np array
```
random_image_array = np.random.random([200, 200])
plt.imshow(random_image_array, cmap='gist_rainbow')
```

### Applying pseudocolor schemes to image plots
```
lum_img = img[:, :,0]
plt.imshow(lum_img, cmap='gist_rainbow')
plt.imshow(lum_img, cmap='hot')
```





