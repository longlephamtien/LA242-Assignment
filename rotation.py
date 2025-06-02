import numpy as np

def rotation(theta_x, theta_y, theta_z):
    """
    Returns a 3x3 rotation matrix for given angles around x, y, and z axes.
    
    Parameters:
    theta_x (float): rotation angle around X-axis (in radians)
    theta_y (float): rotation angle around Y-axis (in radians)
    theta_z (float): rotation angle around Z-axis (in radians)
    
    Returns:
    numpy.ndarray: 3x3 rotation matrix
    """
    # Rotation around X-axis
    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(theta_x), -np.sin(theta_x)],
        [0, np.sin(theta_x), np.cos(theta_x)]
    ])

    # Rotation around Y-axis
    Ry = np.array([
        [np.cos(theta_y), 0, np.sin(theta_y)],
        [0, 1, 0],
        [-np.sin(theta_y), 0, np.cos(theta_y)]
    ])

    # Rotation around Z-axis
    Rz = np.array([
        [np.cos(theta_z), -np.sin(theta_z), 0],
        [np.sin(theta_z), np.cos(theta_z), 0],
        [0, 0, 1]
    ])

    # Combined rotation matrix
    rotmat = Rx @ Ry @ Rz  # Matrix multiplication using @ operator

    return rotmat

