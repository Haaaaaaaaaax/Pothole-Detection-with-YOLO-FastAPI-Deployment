# This section is for Alcamp instructor please ignore

This is my data on Roboflow for my task
https://app.roboflow.com/haaaaaaaaaax/faces-detection-hi8su/1

# Pothole Detection with YOLO and FastAPI Deployment

This project implements a pothole detection system using YOLOv11n and YOLOv11s models, fine-tuned on pothole data from RoboFlow. The system is deployed using FastAPI for easy integration and real-time inference.

## Overview

The project uses state-of-the-art YOLO (You Only Look Once) models to detect potholes in images. Two variants of the model are implemented:
- YOLOv11n (nano version)
- YOLOv11s (small version)

Both models have been fine-tuned on a specialized pothole dataset from RoboFlow to achieve optimal detection performance.

## Features

- Real-time pothole detection
- FastAPI deployment for easy integration
- Support for both YOLOv11n and YOLOv11s models
- Simple REST API interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Haaaaaaaaaax/Pothole-Detection-with-YOLO-FastAPI-Deployment.git
cd Pothole-Detection-with-YOLO-FastAPI-Deployment
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the FastAPI server:
```bash
uvicorn main:app --reload
```

2. The API will be available at `http://localhost:8000`

3. Access the API documentation at `http://localhost:8000/docs`


## Model Information

- **YOLOv11n**: Lightweight model suitable for resource-constrained environments
- **YOLOv11s**: More accurate model with slightly higher computational requirements

Both models have been fine-tuned on pothole data from RoboFlow to ensure optimal detection performance.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For any questions or suggestions, please open an issue in the GitHub repository.
