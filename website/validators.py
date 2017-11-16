def validate_transfile_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.txt',]
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Please upload a .txt file with UTF-8 encoding.')

def validate_imagefile_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png', '.jpeg', '.svg',]
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Please upload a .jpg or .png or .svg or .jpeg image.')

def validate_resourceitem_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1] # [0] returns path+filename
    valid_extensions = ['.ppt', '.pptx', '.pdf', '.mp3', '.mp4',]
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Please upload a .ppt or .pptx or .pdf or .mp3 or .mp4 resource item.')

