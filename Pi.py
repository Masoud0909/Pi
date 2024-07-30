# The value of pi can be computed according to the following formula:

# 	pi / 4 =  1 - 1/3 + 1/5 - 1/7 + 1/9 - ... 

# Write an algorithm to compute pi and output it. Because the formula is an infinite
# series and an algorithm must stop after a finite number of steps you
# should stop when a new term becomes smaller than a very small number
# (epsilon) entered by the user. 

#Getting the value of Epsilon:
epsilon=float(input("Enter the value of epsilon: "))

#Initialize Variables
pi_over_4 = 0           # Holds the accumulated value of the series for pi over 4
term = 1                # current term in the series
denominator = 1         # incerement by 2 in each iteration
sign = 1                # sign of each term in the series

#Implementing the while loop
while abs(term)>=epsilon:   #as long as absolute value of term is >= epsilon
    pi_over_4+=term         #add the current term to the accumulated one
    denominator+=2          #update the denominator for the next term in the series       
    sign*=-1                #alternates the sign for the next term
    term = sign / denominator#NEW TERM BASED ON THE UPDATED  denominator and sign

#Calculating Pi
pi = pi_over_4 * 4
print (f"Approximate value of pi: {pi}")    


