# Problem 3
## Rearrange Array Elements

### Efficiency

- space   O(n)
- time    O(log(n))

Space complexity is O(n) for collection size.
Time complexity is O(log(n)) as every new guess is x/2 closer to the answer.

### Code Design

The intial guess being x/2 saves some iterations.