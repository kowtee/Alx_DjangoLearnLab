# Blog Post Management (CRUD)

## Overview
This feature adds full CRUD operations for the `Post` model using Django class-based views.

## Views Implemented
- **PostListView**: Displays all posts (public).
- **PostDetailView**: Displays a single post (public).
- **PostCreateView**: Allows authenticated users to create posts.
- **PostUpdateView**: Allows only the author to edit a post.
- **PostDeleteView**: Allows only the author to delete a post.

## Forms
- `PostForm` is a ModelForm for `title` and `content`.
- `author` is automatically set from the logged-in user in Create/Update views.

## URLs
- `/posts/` - list
- `/posts/new/` - create
- `/posts/<pk>/` - detail
- `/posts/<pk>/edit/` - update
- `/posts/<pk>/delete/` - delete

## Permissions
- Create requires login via `LoginRequiredMixin`.
- Update and delete require login and author ownership via `UserPassesTestMixin`.

## Security
- All post forms include CSRF protection.

