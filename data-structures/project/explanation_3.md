# Problem 3
## Huffman Coding

### Efficiency

Here I provided the measure of `MinPriorityQueue`:

- space   O(n)
- time:
    - insert  O(log(n))
    - del_min O(log(n))
    - including building time O(nlog(n)) as it is insert for every element

The efficiency is achieved by using semi-ordered heap data structure. The drawback of it is that for all cases the complexity is the same, thus there are no best and worst case for this data structure.


### Code Design

There is a complexity associated with heap implementation. It could have been mitigated with simpler data structures, like ordered list, that would require traversal of the complete space for the worst case.

Apart from `MinPriorityQueue`, I just followed the steps of the algorithm in the problem definition.