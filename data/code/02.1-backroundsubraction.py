import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, help='video path', required=True)
parser.add_argument('--algo', type=str, help='Background subtraction method (KNN, MOG2).', default='MOG2')

args = parser.parse_args()

def rescale_frame(frame, percent=0.75):
    width = int(frame.shape[1] * percent)
    height = int(frame.shape[0] * percent)
    dim = (width, height)
    #print(dim)
    return cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)



print('Loading file {}.'.format(args.input))
capture = cv2.VideoCapture(args.input)

if not capture.isOpened():
    print('Unable to open: ' + args.input)
    exit(0)

OPENCV_BACKGROUND_SUBTRACTION = {
    "MOG2": cv2.createBackgroundSubtractorMOG2,
    "KNN": cv2.createBackgroundSubtractorKNN
}


backSub = OPENCV_BACKGROUND_SUBTRACTION[args.algo]()

while True:
    ret, frame = capture.read()
    if frame is None:
        break

    frame = rescale_frame(frame,0.5)

    fgMask = backSub.apply(frame)
    cv2.imshow('frame', fgMask)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()