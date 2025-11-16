# manual_implementation.py
# Manual implementation without relying on Python's built-in sorted()

def sort_dicts_manual(data, key):
    """
    Manually sorts a list of dictionaries by a given key using selection sort.
    This is for demonstration and not optimized.

    Args:
        data (list): List of dictionaries.
        key (str): Key used for sorting.

    Returns:
        list: Sorted list of dictionaries.
    """
    arr = data.copy()
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j][key] < arr[min_idx][key]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# Example usage
if __name__ == "__main__":
    items = [
        {"name": "Alice", "age": 24},
        {"name": "Bob", "age": 20},
        {"name": "Charlie", "age": 26}
    ]

    print(sort_dicts_manual(items, "age"))
