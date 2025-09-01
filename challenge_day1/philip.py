_NAME: str = "Philip"

def get_name() -> str:
  return _NAME

def get_paragraph(paragraph: int) -> str:
  if paragraph == 1: 
    return "Marcus stood at the edge of the ancient forest, watching as Eldin emerged from the shadows with a mysterious map. Justus pointed toward the distant mountains while Twan checked his compass, and Tom adjusted his backpack nervously. Nikola whispered something urgent to Jelle about the legends they'd heard in the villa."
  elif paragraph == 2: 
    return "Deep within the cavern, Marcus held the torch high as Eldin deciphered the ancient runes carved into the stone walls. Justus discovered a hidden passage while Twan found strange symbols etched into the ground, and Tom noticed the air growing colder with each step. Nikola and Jelle exchanged worried glances as mysterious sounds echoed from the depths ahea."
  elif paragraph == 3: 
    return "As dawn broke over the mountain peak, Marcus raised the golden artifact triumphantly while Eldin smiled with satisfaction at their successful quest. Justus cheered loudly as Twan documented their discovery, and Tom finally relaxed for the first time in days. Nikola and Jelle began planning their journey home, knowing they had changed the course of history forev."
  else: 
    return "Paragraph not found."