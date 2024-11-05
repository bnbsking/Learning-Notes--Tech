# Dataset
+ DNN house price prediction
    https://www.kaggle.com/harlfoxem/housesalesprediction

+ DNN pokemon battle binary classification
    https://www.kaggle.com/terminus7/pokemon-challenge

+ CNN Image recognition
    http://www.cs.toronto.edu/~kriz/cifar.html

+ tensorflow datasets
    https://www.tensorflow.org/datasets/


# Environment setup
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


### Jupyter notebook style setting
jt -fs 12 -tfs 12 -ofs 12 -T -N -cellw 95% -t chesterish
