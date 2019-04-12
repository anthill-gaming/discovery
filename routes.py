# For more details about routing, see
# http://www.tornadoweb.org/en/stable/routing.html
from tornado.web import url
from discovery import handlers
from discovery.api.compat.rest import routes as rest_routes
from anthill.framework.utils.urls import include

route_patterns = [
    url(r'^/', include(rest_routes.route_patterns, namespace='api')),  # for compatibility only
]
