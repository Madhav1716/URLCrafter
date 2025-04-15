#!/usr/bin/env python3
"""
Example usage of the URLCrafter library.
Created by Madhav Panchal (2025)
"""

from urlcrafter import URL

def main():
    print("URLCrafter Example Usage\n" + "=" * 20 + "\n")
    
    # Simple URL building
    print("Basic URL Building:")
    url = URL("https://example.com").add_path("products").add_param("page", 2).build()
    print(f"  {url}")
    
    # Building a URL from scratch
    print("\nBuilding from scratch:")
    url = URL().set_scheme("https").set_netloc("api.example.com").set_path("/v1/users").build()
    print(f"  {url}")
    
    # Parsing an existing URL
    print("\nParsing and modifying:")
    url = URL.parse("https://shop.example.com/products?category=electronics")
    url.add_path("laptops").add_param("brand", "apple").remove_param("category")
    print(f"  {url.build()}")
    
    # Using slugify
    print("\nUsing slugify:")
    article_title = "10 Python Tips & Tricks for 2025!"
    url = URL("https://blog.example.com").add_path("articles").add_slugified_path(article_title).build()
    print(f"  Original: '{article_title}'")
    print(f"  URL: {url}")
    
    # Multiple query parameters
    print("\nWorking with query parameters:")
    params = {
        "sort": "price",
        "order": "asc",
        "limit": 20
    }
    url = URL("https://api.example.com/products").add_params(params).build()
    print(f"  {url}")
    print("  Updating a parameter:")
    url = URL(url).add_param("sort", "rating").build()
    print(f"  {url}")
    
    # Using fragments
    print("\nUsing fragments:")
    url = URL("https://docs.example.com/guide").set_fragment("installation").build()
    print(f"  {url}")
    
    # Building URLs for a REST API
    print("\nREST API URLs:")
    base_api = URL("https://api.example.com/v1")
    
    # GET /users
    users_endpoint = URL(base_api.build()).add_path("users").build()
    print(f"  Users endpoint: {users_endpoint}")
    
    # GET /users/123
    user_detail = URL(base_api.build()).add_path("users").add_path("123").build()
    print(f"  User detail: {user_detail}")
    
    # GET /users/123/posts?status=published
    user_posts = URL(base_api.build()).add_path("users/123/posts").add_param("status", "published").build()
    print(f"  User posts: {user_posts}")
    
    # Pagination helper
    print("\nPagination helper:")
    
    def generate_paginated_urls(base_url, total_pages):
        """Generate a list of paginated URLs."""
        return [URL(base_url).add_param("page", i).build() for i in range(1, total_pages + 1)]
    
    pagination_urls = generate_paginated_urls("https://blog.example.com/articles", 3)
    for i, page_url in enumerate(pagination_urls, 1):
        print(f"  Page {i}: {page_url}")


if __name__ == "__main__":
    main() 