import philip
import justus
import Twan
import tom
import nikola
import jelle

_TEAM_NAME: str = "Eldin fanclub"

def get_team() -> None:
  print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
  print(f"This is Team '{_TEAM_NAME}'. We are:")

  for member in [philip, justus, Twan, tom, nikola, jelle]:
    print(f"- {member.get_name()}")

  print("")
  print("Story:")
  for i in range(1, 4):
    for member in [philip, justus, Twan, tom, nikola, jelle]:
      print(f"- {member.get_paragraph(i)}")
  print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")


get_team()