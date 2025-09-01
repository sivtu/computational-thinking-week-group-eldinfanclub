_NAME: str = "Twan"

def get_name() -> str:

  return _NAME

def get_paragraph(paragraph: int) -> str:
    if paragraph == 1:
        return "Thalen was the last to arrive. He had not been called by light or whispers but by loyalty—he refused to let his friends vanish without him."
    elif paragraph == 2:
        return "He pushed through the trees with determination, sweat beeding on his brow. When he broke into the clearing, he froze at the sight of the orb and the gathering of familiar and unfamiliar faces."
    elif paragraph == 3:
        return "Something inside him stirred—a realization that this night was the beginning of a story greater than any of them. The orb pulsed brighter, as if agreeing."
    else:
        return "Paragraph not found."
