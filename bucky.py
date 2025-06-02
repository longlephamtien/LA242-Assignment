import numpy as np

def bucky():
    """
    Generate vertices and edges for a buckminsterfullerene (C60) molecule
    as a truncated icosahedron with exactly 60 vertices.
    
    Returns:
        vertices: numpy array of shape (60, 3) containing the 3D coordinates of the vertices
        edges: list of tuples containing the indices of vertices that form edges
    """
    # Start with the vertices of a regular icosahedron
    phi = (1 + np.sqrt(5)) / 2  # Golden ratio
    
    # The 12 vertices of a regular icosahedron
    icosa_vertices = []
    for i in [-1, 1]:
        icosa_vertices.append([0, i, phi])
        icosa_vertices.append([0, i, -phi])
        icosa_vertices.append([phi, 0, i])
        icosa_vertices.append([-phi, 0, i])
        icosa_vertices.append([i, phi, 0])
        icosa_vertices.append([i, -phi, 0])
    
    icosa_vertices = np.array(icosa_vertices)
    
    # Edges of the icosahedron (30 edges)
    icosa_edges = []
    threshold = 2.1
    
    for i in range(len(icosa_vertices)):
        for j in range(i+1, len(icosa_vertices)):
            dist = np.linalg.norm(icosa_vertices[i] - icosa_vertices[j])
            if dist < threshold:
                icosa_edges.append((i, j))
    
    # For each edge of the icosahedron, compute the truncation point
    # For a truncated icosahedron, we keep 1/3 of each edge from each vertex
    trunc_factor = 1/3
    
    vertices = []
    
    # For each edge, compute two new vertices (one for each endpoint)
    # This gives us 60 vertices (2 vertices × 30 edges)
    for i, j in icosa_edges:
        v_i = icosa_vertices[i]
        v_j = icosa_vertices[j]
        
        # Truncation point near vertex i
        t_i = v_i + trunc_factor * (v_j - v_i)
        vertices.append(t_i)
        
        # Truncation point near vertex j
        t_j = v_j + trunc_factor * (v_i - v_j)
        vertices.append(t_j)
    
    vertices = np.array(vertices)
    
    # Normalize vertices to place them on a unit sphere
    norms = np.linalg.norm(vertices, axis=1)
    vertices = vertices / norms[:, np.newaxis]
    
    # Remove duplicate vertices (with small tolerance)
    unique_vertices = []
    tolerance = 1e-10
    
    for v in vertices:
        is_duplicate = False
        for u in unique_vertices:
            if np.linalg.norm(v - u) < tolerance:
                is_duplicate = True
                break
        if not is_duplicate:
            unique_vertices.append(v)
    
    vertices = np.array(unique_vertices)
    
    # Generate edges by connecting vertices that are close to each other
    edges = []
    threshold = 0.6  # Adjusted for C60 structure
    
    for i in range(len(vertices)):
        for j in range(i+1, len(vertices)):
            dist = np.linalg.norm(vertices[i] - vertices[j])
            if dist < threshold:
                edges.append((i, j))
    
    return vertices, edges