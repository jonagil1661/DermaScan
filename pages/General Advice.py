






import streamlit as st

st.title("🌿 Personalized Skincare Tips")

st.write("""
💡 **Understanding your skin type** is the first step to creating a great skincare routine.  
Select your skin type below to receive **personalized skincare recommendations**,  
including a **daily routine**, **recommended ingredients**, and **common mistakes to avoid**.
""")

# User selects skin type
skin_type = st.selectbox("🔍 Select your skin type:", ["-- Select --", "Dry", "Oily", "Combination", "Sensitive"])

if skin_type != "-- Select --":
    st.write(f"## ✨ Skincare Guide for {skin_type} Skin")
    
    # Recommended skincare routine
    st.subheader("📌 Daily Skincare Routine")

    if skin_type == "Dry":
        st.write("""
        **Morning Routine:**
        1️⃣ Use a gentle, hydrating cleanser (cream or oil-based).  
        2️⃣ Apply a hydrating toner (rose water or glycerin-based).  
        3️⃣ Use a **hyaluronic acid serum** to lock in moisture.  
        4️⃣ Apply a **rich moisturizer** with ceramides & shea butter.  
        5️⃣ Finish with a broad-spectrum **SPF 30+ sunscreen**.  

        **Night Routine:**
        1️⃣ Double cleanse if wearing makeup (oil-based first, then a gentle cleanser).  
        2️⃣ Use a **hydrating essence or toner** to prep the skin.  
        3️⃣ Apply a **moisturizing serum** (hyaluronic acid or niacinamide).  
        4️⃣ Lock in hydration with a **thick night cream** or sleeping mask.  
        """)

    elif skin_type == "Oily":
        st.write("""
        **Morning Routine:**
        1️⃣ Wash with a **foaming or gel-based cleanser**.  
        2️⃣ Apply an **alcohol-free toner** (witch hazel or green tea-based).  
        3️⃣ Use a **niacinamide or salicylic acid serum** to reduce oil.  
        4️⃣ Apply a lightweight, oil-free **gel moisturizer**.  
        5️⃣ Finish with a **matte SPF 30+ sunscreen**.  

        **Night Routine:**
        1️⃣ Cleanse with a **salicylic acid-based cleanser**.  
        2️⃣ Use a gentle exfoliant (2-3 times per week, **avoid over-exfoliating**).  
        3️⃣ Apply a **lightweight serum** (retinol or tea tree oil for acne).  
        4️⃣ Finish with an **oil-free moisturizer**.  
        """)

    elif skin_type == "Combination":
        st.write("""
        **Morning Routine:**
        1️⃣ Use a **gentle foaming cleanser** (not too drying).  
        2️⃣ Apply a **hydrating toner** (rose water or aloe vera-based).  
        3️⃣ Use a serum targeting **oily zones** (niacinamide) & **dry zones** (hyaluronic acid).  
        4️⃣ Apply a **lightweight, non-greasy moisturizer**.  
        5️⃣ Finish with a **broad-spectrum SPF 30+ sunscreen**.  

        **Night Routine:**
        1️⃣ Double cleanse if wearing makeup.  
        2️⃣ Use a **gentle exfoliant (once or twice a week)**.  
        3️⃣ Apply a **targeted treatment** (retinol for fine lines, salicylic acid for oil control).  
        4️⃣ Lock in hydration with a **lightweight night cream**.  
        """)

    elif skin_type == "Sensitive":
        st.write("""
        **Morning Routine:**
        1️⃣ Wash with a **fragrance-free, hypoallergenic cleanser**.  
        2️⃣ Apply a **soothing toner** (chamomile or oat-based).  
        3️⃣ Use a **barrier-repair serum** (ceramides, squalane, or centella asiatica).  
        4️⃣ Apply a **gentle moisturizer** (no alcohol, parabens, or artificial fragrance).  
        5️⃣ Use a **mineral sunscreen** (zinc oxide-based, SPF 30+).  

        **Night Routine:**
        1️⃣ Cleanse with a **mild, non-foaming cleanser**.  
        2️⃣ Use a **hydrating mist or calming essence**.  
        3️⃣ Apply a **gentle serum** (avoid retinol unless recommended by a doctor).  
        4️⃣ Finish with a **fragrance-free, soothing moisturizer**.  
        """)

    # Recommended ingredients
    st.subheader("🌱 Best Ingredients for Your Skin Type")
    
    if skin_type == "Dry":
        st.write("""
        ✅ **Hydration Boosters:** Hyaluronic acid, glycerin, ceramides, squalane.  
        ✅ **Nourishing Oils:** Jojoba oil, argan oil, shea butter.  
        ✅ **Calming Agents:** Aloe vera, oat extract.  
        """)
    elif skin_type == "Oily":
        st.write("""
        ✅ **Oil Control:** Niacinamide, salicylic acid, witch hazel.  
        ✅ **Pore Refiners:** Clay (kaolin, bentonite), zinc PCA.  
        ✅ **Antibacterial:** Tea tree oil, green tea extract.  
        """)
    elif skin_type == "Combination":
        st.write("""
        ✅ **Hydration for Dry Areas:** Hyaluronic acid, ceramides.  
        ✅ **Oil Control for T-Zone:** Niacinamide, green tea extract.  
        ✅ **Balanced Exfoliation:** Lactic acid, polyhydroxy acids (PHAs).  
        """)
    elif skin_type == "Sensitive":
        st.write("""
        ✅ **Barrier Repair:** Ceramides, squalane, centella asiatica.  
        ✅ **Soothing Ingredients:** Oat extract, chamomile, licorice root.  
        ✅ **Minimalist Approach:** Avoid alcohol, fragrances, sulfates.  
        """)

    # Common mistakes to avoid
    st.subheader("🚫 Common Skincare Mistakes to Avoid")

    
    if skin_type == "Dry":
        st.markdown("""
            ❌ Using foaming cleansers that strip moisture.<br>
            ❌ Skipping moisturizer.<br>
            ❌ Taking hot showers that dehydrate skin.<br>
        """, unsafe_allow_html=True)
    
    elif skin_type == "Oily":
        st.markdown("""
            ❌ Overwashing, which triggers more oil production.<br>
            ❌ Using alcohol-based toners that cause irritation.<br>
            ❌ Avoiding moisturizer (even oily skin needs hydration!).<br>
        """, unsafe_allow_html=True)
    elif skin_type == "Combination":
        st.markdown("""
            ❌ Using the same routine for entire face.<br>
            ❌ Ignoring different needs of T-zone and dry areas.<br>
            ❌ Over-exfoliating, which worsens oil and dryness.<br>
        """, unsafe_allow_html=True)
    elif skin_type == "Sensitive":
        st.markdown("""
            ❌ Using too many active ingredients at once.<br>
            ❌ Trying harsh exfoliants (like strong retinol or glycolic acid).<br>
            ❌ Ignoring patch tests before trying new products.<br>
        """, unsafe_allow_html=True)

    # Final advice
    st.subheader("📌 Final Tips")
    st.write("""
    ✅ Always wear **sunscreen daily** to protect your skin.  
    ✅ Keep a **simple, consistent routine**—avoid too many new products.  
    ✅ Drink **plenty of water** and follow a **healthy diet** for clear skin.  
    """)




    st.markdown("## 📚 Sources")

    if skin_type == "Dry":
        with st.expander("🔹 Sources for Dry Skin"):
            st.markdown("""
            🔗 [American Academy of Dermatology - Dermatologists' top tips for relieving dry skin](https://www.aad.org/public/everyday-care/skin-care-basics/dry/dermatologists-tips-relieve-dry-skin)  
            🔗 [Cleveland Clinic - Dry Skin](https://my.clevelandclinic.org/health/diseases/16940-dry-skin)  
            """)

    elif skin_type == "Oily":
        with st.expander("🔹 Sources for Oily Skin"):
            st.markdown("""
            🔗 [Medical News Today - Oily skin: Causes and treatments](https://www.medicalnewstoday.com/articles/321090)  
            🔗 [National Library of Medicine - Oily Skin & Acne](https://pmc.ncbi.nlm.nih.gov/articles/PMC5605215/)  
            """)

    elif skin_type == "Combination":
        with st.expander("🔹 Sources for Combination Skin"):
            st.markdown("""
            🔗 [oneskin - Comprehensive Guide to Combination Skin](https://www.oneskin.co/blogs/reference-lab/combination-skin)  
            🔗 [Mayo Clinic - Understanding Skin Type](https://www.mayoclinic.org/healthy-lifestyle/adult-health/in-depth/skin-care/art-20048237)  
            """)

    elif skin_type == "Sensitive":
        with st.expander("🔹 Sources for Sensitive Skin"):
            st.markdown("""
            🔗 [WebMD - Common Questions About Sensitive Skin](https://www.webmd.com/beauty/sensitive-skin-20-questions)  
            🔗 [Epiphany Dermatology - Sensitive Skin? Avoid These Products](https://www.epiphanydermatology.com/medical-dermatology/sensitive-skin/)  
            """)

    with st.expander("🌍 General Skincare Advice"):
        st.markdown("""
        🔗 [AAD - Skincare Tips](https://www.aad.org/public/everyday-care/skin-care-basics)  
        🔗 [NIH - Science of Skincare](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5796020/)  
        """)

st.success("✨ Healthy skin starts with the right routine! Stay consistent and listen to your skin’s needs. 😊")




















