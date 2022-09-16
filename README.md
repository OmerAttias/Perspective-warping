# Perspective-warping
Plant an image within a video on top of existing image while adjusting the dynamic perspective of the original image in the video


- the main goal for this project is to get to know the agumented rality world.
- the mission was to take a random image and implement it on a video which contain another image. the new implemented image should "behave" in an identical dynamic perspective  to the original one.
- For the explantion lets call the original image "template image" and for the new image "target image".
- first i took a single frame from the video in order to analyze the template image. i change the image color model from RGB to gray scale and search for "Key points". at the same time i took the same image but non video one and analyzed it in the same way as the cutted one (i didnt use the target image phot yet but only the cutted image from the video and another same image but not from the video).
- Each of all the detected keypoints need to be a unique fingerprint. The algorithm must find the feature again in a different image. This might have a different perspective, lightning situation, etc. Even under these circumstances, a match has to be possible.
- the cuted single frame will be compared to the original non video image. every key point from one image passing throgh the other image keypoints and the colser one are cosidere a match.


-after finding the mached keypoints, i created the homography matrix which is a magic matrix suppose to take into account Perspective-warping of the tamplates image. 

- ones we have the homography matrix we can implement the target image on top of the tamplaete one and creating a new video.
- at this point, the only image that projected on the new video is the image itself. the backround didnt pass to the new video and it need to manually implement on the new video.

