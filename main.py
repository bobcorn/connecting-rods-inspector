#!/usr/bin/env python
"""
Main execution file.
"""

import cv2
import utils
import numpy as np

__author__ = "Marco Rossini"
__copyright__ = "Copyright 2020, Marco Rossini"
__date__ = "2020/05"
__license__ = "MIT"
__version__ = "1.0"

# ----------------------------------------------------------------------------------------------------------------------

# Read and store all images into an array
images, file_names = utils.get_images_as_array()

# Iterate over all images
for i, image in enumerate(images):
    # Show current image and print its name
    utils.show_image(file_names[i], image)
    utils.print_image_info(file_names[i])

    # Apply a median blur four times to remove disturbing dust and refine edges
    image = utils.median_blur(image, 3, 4)

    # Binarize the image to separate foreground and background
    threshold, binarized = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Show binarized image
    utils.show_image(file_names[i], binarized)

    # Check for touching objects and separate them if needed, specifying a timeout of 1 iteration (customisable)
    binarized = utils.separate_touching_objects(binarized, 1)

    # We may consider performing a dilation to re-join any unintentionally broken contours by the previous
    # operation, which may lead to a classification error of the rod type (uncomment to apply)
    # component = cv2.dilate(component, np.ones((3, 3), np.uint8), iterations=1)

    # Create a RGB copy of the current image for visualisation purposes
    display = cv2.cvtColor(binarized.copy(), cv2.COLOR_GRAY2RGB)

    # Perform a connected components labeling on separated components
    retval, labels, stats, centroids = cv2.connectedComponentsWithStats(binarized, 4)

    # Iterate over the detected components to analyse every single object
    # (range starts from 1 to exclude outer background)
    for w in range(1, retval):
        # Isolate current binarized component
        component = utils.get_component(labels, w)

        # Perform a second connected components labeling on every (inverted) component to detect holes
        retval_in, labels_in, stats_in, centroids_in = cv2.connectedComponentsWithStats(255 - component, 4)

        # Initialize an empty array to store holes information
        holes = []

        # Iterate over the detected inner components to analyse every single hole
        # (range starts from 2 to exclude outer background)
        for j in range(2, retval_in):
            # Get component's diameter
            diameter = utils.get_hole_diameter(stats_in[j][4])

            # Create and store the hole object into the array
            hole = (centroids_in[j], diameter)
            holes.append(hole)

        # Compute component's moments and orientation
        moments = cv2.moments(component, True)
        angle = utils.get_angle(moments)

        # If 'get_angle' returns 'None' the component is a spurious shape, so ignore it
        if not angle:
            continue

        # Get component's oriented MER
        mer, length, width = utils.get_oriented_mer(component, angle, centroids[w])

        # If current component is not a rod, ignore it
        if utils.is_not_a_rod(length, width, holes):
            continue

        else:
            # Assign a random color to the component for visualisation purposes
            display = utils.color_component(display, labels, w)

            # Iterate over every detected hole to draw its information (not actually needed, just for visualisation)
            for j in range(2, retval_in):
                # Isolate current binarized component (not actually needed, just for visualisation)
                component_in = utils.get_component(labels_in, j)

                # Compute component's moments and orientation (not actually needed, just for visualisation)
                moments_in = cv2.moments(component_in, True)
                angle_in = utils.get_angle(moments_in)

                # Get component's oriented MER (not actually needed, just for visualisation)
                mer_in, length_in, width_in = utils.get_oriented_mer(component_in, angle_in, centroids_in[j])

                # Draw component's centroid and MER (not actually needed, just for visualisation)
                utils.draw_centroid(display, centroids_in[j])
                utils.draw_oriented_mer(display, mer_in)

            # Get rod's width at barycenter
            bar_points, bar_width = utils.get_barycenter_width(component, angle, centroids[w])

            # Draw rod's information (centroid, MER, major orientation axis and width at barycenter)
            utils.draw_centroid(display, centroids[w])
            utils.draw_oriented_mer(display, mer)
            utils.draw_orientation_axis(display, centroids[w], angle, length)
            utils.draw_barycenter_width(display, bar_points)

        # Print current rod information and show it
        utils.print_rod_info(centroids[w], mer, angle, length, width, bar_width, holes)
        utils.show_image(file_names[i], display)
