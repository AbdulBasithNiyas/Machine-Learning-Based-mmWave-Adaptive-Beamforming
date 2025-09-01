import numpy as np


def create_ula_positions(num_elements, d):
    """
    Generate element positions for a Uniform Linear Array (ULA).

    Args:
        num_elements (int): Number of antenna elements.
        d (float): Spacing between elements (in meters).

    Returns:
        np.ndarray: 1D array of element positions along x-axis.
    """
    return np.arange(num_elements) * d


def create_upa_positions(rows, cols, dx, dy):
    """
    Generate element positions for a Uniform Planar Array (UPA).

    Args:
        rows (int): Number of rows in the array.
        cols (int): Number of columns in the array.
        dx (float): Spacing between columns (x-direction).
        dy (float): Spacing between rows (y-direction).

    Returns:
        np.ndarray: (rows*cols, 3) array of 3D positions (x, y, z).
    """
    x = np.arange(cols) * dx
    y = np.arange(rows) * dy
    xv, yv = np.meshgrid(x, y)
    z = np.zeros_like(xv)
    positions = np.stack([xv.ravel(), yv.ravel(), z.ravel()], axis=-1)
    return positions


def create_circular_array(num_elements, radius):
    """
    Generate element positions for a Circular Array (XY plane).

    Args:
        num_elements (int): Number of antenna elements.
        radius (float): Radius of the circle.

    Returns:
        np.ndarray: (num_elements, 3) array of 3D positions (x, y, z).
    """
    angles = np.linspace(0, 2 * np.pi, num_elements, endpoint=False)
    x = radius * np.cos(angles)
    y = radius * np.sin(angles)
    z = np.zeros_like(x)
    positions = np.stack([x, y, z], axis=-1)
    return positions
