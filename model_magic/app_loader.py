from django.apps import apps


class AppModelLoader:

    def load_models(self):
        apps_with_models = [app for app in apps.get_app_configs() if app.get_models()] # noqa

        return tuple(
            (app.name, model.__name__)
            for app in apps_with_models
            for model in app.get_models()
        )
