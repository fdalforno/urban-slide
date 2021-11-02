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


def rescale_frame(frame, percent=0.75):
    width = int(frame.shape[1] * percent)
    height = int(frame.shape[0] * percent)
    dim = (width, height)
    #print(dim)
    return cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

frame_count = 0
frame_old = None
while True:
    ret, frame = capture.read()
    if frame is None:
        break
    
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = rescale_frame(gray,0.5)

    if frame_count > 0:
        frame_diff = cv2.absdiff(gray, frame_old)
        cv2.imshow('frame', frame_diff)
        #cv2.imwrite("frame%d.jpg" % frame_count, frame_diff)
        
    frame_old = gray
    frame_count += 1

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()