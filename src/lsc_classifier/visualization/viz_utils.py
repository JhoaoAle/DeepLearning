import torch
import matplotlib.pyplot as plt

def visualize_activations(model, image_tensor, save_path=None):
    """
    Visualize feature maps after each convolution or pooling layer.

    Args:
        model: your LSCClassifier model
        image_tensor: shape [1, 3, H, W]
        save_path: optional filepath to save the figure
    """
    # Put model in eval mode
    model.eval()
    
    x = image_tensor
    activations = []

    # We'll step through model.net sequentially
    for i, layer in enumerate(model.net):
        x = layer(x)
        
        # Only save outputs with 4D shape = feature maps
        if x.dim() == 4:
            activations.append((i, layer, x.detach().cpu()))
    
    # Plot each feature map grid
    fig_num = 1
    for idx, layer, feature_maps in activations:
        num_channels = feature_maps.shape[1]
        
        # We'll show up to first 8 channels to avoid huge figures
        num_show = min(8, num_channels)

        fig, axes = plt.subplots(1, num_show, figsize=(num_show*2, 2))
        fig.suptitle(f"Layer {idx}: {layer.__class__.__name__}")

        for i in range(num_show):
            ax = axes[i]
            fmap = feature_maps[0, i, :, :]
            ax.imshow(fmap, cmap="viridis")
            ax.axis("off")

        plt.tight_layout()
        if save_path:
            plt.savefig(f"{save_path}_layer{idx}.png")
            plt.close(fig)
        else:
            plt.show()
        
        fig_num += 1