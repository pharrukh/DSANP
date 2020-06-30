# Problem 2
## Search in a Rotated Sorted Array

### Efficiency

- space   O(n)
- time    O(log(n))

Space complexity is O(n): O(n) for collection size and O(log(n)) for a call stack.
Time complexity O(log(n)). Here is the break-down: O(log(n)) for pivot finding O(log(n/2)) for the left section and O(log(n/2)) for the right section.
Thus the result is O(log(n)) + O(log(n/2)) + O(log(n/2)) which boils down to O(log(n)).

### Code Design

Spliting of the task into subproblems: finding pivot and binary search.
The most complex task so far out of 1,2,4,6.