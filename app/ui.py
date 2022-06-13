from m3_ext.ui import all_components as ext
from objectpack.ui import BaseEditWindow


class UserAddWindow(BaseEditWindow):
    def _init_components(self):
        super(UserAddWindow, self)._init_components()

        self.field__username = ext.ExtStringField(
            label="Username",
            name="username",
            anchor="100%",
            allow_blank=False
        )

        self.field__password = ext.ExtStringField(
            label="Password",
            name="password",
            anchor="100%",
            allow_blank=False
        )

        self.field__email = ext.ExtStringField(
            label="Email",
            name="email",
            anchor="100%"
        )

        self.field__first_name = ext.ExtStringField(
            label="First name",
            name="first_name",
            anchor="100%"
        )

        self.field__last_name = ext.ExtStringField(
            label="Last name",
            name="last_name",
            anchor="100%"
        )

        self.field__is_superuser = ext.ExtCheckBox(
            label="Is superuser",
            name="is_superuser",
        )

        self.field__is_staff = ext.ExtCheckBox(
            label="Is staff",
            name="is_staff",
        )

        self.field__is_active = ext.ExtCheckBox(
            label="Is active",
            name="is_active"
        )

        self.field__date_joined = ext.ExtDateField(
            label="Date joined",
            name="date_joined",
            anchor="100%",
            allow_blank=False,
            format="d.m.Y"
        )

        self.field__last_login = ext.ExtDateField(
            label="Last login",
            name="last_login",
            anchor="100%",
            format="d.m.Y"
        )

    def _do_layout(self):
        super(UserAddWindow, self)._do_layout()

        self.form.items.extend((
            self.field__username,
            self.field__password,
            self.field__email,
            self.field__first_name,
            self.field__last_name,
            self.field__is_superuser,
            self.field__is_staff,
            self.field__is_active,
            self.field__date_joined,
            self.field__last_login
        ))

    def set_params(self, params):
        super(UserAddWindow, self).set_params(params)

        self.height = "auto"
