from transformers import AutoTokenizer, AutoModelWithLMHead
from deepface import DeepFace
tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-emotion")

model = AutoModelWithLMHead.from_pretrained("mrm8488/t5-base-finetuned-emotion")



def get_emotion(text):
  input_ids = tokenizer.encode(text + '</s>', return_tensors='pt')

  output = model.generate(input_ids=input_ids,
               max_length=2)
  
  dec = [tokenizer.decode(ids) for ids in output]
  label = dec[0]
  return label
#print(get_emotion("i feel as if i havent blogged in ages are at least truly blogged i am doing an update cute"))



def face_expression(file_path):
    backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']
    #face = DeepFace.detectFace(img_path = "img.jpg", target_size = (224, 224), detector_backend =backends[4])
    
    try:
        obj=DeepFace.analyze(img_path=file_path,actions=['emotion'])
    except:
        noface={'message' : 'no face exists here'}
        return noface
    return obj

import os
import sys
import urllib.request
import json

client_id = "3IcEzV3WWP77e0DICyin" # 개발자센터에서 발급받은 Client ID 값
client_secret = "9MXpqzqgti" # 개발자센터에서 발급받은 Client Secret 값


def translate(sentences):
     
    eng=[]
    for sentence in sentences:
        encText = urllib.parse.quote(sentence)
        data = "source=ko&target=en&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            words=json.loads(response_body.decode('utf-8'))
            #print(words)
            #print(words['message'])
            #print(words['message']['result'])
            #print(words['message']['result']['translatedText'])
            words=words['message']['result']['translatedText']
            eng.append(words)
        else:
            print("Error Code:" + rescode)
    return eng

#sentences=['이번에는 미국 테네시 주로 가보실까요. 생애 첫 등교에 나선 4살 안나 양이 일열로 늘어선 경찰관들의 환영을 받으며 등장합니다.',
# '한 명 한 명 힘차게 손벽을 부딪히며 반갑게 인사를 나누는데요.',
# '안나에 든든한 지원군을 자처한 경찰관들 왜 이런 자리를 마련했을까요.',
# '안나의 아빠 캐빈 경사는 20년 차 베테랑으로 지난해 11월 의료 응급 상황을 겪은 후 근무 중 돌연 순직했는데요.',
# '그런 안나가 아빠의 빈자리를 느끼지 않도록 경찰 동료 30여 명이 일일 아빠로 깜짝 변신한 겁니다.',
# '안나에게 결코 잊지 못할 하루를 선물했네요. 투데이 와글와글이었습니다.']
#eng=translate(sentences)
#print(get_emotion(eng[0]).split()[1])


naver_url="https://clovaspeech-gw.ncloud.com/external/v1/3598/b5defce23910b08b500375ac0ddca79a4fe93a9c72b49b980e5a853dc3ec8667"
naver_secret="ea397aca834f4de9beab17da75f46ddf"
def Speech2Text(name):
    shell="curl --location --request POST '" + naver_url + "/recognizer/upload' --header 'X-CLOVASPEECH-API-KEY: " + naver_secret + " ' --form 'media=@/home/ubuntu/yourchoice/media/Speech/" + str(name) + ".mp4' --form 'params={\"language\":\"ko-KR\",\"completion\":\"sync\"};type=application/json'"

    stream=os.popen(shell)
    output=stream.read()

    ar=json.loads(output)
            #print(ar)

    text=[]
    for i in ar["segments"]:
        text.append(i["text"])
    
    return text
#import os
#import numpy as np
#import matplotlib.pyplot as plt
#import cv2
#from PIL import Image
#import torch
#import tensorflow as tf
#from tensorflow.keras.models import Model,Sequential, load_model,model_from_json
#from tensorflow.compat.v1.keras.backend import set_session
#config = tf.compat.v1.ConfigProto()
#sess=tf.compat.v1.Session(config=config)
#set_session(sess)
#
#from facial_analysis import FacialImageProcessing
#imgProcessing=FacialImageProcessing(False)
#import torch
#use_cuda = torch.cuda.is_available()
#print(use_cuda)
#
#device = 'cuda' if use_cuda else 'cpu'
#
#from hsemotions.facial_emotions import HSEmotionRecognizer
#
#model_name='enet_b0_8_best_afew'
#model_name='enet_b0_8_best_vgaf'
#model_name='enet_b0_8_va_mtl'
#model_name='enet_b2_8'
#
#fer=HSEmotionRecognizer(model_name=model_name,device=device)


#def face_expression_recognizer(file_path):
#    fpath=file_path
#    frame_bgr=cv2.imread(fpath)
#    frame = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
#
#    bounding_boxes, points = imgProcessing.detect_faces(frame)
#    points = points.T
#    emotion=0
#    face_img=0
#    for bbox,p in zip(bounding_boxes, points):
#        box = bbox.astype(int)
#        x1,y1,x2,y2=box[0:4]
#        face_img=frame[y1:y2,x1:x2,:]
#        emotion,scores=fer.predict_emotions(face_img,logits=True)
#        print(emotion,scores)
#    
#    return emotion,face_img

#face_expression_recognizer(
        
