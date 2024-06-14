from .sd3_scaling import Sd3ImageScaleToTotalPixels


NODE_CLASS_MAPPINGS = {
    "SD3ImageScaleToTotalPixels": Sd3ImageScaleToTotalPixels,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SD3ImageScaleToTotalPixels": "SD3 Image Scale To Total Pixels",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
