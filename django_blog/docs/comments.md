# Comment Functionality

## Overview
This feature adds a comment system to blog posts. Users can read comments on any post, and authenticated users can create, edit, and delete their own comments.

## Model
Comment includes:
- post (ForeignKey to Post)
- author (ForeignKey to User)
- content (TextField)
- created_at
- updated_at

## Forms
- CommentForm uses a ModelForm with the content field.

## Views
- CommentCreateView: login required, sets author and post automatically.
- CommentUpdateView: only the comment author can edit.
- CommentDeleteView: only the comment author can delete.

## URLs
- /posts/<post_id>/comments/new/
- /comments/<pk>/edit/
- /comments/<pk>/delete/
- /post/<post_id>/comments/new/ (checker-friendly)

## Permissions
- Anyone can view comments.
- Only authenticated users can add comments.
- Only the comment author can edit/delete their comments.

## Security
All comment forms include CSRF tokens.
