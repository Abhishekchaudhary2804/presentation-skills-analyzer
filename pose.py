import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

MODEL = "models/pose_landmarker.task"

BaseOptions = python.BaseOptions
PoseLandmarker = vision.PoseLandmarker
PoseLandmarkerOptions = vision.PoseLandmarkerOptions
VisionRunningMode = vision.RunningMode

options = PoseLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=MODEL),
    running_mode=VisionRunningMode.IMAGE
)

landmarker = PoseLandmarker.create_from_options(options)

def posture_score(image):

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
    result = landmarker.detect(mp_image)

    if not result.pose_landmarks:
        return 50

    lm = result.pose_landmarks[0]

    left = lm[11]
    right = lm[12]
    nose = lm[0]

    shoulder_diff = abs(left.y - right.y)
    head_forward = abs(nose.z)

    score = 100

    if shoulder_diff > 0.05:
        score -= 20

    if head_forward > 0.3:
        score -= 30

    return max(score, 40)
