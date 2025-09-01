_NAME: str = "Nikola"

def get_name() -> str:
  return _NAME

def get_paragraph(paragraph: int) -> str:
  if paragraph == 1: 
    return "Seren wasn’t in the forest—yet she felt it. She was in the village square when the strange hum vibrated through her bones. Her pendant, a family heirloom, suddenly glowed faintly, as if echoing the orb miles away."
  elif paragraph == 2: 
    return "Startled, Seren dropped the basket she was carrying. Apples rolled across the cobblestones, but she barely noticed. The pull toward the woods was undeniable."
  elif paragraph == 3: 
    return "She left everythang behind and ran, guided not by sight but by instinct. Whatever was happening, she was part of it now."
  else: 
    return "Paragraph not found."