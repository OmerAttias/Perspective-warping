# Perspective-warping

Plant an image within a video on top of existing image while adjusting the dynamic perspective of the original image in the video.

- The main goal for this project is to get to know the augmented reality world.

-  The mission was to take a random image and implement it on a video which contain another image. The new implemented image should "behave" in identical dynamic perspective ratio to the original one for the entier video.

- For the explanation let's call the original image "template image" and for the new image "target image".

  - Target image:
  
    <img src="https://user-images.githubusercontent.com/101269937/190626910-54b78195-f7c1-4209-8900-88848a1a0be0.jpg" width="150" height="200">

  - Template image:
  
    <img src="https://user-images.githubusercontent.com/101269937/190627203-ca49c9f2-938f-44c7-a6fe-edc4d18e231f.jpeg" width="150" height="200">






- first i took a single frame from the video in order to analyze the template image. i change the image color model from RGB to gray scale and search for "Key points". at the same time i took the same image but non video one and analyzed it in the same way as the cutted one (i didnt use the target image phot yet but only the cutted image from the video and another same image but not from the video).
- Each of all the detected keypoints need to be a unique fingerprint. The algorithm must find the feature again in a different image. This might have a different perspective, lightning situation, etc. Even under these circumstances, a match has to be possible.
- the cuted single frame will be compared to the original non video image. every key point from one image passing throgh the other image keypoints and the colser one are cosidere a match.


-after finding the mached keypoints, i created the homography matrix which is a magic matrix suppose to take into account Perspective-warping of the tamplates image. 

- ones we have the homography matrix we can implement the target image on top of the tamplaete one and creating a new video.
- at this point, the only image that projected on the new video is the image itself. the backround didnt pass to the new video and it need to manually implement on the new video.

<img src="https://user-images.githubusercontent.com/101269937/190387214-c057423b-1352-4f03-af55-8d9f55fd5d20.jpg" width="250" height="200">
