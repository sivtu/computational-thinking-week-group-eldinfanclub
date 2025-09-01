_NAME: str = "Justus"

def get_name() -> str:
  return _NAME

def get_paragraph(paragraph: int) -> str:
  if paragraph == 1: 
    return "Dorian had been wandering alone for days, a traveler without a home. When the glow rose into the sky, he thought it was a sign meant for him."
  elif paragraph == 2: 
    return "He trudged through the undergrowth, his staff steadying him as he followed the strange light. For years, he had searched for purpose, for something to prove his wandering wasn’t wasted."
  elif paragraph == 3: 
    return "When he saf Lyra and Kael in the clearing, he paused. He wasn’t the only one called here. Maybe the light had chosen more than just him."
  else: 
    return "Paragraph not found."