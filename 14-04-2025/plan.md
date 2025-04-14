## Task
- take number k
- take an array of numbers
- return true if any 2 numbers add up to k

## Constraints
- Only compare 2 numbers
- Don't compare the current number against itself
- Try to do this in one pass

## Stretch goal
- Run tests
    - against multiple arrays
    - different values of k
    - case where no items add up to k (return false)
    - case where value adds up to k (return true)
    - case where only adding a number to itself adds up to k (return false)

## Solution

```
var numbersToCheck = [10, 15, 3, 7]
var k = 17

foreach ( numbersToCheck as currentNumber )
    if ( numbersToCheck[currentNumber] )
        continue

    if ( map( numbersToCheck ) + currentNumber === k )
        return true

    return false
```

