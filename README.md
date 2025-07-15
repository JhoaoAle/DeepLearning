
---
# DeepLearning - LSC Hand Sign Recognition

**Author:** Jhoao Alejandro Martinez



## Project Overview

This project builds a deep learning pipeline to recognize letters from **Lengua de Señas Colombiana (LSC)** using images of hand signs. It consists of:

- Hand detection in video streams (object detection)
- Classification of detected hand regions into LSC letters using a CNN
- Real-time webcam application for live predictions
- Visualization tools for inspecting how the model processes images

---



## Project Structure

```
└── DeepLearning
    └── .kaggle
    └── configs
        ├── classification_config.yaml
        ├── detection_config.yaml
    └── data
        └── annotations
        └── external
        └── models
        └── processed
        └── raw
        └── results
    └── notebooks
        ├── visualize_activations.ipynb
    └── realtime_app
        ├── webcam_app.py
    └── scripts
        ├── 1_download_data.py
        ├── 2_split_dataset.py
        ├── 3_test_data_loader.py
        ├── run_detection.py
        ├── run_inference.py
        ├── run_training.py
    └── src
        └── lsc_classifier
            └── __pycache__
            └── classification
                └── __pycache__
                ├── model.py
                ├── predict.py
                ├── train.py
            └── data
                └── __pycache__
                ├── dataset.py
                ├── transformations.py
            └── detection
                ├── detector.py
                ├── utils.py
            └── utils
                ├── helpers.py
            └── visualization
                └── __pycache__
                ├── viz_utils.py
            ├── __init__.py
    └── tests
        ├── test_detector.py
        ├── test_model.py
        ├── test_pipeline.py
    ├── .gitignore
    ├── pyproject.toml
    ├── README.md
    └── requirements.txt
```


