from rest_framework.permissions import BasePermission

class islevel1(BasePermission):
    def has_permission(self,request,view):
        return request.user.islevel1() and request.method == "GET"
    
class islevel2(BasePermission):
    def has_permission(self,request,view):
        return request.user.islevel2()
    
class islevel3(BasePermission):
    def has_permission(self,request,view):
        return request.user.islevel3()