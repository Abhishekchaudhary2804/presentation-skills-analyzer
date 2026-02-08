def confidence_score(eye, posture, gesture, voice):

    return int(0.3*eye + 0.25*posture + 0.25*gesture + 0.2*voice)


def generate_tips(eye, posture, gesture, voice):

    tips = []

    if eye < 50:
        tips.append("Increase eye contact with camera")

    if posture < 70:
        tips.append("Straighten posture and reduce slouch")

    if gesture < 60:
        tips.append("Use more natural hand gestures")

    if voice < 50:
        tips.append("Try speaking more consistently and clearly")

    if not tips:
        tips.append("Great presentation skills!")

    return tips
