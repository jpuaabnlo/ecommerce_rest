from rest_framework import generics

class GeneralListApiView(generics.ListAPIView):
    serializer_class = None
    '''Crear una Api View general'''
    def get_queryset(self):
        '''para conseguir el modelo prncipal de la clase Meta'''
        model = self.get_serializer().Meta.model
        return model.objects.filter(state = True)