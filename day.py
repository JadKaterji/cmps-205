# Asssignment 6 part 8
import sys
month = sys.argv[1]
day = int(sys.argv[2])


days_of_months = {'jan':31, 'feb':28, 'mar':31, 'apr':30, 'may':31, 'jun':30, 'jul':31, 'aug':31, 'sep':30, 'oct':31, 'nov':30, 'dec':31}
def day_of_the_year(month,days):
    sum = 0
    for (i,j) in days_of_months.items():
        if i != month:
            sum += j 
        else:
            sum += day
            break
    return(sum)
print(day_of_the_year(month, day))