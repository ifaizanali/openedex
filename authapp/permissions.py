from rest_framework import permissions


class IsAuthenticated(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        print(request.headers)
        return super(IsAuthenticated, self).has_permission(request, view)
