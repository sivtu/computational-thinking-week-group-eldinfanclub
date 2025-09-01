_NAME: str = "Tom"

def get_name() -> str:
  return _NAME

def get_paragraph(paragraph: int) -> str:
  if paragraph == 1: 
    return "Kael had been following Lyra at a distance. He never trusted sudden lights in the woods, his village’s stories always ended with someone lost. Still, he couldn’t let her wander into danger alone."
  elif paragraph == 2: 
    return "He crouched behind a fallen tree, his bow ready. The orb’s glow reflected in his eyes, mesmerizing and unsettling at once. He wanted to shout, to call Lyra back, but the words froze in his throat."
  elif paragraph == 3: 
    return "Instead, he watched. If the orb made a move, Kael swore he’d strike, no matter how impossible the figt."
  else: 
    return "Paragraph not found."