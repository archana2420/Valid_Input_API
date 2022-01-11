from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class Valid_Input_APIView(APIView):

    def post(self,request):
        valid=[]
        invalid=[]
        for i in request.data:
            val=str(i)
            if val.isnumeric():
                if i<=0:
                    invalid.append(i)
                else:
                    valid.append(i)
            else:
                invalid.append(i)



        min1=min(valid)
        max1=max(valid)
        average=sum(valid)/len(valid)
        valid_enteries=len(valid)
        invalid_enteries=len(invalid)


        context={'valid_enteries':valid_enteries,'invalid_enteries':invalid_enteries,'min':min1,'max':max1,'average':average}
        return Response(context)
