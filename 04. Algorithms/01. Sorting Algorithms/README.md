# Sorting Algorithms in Python

Sorting is the process of arranging a collection of elements in a specific order. In computer science, sorting algorithms are used to perform this task efficiently on large datasets. Python provides several built-in sorting functions, such as sorted() and sort(), but it's also useful to know some of the popular sorting algorithms and their implementations.

## 1. Selection Sort

Selection sort is a simple sorting algorithm that sorts an array by repeatedly finding the minimum element from the unsorted part of the array and placing it at the beginning of the sorted part. It has a time complexity of O(n^2) and a space complexity of O(1).

Selection sort is easy to implement, but it's not very efficient for large datasets, as it requires a lot of comparisons and swaps.

## 2. Bubble Sort

Bubble sort is another simple sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order. It has a time complexity of O(n^2) and a space complexity of O(1).

Bubble sort is also not very efficient for large datasets, but it can perform better than selection sort in some cases, especially when the array is almost sorted.

## 3. Insertion Sort

Insertion sort is a sorting algorithm that works by iterating over an array and inserting each element into its correct position in a sorted sublist. It has a time complexity of O(n^2) and a space complexity of O(1).

Insertion sort is efficient for small datasets or for arrays that are almost sorted, but it's not recommended for large datasets, as it requires a lot of comparisons and swaps.

## 4. Merge Sort

Merge sort is a divide-and-conquer sorting algorithm that works by recursively dividing an array into halves, sorting each half, and then merging the two sorted halves. It has a time complexity of O(n log n) and a space complexity of O(n).

Merge sort is efficient for large datasets, as it has a consistent time complexity regardless of the input data. However, it requires extra space to store the merged subarrays.

## 5. Shell Sort

Shell sort is an efficient sorting algorithm that works by comparing elements that are distant from each other, and then gradually reducing the gap between them until the array is completely sorted. It has a time complexity of O(n log n) and a space complexity of O(1).

Shell sort is efficient for medium-sized datasets, but it's not as fast as merge sort or quick sort.

## 6. Counting Sort

Counting sort is a non-comparison based sorting algorithm that works by counting the number of occurrences of each element in the array and then using this information to arrange the elements in order. It has a time complexity of O(n + k) and a space complexity of O(k), where k is the range of values in the array.

Counting sort is very efficient for datasets with a small range of values, but it's not suitable for arrays with a large range of values, as it requires a lot of memory.

## 7. Radix Sort

Radix sort is a non-comparison based sorting algorithm that works by sorting elements based on their digits or characters. It has a time complexity of O(d(n + k)), where d is the number of digits or characters in the input, n is the number of elements, and k is the range of values.

Radix sort is very efficient for datasets with a fixed number of digits or characters, but it's not suitable for arrays with a variable number of digits or characters, as it requires extra memory.

## 8. Quick Sort

Quick sort is a divide-and-conquer sorting algorithm that works by selecting a pivot element and
