from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from PIL import Image, UnidentifiedImageError
import io

from YOLOv11n_infer import predict as nano_predict
from YOLOv11s_infer import predict as small_predict



app = FastAPI()

@app.post('/YOLOv11n')
async def nano_prediction(file: UploadFile = File(...)):
    try:
        img = Image.open(file.file).convert('RGB')
    except UnidentifiedImageError:
        raise HTTPException(status_code= 400, detail= f"Uploaded file is not a valid image.")
    except Exception as e:
        raise HTTPException(status_code=500, detail= f"Error reading image: {e}")

    try:
        predicted_img = nano_predict(img)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model prediction failed: {str(e)}")

    buffer = io.BytesIO()
    predicted_img.save(buffer, format='PNG')
    buffer.seek(0)

    return StreamingResponse(buffer, media_type='image/png')

@app.post('/YOLOv11s')
async def small_prediction(file: UploadFile = File(...)):
    try:
        img = Image.open(file.file).convert('RGB')
    except UnidentifiedImageError:
        raise HTTPException(status_code= 400, detail= f"Uploaded file is not a valid image.")
    except Exception as e:
        raise HTTPException(status_code=500, detail= f"Error reading image: {e}")

    try:
        predicted_img = small_predict(img)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model prediction failed: {str(e)}")

    buffer = io.BytesIO()
    predicted_img.save(buffer, format='PNG')
    buffer.seek(0)

    return StreamingResponse(buffer, media_type='image/png')