# For more details about routing, see
# http://www.tornadoweb.org/en/stable/routing.html
from tornado.web import url
from .api.v1.rest import routes as rest_routes
from anthill.framework.utils.urls import include
from . import handlers


route_patterns = [
    url(r'^/aoi/v1', include(rest_routes.route_patterns, namespace='api')),  # for compatibility only
]
