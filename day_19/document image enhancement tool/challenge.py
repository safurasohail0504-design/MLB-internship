import os
import cv2
import numpy as np

input_dir="C:/Users/User/Documents/GitHub/day_19/Input Images/"
output_dir="C:/Users/User/Documents/GitHub/day_19/Document Image Enhancement Tool/Challenge Output Images/"

images=[
"challenge1.jpg",
"challenge2.jpeg",
"challenge3.webp",
"challenge4.webp",
"challenge5.jpg"
]

def order_points(pts):
    rect=np.zeros((4,2),dtype="float32")
    s=pts.sum(axis=1)
    rect[0]=pts[np.argmin(s)]
    rect[2]=pts[np.argmax(s)]
    diff=np.diff(pts,axis=1)
    rect[1]=pts[np.argmin(diff)]
    rect[3]=pts[np.argmax(diff)]
    return rect

def perspective(img):
    h,w=img.shape[:2]

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)

    edge=cv2.Canny(blur,30,150)

    kernel=np.ones((5,5),np.uint8)
    edge=cv2.dilate(edge,kernel,iterations=2)
    edge=cv2.erode(edge,kernel,iterations=1)

    contours,_=cv2.findContours(edge,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    contours=sorted(contours,key=cv2.contourArea,reverse=True)

    page=None
    area=h*w

    for c in contours:
        if cv2.contourArea(c)<area*0.10:
            continue

        peri=cv2.arcLength(c,True)
        approx=cv2.approxPolyDP(c,0.02*peri,True)

        if len(approx)==4:
            page=approx
            break

    if page is None:
        return img

    pts=page.reshape(4,2).astype("float32")

    center=np.mean(pts,axis=0)
    pts=center+(pts-center)*1.08

    rect=order_points(pts)

    tl,tr,br,bl=rect

    widthA=np.linalg.norm(br-bl)
    widthB=np.linalg.norm(tr-tl)
    maxWidth=max(int(widthA),int(widthB))

    heightA=np.linalg.norm(tr-br)
    heightB=np.linalg.norm(tl-bl)
    maxHeight=max(int(heightA),int(heightB))

    dst=np.array([
        [0,0],
        [maxWidth-1,0],
        [maxWidth-1,maxHeight-1],
        [0,maxHeight-1]
    ],dtype="float32")

    matrix=cv2.getPerspectiveTransform(rect,dst)

    warp=cv2.warpPerspective(img,matrix,(maxWidth,maxHeight))

    return warp

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for file in images:

    path=os.path.join(input_dir,file)

    img=cv2.imread(path)

    if img is None:
        print(file,"not found")
        continue

    corrected=perspective(img)

    gray=cv2.cvtColor(corrected,cv2.COLOR_BGR2GRAY)

    blur=cv2.GaussianBlur(gray,(5,5),0)

    bright=cv2.convertScaleAbs(blur,alpha=1.0,beta=35)

    contrast=cv2.convertScaleAbs(bright,alpha=1.3,beta=0)

    kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])

    sharp=cv2.filter2D(contrast,-1,kernel)

    cv2.imwrite(os.path.join(output_dir,"corrected_"+file),corrected)
    cv2.imwrite(os.path.join(output_dir,"enhanced_"+file),sharp)

    cv2.imshow("Original",img)
    cv2.imshow("Perspective Corrected",corrected)
    cv2.imshow("Final Enhanced",sharp)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("Challenge task completed successfully.")