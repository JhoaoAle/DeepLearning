from torchvision import transforms

def get_transforms(image_size=64, grayscale=False):
    transform_list = []
    
    if grayscale:
        transform_list.append(transforms.Grayscale(num_output_channels=1))

    transform_list.extend([
        transforms.Resize((image_size, image_size)),
        transforms.ToTensor(),
    ])
    
    return transforms.Compose(transform_list)