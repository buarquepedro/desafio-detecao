# coding: utf8

import cv2
import numpy as np

from django.shortcuts import render

from .models import Opencv
from .forms import FormOpencv


def load_image(obj):
    imagem_np = np.asarray(bytearray(obj.imagem.read()), dtype="uint8")
    return cv2.imdecode(imagem_np, cv2.IMREAD_COLOR)


def deteccao(request):
    form = FormOpencv(request.POST or None, request.FILES or None)
    if form.is_valid():
        modelo = Opencv(imagem=request.FILES['imagem'])
        imagem = load_image(modelo)

        # Salva imagem original para posterior comparacao
        cv2.imwrite("PDI/core_1/static/img/deteccao_original.png", imagem)

        # Faz a deteccao na imagem convertida para gray
        gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        xml_face = cv2.CascadeClassifier('PDI/cascades/haarcascade_frontalface_default.xml')
        faces = xml_face.detectMultiScale(gray, 1.3, 5)

        red_color = (0, 0, 255)
        for (x, y, w, h) in faces:
            cv2.rectangle(imagem, (x, y), (x + w, y + h), red_color, 2)

        cv2.imwrite("PDI/core_1/static/img/deteccao.png", imagem)
        return render(request, 'deteccao.html', {'form': form, 'data': True})
    else:
        form = FormOpencv()
    return render(request, "deteccao.html", {'form': form})
