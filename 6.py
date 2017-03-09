def sum_of_squares(max):
    movingTotal = 0
    for i in range(1,max+1):
        movingTotal += i*i
    return movingTotal

def square_of_sum(max):
    return pow(sum(range(max+1)),2)

def main():
    return(square_of_sum(100) - sum_of_squares(100))

if __name__ == "__main__": main()
