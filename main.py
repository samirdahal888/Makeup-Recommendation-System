from recommender_utils import validate_face_shape,validate_skin_tone,validate_skin_type
from makeup_factory import get_advisor
# from models.base_advisor import Baseadvisor

def main():
    name = input("Enter your name:")
    skin_type = input("Enter your skin type:")
    face_shape  = input("Enter your face shape:")
    skin_tone = input("Enter your skin_tone:")


    #valided input
    if not (validate_face_shape(face_shape) and validate_skin_tone(skin_tone) and validate_skin_type(skin_type)):
            print("Invalid input provided. Please check face shape, skin tone, or skin type.")
            return


    #create advisor
    advisor = get_advisor(name,skin_type,face_shape,skin_tone)

    print('-------------------------------------------------------------------------------------------------------------------------------------')

    print(advisor.get_user_information())
    print()
    advisor.recommend_makeup()
    print()
    print(advisor.general_tips())
    print()

if __name__ == "__main__":
    main()



    

