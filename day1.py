# -*- coding:utf-8 -*-
# author:zpy time:2020/8/1  11:34
# file:day1.py
# software:{PyCharm}
# start = datetime.datetime.now()
# end = datetime.datetime.now()
# print('final is in:%s seconds' % (end - start))


# read & show image
import cv2 as cv


img = cv.imread('opencv.jpg')
cv.namedWindow('img', cv.WINDOW_AUTOSIZE)
cv.imshow('img', img)
cv.imwrite('image.jpg',img)

cv.waitKey()
cv.destroyAllWindows()
