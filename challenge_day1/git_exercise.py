import philip
import justus
import Twan

_TEAM_NAME: str = "Eldinfanclub"

def get_team() -> None:
  print(f"This is Team {_TEAM_NAME}. We are:")
  print(philip.get_name())
  print(justus.get_name())
  print(Twan.get_name())


get_team()