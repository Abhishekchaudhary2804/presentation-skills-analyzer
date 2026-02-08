from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(scores, tips, output_path="session_report.pdf"):

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(output_path, pagesize=A4)

    content = []

    content.append(Paragraph("<b>Presentation Skill Analysis Report</b>", styles["Title"]))

    for key, value in scores.items():
        content.append(Paragraph(f"{key}: {value}", styles["Normal"]))

    content.append(Paragraph("<br/><b>Improvement Tips</b>", styles["Heading2"]))

    for t in tips:
        content.append(Paragraph(f"- {t}", styles["Normal"]))

    doc.build(content)

    print(f"PDF Generated: {output_path}")

    return output_path
