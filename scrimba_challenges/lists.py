sales_w1 = [7, 3, 42, 19, 15, 35, 9]
sales_w2 = [12, 4, 26, 10, 7, 28]
sales = []
new_day = input("Enter number of lemonades for new day: ")

# add another day to week two by capturing number as input
sales_w2.append(int(new_day))
# combine two lists into the sales list
sales.extend(sales_w1)
sales.extend(sales_w2)
# sales = sales_w1 + sales_w2
# now sort the list
# sales.sort()
# calculate how much earned on the worst day -> min
# worst_day_prof = sales[0] * 1.5
## we can actually do this for efficiency
worst_day_prof = min(sales) * 1.5

# calculate how much earned on the best day -> max
# best_day_prof = sales[-1] * 1.5
best_day_prof = max(sales) * 1.5
print(f'worst day profit: $ {worst_day_prof}')
print(f'best day profit: $ {best_day_prof}')
# calculate how much earned separately and in total
print(f'combined day profit: $ {worst_day_prof + best_day_prof}')