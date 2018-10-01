#!/usr/bin/env bash

case "$(uname -s)" in
   Darwin)
     PYUIC5="./venv/bin/pyuic5"
     ;;

   Linux)
     PYUIC5="./venv/bin/pyuic5"
     ;;

   CYGWIN*|MINGW32*|MINGW64*|MSYS*)
     PYUIC5="./venv/Scripts/pyuic5.exe"
     ;;

   *)
     echo 'Unfortunately, your operating system are not supported by this script.'
     exit 1
     ;;
esac


$PYUIC5 ui/pyqt5_bootstrap__MainWindow.ui -o pyqt5_bootstrap/Ui_MainWindow.py
