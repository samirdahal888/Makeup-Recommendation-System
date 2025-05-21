
def validate_face_shape(face_shape):
    valid_shapes = ['oval', 'round', 'square', 'heart']
    return face_shape.lower() in valid_shapes

def validate_skin_tone(skin_tone):
    valid_tones = ['fair', 'medium', 'olive', 'deep']
    return skin_tone.lower() in valid_tones

def validate_skin_type(skin_type):
    valid_types = ['dry', 'oily', 'normal']
    return skin_type.lower() in valid_types
