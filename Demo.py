import script
import cv2

patches, _ = script.get_patches_and_labels(50, 200)
cv2.namedWindow("window1", 1)
cv2.imshow("window1", patches[0])
cv2.waitKey(0)
