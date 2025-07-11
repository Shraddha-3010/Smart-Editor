def find_largest_integer(numbers):
  """Finds the largest integer in a list.

  Args:
    numbers: A list of integers.

  Returns:
    The largest integer in the list. Returns None if the list is empty.
  """
  if not numbers:
    return None
  return max(numbers)