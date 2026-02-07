import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

MODEL = "models/hand_landmarker.task"

BaseOptions = python.BaseOptions
HandLandmarker = vision.HandLandmarker
HandLandmarkerOptions = vision.HandLandmarkerOptions
VisionRunningMode = vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=MODEL),
    running_mode=VisionRunningMode.IMAGE,
    num_hands=2
)

landmarker = HandLandmarker.create_from_options(options)

prev = None

def gesture_score(image):

    global prev

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
    result = landmarker.detect(mp_image)

    if not result.hand_landmarks:
        return 40

    wrist = result.hand_landmarks[0][0]

    if prev is None:
        prev = wrist
        return 50

    movement = abs(wrist.x - prev.x) + abs(wrist.y - prev.y)
    prev = wrist

    if movement < 0.01:
        return 40     # too little

    if movement > 0.05:
        return 60     # too much

    return 90         # natural
