import comfy
import comfy_extras.nodes_post_processing as npp


class Sd3ImageScaleToTotalPixels(npp.ImageScaleToTotalPixels):
    def upscale(self, image, upscale_method, megapixels, *args, **kwargs):
        """
        A wrapper for ImageScaleToTotalPixels.upscale that ensures the width and height are multiples of 64.

        NOTE: This does not preserve aspect ratio exactly. It will round down the width and height to fit
        within the requested megapixels while maintaining a multiple of 64. This can result in a loss
        fidelity to the requested aspect ratio, but the distortion should be minimal unless the
        input image is very small.
        """

        # Add in args/kwargs to future-proof against changes in the base class
        image = super().upscale(image, upscale_method, megapixels, *args, **kwargs)[0]
        samples = image.movedim(-1,1)
        width = samples.shape[3]
        height = samples.shape[2]
        if width % 64 != 0 or height % 64 != 0:
            if width % 64 != 0:
                width = width // 64 * 64
            if height % 64 != 0:
                height = height // 64 * 64
            samples = comfy.utils.common_upscale(samples, width, height, upscale_method, "disabled")
            samples = samples.movedim(1,-1)
            return (samples,)
        return (image,)
