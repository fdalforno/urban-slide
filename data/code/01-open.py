import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, help='video path', default='..\video.mp4')
args = parser.parse_args()

print('Loading file {}.'.format(args.input))
capture = cv2.VideoCapture(args.input)

if not capture.isOpened():
    print('Unable to open: ' + args.input)
    exit(0)

while True:
    ret, frame = capture.read()
    if frame is None:
        break
    
    cv2.imshow("tracker output", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()