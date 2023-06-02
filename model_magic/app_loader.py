from django.apps import apps


class AppModelLoader:
    def __init__(self, app_name="_all_"):
        self.app_name = app_name

    def load_models(self):
        if self.app_name == "_all_":
            apps_with_models = [app for app in apps.get_app_configs() if app.get_models()] # noqa
        else:
            app = apps.get_app_config(self.app_name)
            apps_with_models = [app] if app.get_models() else []

        return tuple(
            (app.name, model.__name__)
            for app in apps_with_models
            for model in app.get_models()
        )
