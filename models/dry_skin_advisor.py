from models.base_advisor import Baseadvisor

class DrySkinAdvisor(Baseadvisor):
    def recommend_makeup(self):
        print("Recommended Makeup for Dry Skin:")
        print("- Use hydrating foundation")
        print("- Apply cream-based blush")
        print("- Avoid matte lipstick as it may dry your lips")