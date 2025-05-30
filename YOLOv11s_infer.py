from ultralytics import YOLO
from PIL import Image

model = YOLO('YOLOv11s_finetuned_on_potholes.pt')

def predict(img):
    res_image = model.predict(img)
    res_image = res_image[0]

    img_to_plot = res_image.plot()

    pil_image = Image.fromarray(img_to_plot)

    return pil_image

if __name__ == '__main__':
    img_path = '615_jpg.rf.b1a99fab58ae0a778274c1f5b126d2d3.jpg'
    predicted_image = predict(img_path)

    predicted_image.show()