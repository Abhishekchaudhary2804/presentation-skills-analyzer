import streamlit as st
import cv2
import pandas as pd
from audio import AudioAnalyzer
import tempfile
from face import eye_contact
from pose import posture_score
from hands import gesture_score
from scoring import confidence_score, generate_tips
from pdf_report import generate_pdf

# ================= STYLE =================

st.set_page_config(layout="wide")

st.markdown("""
<style>
body {background:#0f172a;}
.metric-box {
    background:#111827;
    padding:12px;
    border-radius:12px;
    margin-bottom:10px;
}
.tipbar {
    background:linear-gradient(90deg,#22c55e,#16a34a);
    padding:15px;
    border-radius:12px;
    color:white;
    font-size:18px;
}
</style>
""", unsafe_allow_html=True)

st.title("🎤 Presentation Skills Analyzer")

# ================= CONTROLS =================

c1,c2 = st.columns(2)
with c1:
    start = st.button("🎥 Start Camera")
with c2:
    upload = st.file_uploader("📁 Upload Video", type=["mp4","avi"])

source = None
if start:
    source = 0
if upload:
    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmp.write(upload.read())
    source = tmp.name

# ================= MAIN LAYOUT =================

left, mid, right = st.columns([3,4,2])

FRAME = mid.image([])

# STATIC PLACEHOLDERS
eye_box = right.empty()
posture_box = right.empty()
gesture_box = right.empty()
voice_box = right.empty()
conf_box = right.empty()

chart_box = left.empty()
tip_box = st.empty()

session=[]
total=0
eye=0

audio = AudioAnalyzer()

if source is not None:

    audio.start()
    cap=cv2.VideoCapture(source)

    while cap.isOpened():

        ret,frame=cap.read()
        if not ret:
            break

        rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        total+=1
        if eye_contact(rgb):
            eye+=1

        eye_score=int((eye/(total+1))*100)
        posture=posture_score(rgb)
        gesture=gesture_score(rgb)
        voice=audio.speaking_pace_score()

        conf=confidence_score(eye_score,posture,gesture,voice)

        session.append([eye_score,posture,gesture,voice,conf])

        FRAME.image(rgb)

        eye_box.markdown(f"<div class='metric-box'>👀 Eye Contact: {eye_score}%</div>",unsafe_allow_html=True)
        posture_box.markdown(f"<div class='metric-box'>🧍 Posture: {posture}</div>",unsafe_allow_html=True)
        gesture_box.markdown(f"<div class='metric-box'>✋ Gesture: {gesture}</div>",unsafe_allow_html=True)
        voice_box.markdown(f"<div class='metric-box'>🎤 Voice Pace: {voice}</div>",unsafe_allow_html=True)
        conf_box.markdown(f"<div class='metric-box'>🔥 Confidence: {conf}</div>",unsafe_allow_html=True)

        if len(session) >10:
            df=pd.DataFrame(session,columns=["Eye","Posture","Gesture","Voice","Confidence"])
            chart_box.line_chart(df)

    cap.release()
    audio.stop()

# ================= AFTER SESSION =================

if len(session)>10:

    df=pd.DataFrame(session,columns=["Eye","Posture","Gesture","Voice","Confidence"])

    with left:
        st.subheader("📊 Session Dashboard")
        st.line_chart(df)

    avg_eye=df.Eye.mean()
    avg_post=df.Posture.mean()
    avg_gest=df.Gesture.mean()
    avg_voice=df.Voice.mean()

    tips=generate_tips(avg_eye,avg_post,avg_gest,avg_voice)

    st.markdown(f"<div class='tipbar'>💡 {tips[0]}</div>",unsafe_allow_html=True)

    csv=df.to_csv(index=False).encode()

    scores={
        "Eye Contact":int(avg_eye),
        "Posture":int(avg_post),
        "Gesture":int(avg_gest),
        "Voice":int(avg_voice),
        "Confidence":int(df.Confidence.mean())
    }
    import tempfile

    
    pdf_path = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name
    generate_pdf(scores,tips,pdf_path)
    with open("session_report.pdf","rb") as f:
        pdf=f.read()

    d1,d2=st.columns(2)
    with d1:
        st.download_button("⬇ Download CSV",csv,"session.csv")
    with d2:
        st.download_button("⬇ Download PDF",pdf,"session_report.pdf")
