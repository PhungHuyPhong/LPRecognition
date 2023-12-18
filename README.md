Detection:

Sử dụng pretrained model Yolov8n trong việc detection

Dataset được sử dụng: https://drive.google.com/file/d/1qJdbpcBlYtDB5sR1wmtjFRF6QqYnrGw_/view?usp=sharing

Model được train trong môi trường Pycharm trên Ubuntu 22.04.3LTS sử dụng YOLO CLI:

```bash
yolo detect train model="yolov8n.pt" data="path/to/dataset/data.yaml" epochs=100 save=True plots=True amp=False workers=1 project="path/to/dir/to/save/your/results"
```
