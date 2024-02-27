from fastapi import FastAPI
import logging
from importlib.metadata import entry_points

logger = logging.getLogger(__name__)


def get_app():
    app = FastAPI(title="GINO FastAPI Demo")
    load_modules(app)
    return app


def load_modules(app=None):
    for ep in entry_points()["gino_fastapi_demo.modules"]:
        logger.info("Loading module: %s", ep.name)
        mod = ep.load()
        if app:
            init_app = getattr(mod, "init_app", None)
            if init_app:
                init_app(app)
