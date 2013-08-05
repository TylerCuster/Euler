def sumSquareDifference():
    # Sum of squares ie (1^2)+(2^2) + (3^2) + ...
    sumSquares = 0
    # Square of sums ie (1 + 2 + 3 + ...)^2
    squareSum = 0
    for i in range(1, 101):
        sumSquares = sumSquares + i**2
        squareSum = squareSum + i
    squareSum = squareSum**2
    return squareSum - sumSquares

print sumSquareDifference()
