# Problem 3
## Rearrange Array Elements

### Efficiency

- space   O(1)
- time    O(log(n))

Space complexity is 1 because there is no call stack.
Time complexity as every new guess is x/2 closer to the answer.

### Code Design

The intial guess being x/2 saves some iterations.