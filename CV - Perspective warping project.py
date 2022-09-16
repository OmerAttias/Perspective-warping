import cv2.cv2
import numpy as np

# calling the target image and change model from rgb to gray
RGB_Target = cv2.imread('ImageTarget.jpeg')
GRAY_Taregt = cv2.cvtColor(RGB_Target,cv2.COLOR_BGR2GRAY)
#RGB_Target = cv2.resize(RGB_Target, (700, 600))

# calling the template image and change model from rgb to gray
RGB_Template = cv2.imread('ImageTemp.jpeg')
GRAY_Template = cv2.cvtColor(RGB_Template,cv2.COLOR_BGR2GRAY)
#RGB_Template = cv2.resize(RGB_Template, (700, 600))

# run sift detection on the target image to find set of features that
# characterize a small image region around the point
# this features are invariant to img changes
sift = cv2.SIFT_create()
kp_Target, des_Target = sift.detectAndCompute(GRAY_Taregt,None)
# print the keypoint and the area they cover
KeyPoint_Target = cv2.drawKeypoints(RGB_Target, kp_Target, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#calling the video function
Video = cv2.VideoCapture('videobook.mp4')


while True:
    # read frame by frame
    ret, VideoImg = Video.read()
    hT, wT, cT = VideoImg.shape
    #VideoImg = cv2.resize(VideoImg, (700,600))


    # changing color model to video image before sifting action
    Gray_VideoImg = cv2.cvtColor(VideoImg,cv2.COLOR_BGR2GRAY)
    #print(VideoImg.shape)

    #sift on the video img
    kp_VideoImg, des_VideoImg = sift.detectAndCompute(Gray_VideoImg, None)
    KeyPoint_VideoImg = cv2.drawKeypoints(VideoImg, kp_VideoImg, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


    # after sifting the target and the video img
    # we do a cross between the descriptors, were one
    # from the first image comparing to th rest of the second
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des_Target,des_VideoImg, k=2)
    GoodMatch =[]
    # create a list of descriptors that were most fit for us
    # via a ratio test
    for m, n in matches:
        if m.distance < 0.5 * n.distance:
            GoodMatch.append(m)
    print(len(GoodMatch))
    imgFeatures = cv2.drawMatches(RGB_Target,kp_Target,VideoImg,kp_VideoImg,GoodMatch, None, flags=4)

    # if there are enouth maches
    # we sorting the results from goodMatch list to
    # the write key points from the target and the video images
    if len(GoodMatch) > 20:
        srcPts = np.float32([kp_Target[m.queryIdx].pt for m in GoodMatch]).reshape(-1,1,2)
        dstPts = np.float32([kp_VideoImg[m.trainIdx].pt for m in GoodMatch]).reshape(-1,1,2)
    # do the homography action witch is basically
    # a matrix that maps the points in one image
    # to the correspodnig points in the other image
        HomographyMat, mask = cv2.findHomography(srcPts,dstPts, cv2.RANSAC, 5)
        print(HomographyMat)


    # after the homography we do the intigration
    # of the template image to the video according to
    # the "H" matrix
        WarpImage = cv2.warpPerspective(RGB_Template, HomographyMat,(VideoImg.shape[1],
                                      VideoImg.shape[0]))

    # warp the empty areas with the original video backround
        VideoImg_copy = VideoImg.copy()

        VideoImg_copy = WarpImage
        mask = (VideoImg_copy == 0)
        WarpImage[mask] = VideoImg[mask]


        #cv2.imshow('WarpImage',WarpImage)
        cv2.imshow('ImageTarget',WarpImage)
        #cv2.imshow('ImageTemplate',KeyPoint_Target)
        #cv2.imshow('VideoImg',imgFeatures)
        cv2.waitKey(1)
