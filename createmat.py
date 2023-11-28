import scipy.io
import numpy as np

def read_ale(filename):
    vertices = []
    regions = []
    boundary = []
    print("Reading file: " + filename)
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
        for _ in range(0, n_regions):
            line = fp.readline()
            l = line.split()
            l.pop(0) # remove number of vertices
            regions.append([int(x) for x in l]) # +1 because ale files are 0-indexed
        # read boundary
        for line in fp:
            if line.startswith('#'):
                continue
            l = line.split()
            if l[0].isdigit():
                boundary = [int(x) for x in l] # +1 because ale files are 0-indexed
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



def createmat(filename):
    vertices, regions, boundary, bounding_box = read_ale(filename + ".ale")

    for i in range(0, len(vertices)):
        vertices[i] = np.array(vertices[i])


    np_regions = []
    for i in range(0, len(regions)):
        sub_region = []
        for v in regions[i]:
            sub_region.append(np.array(v + 1))
        sub_region = np.array(sub_region)
        col_vec = sub_region[:, None]
        new_wea = np.array(col_vec, dtype='uint32')
        np_regions.append(new_wea)
    np_regions = np.array(np_regions)
    np_regions = np_regions[:, None]

    np_boundary = []
    for v in boundary:
        np_boundary.append(np.array(v + 1, dtype='uint32'))
    np_boundary = np.array(np_boundary)
    np_boundary = np_boundary.reshape((np_boundary.shape[0], 1))

    mdic = {"boundary": np_boundary, "elements": np_regions, "vertices": vertices}

    print("Writing file: " + filename + ".mat")
    scipy.io.savemat(filename + ".mat", mdic)


if __name__ == "__main__":
    filename = "..\\testVEM"
    createmat(filename)