"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.

answer: 906609
"""
def ifPal(data):
    strData = str(data)
    if strData==strData[::-1]:
        return True
    else:
        return False

def main():
    highest = 0
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            if ifPal(i*j) and (i*j)> highest:
                highest = i * j

    return(highest)

if __name__ == "__main__": main()
