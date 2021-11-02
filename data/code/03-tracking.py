import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, help='video path', default='../video.mp4')
parser.add_argument('--tracker', type=str, help='tracker', default='csrt')
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




# initialize a dictionary that maps strings to their corresponding
# OpenCV object tracker implementations
OPENCV_OBJECT_TRACKERS = {
    "csrt": cv2.TrackerCSRT_create,
    "kcf": cv2.TrackerKCF_create,
    "boosting": cv2.TrackerBoosting_create,
    "mil": cv2.TrackerMIL_create,
    "tld": cv2.TrackerTLD_create,
    "medianflow": cv2.TrackerMedianFlow_create,
    "mosse": cv2.TrackerMOSSE_create
}
# grab the appropriate object tracker using our dictionary of
# OpenCV object tracker objects
tracker = OPENCV_OBJECT_TRACKERS[args.tracker]()

bbox = None
while True:
    ret, frame = capture.read()
    if frame is None:
        break

    frame = rescale_frame(frame,0.5)

    if bbox:
        (success, box) = tracker.update(frame)
        if success:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x + w, y + h),(0, 255, 0), 2)
    


    cv2.imshow("tracker output", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

    if key == ord("s"):
        bbox = cv2.selectROI(frame)
        tracker.init(frame, bbox)
    

capture.release()
cv2.destroyAllWindows()