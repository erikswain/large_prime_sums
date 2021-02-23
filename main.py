
def findPrimeSum():
    max = 2000000
    for num in range(1000000, max + 1):
        if isPrime(num):
            sum = 0
            # print(num, "is prime!!")
            for val in str(num):
                sum += int(val)
                if isPrime(sum):
                    print(num, "has a prime sum!!! which is: ", sum)

def isPrime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                # print(num, "is not prime")
                # print(i, "times", num//i, "is", num)
                break
        else:
            return True


if __name__ == '__main__':
    findPrimeSum()

