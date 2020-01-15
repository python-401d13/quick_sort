from quick_sort import quick_sort


def test_randomly_sorted():
  """
  A randomly sorted list of integers is sorted by QuickSort.
  """

  expected = [4, 8, 15, 16, 23, 42]

  lst = [8, 4, 23, 42, 16, 15]
  quick_sort(lst, 0, len(lst) - 1)

  assert lst == expected


def test_reverse_sorted():
  """
  A reverse sorted list of integers is sorted by QuickSort.
  """

  expected = [-2, 5, 8, 12, 18, 20]

  lst = [20, 18, 12, 8, 5, -2]
  quick_sort(lst, 0, len(lst) - 1)

  assert lst == expected


def test_few_uniques():
  """
  A list with few unique integers is sorted by QuickSort.
  """

  expected = [5, 5, 5, 7, 7, 12]

  lst = [5, 12, 7, 5, 5, 7]
  quick_sort(lst, 0, len(lst) - 1)

  assert lst == expected


def test_nearly_sorted():
  """
  A list of nearly sorted integers is sorted by QuickSort.
  """

  expected = [2, 3, 5, 7, 11, 13]

  lst = [2, 3, 5, 7, 13, 11]
  quick_sort(lst, 0, len(lst) - 1)

  assert lst == expected