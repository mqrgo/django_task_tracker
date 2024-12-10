from drf_spectacular.utils import OpenApiParameter, OpenApiTypes, extend_schema
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from task_tracker import models, serializers


class Tasks(ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.Task

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='id',
                type=OpenApiTypes.STR,
                description='The id of the task',
                required=True,
            )
        ]
    )
    @action(methods=['get'], detail=False)
    def get_task(self, request: Request) -> Response:
        task_id = request.query_params.get('task_id', None)
        return Response(task_id)
