from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    """
    Allows access only to owner.
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj


class IsAdminOrReadOnly(BasePermission):
    """
    Yalnızca admin kullanıcıların yazma izni var, diğer kullanıcılar sadece okuma yapabilir.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True  # Herkese açık, kimlik doğrulaması gerekmiyor
        return request.user and request.user.is_superuser  # Sadece adminler yazabilir


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
