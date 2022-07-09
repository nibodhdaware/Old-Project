# importing month dictionary from month_code.py
import month_code as mc

# taking input from user for start date
sd = input('Enter a start Date: ')
sm = input('Enter a start Month (in 3 characters like jan): ')
sy = input('Enter start year: ')

# taking input from user for end date
ed = input('Enter a end Date: ')
em = input('Enter a end Month (in 3 characters like jan): ')
ey = input('Enter which year to search: ')
year = ey[2:]

# calculating the number of days between start date and end date
include_end_date = input("Do you want to include end date? (y/n): ")
if include_end_date == 'y':
    end_result = (int)(year) + \
        mc.month_code[em] + (int)(ed) + mc.month_code[sm] + (int)(sd)
else:
    end_result = (int)(year) + \
        mc.month_code[em] + (int)(ed) + mc.month_code[sm] - 1

print("The number of days between start date and end date is: ", end_result)
