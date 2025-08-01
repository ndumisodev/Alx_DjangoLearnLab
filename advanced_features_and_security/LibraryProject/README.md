## Permissions & Groups Setup

This app uses Django's built-in permissions and groups system.

### Custom Permissions
Defined in `Book` model:
- can_view
- can_create
- can_edit
- can_delete

### Groups and Permissions
- **Viewers**: can_view
- **Editors**: can_view, can_create, can_edit
- **Admins**: can_view, can_create, can_edit, can_delete

### How it works
- Views are protected using @permission_required decorators.
- Admins can manage users and assign them to groups.
- Each user only has access to the actions allowed by their group.

Test users are created and manually assigned groups for permission verification.
