def find_optimal_units(value):
  """
  Finds the most optimized set of 6 units (from 1, 2, 5, 10, 20, 50) to reach a target value.

  Args:
      value: The target value (less than 100) to reach with the units.

  Returns:
      A list containing the 6 units used and the total number of units used, 
      or None if not achievable with 6 units.
  """
  units = [50, 20, 10, 5, 2, 1]  # Units in descending order

  # Initialize variables
  used_units = []
  total_units = 0

  # Loop through units in descending order
  for unit in units:
    if value >= unit:
      count, remainder = divmod(value, unit)
      used_units.extend([unit] * count)
      value = remainder
      total_units += count
      if value == 0:
        break  # Exit loop if target value is reached

  # Check if target value is achievable with 6 units
  if len(used_units) > 6 or value > 0:
    return None  # Not achievable with 6 units

  return used_units, total_units

# Example usage
value = 99
optimal_set, total_units = find_optimal_units(value)

if optimal_set:
  print(f"For value {value}:")
  print(f"  Optimal units: {optimal_set}")
  print(f"  Total units used: {total_units}")
  print(f"  Average units used: {total_units / len(optimal_set):.2f}")
else:
  print(f"Value {value} cannot be reached with 6 units.")
    