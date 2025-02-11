import streamlit as st
import requests

def get_skin_profile(answers):
    """Determine skin type based on quiz answers."""
    if answers["oily"] > 3 and answers["acne"] > 3:
        return "Oily & Acne-Prone"
    elif answers["dry"] > 3 and answers["sensitive"] > 3:
        return "Dry & Sensitive"
    elif answers["aging"] > 3:
        return "Aging & Mature"
    elif answers["sun_exposure"] > 3:
        return "Sun-Damaged"
    elif answers["texture"] == "Uneven":
        return "Textured & Uneven"
    else:
        return "Normal/Combination"

def recommend_ingredients(skin_profile):
    """Map skin profiles to beneficial skincare ingredients."""
    recommendations = {
        "Oily & Acne-Prone": ["Salicylic Acid", "Niacinamide", "Oil-Free Moisturizers"],
        "Dry & Sensitive": ["Hyaluronic Acid", "Ceramides", "Fragrance-Free Formulas"],
        "Aging & Mature": ["Retinol", "Vitamin C", "Peptides"],
        "Sun-Damaged": ["Vitamin C", "Niacinamide", "SPF Protectants"],
        "Textured & Uneven": ["AHA/BHA", "Retinol", "Exfoliating Acids"],
        "Normal/Combination": ["Green Tea Extract", "Hyaluronic Acid", "Balanced Moisturizers"]
    }
    return recommendations.get(skin_profile)

def main():
    st.title("Skin Type Quiz & Product Recommendations")
    
    st.subheader("Answer the following questions:")
    
    answers = {}
    
    answers["oily"] = st.slider("How oily is your skin?", 1, 5, 3)
    
    answers["dry"] = st.slider("How dry is your skin?", 1, 5, 3)
    
    answers["sensitive"] = st.slider("Do you have sensitive skin?", 1, 5, 3)
    
    answers["acne"] = st.slider("How prone are you to acne?", 1, 5, 3)
    
    answers["aging"] = st.slider("Do you have aging concerns?", 1, 5, 3)
    
    answers["sun_exposure"] = st.slider("How often are you exposed to the sun?", 1, 5, 3)
    
    answers["texture"] = st.radio("How would you describe your skin texture?", ["Smooth", "Uneven", "Rough"])
    
    answers["rosacea"] = st.radio("Do you have visible redness or rosacea?", ["Yes", "No"])
    
    answers["hyperpigmentation"] = st.radio("Do you have hyperpigmentation or dark spots?", ["Yes", "No"])
    
    answers["exfoliation"] = st.slider("How often do you exfoliate your skin?", 1, 5, 3)
    
    answers["irritation"] = st.slider("How often does your skin get irritated?", 1, 5, 3)
    
    answers["fine_lines"] = st.slider("Do you have fine lines or wrinkles?", 1, 5, 3)
    
    answers["tightening"] = st.radio("Do you have concerns about skin tightening?", ["Yes", "No"])
    
    answers["pores"] = st.radio("How would you describe the size of your pores?", ["Small", "Medium", "Large"])
    
    answers["oil_control"] = st.slider("Does your skin get oily throughout the day?", 1, 5, 3)
    
    answers["redness"] = st.slider("Does your skin get red or irritated after cleansing?", 1, 5, 3)
    
    answers["sunscreen"] = st.radio("Do you use sunscreen regularly?", ["Yes", "No"])
    
    answers["hydration"] = st.slider("How well-hydrated does your skin feel?", 1, 5, 3)
    
    answers["elasticity"] = st.slider("How would you rate the elasticity of your skin?", 1, 5, 3)
    
    answers["seasonal_changes"] = st.radio("Does your skin change with the seasons?", ["Yes", "No"])

    if st.button("Get My Skin Type & Recommendations"):
        skin_profile = get_skin_profile(answers)
        st.success(f"Your Skin Type: {skin_profile}")

if __name__ == "__main__":
    main()
