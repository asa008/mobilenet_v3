""" Configurations shared between PyTorch and Keras. """

CONFIG = {
    "large": [
        # in_ch, exp, out_ch, ks, stride, dilation, se, activation
        [16, 16, 16, 3, 1, 1, None, "relu"],
        [16, 64, 24, 3, 2, 1, None, "relu"],
        [24, 72, 24, 3, 1, 1, None, "relu"],
        [24, 72, 40, 5, 2, 1, 0.25, "relu"],
        [40, 120, 40, 5, 1, 1, 0.25, "relu"],
        [40, 120, 40, 5, 1, 1, 0.25, "relu"],
        [40, 240, 80, 3, 2, 1, None, "hardswish"],
        [80, 200, 80, 3, 1, 1, None, "hardswish"],
        [80, 184, 80, 3, 1, 1, None, "hardswish"],
        [80, 184, 80, 3, 1, 1, None, "hardswish"],
        [80, 480, 112, 3, 1, 1, 0.25, "hardswish"],
        [112, 672, 112, 3, 1, 1, 0.25, "hardswish"],
        [112, 672, 160, 5, 2, 1, 0.25, "hardswish"],
        [160, 960, 160, 5, 1, 1, 0.25, "hardswish"],
        [160, 960, 160, 5, 1, 1, 0.25, "hardswish"],
    ],
    "small": [
        # in_ch, exp, out_ch, ks, stride, dilation, se, activation
        [16, 16, 16, 3, 2, 1, 0.25, "relu"],
        [16, 72, 24, 3, 2, 1, None, "relu"],
        [24, 88, 24, 3, 1, 1, None, "relu"],
        [24, 96, 40, 5, 2, 1, 0.25, "hardswish"],
        [40, 240, 40, 5, 1, 1, 0.25, "hardswish"],
        [40, 240, 40, 5, 1, 1, 0.25, "hardswish"],
        [40, 120, 48, 5, 1, 1, 0.25, "hardswish"],
        [48, 144, 48, 5, 1, 1, 0.25, "hardswish"],
        [48, 288, 96, 5, 2, 1, 0.25, "hardswish"],
        [96, 576, 96, 5, 1, 1, 0.25, "hardswish"],
        [96, 576, 96, 5, 1, 1, 0.25, "hardswish"],
    ],
    "large_detection": [
        # in_ch, exp, out_ch, ks, stride, dilation, se, activation
        [16, 16, 16, 3, 1, 1, None, "relu"],
        [16, 64, 24, 3, 2, 1, None, "relu"],
        [24, 72, 24, 3, 1, 1, None, "relu"],
        [24, 72, 40, 5, 2, 1, 0.25, "relu"],
        [40, 120, 40, 5, 1, 1, 0.25, "relu"],
        [40, 120, 40, 5, 1, 1, 0.25, "relu"],
        [40, 240, 80, 3, 2, 1, None, "hardswish"],
        [80, 200, 80, 3, 1, 1, None, "hardswish"],
        [80, 184, 80, 3, 1, 1, None, "hardswish"],
        [80, 184, 80, 3, 1, 1, None, "hardswish"],
        [80, 480, 112, 3, 1, 1, 0.25, "hardswish"],
        [112, 672, 112, 3, 1, 1, 0.25, "hardswish"],
        [112, 672, 80, 5, 2, 1, 0.25, "hardswish"],
        [80, 480, 80, 5, 1, 1, 0.25, "hardswish"],
        [80, 480, 80, 5, 1, 1, 0.25, "hardswish"],
    ],
    "small_detection": [
        # in_ch, exp, out_ch, ks, stride, dilation, se, activation
        [16, 16, 16, 3, 2, 1, 0.25, "relu"],
        [16, 72, 24, 3, 2, 1, None, "relu"],
        [24, 88, 24, 3, 1, 1, None, "relu"],
        [24, 96, 40, 5, 2, 1, 0.25, "hardswish"],
        [40, 240, 40, 5, 1, 1, 0.25, "hardswish"],
        [40, 240, 40, 5, 1, 1, 0.25, "hardswish"],
        [40, 120, 48, 5, 1, 1, 0.25, "hardswish"],
        [48, 144, 48, 5, 1, 1, 0.25, "hardswish"],
        [48, 288, 48, 5, 2, 1, 0.25, "hardswish"],
        [48, 288, 48, 5, 1, 1, 0.25, "hardswish"],
        [48, 288, 48, 5, 1, 1, 0.25, "hardswish"],
    ],
    # Stride 16, last 3 blocks dilated by 2.
    "large_segmentation": [
        # in_ch, exp, out_ch, ks, stride, dilation, se, activation
        [16, 16, 16, 3, 1, 1, None, "relu"],
        [16, 64, 24, 3, 2, 1, None, "relu"],
        [24, 72, 24, 3, 1, 1, None, "relu"],
        [24, 72, 40, 5, 2, 1, 0.25, "relu"],
        [40, 120, 40, 5, 1, 1, 0.25, "relu"],
        [40, 120, 40, 5, 1, 1, 0.25, "relu"],
        [40, 240, 80, 3, 2, 1, None, "hardswish"],
        [80, 200, 80, 3, 1, 1, None, "hardswish"],
        [80, 184, 80, 3, 1, 1, None, "hardswish"],
        [80, 184, 80, 3, 1, 1, None, "hardswish"],
        [80, 480, 112, 3, 1, 1, 0.25, "hardswish"],
        [112, 672, 112, 3, 1, 1, 0.25, "hardswish"],
        [112, 672, 80, 5, 1, 2, 0.25, "hardswish"],
        [80, 480, 80, 5, 1, 2, 0.25, "hardswish"],
        [80, 480, 80, 5, 1, 2, 0.25, "hardswish"],
    ],
    # Stride 16, last 3 blocks dilated by 2.
    "small_segmentation": [
        # in_ch, exp, out_ch, ks, stride, dilation, se, activation
        [16, 16, 16, 3, 2, 1, 0.25, "relu"],
        [16, 72, 24, 3, 2, 1, None, "relu"],
        [24, 88, 24, 3, 1, 1, None, "relu"],
        [24, 96, 40, 5, 2, 1, 0.25, "hardswish"],
        [40, 240, 40, 5, 1, 1, 0.25, "hardswish"],
        [40, 240, 40, 5, 1, 1, 0.25, "hardswish"],
        [40, 120, 48, 5, 1, 1, 0.25, "hardswish"],
        [48, 144, 48, 5, 1, 1, 0.25, "hardswish"],
        [48, 288, 48, 5, 1, 2, 0.25, "hardswish"],
        [48, 288, 48, 5, 1, 2, 0.25, "hardswish"],
        [48, 288, 48, 5, 1, 2, 0.25, "hardswish"],
    ],
}