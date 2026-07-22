import cv2

video=cv2.VideoCapture("input video/sample_video.mp4")

fps=video.get(cv2.CAP_PROP_FPS)
width=video.get(cv2.CAP_PROP_FRAME_WIDTH)
height=video.get(cv2.CAP_PROP_FRAME_HEIGHT)
frames=video.get(cv2.CAP_PROP_FRAME_COUNT)

print("FPS:",fps)
print("Width:",width)
print("Height:",height)
print("Total Frames:",frames)

while True:

    ret,frame=video.read()

    if not ret:
        break

    frame=cv2.resize(frame,(900,500))

    cv2.imshow("Video",frame)

    if cv2.waitKey(30)&0xFF==ord('q'):
        break

video.release()
cv2.destroyAllWindows()