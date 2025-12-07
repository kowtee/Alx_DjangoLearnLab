
# Tagging and Search Functionality

## Overview
This feature adds tagging and search to the Django blog.

## Tagging
- A Tag model with a unique name field is added.
- Post has a ManyToMany relationship with Tag.
- Posts can have multiple tags and each tag can belong to multiple posts.

## PostForm Tag Input
- PostForm includes a "tags" field that accepts comma-separated values.
- New tags are automatically created if they do not exist.

## Search
- A search page supports queries across:
  - title
  - content
  - tags
- Implemented using Django Q objects and distinct().

## URLs
- /tags/<tag_name>/ - filter posts by tag
- /search/ - search posts by keyword

## Usage
1. Create or edit a post and enter tags separated by commas.
2. Click a tag link to view all posts under that tag.
3. Use the search bar on the posts list page to find content.
