# Problem 1
## Least Recently Used Cache

### Efficiency

- space   O(n)
- time:
    - get     O(1)
    - set     O(1)

As no iteration is made the item is returned with 0(1) time complexity.

### Code Design

Data structures used are a `map` and `doubly linked list`.
First is used to perform O(1) look up of the available values.
As by definition cache is to store limitied relatively small number of items, I find it efficient.
The second is used because it provides instant access to last and first items, all that we need for cache.