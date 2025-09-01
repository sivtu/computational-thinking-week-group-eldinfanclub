import philip

_TEAM_NAME: str = "Philip"

def get_team() -> None:
  print(f"This is Team {_TEAM_NAME}. We are:")
  print(philip.get_name())


get_team()