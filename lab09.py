import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from rotation import rotation
from bucky import bucky
from scipy.spatial import ConvexHull

def plot_cube(vertices, edges, title="Cube", figsize=(6, 6)):
    """Plots a 3D cube or its 2D projection."""
    fig = plt.figure(figsize=figsize)
    if vertices.shape[1] == 2:
        ax = fig.add_subplot(111)
        for i in range(8):
            for j in range(i + 1, 8):
                if edges[i, j] == 1:
                    ax.plot([vertices[i, 0], vertices[j, 0]],
                            [vertices[i, 1], vertices[j, 1]], 'b')
        ax.set_title(title)
        ax.set_aspect('auto')
        ax.set_xlabel('X')
        ax.set_ylabel('Z')
    else:
        ax = fig.add_subplot(111, projection='3d')
        for i in range(8):
            for j in range(i + 1, 8):
                if edges[i, j] == 1:
                    ax.plot([vertices[i, 0], vertices[j, 0]],
                            [vertices[i, 1], vertices[j, 1]],
                            [vertices[i, 2], vertices[j, 2]], 'b')
        ax.set_title(title)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_box_aspect([1, 1, 1])

    plt.show()

def plot_buckyball(vertices, edges, title="Buckyball", figsize=(6, 6)):
    """Plots the buckyball structure in 3D or its 2D projection."""
    fig = plt.figure(figsize=figsize)

    if vertices.shape[1] == 3:
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], c='r', marker='o')

        for edge in edges:
            x_vals = [vertices[edge[0]][0], vertices[edge[1]][0]]
            y_vals = [vertices[edge[0]][1], vertices[edge[1]][1]]
            z_vals = [vertices[edge[0]][2], vertices[edge[1]][2]]
            ax.plot(x_vals, y_vals, z_vals, c='b')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(title)
        ax.set_box_aspect([1, 1, 1])
    else:
        ax = fig.add_subplot(111)
        ax.scatter(vertices[:, 0], vertices[:, 1], c='r', marker='o')

        for edge in edges:
            x_vals = [vertices[edge[0]][0], vertices[edge[1]][0]]
            y_vals = [vertices[edge[0]][1], vertices[edge[1]][1]]
            ax.plot(x_vals, y_vals, c='b')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title(title)
        plt.axis('equal')
        
    plt.show()

def plot_3d_model(vertices, faces, title="3D Model with Edges", figsize=(6, 6)):
    """Plots a 3D model with edges using faces and vertices."""
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='3d')
    
    for j in range(faces.shape[0]):
        for k in range(3):
            x_vals = [vertices[faces[j, k], 0], vertices[faces[j, (k + 1) % 3], 0]]
            y_vals = [vertices[faces[j, k], 1], vertices[faces[j, (k + 1) % 3], 1]]
            z_vals = [vertices[faces[j, k], 2], vertices[faces[j, (k + 1) % 3], 2]]
            ax.plot(x_vals, y_vals, z_vals, 'b')
    
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_box_aspect([1, 1, 1])

    plt.show()


def plot_2d_projection(vertices, faces, title="2D Projection of 3D Model", figsize=(6, 6)):
    """Plots a 2D projection of a 3D model."""
    fig, ax = plt.subplots(figsize=figsize)
    
    for j in range(faces.shape[0]):
        for k in range(3):
            ax.plot([vertices[faces[j, k], 0], vertices[faces[j, (k + 1) % 3], 0]],
                    [vertices[faces[j, k], 1], vertices[faces[j, (k + 1) % 3], 1]], 'b')
    
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.axis('equal')
    plt.show()


def main():
    # Problem 1: Cube
    Vertices = np.array([
        [1, 1, 1], [-1, 1, 1], [1, -1, 1], [1, 1, -1],
        [-1, -1, 1], [-1, 1, -1], [1, -1, -1], [-1, -1, -1]
    ])
    Edges = np.zeros((8, 8))
    Edges[0, 1], Edges[0, 2], Edges[0, 3] = 1, 1, 1
    Edges[1, 4], Edges[1, 5] = 1, 1
    Edges[2, 4], Edges[2, 6] = 1, 1
    Edges[3, 5], Edges[3, 6] = 1, 1
    Edges[4, 7], Edges[5, 7], Edges[6, 7] = 1, 1, 1
    Edges += Edges.T

    theta1, theta2, theta3 = np.pi / 3, np.pi / 4, np.pi / 6
    rotmat = rotation(theta1, theta2, theta3)
    VertRot = Vertices @ rotmat.T
    print(f"Rotation matrix:\n{rotmat}")
    print(f"Rotated vertices:\n{VertRot}")
    VertRotPrj = VertRot[:, [0, 2]]

    plot_cube(Vertices, Edges, title="Original Cube")
    plot_cube(VertRot, Edges, title="Rotated Cube")
    plot_cube(VertRotPrj, Edges, title="Projection of Rotated Cube")

    # Problem 2: Buckyball
    Vertices2, Edges2 = bucky()
    plot_buckyball(Vertices2, Edges2)
    Vertices2Num = Vertices2.shape[0]
    print(f"Number of vertices in the buckyball: {Vertices2Num}")
    Vert2Rot = Vertices2 @ rotmat.T
    Vert2Prj = Vert2Rot[:, [0, 1]]
    plot_buckyball(Vert2Prj, Edges2, title="2D Projection of Buckyball")

    # Problem 3: Fawn
    v_mat = scipy.io.loadmat('v.mat')
    f_mat = scipy.io.loadmat('f.mat')
    v = v_mat['v']
    f = f_mat['f'] - 1

    mFaces, nFaces = f.shape
    print(f"Number of faces (mFaces): {mFaces}, Number of vertices per face (nFaces): {nFaces}")

    plot_3d_model(v, f, title="3D Model of Fawn")
    vRot = v @ rotmat.T
    vRotPrj = vRot[:, [0, 1]]
    plot_2d_projection(vRotPrj, f, title="2D Projection of 3D Fawn")

    # Alternative 2D projection using a different rotation matrix
    rotmat2 = rotation(-np.pi / 3, 0, np.pi / 4)
    vRot = v @ rotmat2.T
    vPrj = vRot[:, [0, 1]]
    plot_2d_projection(vPrj, f, title="Alternative 2D Projection of 3D Fawn")

    # Problem 4: Additional 3D Model - Convex Hull
    np.random.seed(42)
    points = np.random.rand(30, 3) * 10 - 5  # Random points in a cube [-5, 5]^3

    hull = ConvexHull(points)
    vertices = points
    faces = hull.simplices

    plot_3d_model(vertices, faces, title="Original Convex Hull")
    rotmat = rotation(np.pi/6, np.pi/4, np.pi/3)
    rotated_vertices = vertices @ rotmat.T
    plot_3d_model(rotated_vertices, faces, title="Rotated Convex Hull")

    projected_vertices = rotated_vertices[:, [0, 1]]
    plot_2d_projection(projected_vertices, faces, title="2D Projection of 3D Convex Hull")

if __name__ == "__main__":
    main()
