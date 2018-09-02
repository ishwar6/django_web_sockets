from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from notifier.consumers import EchoConsumer, Tick, NoseyConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("user/", NoseyConsumer),
    ])
})