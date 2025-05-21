from models.dry_skin_advisor import DrySkinAdvisor
from models.normal_skin_advisor import NormalSkinAdvisor
from models.oily_skin_advisor import OilySkinAdvisor

def get_advisor(name,skin_type,face_shape,skin_tone):
    if skin_type=='dry':
        return DrySkinAdvisor(name,face_shape,skin_tone)
    if skin_type=='oily':
        return OilySkinAdvisor(name,face_shape,skin_tone)
    if skin_type=='normal':
        return NormalSkinAdvisor(name,face_shape,skin_tone)
    
    else:
        return 'something went wrong'
