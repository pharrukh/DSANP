# Problem 5
## Autocomplete with Tries

### Efficiency

- add a word
    - time complexity O(n) where n is the length of a world
    - space complexity - not applicable as it uses the class to store values

- find a prefix
    - time complexity O(n) where n is the length of a world
    - space complexity - not applicable as it uses the class to store values

- get suffixes
    - time complexity O(m) where m is the number words in a node
    - space complexity O(m)

- overall
    - space complexity O(k) where k is the result of n / 26 when n -> infinity, assuming only english words are used

### Code Design

I struggled to use list concatination and instead used the non-class function