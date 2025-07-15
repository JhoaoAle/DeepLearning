import os
from torch.utils.data import Dataset
from PIL import Image

class LSCDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        """
        Args:
            root_dir (str): path to train/ or val/ folder
            transform (callable, optional): image transforms
        """
        self.root_dir = root_dir
        self.transform = transform

        # Scan all images and labels
        self.samples = []
        self.labels = sorted(os.listdir(root_dir))
        self.label_to_idx = {label: idx for idx, label in enumerate(self.labels)}

        for label in self.labels:
            label_dir = os.path.join(root_dir, label)
            if not os.path.isdir(label_dir):
                continue
            for fname in os.listdir(label_dir):
                fpath = os.path.join(label_dir, fname)
                self.samples.append((fpath, label))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        img_path, label = self.samples[idx]
        image = Image.open(img_path).convert("RGB")

        if self.transform:
            image = self.transform(image)

        label_idx = self.label_to_idx[label]
        return image, label_idx
