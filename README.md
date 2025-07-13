
## Table of Contents
  * [Table of Contents](#table-of-contents)  
  * [Project Structure](#project-structure) 




## Project Structure

```
DeepLearning/
│
├── configs/                               # YAML configs for experiments
│   ├── classification_config.yaml         # Hyperparameters for classifier (e.g. learning rate, epochs)
│   └── detection_config.yaml              # Settings for detection model (e.g. threshold, model path)
│
├── data/                                  # All datasets and model artifacts
│   ├── annotations/                       # Label files, e.g. bounding boxes, classes
│   ├── external/                          # Downloaded datasets, pretrained weights
│   ├── models/                            # Saved trained model files (.h5, .pt, etc.)
│   ├── processed/                         # Cropped hand images, cleaned datasets
│   ├── raw/                               # Raw video/image data as originally collected
│   └── results/                           # Outputs like predictions, logs, metrics
│
├── realtime_app/                          # Local real-time webcam app
│   └── webcam_app.py                      # Script for live webcam detection & classification
│
├── scripts/                               # CLI scripts for reproducible runs
│   ├── run_detection.py                   # Script to run hand detection on data
│   ├── run_inference.py                   # Script to perform inference using trained models
│   └── run_training.py                    # Script to train models
│
├── src/                                   # Main Python package with core logic
│   └── lsc_classifier/                    # Your project’s Python package
│       │
│       ├── classification/                # CNN architecture and classification logic
│       │   ├── model.py                   # Defines your CNN model
│       │   ├── predict.py                 # Functions to run predictions using the trained model
│       │   ├── train.py                   # Code to train the classifier
│       │
│       ├── data/                          # Data handling and preprocessing
│       │   ├── dataset.py                 # Dataset classes for loading training/test data
│       │   ├── transformations.py         # Data augmentation and preprocessing utilities
│       │
│       ├── detection/                     # Hand detection code
│       │   ├── detector.py                # Code to load and run object detector (e.g. YOLO, Faster R-CNN)
│       │   ├── utils.py                   # Helper functions specific to detection
│       │
│       ├── utils/                         # Miscellaneous utilities
│       │   ├── helpers.py                 # General-purpose helper functions
│       │
│       ├── visualization/                 # Tools for visual outputs
│       │   ├── viz_utils.py               # Draw bounding boxes, plot metrics, visualize predictions
│       │
│       └── __init__.py                    # Makes this a Python package
│
├── tests/                                 # Unit and integration tests
│   ├── test_detector.py                   # Tests for hand detection code
│   ├── test_model.py                      # Tests for classification model
│   └── test_pipeline.py                   # Tests for the end-to-end pipeline
│
├── venv/                                  # Virtual environment for dependencies
│
├── .gitignore                             # Files/folders to exclude from version control
├── pyproject.toml                         # Project metadata and dependencies (PEP 518/PEP 621)
├── README.md                              # Project overview and instructions
└── requirements.txt                       # List of Python package dependencies
```