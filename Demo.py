import script

patches, _ = script.get_patches_and_labels(imagesPath="Images", PositivePointsPath="Points/PositivePoints.txt", 32, 32)
cv2.namedWindow("window1", 1)
cv2.imshow(window1, patches[0])
cv2.waitKey(0)
