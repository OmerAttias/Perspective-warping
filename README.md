# "Perspective-warping"

## Description

**Plant an image within a video on top of existing image while adjusting the dynamic perspective of the original image in the video.**

## Installation packages

```python

import cv2
import numpy as np

```

## Quick review :man_cartwheeling:	

- The main goal for this project is to have an Initial introduction with the basics of the augmented reality world.

-  The mission was to take a random image and implement it on a video which contain another image. The new implemented image should "behave" in identical dynamic perspective ratio to the original one for the entier video.

- For the explanation let's call the original image "target image" and to the implemented desire image "Template image".

  - Target image:
    <p align="center">
    <img src="https://user-images.githubusercontent.com/101269937/190626910-54b78195-f7c1-4209-8900-88848a1a0be0.jpg" width="150" height="200">
    </p>


  - Template image:
  
    <p align="center">
    <img src="https://user-images.githubusercontent.com/101269937/190627203-ca49c9f2-938f-44c7-a6fe-edc4d18e231f.jpeg" width="150" height="200">
    </p>


- First i took a single frame from the video in order to analyze the target image. i change the image color model from RGB to gray scale and search for "Key points". at the same time i took the same visually image but not from the video and analyzed it in the same way as the cutted one (i didnt use the template image photo yet).

  <p align="center">
  <img src="https://user-images.githubusercontent.com/101269937/190628720-235e647a-88b4-46b3-94d1-9a67d727a36b.jpg" width="220" height="250">
  </p>
  
  <p align="center">
  <img src="https://user-images.githubusercontent.com/101269937/190628763-1c6c64ec-c609-4bd6-8aa7-f292db356cd8.jpg" width="220" height="250">
  </p>



> Each of all the detected keypoints need to be a unique fingerprint. The algorithm must find the feature again in a different image. This might have a different perspective, lightning situation, etc. Even under these circumstances, a match has to be possible. For more inforamtion, see https://www.andreasjakl.com/basics-of-ar-anchors-keypoints-feature-detection/

- The cutted single frame will be compared to the original non video image. every key point from one image Passes through the other image keypoints and the closest one are considerd a match.

    <p align="center">
    <img src="https://user-images.githubusercontent.com/101269937/190629042-eb7fce77-e76f-42d6-b796-88720fb61da1.jpg" width="400" height="200">
    </p>


- After finding the matched keypoints, i created the homography matrix which is a "magic" matrix which take into account Perspective-warping of the target image. 
    <p align="center">
    <img src="https://user-images.githubusercontent.com/101269937/190629105-991db5a6-d959-4182-bbbb-e1fa7483d399.jpg" width="350" height="100">
    </p>


- Ones we have the homography matrix we can implement the template image on top of the target one and creating a new video.

- At this point, the only image that projected on the new video is the image itself. The background didn't pass to the new video and it needs a manually implementation on the new video.
  <p align="center">
  <img src="https://user-images.githubusercontent.com/101269937/190629262-4508e234-4e98-46d4-b39d-a2be9d8022ad.jpg" width="350" height="200">
  </p>

      
## Final video result:

 https://www.youtube.com/watch?v=kKpuiPszo1I&feature=youtu.be
      
