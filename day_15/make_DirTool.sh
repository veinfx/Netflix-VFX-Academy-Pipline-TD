#!/bin/bash

DIRNAME=$(zenity --entry --title="폴더 이름을 적어주세요" --text="")

if [ -d "$HOME/$DIRNAME" ]; then
	zenity --error --text="폴더가 존재합니다."
else
	mkdir "$HOME/$DIRNAME"
fi
