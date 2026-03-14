
# NeedAPP_DLAPP
#### A common software and tool downloader
<p>
    <img alt="Dynamic JSON Badge" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dgithub%26queryKey%3Dliyunhan177&query=%24.data.totalSubs&suffix=%20followers&label=GitHub&color=262626">
    <img alt="Dynamic JSON Badge" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.bilibili.com%2Fx%2Frelation%2Fstat%3Fvmid%3D571556798&query=data.follower&style=flat&logo=bilibili&logoColor=white&label=bilibili%20fans&labelColor=%23F37697">
    <img src="https://img.shields.io/badge/Language-Python-blue" alt="">
    <img src="https://img.shields.io/badge/OS-Windows-blue" alt="">
    <img src="https://img.shields.io/github/stars/liyunhan177/NeedAPP_DLAPP.svg" alt="">
    <img alt="" src="https://img.shields.io/badge/version-0.2.0-yellow">
</p>

[English](README.en.md) [中文](README.zh.md)  

## Catalog

- [🚀 Quick Start](#quick-start)
- [📦 Installation Guide](#installation-guide)
- [🛠 User Guide](#user-guide)
- [🤝 Contributing](#contributing)
- [🌠 Future Roadmap](#future-roadmap)
- [📝 Special Notes](#special-notes)

## Quick Start
__Project Structure__
```aiignore
NeedAPP_DLAPP
├─ pyproject.toml
├─ README.md
├─ test
│  ├─ about is folder.txt
│  └─ test_func
│     └─ 你真的看提示了吗.py
├─ src
│  ├─ main_page.py
│  └─ __init__.py
├─ res
│  ├─ sound
│  │  └─ test_sound.mp3
│  └─ IMG
│     ├─ DL.png
│     ├─ logo.ico
│     └─ test_img.jpg
├─ lib
│  ├─ __init__.py
│  ├─ page
│  │  ├─ browser.py
│  │  ├─ input.py
│  │  ├─ media.py
│  │  ├─ music.py
│  │  ├─ nowifi.py
│  │  └─ video.py
│  └─ package
│     └─ wifi_detection.py
├─ docs
│  └─ README.md
└─ data
   └─ data.json
```
## Installation Guide
### 1. Clone the repository
```bash
git clone https://github.com/liyunhan177/NeedAPP_DLAPP.git
```
### 2. Install dependencies
```bash
pip install pywifi ttkbootstrap
```
### 3. Run the project
```bash
python src/main_page.py
```
## User Guide

### Feature Introduction
#### __This project aims to provide a fast and convenient software downloader. Users can select the type of software they want to download through a graphical interface and download it directly from the official website. Local installation package download functionality will be developed in the future.__
## Contributing
#### __Issues and Pull Requests are welcome to improve this project!__
## Future Roadmap
- [x] Project initialization and infrastructure setup
- [x] Listing of software types
- [ ] Button control design for each software
- [ ] Official website redirect
- [ ] Implement basic software download functionality
- [ ] UI beautification
- [ ] Package the project as an executable
## Special Notes
#### __The author is a student, and this project is only a personal hobby project with no guarantee of long-term maintenance. The code quality may not be perfect, please understand.__


