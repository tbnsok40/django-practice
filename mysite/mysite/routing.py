from channels.auth import AuthMiddlewareStack  # AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter  # add URLRouter
import chat.routing  # chat.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})
