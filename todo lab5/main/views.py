from rest_framework import viewsets
from main.models import *
from main.serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action



class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.filter(mark=True)
    serializer_class = TaskSerializer

    def retrieve(self, *args, **kwargs):
        self.serializer_class = ShowTaskSerializer
        return viewsets.ModelViewSet.retrieve(self, *args, **kwargs)

    @action(detail=True, methods=['GET'], url_path='completed')
    def completed(self, request, pk):
        queryset = Task.objects.filter(id=pk, mark=False)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)
