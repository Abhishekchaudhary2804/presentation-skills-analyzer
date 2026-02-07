import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

MODEL = "models/face_landmarker.task"

BaseOptions = python.BaseOptions
FaceLandmarker = vision.FaceLandmarker
FaceLandmarkerOptions = vision.FaceLandmarkerOptions
VisionRunningMode = vision.RunningMode

options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=MODEL),
    running_mode=VisionRunningMode.IMAGE,
    num_faces=1
)

landmarker = FaceLandmarker.create_from_options(options)

def eye_contact(image):

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)

    result = landmarker.detect(mp_image)

    if not result.face_landmarks:
        return False

    landmarks = result.face_landmarks[0]

    left = landmarks[33]
    right = landmarks[263]

    cx = (left.x + right.x) / 2

    return 0.45 < cx < 0.55
