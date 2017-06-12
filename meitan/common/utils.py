# -*- coding: utf-8 -*-
from cloudinary.utils import cloudinary_url
import cloudinary

def get_cloudinary_thumb(image, *args, **kwargs):
    return cloudinary_url(image.public_id, *args, **kwargs)[0]
