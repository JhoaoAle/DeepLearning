import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.lsc_classifier.data.dataset import LSCDataset
from src.lsc_classifier.data.transformations import get_transforms
from torch.utils.data import DataLoader

dataset = LSCDataset(
    root_dir="data/processed/train",
    transform=get_transforms(image_size=64)
)

loader = DataLoader(dataset, batch_size=16, shuffle=True)

for images, labels in loader:
    print(images.shape)
    print(labels.shape)
    break