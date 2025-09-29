from fastapi import FastAPI

from core.app_schema import AppSchema
from core.exception import AppNotFoundException


apps = {
    "main": {
        "name": "Main App",
        "description": "Main application",
        "version": "1.0.0",
        "path": "/",
        "router": None,  # This will be set when the app is mounted
    },
    "user": {
        "name": "User App",
        "description": "User management application",
        "version": "1.0.0",
        "path": "/user",
        "router": None,  # This will be set when the app is mounted
    },
}


def get_app_info(app_name: str) -> AppSchema:
    """Get application information by name."""
    app_info = apps.get(app_name)
    if app_info:
        return AppSchema(
            name=app_info["name"],
            description=app_info["description"],
            version=app_info["version"],
            path=app_info["path"],
        )
    else:
        raise AppNotFoundException(app_name=app_name)


def mount_app(app_name: str, app: FastAPI):
    """Mount an application to the main app."""
    if app_name in apps:
        apps[app_name]["router"] = app
        return True
    else:
        return False


def create_main_app() -> FastAPI:
    """Create the main FastAPI application."""
    main_app_info = get_app_info("main")
    
    main_app = FastAPI(
        title=main_app_info.name,
        description=main_app_info.description,
        version=main_app_info.version,
    )

    # Mount sub-apps
    for app_name, app_info in apps.items():
        if app_info["router"]:
            main_app.mount(app_info["path"], app_info["router"])

    return main_app
