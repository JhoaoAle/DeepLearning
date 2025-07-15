import os
import shutil
import random

def split_dataset(source_dir, dest_dir, split_ratio=0.8):
    """
    Splits a folder of images into train/val subfolders.

    Parameters:
        source_dir (str): path to the original dataset (one subfolder per class)
        dest_dir (str): path to store train/val folders
        split_ratio (float): fraction of images to put in training set
    """


    random.seed(42)

    # List all class folders (A, B, C, etc.)
    classes = [
        d
        for d in os.listdir(source_dir)
        if os.path.isdir(os.path.join(source_dir, d))
    ]

    for class_name in classes:
        class_dir = os.path.join(source_dir, class_name)

        # List all images in this class
        images = os.listdir(class_dir)

        # Randomize the order so splits are not alphabetical
        random.shuffle(images)

        # Compute how many go into the training set
        split_point = int(len(images) * split_ratio)

        # Slice the shuffled list into train and val
        train_imgs = images[:split_point]
        val_imgs = images[split_point:]

        for phase, files in zip(["train", "val"], [train_imgs, val_imgs]):
            # Create output folder for this class
            out_class_dir = os.path.join(dest_dir, phase, class_name)
            os.makedirs(out_class_dir, exist_ok=True)

            # Copy each file to its new location
            for f in files:
                src_path = os.path.join(class_dir, f)
                dst_path = os.path.join(out_class_dir, f)
                shutil.copy2(src_path, dst_path)

if __name__ == "__main__":
    split_dataset(
        source_dir="data/raw",
        dest_dir="data/processed",
        split_ratio=0.8
    )
