from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Materials OK ")

# views.py
from django.db.models import Sum


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import Financedata
from .serializers import FinanceDataSerializer


class FinanceDataView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # GET → data fetch
    def get(self, request):
        user = request.user
        role = user.profile.role

        if role == 'admin':
            data = Financedata.objects.all()

        elif role == 'analyst':
            data = Financedata.objects.all()

        else:  # normal user
            data = Financedata.objects.filter(uploaded_by=user)

        serializer = FinanceDataSerializer(data, many=True)
        return Response(serializer.data)

    # POST → create data
    def post(self, request):
        serializer = FinanceDataSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(uploaded_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT → update data
    def put(self, request, pk):
        user = request.user
        role = user.profile.role

        try:
            obj = Financedata.objects.get(id=pk)
        except Financedata.DoesNotExist:
            return Response({"error": "Data not found"}, status=404)

        # Role check
        if role in ['admin', 'analyst']:
            serializer = FinanceDataSerializer(obj, data=request.data)

            if serializer.is_valid():
                serializer.save(uploaded_by=obj.uploaded_by)
                return Response(serializer.data)

            return Response(serializer.errors, status=400)

        return Response({"error": "Permission Denied"}, status=403)

    # DELETE → delete data
    def delete(self, request, pk):
        user = request.user
        role = user.profile.role

        try:
            obj = Financedata.objects.get(id=pk)
        except Financedata.DoesNotExist:
            return Response({"error": "Data not found"}, status=404)

        if role == 'admin':
            obj.delete()
            return Response({"message": "Deleted successfully"})

        return Response({"error": "Only admin can delete"}, status=403)
    
    
    





class DashboardView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        role = user.profile.role

        #role-based data
        if role in ['admin', 'analyst']:
            data = Financedata.objects.all()
        else:
            data = Financedata.objects.filter(uploaded_by=user)

        #total income
        total_income = data.filter(category="Income").aggregate(Sum('amount'))['amount__sum'] or 0

        # total expense
        total_expense = data.exclude(category="Income").aggregate(Sum('amount'))['amount__sum'] or 0

        # net balance
        net_balance = total_income - total_expense

        # recent activity
        recent = data.order_by('-uploaded_at')[:5].values()

        #  category wise
        category_data = data.values('category').annotate(total=Sum('amount'))

        return Response({
            "total_income": total_income,
            "total_expense": total_expense,
            "net_balance": net_balance,
            "recent_transactions": list(recent),
            "category_wise": list(category_data)
        })