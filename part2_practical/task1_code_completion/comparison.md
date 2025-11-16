# Task 1 – Comparison of AI-Generated and Manual Code Implementations

This task required implementing a function to sort a list of dictionaries by a specific key. Two versions were created: an AI-generated implementation (via a code completion tool) and a manually written version.

## 1. Efficiency
The AI-generated version uses Python’s built-in `sorted()` function with a lambda expression. This runs in **O(n log n)** time and is the idiomatic, optimal way to sort collections in Python.  
The manual version uses a **selection sort**, which runs in **O(n²)** time. It is significantly slower for large datasets, but intentionally demonstrates full algorithmic reasoning.

## 2. Readability and Maintainability
The AI code is concise, minimal, and follows common Python conventions. It is easier to read and maintain.  
The manual version is longer and more verbose, but more transparent. It shows every comparison and swap, making the sorting logic explicit.

## 3. Error Handling and Robustness
The AI-generated version handles missing keys gracefully via `.get()`, reducing runtime errors.  
The manual version assumes the key exists, making it more fragile without extra validation.

## 4. Productivity Impact
AI clearly reduces development time by generating high-quality boilerplate instantly. However, its output still requires human review to ensure correctness and security.  
The manual implementation proves fundamental understanding that AI cannot replace.

**Conclusion:**  
The AI version is superior for real-world use, but the manual version provides essential insight into algorithmic decision-making.
