from app.services.schema import ServiceType


def get_service(service_type: ServiceType, default=None):
    from app.services.manager import service_manager

    if not service_manager.factories:
        service_manager.register_factories()
    return service_manager.get(service_type, default)


def initialize_settings_service() -> None:
    from app.services.settings import factory as settings_factory

    get_service(ServiceType.SETTINGS_SERVICE, settings_factory.SettingsServiceFactory())


async def initialize_services() -> None:
    initialize_settings_service()
