Presentation & Communication Skills Analyzer

A real-time computer vision system that analyzes presentation skills using webcam or recorded video.
The system evaluates eye contact, posture, hand gestures, and overall confidence, then generates a CSV session log and PDF performance report with improvement tips.

Built using Python + OpenCV + MediaPipe Tasks API.
# Live Project LINK
#link- https://abhishek-chaudhary-g62jnwtsgak6qkfgw8ses3.streamlit.app/
🚀 Features

✅ Live webcam or recorded video support
✅ Eye contact / gaze stability analysis
✅ Posture & slouch detection
✅ Hand gesture usage scoring
✅ Overall confidence score (0–100)
✅ Rule-based improvement tips
✅ Session CSV export
✅ Automated PDF report generation

🧠 Skill Metrics

The system computes:

Eye Contact Score

Posture Score

Gesture Score

Confidence Score

Confidence is calculated as:

Confidence = 0.4 × Eye + 0.3 × Posture + 0.3 × Gesture

📁 Project Structure
presentation_analyzer/
│
├── main.py              # Main application
├── face.py              # Eye contact detection
├── pose.py              # Posture detection
├── hands.py             # Gesture detection
├── scoring.py           # Confidence + tips logic
├── pdf_report.py        # PDF generator
│
├── models/
│   ├── face_landmarker.task
│   ├── pose_landmarker.task
│   └── hand_landmarker.task
│
├── session.csv          # Auto-generated after run
├── session_report.pdf  # Final PDF report
└── README.md

🛠 Tech Stack

Python 3.11

OpenCV

MediaPipe Tasks API

NumPy

Pandas

ReportLab (PDF generation)

⚙ Installation
1. Create virtual environment (Python 3.11)
py -3.11 -m venv venv
venv\Scripts\activate

2. Install dependencies
pip install mediapipe opencv-python numpy pandas matplotlib reportlab

3. Download Models

Create folder:

models/


Download and place inside:

face_landmarker.task

pose_landmarker.task

hand_landmarker.task

(From MediaPipe official model zoo.)

▶ Run Application
python main.py


Press Q to stop session.

After exit:

session.csv is created

session_report.pdf is generated automatically

📄 Output
CSV:

Frame-wise scores for Eye, Posture, Gesture, Confidence.

PDF:

Final averages + personalized improvement tips.

💡 Example Improvement Tips

Increase eye contact with camera

Straighten posture and reduce slouch

Use more natural hand gestures

🎯 Use Cases

Presentation practice

Interview preparation

Public speaking improvement

Soft-skills analytics demo

🏆 Resume Description

Built a real-time Presentation Skills Analyzer using Python, OpenCV and MediaPipe Tasks API to evaluate eye contact, posture, gestures and confidence, generating automated CSV and PDF performance reports.

🔮 Future Improvements

Audio speaking pace analysis

ML classifier (confident / nervous / distracted)

Web dashboard

Historical session comparison


📈 Evaluation Notes

Eye contact estimated using iris center approximation.

Posture calculated via shoulder alignment and head forward distance.

Hand gestures measured using wrist movement across frames.

Scores are rule-based and not ML-trained.

Lighting and camera angle affect accuracy.

Designed for single-person frontal presentation.

👤 Author

Abhishek Chaudhary
AI / Computer Vision Project
