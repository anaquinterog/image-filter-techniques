import cv2
from cvlib import read_image, visualise_image
import os

def apply_median_filter(image, kernel_size=3):
     """
    MEDIAN FILTER 
    inputs:
    image (numpy.ndarray): Input image.
    kernel_size (int): Size of the kernel for median filtering. Default is 3.

    outputs:
    numpy.ndarray: Median filtered image.
    """
    return cv2.medianBlur(image, kernel_size)

def apply_average_filter(image, kernel_size=(3, 3)):
    """
    AVG FILTER

    inputs:
    image (numpy.ndarray): Input image.
    kernel_size (tuple): Size of the kernel for averaging. Default is (3, 3).

    outputs:
    numpy.ndarray: Average filtered image.
    """
    return cv2.blur(image, kernel_size)

def apply_gaussian_filter(image, kernel_size=(3, 3), sigmaX=0):
     """
    GAUSSIAN FILTER
    inputs:
    image (numpy.ndarray): Input image.
    kernel_size (tuple): Size of the kernel for Gaussian filtering. Default is (3, 3).
    sigmaX (float): Standard deviation in X direction. Default is 0.

    outputs:
    numpy.ndarray: Gaussian filtered image."""
    return cv2.GaussianBlur(image, kernel_size, sigmaX)

if __name__ == "__main__":
    # Define the path to the image
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    image_path = '.../newcastle-beach.jpeg'

    # Read the image
    image = read_image(image_path)

    #  median filter
    median_filtered = apply_median_filter(image)

    #  average filter
    average_filtered = apply_average_filter(image)

    #  Gaussian filter
    gaussian_filtered = apply_gaussian_filter(image)

    # Visualize the original and filtered images
    visualize_image(image, "Original Image")
    visualize_image(median_filtered, "Median Filtered Image")
    visualize_image(average_filtered, "Average Filtered Image")
    visualize_image(gaussian_filtered, "Gaussian Filtered Image")
