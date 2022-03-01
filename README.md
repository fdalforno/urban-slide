# Slide presentazione fablab
Gestione slide presentazione fablab

## License

MIT licensed

npm start --port=8001
http://localhost:8001


C:\Program Files (x86)\Intel\openvino_2021\bin\setupvars.bat

python 01-open.py --input ..\video.mp4
python 02-framedifferencing.py --input ..\video.mp4
python 02.1-backroundsubraction.py --input ..\video.mp4 --algo KNN
