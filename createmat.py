import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from mpl_toolkits.axes_grid1 import make_axes_locatable

def read_ale(filename):
    vertices = []
    regions = []
    boundary = []
    with open(filename) as fp:
        # Read number of vertices
        for line in fp:
            if line.startswith('#'):
                continue
            l = line.split()
            if l[0].isdigit():
                n_vertices = int(l[0])
                break
        # read vertices
        for i in range(0, n_vertices):
            line = fp.readline()
            l = line.split()
            vertices.append((float(l[0]), float(l[1])))
        # read number of regions
        for line in fp:
            if line.startswith('#'):
                continue
            l = line.split()
            if l[0].isdigit():
                n_regions = int(l[0])
                break
        # read regions
        for i in range(0, n_regions):
            line = fp.readline()
            l = line.split()
            l.pop(0)
            regions.append([int(x) for x in l])
        # read boundary
        for line in fp:
            if line.startswith('#'):
                continue
            l = line.split()
            if l[0].isdigit():
                boundary = [int(x) for x in l]
                break
        #read bounding box
        for line in fp:
            if line.startswith('#'):
                continue
            l = line.split()
            if len(l) == 4:
                x_min = float(l[0])
                x_max = float(l[1])
                y_min = float(l[2])
                y_max = float(l[3])
                break
    return vertices, regions, boundary, (x_min, x_max, y_min, y_max)

vertices, regions, boundary, bounding_box = read_ale("meshes/testVEM.ale")

for i in range(0, len(vertices)):
    vertices[i] = np.array(vertices[i])

#print(regions)
#np_regions =  np.empty((0,len(regions))) 
#for i in range(0, len(regions)):
#    sub_element = np.empty((0,len(regions[i]))) 
#    for v in regions[i]:
#        sub_element = np.append(sub_element, np.array(v), axis=1)
#    np_regions = np.append(np_regions, sub_element)
#print(np_regions)
mesh = scipy.io.loadmat("meshes/voronoi.mat")

np_regions = []
for i in range(0, len(regions)):
    sub_region = []
    for v in regions[i]:
        sub_region.append(np.array(v))
    sub_region = np.array(sub_region)
    col_vec = sub_region[:, None]
    new_wea = np.array(col_vec, dtype='uint16')
    np_regions.append(new_wea)
np_regions = np.array(np_regions)
np_regions = np_regions[:, None]

np_boundary = []
for v in boundary:
    np_boundary.append(np.array(v, dtype='uint16'))
np_boundary = np.array(np_boundary)
np_boundary = np_boundary[:, None]

mdic = {"boundary": boundary, "elements": regions, "vertices": vertices}

scipy.io.savemat("meshes/testVEM500.mat", mdic)

#print(mesh['elements'])
#print(mesh.keys())
#print(regions)