from rest_framework import permissions


class AllowCreateListAdminOnly(permissions.BasePermission):
    """
    Bu izin sınıfı, kullanıcıların hesap oluşturmasına ve yalnızca yönetici kullanıcıların
    kullanıcıları listeleyebilmesine izin verir.
    """

    def has_permission(self, request, view):
        # Yönetici kullanıcılar her zaman izinlidir
        if request.user and request.user.is_staff:
            return True

        # POST istekleri (yani hesap oluşturma) her zaman izinlidir
        if request.method == 'POST':
            return True

        # Diğer tüm istekler reddedilir
        return False
