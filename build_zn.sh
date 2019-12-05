#!/usr/bin/env bash
SR_LIB=$(python -c "import speech_recognition as sr, os.path as p; print(p.dirname(sr.__file__))")
sudo apt-get install --yes unzip
sudo unzip -o zh-CN.zip -d "$SR_LIB"
sudo chmod --recursive a+r "$SR_LIB/zh-CN/"