# PlantAid: Crop Disease Detection using TensorFlow CNN

![GitHub](https://img.shields.io/badge/Language-Python-blue)
![GitHub](https://img.shields.io/badge/Framework-TensorFlow-orange)
![GitHub](https://img.shields.io/badge/Backend-FastAPI-green)
![GitHub](https://img.shields.io/badge/Frontend-Next.js-purple)

A web application that analyzes leaf photos of various crops to detect diseases using a **TensorFlow CNN model**. The application supports **14+ crops**, including potato, tomato, pepper, apple, blueberry, cherry, corn, grape, orange, peach, raspberry, soybean, squash, and strawberry.

---

## Features

- **Disease Detection:** Upload a leaf photo, and the app will detect if there is any disease and identify it.
- **Multi-Crop Support:** Works for 14+ crops, with the flexibility to add more.
- **User-Friendly Interface:** Built with **Next.js** for a seamless frontend experience.
- **Scalable Backend:** Powered by **FastAPI** for efficient and fast predictions.
- **Future Plans:** Developing a mobile app that can run offline for use in remote areas.

---

## Tech Stack

- **Deep Learning:** TensorFlow, Convolutional Neural Networks (CNN)
- **Backend:** FastAPI
- **Frontend:** Next.js
- **Deployment:** Docker, Hugging Face

---

## Dataset

The model was trained on a [Plant Village](https://www.kaggle.com/datasets/arjuntejaswi/plant-village) & [New Plant Diseases](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset) dataset of crop leaf images, categorized by crop type and disease. The dataset includes images for all supported crops.

---

## Future Enhancements

- Add support for more crops.
- Develop a mobile app version that works offline.
- Improve model accuracy with more training data.
- Add multilingual support for farmers.

---

## Acknowledgments

A special thanks to **Bipin Dada** for his invaluable help with model format conversion and deployment. Without his guidance, this project would not have been possible.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

---

Batch: there have 32 images in one set of file
Cache: there have to cache all images for better performance while training the dataset

Learn: Optimize tensorflow pipeline performance: prefetching & cache

Data Augmentation: 1 image transform to 4 images by horizontal flip, contrast, zoom, rotation

Learn: Simple explanation of convolutional neural network

Search: Tensorflow Con2D layers, Tensorflow callback history

Activation function is Relu

Trail & Error
Dense Activation function softmax

TODO:
Prescription, Medicine sell button, Nearest Agronomist, Bangla
