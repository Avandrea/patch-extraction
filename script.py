import cv2
import numpy
import os

def get_patches_and_labels(imagesPath="images",
                           PositivePointsPath="points/PositivePoints.txt", 
                           height, width):
    imageNames = os.listdir(imagesPath)
    labels = []
    vector = []
    patches = []
    halfHeight = int(height/2)
    halfWidth = int(width/2)
    positive_file = open(PositivePointsPath, "r")

    lines = (positive_file.readlines())
    for a in range(0, len(lines)):
        word = str.split(lines[a], sep="\t")
        if word[1].endswith('\n'):
            word[1] = word[1][:-1]
        vector.append(word)
    cv2.namedWindow('W1', 1)

    for imageName in imageNames:
        fullImagePath = os.path.join(imagesPath, imageName)
        img = cv2.imread(fullImagePath)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        cv2.imshow('W1', img)
        cv2.waitKey(30)
        patch = [None] * len(vector)
        label = [None] * len(vector)
        k = 0
        for i in range(0, len(vector)):
            if (int(vector[i][1]) - halfHeight) < 0 or (int(vector[i][1]) + halfHeight) > img.shape[0] or (
                        int(vector[i][0]) - halfWidth) < 0 or (int(vector[i][0]) + halfWidth) > img.shape[1]:
                continue
            rect = numpy.copy(
                img[int(vector[i][1]) - halfHeight:int(vector[i][1]) + halfHeight,
                int(vector[i][0]) - halfWidth:int(vector[i][0]) + halfWidth])
            patch[k] = rect
            label[k] = 1
            k += 1
        patches.extend(patch)
        labels.extend(label)
        
    for ii in range (0, len(patches)):
        cv2.imwrite('output/' + str(ii) + '.jpeg', patches[ii])

    print("There are " + str(len(patches)) + " patches and " + str(len(labels)) + " labels")
    print("The patches have size " + str(patches[0].shape))
    return patches, labels
