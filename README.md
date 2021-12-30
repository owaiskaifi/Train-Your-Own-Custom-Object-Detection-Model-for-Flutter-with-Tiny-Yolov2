This fork is made to train and create a TFLite of your Custom Object Detection Model compatible with [Flutter](https://flutter.dev/) and [TFLite 1.1.2](https://pub.dev/packages/tflite) library.


## REQUIREMENTS
- Windows 7 or 10 (64bits)
- Nvidia GPU (GTX 650 or newer) for CUDA Acceleration

REMOVE FROM PATH ANY OTHER STANDALONE PYTHON YOU MAY HAVE

At "Environment Variables" > "System" > "Path" > "Edit"
&ensp;Remove: (e.g)
&emsp;H:\ProgramData\Python\Python310\Scripts\
&emsp;H:\ProgramData\Python\Python310\

You can add it back when finished.

## INSTALLATION

Note: Everything is very version sensitive, so use the exactly version mentioned above.

### 0- Install Visual Studio 2017 Library

<code>https://visualstudio.microsoft.com/vs/older-downloads/</code>

&emsp;I´m not sure if works with newer versions.

### 1- Install Anaconda 3

<code>https://www.anaconda.com/products/individual</code>

&emsp;The one I´m using is "Anaconda3-2021.11-Windows-x86_64" but newer 
&emsp;releases should be compatible as long is version 3.

### 2- Add to "Environment Variables" > "System" > "Path" > "New"

	[YOUR DIRECTORY]\Anaconda3\Scripts\
	[YOUR DIRECTORY]\Anaconda3\Library\
	[YOUR DIRECTORY]\Anaconda3\Library\bin\
	[YOUR DIRECTORY]\Anaconda3\Library\mingw-w64\bin\


### 3- Uninstall any CUDA you might have
	
	The NVIDIA softwares you ALLOW to have:
	-NVIDIA Control Panel
	-NVIDIA Driver
	-NVIDIA Geforce Experience
	-NVIDIA RTX
	-NVIDIA RTX Voice
	-NVIDIA PhysX
	-NVIDIA USB C
	-NVIDIA FrameView SDK

	Uninstall the following:
	-NVIDIA CUDA
	-NVIDIA Nsight
	-NVIDIA Tools
	
	Reboot the computer


### 4- Download CUDA CUDA 10.0

<code>https://developer.nvidia.com/cuda-10.0-download-archive</code>


### 5- Install CUDA 10.0 

	5.1- Choose "Custom Installation"
	5.2- Create a shorter path (e.g. C:\CUDA) because the default path will be too long and we will not be able to add it to "Environment Variables Path"
	5.3- It MUST be in the same directory of Windows (e.g. C:)


### 6- Add to "Environment Variables" > "System" > "Path" > "New"

	Usually added automatically:

	[YOUR DIRECTORY]\CUDA\bin (e.g. C:\CUDA\bin )
	[YOUR DIRECTORY]\CUDA\libnvvp (e.g. C:\CUDA\libnvvp )

	You always need to add it:

	[YOUR DIRECTORY]\CUDA\extras\CUPTI\libx64 (e.g. C:\CUDA\extras\CUPTI\libx64 )


### 7- Download cuDNN v7.6.5 (November 5th, 2019), for CUDA 10.0

<code>https://developer.nvidia.com/rdp/cudnn-archive</code>


### 8- Install cuDNN

	8.1- Under the .zip file, move "cuda > bin > *.dll" to your "CUDA > bin" folder
	8.2- Create a copy and rename "cudnn64_7.dll" to "cudnn64_100.dll"

	8.3- Under the .zip file, move "cuda > include > *.h" to your "CUDA > include" folder

	8.4- Under the .zip file, move "cuda > lib > x64 > *.lib" to your "CUDA > lib > x64" folder

	8.5- REBOOT the computer

## ENVIRONMENT SETUP


### 1- Initiate Anaconda

	1.1- Open "cmd" type: conda init
	1.2- Close and reopen "cmd"


### 2- Setup Environment

	2.1- Open "cmd" on ADMIN MODE type: conda deactivate
	2.2- On "cmd" type: conda create \--name tensor_yolo_1.15 python=3.7.0
	2.3- On "cmd" type: conda activate tensor_yolo_1.15
	2.6- On "cmd" type: 
		 pip install tensorflow-gpu==1.15.0
		 pip install Cython==0.29.26
		 pip install opencv-python==4.5.4.60
		 pip3 install \--extra-index-url https://google-coral.github.io/py-repo/ tflite==2.4.0
		 conda install pyqt=5
		 conda install -c anaconda lxml=4.6.1
		 pip install in_place==0.5.0

### 3- Setup the Project

3.1- Download and extract
&nbsp;<code>https://github.com/IfProgrammingIsMagicImaWizard/darkflow</code>

	 With conda activate tensor_yolo_1.15:
		On "cmd" type: cd /d "PATH TO THE PROJECT FOLDER" 	    
				(e.g     cd /d "D:\Projetos\Flutter\darkflow" )
		On "cmd" type: python setup.py build_ext \--inplace

3.2- Download YOLO V2 Weights
	<code>https://pjreddie.com/darknet/yolo/</code>
	![](https://i.imgur.com/TMHDb3h.png)
	
3.3- Put into <code>darkflow/bin</code>

### 4- Setup the labelImg

4.1- Download <code>labelImg</code> and extract into <code>darkflow/labelImg</code>:
		<code>https://github.com/tzutalin/labelImg</code>


 	4.2- With conda activate tensor_yolo_1.15:
		On "cmd" type: cd /d "PATH TO labelImg" 
				(e.g     cd /d "D:\Projetos\Flutter\darkflow\labelImg" )
		On "cmd" type: pyrcc5 -o resources.py resources.qrc

 	4.3- Move "resources.py" and "resources.qrc" to ´libs´ folder 		(e.g darkflow\labelImg\libs )

## IMAGE LABELLING

### 1- Data Gathering

Put all your images into `darkflow\train\Images` folder.

Make all images square, .jpg, up to <code>416x416</code> pixels with <code>Photoshop</code> and [iloveimg.com](https://www.iloveimg.com/).

Run <code>labelImg.py</code> on <code>darkflow\labelImg</code> folder.

### 2- Image labelling

With labelImg Open:

- Go to view > Enable Auto Save Mode
- Set ´Save Dir´ to <code>darkflow\train\Images</code> folder
- Open Dir (Same Path)
- Start Labeling
- Short Cuts:
- W - Draw Label
- A - Next Image
- D - Previous Image

### 3- Move .xml files

Move the </code>.xlm</code> files from <code>darkflow\train\Images</code> to <code>darkflow\train\annotation</code>

### 4- (Optional) Update Annotation´s path to the Image file

If you are using images from a database (like RoboFlow or Kaggle) you will notice that, opening the Annotation with text editor like Notepad, the Annotation´s path to the Image file is not correct.

Example:

It is this:
<code><path>\0_ELAADEN_CACHE_FLOW.jpg\</path></code>
<br>When it should be this:
<code><path>D:\Flutter\YOLO_V2\darkflow\train\Images\0_ELAADEN_CACHE_FLOW.jpg\</path></code>
<br>
To update the Annotation to your liking edit the <code>darkflow\update_annotation.py</code> script and run on <code>tensor_yolo_1.15</code> environment:<br><br><code>conda activate tensor_yolo_1.15</code> and then <code>python PATH_TO_THE_SCRIPT</code>

##  TRAIN YOUR MODEL

### 1- Edit <code>labels.txt</code>

Edit <code>darkflow/labels.txt</code> to match with your classes.

### 2- Edit cfg file

On <code>darkflow\cfg</code> create a copy (bacause we will need the original too) <BR>&emsp;of the <code>yolov2-tiny-voc.cfg</code> and rename it <br><br>&emsp;&emsp;&emsp;&emsp;&emsp;(e.g <code>yolov2-tiny-voc-c16.cfg</code> because I have 16 classes )
<br>
- Open with a text editor like Atom or Notepad++.

- Go to the bootom and edit the <code>line 124</code> and put the amount of classes you have (e.g classes = 20 )

- Now we need to alter the last layer´s filter to match our amount of classes

- Go to <code>line 118</code> the amount will be the result of this formula:<br> <code>(num classes + 5) * 5 </code>

Examples:
<br> 1 class -> (1 + 5) \* 5 = 30 -> filters=30
<br> 20 classes -> (20 + 5) \* 5 = 125 -> filters=125

### 3- (Optional) Choosing another model

In this turorial we are using Tiny YoloV2 Weights and Cfg.
<br>If you want to use other model download the Weights and Cfg from <code>https://pjreddie.com/darknet/yolo/</code>
<br>Put the Weight in the <code>darkflow/bin</code> folder and Cfg in the <code>darkflow/cfg</code> folder.

### 4- Train our model

	With conda activate tensor_yolo_1.15:
		On "cmd" type: cd /d "PATH TO THIS PROJECT" 	     (e.g     cd /d "D:\Projetos\Flutter\darkflow\" )
		On "cmd" type:

<code>python flow \--model cfg/yolov2-tiny-voc-16.cfg \--load bin/yolov2-tiny-voc.weights \--train \--annotation train/annotation \--dataset train/Images \--gpu 0.8 \--epoch 1000</code>
<br>
Explanation:

<br><code>\--model</code> Path to your modifed cfg (it will look for the original too)
<br><code>\--load</code> Path to the pre trained wights
<br><code>\-- train</code> Command to train
<br><code>\--annotation</code> Path to the annotation´s folder
<br><code>\--dataset</code> Path to the images folder
<br><code>\--gpu</code> Command to use the GPU, 0.8 means 80%, recommended to be safe since Windows use a bit of the GPU to function
<br><code>\--epoch</code> Amount of training, default is 5000, but start with 1000 to see if everthing is working

On a Ryzen 3700x and 1660Ti training 1000 epochs took 30 min using GPU or 60 hours using CPU.

### 5- Test our model

With the training finished we should have <code>darkflow\ckpt</code> folder.

#### 5.1 Testing CKPT on Images

Prepare the <code>darkflow\sample_img</code> folder with some images.

	With conda activate tensor_yolo_1.15:
		On "cmd" type: cd /d "PATH TO THIS PROJECT" 	     (e.g     cd /d "D:\Projetos\Flutter\darkflow\" )
		On "cmd" type:

<code>python flow \--imgdir sample_img/ \--model cfg/yolov2-tiny-voc-16.cfg \--load 10750 \--gpu 0.8  \--threshold 0.0</code>

<br>Explanation:

<br><code>\--model</code> Path to your modifed cfg
<br><code>\--load</code> Path to your trained wights
<br><code>\--imgdir</code> Path to the sample images folder
<br><code>\--gpu</code> Command to use the GPU, 0.8 means 80%, recommended to be safe since Windows use a bit of the GPU to function
<br><code>threshold 0.0</code> Set so just confidence above this number will be return, 0.0 return all, up to 1.0 (100%)

You can also get the resuts in Json format by adding <code>\--json</code>

<br></brIn>In the example above we load our ckpt on checkpoint 10750 that is in our ckpt folder:

![](https://i.imgur.com/UbFTVzP.png)

If everthing works right your input image should be transform into an output like this:

![](https://i.imgur.com/g9ZfFlh.png)

#### 5.2 Testing CKPT on Video

You can also test using a video, but in my case it didn´t work, it don´t draw the boxes
But the command is the above:

<code>python flow \--model cfg\yolov2-tiny-voc-16.cfg \--load 10750 \--demo G:\Download\video.avi \--gpu 0.8 \--saveVideo \--threshold 0.0</code>

If you out of VRAM use CPU:

<code>python flow \--model cfg\yolov2-tiny-voc-16.cfg \--load 10750 \--demo G:\Download\video.avi \--saveVideo \--threshold 0.0</code>

### 6- Convert to .pb

Also known as generate frozen graph or genarate saved model.

	With conda activate tensor_yolo_1.15:
		On "cmd" type: cd /d "PATH TO THIS PROJECT" 	     (e.g     cd /d "D:\Projetos\Flutter\darkflow\" )
		On "cmd" type:

<code>python flow \--model cfg/yolov2-tiny-voc-16.cfg \--load 10750 \--savepb</code>

<br>Explanation:

<br><code>\--model</code> Path to your modifed cfg
<br><code>\--load</code> Path to your trained wights
<br><code>\--savepb</code> Command to save pb file

#### 6.1 Testing .pb on Images

Similar to testing our CKPT model we can test our .pb:

<code>python flow \--pbLoad built_graph/yolov2-tiny-voc-16.pb \--metaLoad built_graph/yolov2-tiny-voc-16.meta \--imgdir sample_img/</code>

### 7- Convert to TFLite

	With conda activate tensor_yolo_1.15:
		On "cmd" type: cd /d "PATH TO THIS PROJECT" 	     (e.g     cd /d "D:\Projetos\Flutter\darkflow\" )
		On "cmd" type:

<code>tflite_convert \--graph_def_file="built_graph\\yolov2-tiny-voc-16.pb" \--output_file="G:\\Download\\yolov2_28_12_2021_22_40.tflite"  \--input_format=TENSORFLOW_GRAPHDEF \--output_format=TFLITE \--input_shape=1,416,416,3 \--input_array=input \--output_array=output \--inference_type=FLOAT \--input_data_type=FLOAT</code>

Change just <code>\--graph_def_file</code> and <code>\--output_file</code>

This will generate a model compatible with [Flutter](https://flutter.dev/) and [tflite 1.1.2](https://pub.dev/packages/tflite)

Note: There is a significant loss in accuracy when converting to TFlite (I'm case was about 13%) but that is the price for performance.

### 8- Using on Flutter

&emsp;Download sample project: https://github.com/IfProgrammingIsMagicImaWizard/sample_object_detection

The result is something like:

	[{"label": "Cat", 
	"confidence": 0.83, 
	"topleft": {"x": 11, "y": 90}, 
	"bottomright": {"x": 66, "y": 179}}, 
	
	{"label": "Dog", 
	"confidence": 0.93, 
	"topleft": {"x": 191, "y": 274}, 
	"bottomright": {"x": 246, "y": 351}}, 

	{"label": "Bird", 
	"confidence": 0.88, 
	"topleft": {"x": 109, "y": 8}, 
	"bottomright": {"x": 154, "y": 79}}]

You can use the box information do draw on a Image, Video or Live Feed.

You can know more at: https://pub.dev/packages/tflite/example


## ACKNOWLEDGMENT

Thanks to [Mark Jay](https://www.youtube.com/channel/UC2W0aQEPNpU6XrkFCYifRFQ) of which most of the tutorial was based on.
