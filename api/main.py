from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Green Spark": "PlantAid"}


potato_model = tf.keras.models.load_model("./models/potato/4/model.keras")
tomato_model = tf.keras.models.load_model("./models/tomato/1/model.keras")

potato_class = ["Early Blight", "Late Blight", "Healthy"]
tomato_class = [
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato Septoria leaf spot",
    "Two spotted spider mite",
    "Tomato__Target_Spot",
    "Tomato__Tomato_YellowLeaf__Curl_Virus",
    "Tomato__Tomato_mosaic_virus",
    "Tomato_healthy",
]


def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image


@app.post("/predict/potato")
async def predict_potato(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)

    predictions = potato_model.predict(img_batch)

    predicted_class = potato_class[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {"class": predicted_class, "confidence": f"{float(confidence*100)}%"}


@app.post("/predict/tomato")
async def predict_tomato(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)

    predictions = tomato_model.predict(img_batch)

    predicted_class = tomato_class[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {"class": predicted_class, "confidence": f"{float(confidence*100)}%"}


