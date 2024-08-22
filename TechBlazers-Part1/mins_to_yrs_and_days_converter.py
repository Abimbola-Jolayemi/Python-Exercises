def mins_to_yrs_and_days(mins):
	total_days = mins // 1440
	no_of_yrs = total_days // 365
	no_of_days = total_days % 365
	return no_of_yrs, no_of_days

print(mins_to_yrs_and_days(1_000_000_000))