_NAME: str = "Philip"

def get_name() -> str:
  return _NAME

def get_paragraph(paragraph: int) -> str:
  if paragraph == 1: return "The University of Amsterdam, founded in 1632, is one of Europe's largest and most prestigious research university."
  elif paragraph == 2: return "Located in the heart of Amsterdam, UvA offers over 200 English-taught programmes across diverse fields of study."
  elif paragraph == 3: return "With its strong emphasis on research and innovation, UvA consistently ranks among the top universities worldwide."
  else: return "Paragraph not found."