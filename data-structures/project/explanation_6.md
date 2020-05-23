# Problem 6
## Union and Intersection

### Efficiency

n - lenght of the first list
m - lenght of the second list

- space   O(n + m)
- time    O(n + m)

As there is only single traversal for each list the complexity is not more than O(n + m)

### Code Design

For this problem `map` helps to perform instant look-up for both union nad intersection generation. As for this problem the nodes were numbers building hash was not required and thus setting the value to the map takes only O(1) in terms of time. Another possible solution that I found a little more complex is to use `mergesort` then the complexity would be O(nlog(n)) + O(mlog(m)) + O(n + m): sorting of the fist list, sorting of the second and finally traversal over both.