from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import datetime
from .models import Metric, Mistake, Result
from .serializers import *


class MetricAPIView(APIView):

    def get(self, request):
        metrics = Metric.objects.all()
        serializer = MetricSerializer(metrics, many=True)
        return Response({"Metrics": serializer.data})


class QuizPackageView(APIView):

    def get(self, request):
        metrics_1 = Metric.objects.order_by("?")[:10]
        serializer_1 = MetricSerializer(metrics_1, many=True)

        metrics_2 = Metric.objects.order_by("?")[:10]
        serializer_2 = MetricSerializer(metrics_2, many=True)
        
        metrics_3 = Metric.objects.order_by("?")[:40]
        serializer_3 = MetricSerializer(metrics_3, many=True)
        
        return Response({"Round_1": serializer_1.data, "Round_2": serializer_2.data, "Round_3": serializer_3.data})


class MistakeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = User.objects.filter(id=request.user.id)
        serializer = UserSerializer(user, many=True)
        return Response({"MistakesData": serializer.data})


class MistakeCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        mistake = request.data.get("Mistake")
        serializer = MistakeCreateSerializer(data=mistake)

        if serializer.is_valid(raise_exception=True):
            mistake_saved = serializer.save()

        return Response({"Success": "Mistake '{}' created succesfully.".format(mistake_saved.id)})


class MistakeDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user_id = request.GET.get('user_id')
        metric_id = request.GET.get('metric_id')

        mistake = Mistake.objects.get(user_id=user_id, metric_id=metric_id)
        mistake.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ResultCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        result = request.data.get("result")
        serializer = ResultCreateSerializer(data=result)

        if serializer.is_valid(raise_exception=True):
            result_saved = serializer.save()

        return Response({"Success": "Result '{}' created succesfully.".format(result_saved.score)})


class DayTopAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        results = Result.objects.filter(date__gte=datetime.date.today()).order_by("-score")[:10]
        serializer = ResultSerializer(results, many=True)
        return Response({"DayTop": serializer.data})


class WeekTopAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        weekday = datetime.date.today().weekday()
        results = Result.objects.filter(date__gte=datetime.date.today() - datetime.timedelta(days=weekday)).order_by("-score")[:10]
        serializer = ResultSerializer(results, many=True)
        return Response({"WeekTop": serializer.data})


class MonthTopAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        results = Result.objects.filter(date__month=datetime.date.today().month, date__year=datetime.date.today().year).order_by("-score")[:10]
        serializer = ResultSerializer(results, many=True)
        return Response({"MonthTop": serializer.data})
