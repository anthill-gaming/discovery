from anthill.platform.apps import BaseAnthillApplication
from anthill.framework.utils.encoding import force_text
from anthill.framework.conf import settings
import logging
import json

logger = logging.getLogger('anthill.application')


class AnthillApplication(BaseAnthillApplication):
    """Anthill application."""

    def __init__(self):
        super().__init__()
        self.load_services()

    def load_services(self):
        registry = {}
        path = getattr(settings, 'REGISTERED_SERVICES', None)
        try:
            if path is not None:
                with open(path) as f:
                    registry.update(json.load(f))
        except Exception as e:
            logging.warning(force_text(e))
        # noinspection PyAttributeOutsideInit
        self.registry = registry
