from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from .deeplearning import *
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
import requests

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're in index.")


class SceneViewSet(viewsets.ModelViewSet):
    queryset = Scene.objects.all()
    serializer_class = SceneSerializer

class Text_readerViewSet(viewsets.ModelViewSet):
    queryset=Text_reader.objects.all()
    serializer_class = Text_readerSerializer

    def create(self, request):
        serializer = Speech_to_TextSerializer(data = request.data, many=True)
        
        if serializer.is_valid():
            
            text=request.data['Text']
            name=request.data['Name']
            eng=translate([text])[0]

            emotion=get_emotion(str(eng)).split()[1]
            try :
                t=Text_reader.objects.create(Name=name,Text=text,Response={'emotion' : emotion})
            except :
                return HttpResponse('An error occurs.',status=423)
            pub_date=t.pub_date
            response=t.Response
            return JsonResponse(response)
        else:
            return HttpResponse(status=500)

import os
import json
class Speech_to_TextViewSet(viewsets.ModelViewSet):
    queryset=Speech_to_Text.objects.all()
    serializer_class = Speech_to_TextSerializer

    def create(self, request):
        serializer = Speech_to_TextSerializer(data = request.data, many=True)
        uploadedFile = request.FILES.get('uploadedFile')
        
        if uploadedFile != None and serializer.is_valid() :
            name=request.data["Name"]
            
            try :
                s=Speech_to_Text.objects.create(uploadedFile=uploadedFile,Name=name)
            except :
                return HttpResponse('An error occurs.',status=423)
            pub_date=s.pub_date
            kor_texts,times=Speech2Text(name)
            texts=translate(kor_texts)
            emotions=[]

            for text in texts:
                emotions.append(get_emotion(str(text)).split()[1])
            
            s.Response={'texts' : texts, 'emotions' : emotions,'timestamp' : times}
            s.save()
            return JsonResponse(s.Response)
        else:
            return HttpResponse(status=500)


class Face_readerViewSet(viewsets.ModelViewSet):
    queryset=Face_reader.objects.all()
    serializer_class = Face_readerSerializer
    
    def create(self, request):
        serializer = Face_readerSerializer(data = request.data, many=True)
        uploadedFile = request.FILES.get('uploadedFile')
        

        if uploadedFile != None and serializer.is_valid() :
            name=request.data["Name"]
            #print("uploaded name : " + str(name))
            # 차후 동영상에 대해서 프레임을 끊어서 아래의 함수를 돌리는 방안을 검토하자.
            try :
                s=Face_reader.objects.create(uploadedFile=uploadedFile,Name=name)
            except :
                return HttpResponse('An error occurs.',status=423)
            pub_date=s.pub_date
            #expression=face_expression("/home/ubuntu/yourchoice/media/Face/"+name+".jpg")
            expression=movie_extractor("/home/ubuntu/yourchoice/media/Face/"+name)
            s.Response=expression
            s.save()
            return JsonResponse(s.Response)
        else:
            return HttpResponse(status=500)
