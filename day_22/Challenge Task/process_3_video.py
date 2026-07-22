import os
import cv2
script_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(script_dir, "Input Videos")
output_dir = os.path.join(script_dir, "Output Videos")
videos = ["video1.mp4", "video2.mp4", "video3.mp4"]
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
for vid in videos:
    in_path = os.path.join(input_dir, vid)
    cap = cv2.VideoCapture(in_path)
    if not cap.isOpened():
        continue
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = 30.0
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out_orig_path = os.path.join(output_dir, "original_" + vid)
    out_proc_path = os.path.join(output_dir, "processed_" + vid)
    out_orig = cv2.VideoWriter(out_orig_path, fourcc, fps, (w, h), True)
    out_proc = cv2.VideoWriter(out_proc_path, fourcc, fps, (w, h), True)
    win1 = "Original Video"
    win2 = "Processed Video"
    cv2.namedWindow(win1, cv2.WINDOW_NORMAL)
    cv2.namedWindow(win2, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(win1, 640, 360)
    cv2.resizeWindow(win2, 640, 360)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blur, 50, 150)
        edges_color = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        out_orig.write(frame)
        out_proc.write(edges_color)
        cv2.imshow(win1, frame)
        cv2.imshow(win2, edges_color)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    cap.release()
    out_orig.release()
    out_proc.release()
    cv2.destroyAllWindows()