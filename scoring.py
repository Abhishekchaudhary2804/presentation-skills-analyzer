def confidence_score(eye, posture, gesture):

    return int(0.4*eye + 0.3*posture + 0.3*gesture)


def generate_tips(eye, posture, gesture):

    tips = []

    if eye < 50:
        tips.append("Increase eye contact with camera")

    if posture < 70:
        tips.append("Straighten posture and reduce slouch")

    if gesture < 60:
        tips.append("Use more natural hand gestures")

    if not tips:
        tips.append("Great presentation skills!")

    return tips
