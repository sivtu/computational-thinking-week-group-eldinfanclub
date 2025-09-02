from datetime import datetime

def solution_station_2(real_input: str) -> str:
  """
  Given a date string 'YYYY-MM-DD', return the corresponding weekday in Japanese.
  """
  weekday_jp = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]
  dt = datetime.strptime(real_input, "%Y-%m-%d")
  return weekday_jp[dt.weekday()]