# (base) xuwira30@turing:~/DATASETS/Data/cvat/Coins/src$ joe train.py
# device="cuda" cuda gpu de envidia, una capa por encima
#  target="../tmp";  si en vez de constantes se pone como parámetro vale para otros modelos
#  runs  ="../runs"; si en vez de constantes se pone como parámetro vale para otros modelos
# (base) xuwira30@turing:~/DATASETS/Data/cvat/Coins/src$ nohup ./train.py > log.txt 2>&1 &
# para que trabaje en segundo plano aunque se corte lo de la consola, devuelve un número
# (base) xuwira30@turing:~/DATASETS/Data/cvat/Coins/src$ sensors        mira la temperatura de la CPU
# (base) xuwira30@turing:~/DATASETS/Data/cvat/Coins/src$ nvidia-smi     la versión de CUDA de nvisia tiene que coincidir tiene que ser la misma
# NVIDIA SMI nohup ./train.py > log.txt 2>&1 &  no se si esta bien esta línea
# python3 -m venv .coins
# pip install ultralytics tensorrt
# copiar directorios data, src y tmp 


#from pathlib import Path;

#import cv2;
#import numpy as np;
#import math;
#import random;

"""

from ultralytics import YOLO;

if __name__ == "__main__":

   target="../tmp";
   runs  ="../runs";

   yaml_file = os.path.join(target,'dataset.yaml');
   basemodel = 'yolov8x.pt';

   model = YOLO(task="detect", model=basemodel);

   model.train(imgsz=640, batch=-1, epochs=100, data=yaml_file, device="cuda", project=runs, name=".", exist_ok=True, se

   #metrics = model.val();
   #print(metrics);

   model.export(format="onnx"  );
   model.export(format="engine");

"""

