# joycon-WHILL
### whillとwhill_dataとwhill_packetはいるから置いといて
### K_L_joyconとK_R_joyconはそれぞれWHILLを動かす左と右
gyroとstick切り替えできる
### joycontestはつながるかのテストエラーでなければOKLとRは適宜コードを書き換えて
### WHILL_stickはstickのみでの操作 L使ってる


--- pipかcondaでインストールするもの(仮想環境推奨，もしエラーが出れば適宜ライブラリを足してね)
pythonは3系
hidapi
joycon-python
pygame
pyGLM
whillpy

joyconはbluetoothでWHILLはUSBでシリアルにchmodしてね．
