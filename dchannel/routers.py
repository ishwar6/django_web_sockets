
class ChatRouter(BaseRouter):
    route_name = 'chat-route'
    valid_verbs = ['chat', 'subscribe']

    def get_subscription_channels(self, **kwargs):
        return ['chatroom']

    def chat(self, *args, **kwargs):
        errors = {}
        if 'name' not in kwargs or len(kwargs['name']) is 0:
            errors['name'] = 'Specify a name'

        if 'message' not in kwargs or len(kwargs['message']) is 0:
            errors['message'] = 'Enter a chat message'

        if errors:
            self.send_error(errors)
        else:
            self.send({'status': 'ok'})
            self.publish(self.get_subscription_channels(), kwargs)


route_handler.register(ChatRouter)

class CompanyRouter(ModelRouter):
    serializer_class = CompanySerializer
    model = Company
    route_name = 'company-route'
    include_related = [StaffSerializer, DocumentSerializer, CompanyOwnerSerializer]

    def get_query_set(self, **kwargs):
        return self.model.objects.all()

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['pk'])


route_handler.register(CompanyRouter)


class CompanyUniformRouter(ModelRouter):
    serializer_class = CompanySerializer
    model = Company
    route_name = 'company-route'
    include_related = [StaffSerializer, DocumentSerializer, CompanyOwnerSerializer]

    def get_query_set(self, **kwargs):
        return self.model.objects.all()

 

route_handler.register(CompanyUniformRouter)
