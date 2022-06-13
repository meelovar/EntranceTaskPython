from django.conf.urls import url
from objectpack import desktop

from .actions import ContentTypePack, GroupPack, PermissionPack, UserPack
from .controller import controller


def register_urlpatterns():
    """
    Регистрация конфигурации урлов для приложения
    """
    return [url(*controller.urlpattern)]


def register_actions():
    """
    Регистрация экшен-паков
    """
    return controller.packs.extend([
        ContentTypePack(),
        UserPack(),
        GroupPack(),
        PermissionPack()
    ])


def register_desktop_menu():
    """
    Регистрация элементов рабочего стола
    """
    return desktop.uificate_the_controller(controller, menu_root=desktop.MainMenu.SubMenu("Demo"))
