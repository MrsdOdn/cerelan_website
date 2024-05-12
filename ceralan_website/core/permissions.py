from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    """
    Allows access only to owner.
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj


class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admins to create.
    """

    def has_permission(self, request, view):
        # Allow GET, HEAD or OPTIONS request
        if request.method in SAFE_METHODS:
            return True
        # Deny POST request if user is not admin
        return request.user and request.user.is_superuser


class IsOwnerOrReadOnly(BasePermission):
    """
    Bir nesnenin sahibi ise değiştirme ve silme izni verir.
    """

    def has_object_permission(self, request, view, obj):
        # GET, HEAD veya OPTIONS isteklerine her zaman izin ver
        if request.method in SAFE_METHODS:
            return True

        # Ürünü oluşturan kullanıcı ise izin ver
        return obj.seller == request.user
