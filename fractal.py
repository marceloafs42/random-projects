import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = np.array(Image.open('/home/marcelo/Downloads/fractal.png').convert('L'))

## just to make sure, we make the image a binary. The cutoff is 100 here.
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if(img[i][j] < 100):
            img[i][j] = 0
        else:
            img[i][j] = 255

## the estimation is simple: we divide the image in 2 x 2 squares up to
## 20x20 squares (or anything you want), and see how log mass scales
## with log height. A bigger square is to be interpreted as a smaller
## image, so that size = 1/height, or logsize = - logheight. 

## for each height h, we compute the mass in the most simple way: we simply count
## the non empty squares

## the fractal dimension is the angular coefficient between log mass 
## and log size

heights = np.array([])
mass = np.array([])

## this is certanly not optmized
h = 2
while(h < 20):
    m = 0
    i = 0
    while((i+1)*h < img.shape[0]):
        j = 0
        while((j+1)*h < img.shape[1]):
            ## check if {i,j} square has mass
            square = img[np.ix_(range(i*h, (i+1)*h),range(j*h, (j+1)*h))]
            if 0 in square:
                m = m+1
            j = j+1
        i = i+1
    mass = np.append(mass, m)
    heights = np.append(heights, h)
    h = h + 1 ## you may scale the height as you want

angular, constant = np.polyfit(np.log2(heights), np.log2(mass), 1)

#### some plots
z = constant + angular*np.log2(heights)

fig, ax = plt.subplots()
ax.scatter(np.log2(heights), np.log2(mass), c = 'b')
ax.plot(np.log2(heights), z, c = 'r')
ax.set_xlabel('-log size')
ax.set_ylabel('log mass')

print("the fractal dimension is ", -angular)
print("for great britain, we obtained 1.28, the actual value is ~1.25")