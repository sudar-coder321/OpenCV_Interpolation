import cv2
import sys #for the command line arguments


print(cv2.__version__)
 
path=sys.argv[1]

#path = r'C:\Users\Sudarshan.M.S\Desktop\img1opencv.jpeg'

print('The path is :',path)

img = cv2.imread(path)

img1 = cv2.imread(path,0)

if img is None:
    print('There is no image')
else:
    print('Valid image')

img=cv2.resize(img,(500,500))

welcome_msg='im fine'

print(f'How are you? {welcome_msg}')

cv2.imwrite('img3opencv.jpg',img)

cv2.imshow('img2opencv.jpg',img)

cv2.imshow('BlackandWhiterose.jpg',img1)
#width,height,channels

h,w,c = img.shape

print('height is ',h)
print('weight is ',w)
print('channel is',c)

cv2.waitKey(0)

