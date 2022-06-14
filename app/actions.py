import objectpack.ui
from django.contrib.auth import models
from objectpack.actions import ObjectPack

from .controller import observer
from .ui import UserAddWindow


class ContentTypePack(ObjectPack):
    model = models.ContentType

    columns = (
        {
            "data_index": "app_label",
            "header": "App label"
        },
        {
            "data_index": "model",
            "header": "Model class name"
        }
    )

    add_window = edit_window = objectpack.ui.ModelEditWindow.fabricate(model)

    add_to_desktop = True
    add_to_menu = True


class UserPack(ObjectPack):
    model = models.User

    columns = (
        {
            "data_index": "username",
            "header": "Username",
            "width": 2
        },
        {
            "data_index": "is_superuser",
            "header": "Is superuser",
            "width": 1
        },
        {
            "data_index": "is_staff",
            "header": "Is staff",
            "width": 1
        },
        {
            "data_index": "is_active",
            "header": "Is active",
            "width": 1
        }
    )

    add_window = edit_window = UserAddWindow
    # add_window = edit_window = objectpack.ui.ModelEditWindow.fabricate(model)

    add_to_desktop = True
    add_to_menu = True


class GroupPack(ObjectPack):
    model = models.Group

    columns = (
        {
            "data_index": "name",
            "header": "Name"
        },
    )

    add_window = edit_window = objectpack.ui.ModelEditWindow.fabricate(model)

    add_to_desktop = True
    add_to_menu = True


class PermissionPack(ObjectPack):
    model = models.Permission

    columns = (
        {
            "data_index": "name",
            "header": "Name"
        },
        {
            "data_index": "codename",
            "header": "Codename"
        },
        {
            "data_index": "content_type",
            "header": "Content type"
        }
    )

    add_window = edit_window = objectpack.ui.ModelEditWindow.fabricate(model, model_register=observer)
    add_to_desktop = True
    add_to_menu = True
