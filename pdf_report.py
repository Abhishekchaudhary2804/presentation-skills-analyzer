from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(scores, tips):

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate("session_report.pdf", pagesize=A4)

    content = []

    content.append(Paragraph("<b>Presentation Skill Analysis Report</b>", styles["Title"]))

    for key, value in scores.items():
        content.append(Paragraph(f"{key}: {value}", styles["Normal"]))

    content.append(Paragraph("<br/><b>Improvement Tips</b>", styles["Heading2"]))

    for t in tips:
        content.append(Paragraph(f"- {t}", styles["Normal"]))

    doc.build(content)

    print("PDF Generated: session_report.pdf")
