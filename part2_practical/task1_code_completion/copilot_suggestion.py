# copilot_suggestion.py
# AI-generated version (GitHub Copilot-style)

def sort_dicts(data, key):
    """
    Sorts a list of dictionaries by a specified key.

    Args:
        data (list): List of dictionaries.
        key (str): Dictionary key to sort by.

    Returns:
        list: Sorted list of dictionaries.
    """
    try:
        return sorted(data, key=lambda x: x.get(key))
    except Exception as e:
        raise ValueError(f"Failed to sort dictionaries: {e}")


# Example usage
if __name__ == "__main__":
    items = [
        {"name": "Alice", "age": 24},
        {"name": "Bob", "age": 20},
        {"name": "Charlie", "age": 26}
    ]
    
    print(sort_dicts(items, "age"))
