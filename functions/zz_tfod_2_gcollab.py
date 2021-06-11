from integral import *
import msvcrt
import pyautogui

def crun(text):
	write(text)
	press("shift+enter")


def initial():
	button = "shift"
	keyboard.wait(button)
	crun("!pip install tensorflow-gpu")
	crun("import tensorflow as tf")
	keyboard.wait(button)
	crun("print(tf.__version__")
	crun("## **Cloning TFOD 2.0 Github**")
	crun("!git clone https://github.com/tensorflow/models.git")
	keyboard.wait(button)
	crun("cd models/research")
	keyboard.wait(button)
	crun("!protoc object_detection/protos/*.proto --python_out=.")
	keyboard.wait(button)
	crun("!git clone https://github.com/cocodataset/cocoapi.git")
	keyboard.wait(button)
	crun("cd cocoapi/PythonAPI")
	keyboard.wait(button)
	crun("!make")
	crun("cp -r pycocotools /content/models/research")
	keyboard.wait(button)
	crun("##**Install Object Detection API**")
	instant_write("cd ..")
	instant_write("cd ..")
	crun("cp object_detection/packages/tf2/setup.py .")
	keyboard.wait(button)
	crun("!python -m pip install .")
	keyboard.wait(button)
	crun("!python object_detection/builders/model_builder_tf2_test.py")

def custom():
	button = "shift"
	keyboard.wait(button)
	crun("cd/")
	crun("cd /content")
	crun("mkdir training_demo")
	crun("cd training_demo")
	crun("mkdir annotations")
	crun("mkdir pre-trained-models")
	crun("mkdir exported_models")
	crun("mkdir images")
	crun("mkdir models")
	crun("cd images")
	crun("mkdir test")
	crun("mkdir train")
	crun("cd ..")
	crun("cd models")
	crun("mkdir my_ssd_resnet101_v1_fpn")
	crun("cd ..")
	keyboard.wait(button)

def tensorzoo():
	button="shift"
	keyboard.wait(button)
	crun("cd /content/training_demo/pre-trained-models")
	press("ctrl+t")
	time.sleep(1)
	instant_write("https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md")
	press("ctrl+tab")
	time.sleep(1)
	crun("!wget http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_resnet101_v1_fpn_640x640_coco17_tpu-8.tar.gz")
	crun("!tar -xvf ssd_resnet101_v1_fpn_640x640_coco17_tpu-8.tar.gz")
	crun("pwd")
	crun("cd /content/training_demo")
	keyboard.wait(button)
	crun("!python generate_tfrecord.py -x /content/training_demo/images/train -l /content/training_demo/annotations/label_map.pbtxt -o /content/training_demo/annotations/train.record")
	crun("!python generate_tfrecord.py -x /content/training_demo/images/test -l /content/training_demo/annotations/label_map.pbtxt -o /content/training_demo/annotations/test.record")
	keyboard.wait(button)
	crun("!python model_main_tf2.py --model_dir=/content/training_demo/models/my_ssd_resnet101_v1_fpn --pipeline_config_path=/content/training_demo/models/my_ssd_resnet101_v1_fpn/pipeline.config")

def exporter():
	button = "shift"
	keyboard.wait(button)
	crun("!python exporter_main_v2.py --input_type image_tensor --pipeline_config_path /content/training_demo/models/my_ssd_resnet101_v1_fpn/pipeline.config --trained_checkpoint_dir /content/training_demo/models/my_ssd_resnet101_v1_fpn --output_directory /content/training_demo/exported_models/my_model")

while True:
	val = input("> ")
	if val=="1":initial()
	if val=="2":custom()
	if val=="3": tensorzoo()

"""
start("anaconda prompt")
instant_write("E:")
instant_write("cd projects_python")
instant_write("mkdir "+val)
instant_write("cd "+val)
instant_write("conda create -n tensorflow pip python=3.8")
keyboard.wait("esc")
time.sleep(1)
instant_write("conda activate tensorflow")
keyboard.wait("esc")
time.sleep(1)
instant_write("pip install --ignore-installed --upgrade tensorflow==2.2.0")
keyboard.wait("esc")
time.sleep(1)
instant_write('python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"')
keyboard.wait("esc")
time.sleep(1)
instant_write("mkdir Tensorflow")
instant_write("cd Tensorflow")
instant_write("git clone https://github.com/tensorflow/models.git")
keyboard.wait("esc")
time.sleep("2")
instant_write("cd models\\research")
instant_write("protoc object_detection/protos/*.proto --python_out=.")
instant_write("pip install cython")
instant_write("")

"""