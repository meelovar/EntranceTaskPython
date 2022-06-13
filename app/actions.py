import objectpack.ui
from django.contrib.auth import models
from objectpack.actions import ObjectPack

from .ui import UserAddWindow


class ContentTypePack(ObjectPack):
    model = models.ContentType

    add_window = edit_window = objectpack.ui.ModelEditWindow.fabricate(model)

    add_to_desktop = True
    add_to_menu = True


class UserPack(ObjectPack):
    model = models.User

    add_window = edit_window = UserAddWindow
    # add_window = edit_window = objectpack.ui.ModelEditWindow.fabricate(model)

    add_to_desktop = True
    add_to_menu = True


class GroupPack(ObjectPack):
    model = models.Group

    add_window = edit_window = objectpack.ui.ModelEditWindow.fabricate(model)

    add_to_desktop = True
    add_to_menu = True


class PermissionPack(ObjectPack):
    model = models.Permission

    add_to_desktop = True
    add_to_menu = True
