import cv2
import pandas as pd
from face import eye_contact
from pose import posture_score
from hands import gesture_score
from scoring import confidence_score, generate_tips
from pdf_report import generate_pdf

cap = cv2.VideoCapture(0)

total = 0
eye = 0
session = []

while True:

    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    total += 1

    if eye_contact(rgb):
        eye += 1

    eye_score = int((eye/(total+1))*100)
    posture = posture_score(rgb)
    gesture = gesture_score(rgb)

    confidence = confidence_score(eye_score, posture, gesture)

    session.append([eye_score, posture, gesture, confidence])

    cv2.putText(frame,f"Eye: {eye_score}%",(20,40),
                cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)

    cv2.putText(frame,f"Posture: {posture}",(20,80),
                cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),2)

    cv2.putText(frame,f"Gesture: {gesture}",(20,120),
                cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)

    cv2.putText(frame,f"Confidence: {confidence}",(20,160),
                cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,0),2)

    cv2.imshow("Presentation Analyzer",frame)

    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# ===== Session Summary =====

df = pd.DataFrame(session, columns=["Eye","Posture","Gesture","Confidence"])
df.to_csv("session.csv", index=False)
import matplotlib.pyplot as plt

df.plot(title="Presentation Skill Session")
plt.xlabel("Frames")
plt.ylabel("Score")
plt.show()


final_eye = df["Eye"].mean()
final_posture = df["Posture"].mean()
final_gesture = df["Gesture"].mean()
final_conf = df["Confidence"].mean()

scores = {
    "Eye Contact": int(final_eye),
    "Posture": int(final_posture),
    "Gesture": int(final_gesture),
    "Confidence": int(final_conf)
}

tips = generate_tips(final_eye, final_posture, final_gesture)

generate_pdf(scores, tips)

print("Session saved + PDF generated.")
