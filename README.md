# array_index
Question : 'a' is an array where, a[n] > a[n-1]. 
Given a number P, find the index of P in 'a', if 'a' doesn't have P find the index
where a can be inserted satisfying the array condition of a[n] > a[n-1] ?

Example : a = [1,2,4,5,6] when P = 4, the resulting index is 2.
when P = 7, the resulting index is 5 as that's the only possible place to insert P which satisfies the array condition.

The objective is to write a python function or a class that takes 2 inputs, 'a' and 'P', and returns the index.
