from django.contrib.auth import models
from objectpack.actions import ObjectPack


class ContentTypePack(ObjectPack):
    model = models.ContentType

    add_to_desktop = True
    add_to_menu = True


class UserPack(ObjectPack):
    model = models.User

    add_to_desktop = True
    add_to_menu = True


class GroupPack(ObjectPack):
    model = models.Group

    add_to_desktop = True
    add_to_menu = True


class PermissionPack(ObjectPack):
    model = models.Permission

    add_to_desktop = True
    add_to_menu = True
