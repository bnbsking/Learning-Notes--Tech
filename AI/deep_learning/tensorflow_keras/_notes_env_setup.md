# Windows 10 to Ubuntu 20.04
1. win10 下載ubuntu iso檔 並製作開機碟 gpt FAT

2. win10 執行 diskmgmt.msc 壓縮磁碟區

3. win10 電源選項 關閉快速開機

4. bios 關閉快速開機 關閉安全開機 更改開機順序

5. ubuntu安裝 裝完後拔USB重開機

6. sudo apt update

7. sudo apt install gnome-tweak

8. sudo apt install vim

9. 
```bash
wget -c https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb ＃-c繼續下載
sudo dpkg -i google-chrome-stable_current_amd64.deb ＃dpkg專用於.deb -i install
```
釘選至工作列

10. 安裝顯卡驅動
```bash
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt install ubuntu-drivers-common
ubuntu-drivers devices 			#查看需要裝哪個版本驅動 ＃目前是440
sudo apt install nvidia-driver-440 
sudo reboot

sudo update-pciids
lspci | grep NVIDIA	#確認有無裝好一
dpkg --get-selections   #確認有無裝好二
apt list --installed
```

11. CUDA
    建議dpkg一系列指令
    https://developer.nvidia.com/cuda-downloads
	設定環境變數
```bash
export PATH=/usr/local/cuda-10.2/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64/${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
cuda-install-samples-10.2.sh ~
cd ~/NVIDIA_CUDA-10.2_Samples/5_Simulations/nbody
make
./nbody
```
確認有無安裝 cat /usr/local/cuda/version.txt

12. CUDNN
https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html
確認有無安裝 cat

13. miniconda
https://docs.conda.io/en/latest/miniconda.html
sh安裝在 /home/James/miniconda3
去/etc/env設定環境變數 /home/James/miniconda3/bin
更新環境變數 source ~/.bashrc
可下conda create -n
jupyter notebook 要用conda install 裝
```bash
sudo chown -R $USER:$USER miniconda3
sudo chmod -R 777 miniconda3 
pip install tensorflow-gpu
```


# Docker
1. install docker
2. install nvidia driver on host
3. install nvidia-docker2


# Jetson Nano
+ commands

```bash
sudo apt-get install python3-pip
pip3 install virtualenv
cd pathToInstall
virtualenv -p Python3 myenv
cd ./myenv/bin
source activate

# install NVIDIA SDK Manager

sudo apt-get install libhdf5-serial-dev hdf5-tools
sudo apt-get install zlib1g-dev zip libjpeg8-dev libhdf5-dev
sudo pip3 install -U numpy grpcio absl-py py-cpuinfo psutil portpicker grpcio six mock requests gast h5py astor termcolor

pip install --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v42 tensorflow-gpu==1.14.0+nv19.7
pip install keras==2.3.0
```


# Ubuntu 20.04
+ install nvidia driver e.g. ./NVIDIA-Linux-x86_64-470.74.run
+ install cuda e.g. ./cuda_11.2.2_460.32.03_linux.run
```bash
export PATH=$PATH:/usr/local/cuda-11.2/bin
export LD_LIBRARY_PATH=/usr/local/cuda-11.2/lib64
```
+ install cudnn
```bash
sudo cp cuda/include/* /usr/local/cuda-11.2/include
sudo cp cuda/lib64/* /usr/local/cuda-11.2/lib64
```


# Windows 10
Windows10 + GTX1650 + tensorflow-gpu==1.14 + keras=2.3
1. Nvidia driver 431 installer
2. visual studio 2017 professional installer
3. cuda 10.0 installer
    + check env-path (default: yes)
4. cudnn 7.4 zip
	+ copy three files into `C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v10`
5. miniconda installer
	+ create env
	+ pip install tensorflow-gpu==1.14
	+ pip install keras==2.3
	+ pip install jupyter notebook


# Jupyter notebook style
```bash
jt -fs 12 -tfs 12 -ofs 12 -T -N -cellw 95% -t chesterish
```
