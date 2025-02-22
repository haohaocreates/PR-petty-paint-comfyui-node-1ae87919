# Customized by Andrew Porter for ComfyUI
# 04/21/2024
import os
import subprocess
import importlib.util
import sys
import filecmp
import shutil

import __main__
from .PettyPaint import PettyPaintComponent
from .PettyPaint import PettyPaintSDTurboScheduler
from .PettyPaintImageSave import PettyPaintImageSave
from .PettyPaintText import (
    PettyPaintConvert,
    PettyPaintCountFiles,
    PettyPaintEnsureDirectory,
    PettyPaintExec,
    PettyPaintImageCompositeMasked,
    PettyPaintImagePlacement,
    PettyPaintLoadImage,
    PettyPaintProcessor,
    PettyPaintText,
    PettyPaintToJson,
)
from .PettyPaintText import PettyPaintRemoveAddText
from .PettyPaintImageStore import PettyPaintImageStore
from .PettyPaintText import PettyPaintAppend
from .PettyPaintText import PettyPaintJsonReadArray
from .PettyPaintText import PettyPaintJsonRead
from .PettyPaintText import PettyPaintJsonMap
from .PettyPaintText import PettyPaintConditioningSetMaskAndCombine
from .PettyPaintText import PettyPaintLoadImages
from .PettyPaintText import PettyPaintImageToMask
from .PettyPaintText import PettyPaintTexts_to_Conditioning
from .PettyPaintText import PettyPaintMap

python = sys.executable


NODE_CLASS_MAPPINGS = {
    "PettyPaintMap": PettyPaintMap,
    "PettyPaintTexts_to_Conditioning": PettyPaintTexts_to_Conditioning,
    "PettyPaintImageToMask": PettyPaintImageToMask,
    "PettyPaintLoadImages": PettyPaintLoadImages,
    "PettyPaintComponent": PettyPaintComponent,
    "PettyPaintSDTurboScheduler": PettyPaintSDTurboScheduler,
    "PettyPaintImageSave": PettyPaintImageSave,
    "PettyPaintText": PettyPaintText,
    "PettyPaintRemoveAddText": PettyPaintRemoveAddText,
    "PettyPaintImageStore": PettyPaintImageStore,
    "PettyPaintAppend": PettyPaintAppend,
    "PettyPaintJsonReadArray": PettyPaintJsonReadArray,
    "PettyPaintJsonRead": PettyPaintJsonRead,
    "PettyPaintJsonMap": PettyPaintJsonMap,
    "PettyPaintConditioningSetMaskAndCombine": PettyPaintConditioningSetMaskAndCombine,
    "PettyPaintImageCompositeMasked": PettyPaintImageCompositeMasked,
    "PettyPaintExec": PettyPaintExec,
    "PettyPaintConvert": PettyPaintConvert,
    "PettyPaintToJson": PettyPaintToJson,
    "PettyPaintImagePlacement": PettyPaintImagePlacement,
    "PettyPaintLoadImage": PettyPaintLoadImage,
    "PettyPaintEnsureDirectory": PettyPaintEnsureDirectory,
    "PettyPaintCountFiles": PettyPaintCountFiles,
    "PettyPaintProcessor": PettyPaintProcessor,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "PettyPaintProcessor": "PettyPaintProcessor",
    "PettyPaintCountFiles": "Petty Paint Count Files",
    "PettyPaintEnsureDirectory": "Petty Paint Ensure Directory",
    "PettyPaintLoadImage": "Petty Paint Load Image",
    "PettyPaintImagePlacement": "Petty Paint Image Placement",
    "PettyPaintToJson": "Petty Paint To Json",
    "PettyPaintConvert": "Petty Paint Convert",
    "PettyPaintExec": "Petty Paint Exec",
    "PettyPaintImageCompositeMasked": "Petty Paint Image Composite Masked",
    "PettyPaintMap": "Petty Paint Map",
    "PettyPaintTexts_to_Conditioning": "PettyPaintTexts_to_Conditioning",
    "PettyPaintImageToMask": "PettyPaintImageToMask",
    "PettyPaintLoadImages": "PettyPaintLoadImages",
    "PettyPaintConditioningSetMaskAndCombine": "PettyPaintConditioningSetMaskAndCombine",
    "PettyPaintJsonMap": "PettyPaintJsonMap",
    "PettyPaintJsonReadArray": "PettyPaintJsonReadArray",
    "PettyPaintJsonRead": "PettyPaintJsonRead",
    "PettyPaintAppend": "Petty Paint Append Text",
    "PettyPaintComponent": "Petty Paint",
    "PettyPaintSDTurboScheduler": "Petty Paint SD Turbo Scheduler",
    "PettyPaintImageSave": "Petty Paint Image Save",
    "PettyPaintText": "Petty Paint Text",
    "PettyPaintRemoveAddText": "Petty Paint Remove Add Text",
    "PettyPaintImageStore": "Petty Paint Image Store",
}
print("\033[34mPetty Paint Custom Nodes: \033[92mLoaded\033[0m")
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
