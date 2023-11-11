import matplotlib.pyplot as plt
from pathlib import Path

IMAGES_PATH = Path() / "images" / "figures"
IMAGES_PATH.mkdir(parents=True, exist_ok=True)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    """
    Save a matplotlib figure to a specified file.

    Parameters:
    fig_id (str): The name of the figure to be saved.
    tight_layout (bool): If True, adjust the layout to remove excess padding around the plot. Default is True.
    fig_extension (str): The file extension for the saved figure (e.g., 'png', 'jpg', 'pdf'). Default is 'png'.
    resolution (int): The resolution in dots per inch (DPI) for the saved figure. Default is 300.

    Returns:
    None

    Example:
    save_fig("my_plot", tight_layout=True, fig_extension="png", resolution=300)
    """
    path = IMAGES_PATH / f"{fig_id}.{fig_extension}"  # Generate the path for saving the figure
    if tight_layout:
        plt.tight_layout()  # Adjust the layout to improve appearance if enabled
    plt.savefig(path, format=fig_extension, dpi=resolution)  # Save the figure with specified parameters