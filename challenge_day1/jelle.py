_NAME: str = "jelle"

def get_name() -> str:
  return _NAME

def get_paragraph(paragraph: int) -> str:
    if paragraph == 1: 
        return "Mira had alwayz heard voices others could not. They whispered to her in dreams, and sometimes in the quiet moments of waking life. When the orb appeared, the voices grew louder, clearer."
    elif paragraph == 2: 
        return "They told her to go to the forrest. They told her the others would be there. For the first time, the voices did not sound like a curse, but a guide."
    elif paragraph == 3: 
        return "When she enterd the clearing, the orb’s glow bent slightly toward her, as if recognizing her presence. She shivered but stood tall."
    else: 
        return "Paragraph not found."

