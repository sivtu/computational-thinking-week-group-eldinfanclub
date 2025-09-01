import philip
import justus

_TEAM_NAME: str = "Philip"

def get_team() -> None:
  print(f"This is Team {_TEAM_NAME}. We are:")
  print(philip.get_name())
  print(justus.get_name())


get_team()