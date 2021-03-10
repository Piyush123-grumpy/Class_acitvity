Price_of_house=1000000
credit= True
if credit :
    Price_with_good_credit=(Price_of_house*20/100)
    print(f'The price of housse',Price_with_good_credit)
else:
    Price_with_bad_credit=(Price_of_house*10/100)
    print(f'The price of house',Price_with_bad_credit)