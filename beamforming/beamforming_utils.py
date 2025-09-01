import numpy as np


def create_ula_positions(num_elements, d):
    """
    Create a uniform linear array (ULA) along the x-axis.

    Args:
        num_elements (int): Number of antenna elements.
        d (float): Spacing between elements (in meters).

    Returns:
        np.ndarray: (N,) array of antenna element positions.
    """
    return np.arange(num_elements) * d


def steering_vector(positions, wavelength, angle_deg):
    """
    Compute the steering vector for a given angle.

    Args:
        positions (np.ndarray): Antenna element positions (1D array).
        wavelength (float): Wavelength of the carrier signal.
        angle_deg (float): Steering angle in degrees.

    Returns:
        np.ndarray: Complex-valued steering vector.
    """
    angle_rad = np.radians(angle_deg)
    phase_shifts = 2 * np.pi * positions * np.sin(angle_rad) / wavelength
    return np.exp(1j * phase_shifts)


def array_factor(weights, positions, wavelength, scan_angles_deg):
    """
    Compute the array factor across a range of scan angles.

    Args:
        weights (np.ndarray): Beamforming weights (complex-valued).
        positions (np.ndarray): Antenna element positions.
        wavelength (float): Wavelength of the signal.
        scan_angles_deg (np.ndarray): Angles to scan (in degrees).

    Returns:
        np.ndarray: Normalized array factor (magnitude only).
    """
    AF = []
    for angle in scan_angles_deg:
        sv = steering_vector(positions, wavelength, angle)
        response = np.dot(weights, sv.conj())
        AF.append(np.abs(response))
    AF = np.array(AF)
    return AF / np.max(AF)  # normalize
