
def quick_sort(lst, left, right):
  """
  Sort a list by the QuickSort algorithm.
  """

  if left < right:
    # Partition the list by setting the position of the pivot
    position = partition(lst, left, right)

    print(position)

    # Sort the left
    quick_sort(lst, left, position - 1)

    # Sort the right
    quick_sort(lst, position + 1, right)


def partition(lst, left, right):
  """
  Find the pivot of a list for the QuickSort algorithm.
  """

  # Set a pivot as a point of reference
  pivot = lst[right]

  # Track the largest index of numbers less than the pivot
  low = left - 1
  for i in range(left, right):
    if lst[i] <= pivot:
      low += 1
      swap(lst, i, low)

  swap(lst, right, low + 1)

  return low + 1


def swap(lst, i, low):
  """
  Swap the index of two values in a list.
  """

  temp = lst[low]
  lst[low] = lst[i]
  lst[i] = temp
