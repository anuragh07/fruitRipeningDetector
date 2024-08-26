#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
ripe_lower=np.array([0, 100, 0]) 
ripe_upper=np.array([60, 255, 60])
unripe_lower=np.array([0, 0, 100])
unripe_upper=np.array([80, 80, 255])
cam=cv2.VideoCapture(0)
while True:
    ret, frame=cam.read()
    if not ret:
        break
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    ripe_mask=cv2.inRange(hsv, ripe_lower, ripe_upper)
    unripe_mask=cv2.inRange(hsv, unripe_lower, unripe_upper)
    result_mask=ripe_mask + unripe_mask
    result=cv2.bitwise_and(frame, frame, mask=result_mask)
    ripe_pixel_count=cv2.countNonZero(ripe_mask)
    unripe_pixel_count=cv2.countNonZero(unripe_mask)
    if ripe_pixel_count>unripe_pixel_count:
        ripeness="Ripen"
    else:
        ripeness="Unripen"
    cv2.putText(result, f'Ripeness: {ripeness}', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (204,0,0), 2)
    cv2.imshow('Fruit Ripeness Detection', result)
    if cv2.waitKey(1)&0xFF==27:
        break
cam.release()
cv2.destroyAllWindows()

