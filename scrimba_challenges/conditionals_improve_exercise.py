def num_days(month):
  days = 31
  if month in {"apr" or month == "jun" or month == "sep" or month == "nov"}:
  # if month == "apr" or month == "jun" or month == "sep" or month == "nov":
    days = 30
  elif month == "feb":
    days = 28
  print("number of days in", month, "is", days)


num_days("jun")
# optimize/shorten the code in the function
# try to reduce the number of conditionals
