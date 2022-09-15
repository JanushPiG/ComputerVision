import numpy as np
import matplotlib.pyplot as plt
import time

def lerp(v0, v1, t):
    return (1 - t) * v0 + t * v1

size = 100
image = np.zeros((size, size, 3), dtype="uint8")
assert image.shape[0] == image.shape[1]

color2 = [255, 128, 0]
color1 = [0, 128, 255]

arr = np.linspace(0, 0.5, image.shape[0])
diff = 0.5/size
itt = diff
mem = 0
mem_1 = 0

start_time = time.time()

for j in range(size):
    for i, v in enumerate(arr):
        r = lerp(color1[0], color2[0], v+itt)
        g = lerp(color1[1], color2[1], v+itt)
        b = lerp(color1[2], color2[2], v+itt)
        image[j, i, :]=[r,g,b]
        # mem += 1
    itt = diff*(j+1)
    # mem_1 += 1

print("--- %s seconds ---" % (time.time() - start_time))

# print(mem)
# print(mem_1)

plt.figure(1)
plt.imshow(image)
plt.show()