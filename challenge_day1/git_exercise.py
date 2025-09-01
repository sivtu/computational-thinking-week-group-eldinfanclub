import philip
import justus
import Twan
import tom
import nikola

_TEAM_NAME: str = "Eldinfanclub"

def get_team() -> None:
  print(f"This is Team {_TEAM_NAME}. We are:")
  print(philip.get_name())
  print(justus.get_name())
  print(Twan.get_name())
  print(tom.get_name())
  print(nikola.get_name())


get_team()