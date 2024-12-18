from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
	def has_permission(self, request, view):
		if request.method in permissions.SAFE_METHODS:
			return True
		return request.user.is_staff


class IsAdminOrAuthenticatedForOnlyRead(permissions.BasePermission):
	def has_permission(self, request, view):
		if request.method in permissions.SAFE_METHODS and request.user.is_authenticated:
			return True
		return request.user.is_staff
#
# class IsOwnerReview(permissions.BasePermission):
# 	def has_object_permission(self, request, view, obj):
# 		if request.method in permissions.SAFE_METHODS:
# 			return obj.user == request.user
