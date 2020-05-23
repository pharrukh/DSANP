# Problem 2
## File Recursion

### Efficiency

- space   O(1)
- time    O(n)

Nothing is stored so space complexity is O(1).
Time complexity is O(n) as it is required to traverse all subfolders.

### Code Design

Frankly not sure, if there exists some other solution other than recursive.
The possible bottleneck for this solution is that there is a limit for recursive calls that saves an operating system from endless looping.
One can increase or decrease the max number of self-calls but it is not clear to which value as the depth of folder structure is not known.