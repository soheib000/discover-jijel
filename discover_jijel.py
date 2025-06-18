import streamlit as st

# إعداد واجهة الصفحة
st.set_page_config(page_title="اكتشف جيجل", page_icon="🌊", layout="wide")

# القائمة الجانبية
st.sidebar.title("اكتشف جيجل")
menu = st.sidebar.radio("انتقل إلى:", ["الرئيسية", "الأماكن السياحية", "الفنادق", "الأكلات التقليدية", "اتصل بنا"])

# الصفحة الرئيسية
if menu == "الرئيسية":
    st.title("🌊 مرحباً بكم في ولاية جيجل")
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4f/Jijel_Beauty.jpg", use_column_width=True)
    st.markdown("""
    **جيجل**، جوهرة البحر الأبيض المتوسط، تجمع بين الطبيعة الخلابة، الغابات الكثيفة، الشواطئ الساحرة، والمواقع التاريخية.

    🗺️ استكشف الأماكن السياحية  
    🏨 تعرف على الفنادق  
    🍽️ تذوق الأكلات التقليدية  
    📞 تواصل معنا
    """)

# الأماكن السياحية
elif menu == "الأماكن السياحية":
    st.header("🗺️ الأماكن السياحية في جيجل")

    st.subheader("📍 الكهوف العجيبة")
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/65/Grotte_Jijel.jpg", width=700)
    st.write("تكوينات طبيعية مذهلة تحت الأرض، تُعد من أجمل المعالم السياحية في الجزائر.")

    st.subheader("📍 شاطئ كتامة")
    st.image("https://upload.wikimedia.org/wikipedia/commons/e/e4/Ketama_beach.jpg", width=700)
    st.write("شاطئ رملي نظيف بمياه صافية، مكان مثالي للاسترخاء.")

    st.subheader("📍 غابة بوجموعان")
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3b/Foret_de_jijel.jpg", width=700)
    st.write("وجهة رائعة لعشاق الطبيعة والمشي في الهواء الطلق.")

# الفنادق
elif menu == "الفنادق":
    st.header("🏨 الفنادق والإقامات في جيجل")

    hotels = [
        {"name": "فندق جيجل الكبير", "location": "وسط المدينة", "price": "7000 دج", "features": "WiFi، إفطار، مكيف"},
        {"name": "إقامة المرجان", "location": "القنار", "price": "5000 دج", "features": "مطل على البحر"},
        {"name": "نزل العافية", "location": "رأس العافية", "price": "4000 دج", "features": "قريب من الشاطئ"}
    ]

    for hotel in hotels:
        st.subheader(hotel["name"])
        st.write(f"📍 الموقع: {hotel['location']}")
        st.write(f"💰 السعر: {hotel['price']}")
        st.write(f"✨ المميزات: {hotel['features']}")
        st.markdown("---")

# الأكلات التقليدية
elif menu == "الأكلات التقليدية":
    st.header("🍽️ الأكلات التقليدية في جيجل")
    dishes = {
        "اللوبيا المعسلة": "طبق شتوي مشهور يُحضّر بالفاصولياء والتمر والعسل.",
        "الكسكس بالسمك": "نكهة ساحلية مميزة لطبق الكسكس التقليدي.",
        "الخبيزة": "طبق نباتي يُطهى بالأعشاب والتوابل.",
        "خبز الطاجين": "خبز تقليدي يُطهى فوق الحطب وله نكهة فريدة."
    }

    for dish, desc in dishes.items():
        st.subheader(dish)
        st.write(desc)
        st.markdown("---")

# اتصل بنا
elif menu == "اتصل بنا":
    st.header("📞 اتصل بنا")
    name = st.text_input("الاسم")
    email = st.text_input("البريد الإلكتروني")
    message = st.text_area("رسالتك")

    if st.button("إرسال"):
        if name and email and message:
            st.success("✅ تم إرسال رسالتك بنجاح! شكراً لتواصلك معنا.")
        else:
            st.error("❌ يرجى ملء جميع الحقول قبل الإرسال.")
