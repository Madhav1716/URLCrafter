#!/usr/bin/env python3
"""
Test the installed URLCrafter package.
Created by Madhav Panchal (2025)
"""

from urlcrafter import URL

# Create a simple URL
url = URL("https://example.com").add_path("products").add_param("page", 2).build()
print(f"Created URL: {url}")

# Ensure it matches the expected result
expected = "https://example.com/products?page=2"
assert url == expected, f"Expected '{expected}' but got '{url}'"

print("URLCrafter installed and working correctly!")