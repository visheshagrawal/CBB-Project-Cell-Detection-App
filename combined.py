import cv2 
import numpy as np 
#import argparse

# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,
#	help="path to the image file")
#args = vars(ap.parse_args())
def process():
	raw_image = cv2.imread('1.png')
	#cv2.imshow('Original Image', raw_image)
	#cv2.waitKey(0)

	bilateral_filtered_image = cv2.bilateralFilter(raw_image, 5, 175, 175)
	#cv2.imshow('Bilateral', bilateral_filtered_image)
	#cv2.waitKey(0)

	edge_detected_image = cv2.Canny(bilateral_filtered_image, 10, 200)
	#cv2.imshow('Edge', edge_detected_image)
	#cv2.waitKey(0)


	image = edge_detected_image
	# Set our filtering parameters 
	# Initialize parameter settiing using cv2.SimpleBlobDetector 
	params = cv2.SimpleBlobDetector_Params() 

	# Set Area filtering parameters 
	params.filterByArea = True
	params.minArea = 9

	# Set Circularity filtering parameters 
	params.filterByCircularity = True
	params.minCircularity = 0.01

	# Set Convexity filtering parameters 
	params.filterByConvexity = False
	params.minConvexity = 0.1
		
	# Set inertia filtering parameters 
	params.filterByInertia = False
	params.minInertiaRatio = 0.01

	# Create a detector with the parameters 
	detector = cv2.SimpleBlobDetector_create(params) 
		
	# Detect blobs 
	keypoints = detector.detect(image) 

	# Draw blobs on our image as red circles 
	blank = np.zeros((1, 1)) 
	blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255), 
							cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) 

	number_of_blobs = len(keypoints) 
	text = "Number of Circular Blobs: " + str(len(keypoints)) 
	print(str(len(keypoints)))
	cv2.putText(blobs, text, (20, 550), 
				cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2) 

	# Show blobs 
	cv2.imshow("Filtering Circular Blobs Only", blobs) 
	cv2.waitKey(0) 
	cv2.destroyAllWindows() 
	return number_of_blobs
