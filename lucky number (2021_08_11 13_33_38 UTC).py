from random import randint

print('TRY OUT YOUR LUCK ON OUR LUCKY NUMBERS')
print('________________________________________________________________________________')
count=0
amt=eval(input('Staking amount:'))
print('________________________________________________________________________________')
for yn in range(2):
        win=randint(1,50)
        yn=eval(input('Enter a lucky number between 1 and 50: '))
        if win==yn:
            count=count+5
            print(count)
print('________________________________________________________________________________')
print('Your score is  ',count,'Game points')
print('________________________________________________________________________________')
if count==0:
        print ('Please try again')
else:
        print('You have an amount of Gh$',((count/10)*amt),'.00 to redeem.')
