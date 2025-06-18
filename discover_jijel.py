import streamlit as st
import folium
from streamlit_folium import st_folium

# إعداد الصفحة
st.set_page_config(page_title="اكتشف جيجل", page_icon="🌊", layout="wide")

# القائمة الجانبية
st.sidebar.title("اكتشف جيجل")
menu = st.sidebar.radio("انتقل إلى:", ["الرئيسية", "الأماكن السياحية", "الخريطة", "معرض الصور", "اتصل بنا"])

# بيانات الأماكن السياحية
places = {
   "البحور": [
    {"name": "شاطئ كتامة", "img": "images/ketama.jpg", "desc": "شاطئ رملي واسع بمياه زرقاء صافية."},
    {"name": "شاطئ أندرمان", "img": "images/anderman.jpg", "desc": "شاطئ هادئ مثالي للاسترخاء."},
    {"name": "شاطئ الكورنيش", "img": "images/corniche.jpg", "desc": "كورنيش سياحي بإطلالة رائعة."},
    {"name": "شاطئ زيامة منصورية", "img": "images/ziama.jpg", "desc": "شاطئ طويل تحيط به الجبال."},
    {"name": "شاطئ أفتيس", "img": "images/aftis.jpg", "desc": "أحد أجمل الشواطئ الرملية في جيجل."},
    {"name": "شاطئ أندرو", "img": "images/androu.jpg", "desc": "شاطئ رائع مع منحدرات صخرية."},
    {"name": "شاطئ تاسوست", "img": "images/tassoust.jpg", "desc": "شاطئ حضري نظيف بالقرب من المدينة."}
],

    "الوديان": [
        {"name": "وادي الزهور", "img": "https://upload.wikimedia.org/wikipedia/commons/5/54/Oued_floral.jpg", "desc": "وادٍ تحيط به الزهور والأشجار، مناسب للنزهات."},
        {"name": "وادي الكبير", "img": "https://upload.wikimedia.org/wikipedia/commons/1/12/Oued_elkebir.jpg", "desc": "وادي شهير يمر وسط التضاريس الجبلية."}
    ],
    "الغابات": [
        {"name": "غابة بوجموعان", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3b/Foret_de_jijel.jpg", "desc": "غابة كثيفة ومحمية طبيعية."},
        {"name": "غابة تامنتوت", "img": "https://upload.wikimedia.org/wikipedia/commons/f/f1/Foret_tamntout.jpg", "desc": "غابة متميزة بتنوعها البيولوجي."}
    ],
    "الكهوف": [
        {"name": "الكهوف العجيبة", "img": "https://upload.wikimedia.org/wikipedia/commons/6/65/Grotte_Jijel.jpg", "desc": "كهوف ساحرة تحت الأرض ذات أشكال غريبة."},
        {"name": "مغارة أوقاس", "img": "https://upload.wikimedia.org/wikipedia/commons/9/91/Ouakas_grotte.jpg", "desc": "مغارة أثرية تحوي تشكيلات صخرية جميلة."}
    ]
}

# معرض الصور: جميع الصور في قائمة واحدة
gallery_images = [place["img"] for group in places.values() for place in group]

# ============================ الصفحات ============================

# 🏠 الصفحة الرئيسية
if menu == "الرئيسية":
    st.title("🌊 مرحباً بكم في ولاية جيجل")
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4f/Jijel_Beauty.jpg", use_column_width=True)
    st.markdown("""
    **جيجل**، جوهرة البحر الأبيض المتوسط، تجمع بين الطبيعة الخلابة، الغابات الكثيفة، الشواطئ الساحرة، والكهوف الغامضة.

    - 🗺️ استكشف الأماكن السياحية حسب الفئة
    - 🌍 شاهد خريطة تفاعلية
    - 📸 تصفح معرض الصور
    - 📬 تواصل معنا
    """)

# 🏞️ الأماكن السياحية
elif menu == "الأماكن السياحية":
    st.header("🗺️ الأماكن السياحية حسب النوع")
    for category, spots in places.items():
        st.subheader(f"🔸 {category}")
        cols = st.columns(2)
        for i, spot in enumerate(spots):
            with cols[i % 2]:
                st.image(spot["img"], use_column_width=True)
                st.markdown(f"**{spot['name']}**")
                st.caption(spot["desc"])
        st.markdown("---")

# 🌍 الخريطة التفاعلية
elif menu == "الخريطة":
    st.header("🌍 خريطة تفاعلية للأماكن السياحية")
    m = folium.Map(location=[36.82, 5.77], zoom_start=10)
    folium.Marker([36.82, 5.77], tooltip="شاطئ كتامة").add_to(m)
    folium.Marker([36.75, 5.88], tooltip="الكهوف العجيبة").add_to(m)
    folium.Marker([36.85, 5.74], tooltip="غابة بوجموعان").add_to(m)
    st_folium(m, width=700, height=500)

# 🖼️ معرض الصور
elif menu == "معرض الصور":
    st.header("📸 معرض صور جيجل")
    cols = st.columns(3)
    for i, img in enumerate(gallery_images):
        with cols[i % 3]:
            st.image(img, use_column_width=True)
# 🏨 الفنادق
elif menu == "الفنادق":
    st.header("🏨 الفنادق والإقامات في جيجل")

    hotels = [
        {"name": "فندق جيجل الكبير", "location": "وسط المدينة", "price": "7000 دج", "rating": 4.3, "features": "WiFi، إفطار، مكيف"},
        {"name": "إقامة المرجان", "location": "القنار", "price": "5000 دج", "rating": 4.0, "features": "مطل على البحر"},
        {"name": "نزل العافية", "location": "رأس العافية", "price": "4000 دج", "rating": 3.8, "features": "قريب من الشاطئ"},
        {"name": "دار الضياف زيامة", "location": "زيامة منصورية", "price": "6000 دج", "rating": 4.5, "features": "مطبخ، موقف سيارات"}
    ]

    for hotel in hotels:
        st.subheader(f"🏨 {hotel['name']}")
        st.write(f"📍 الموقع: {hotel['location']}")
        st.write(f"💰 السعر: {hotel['price']}")
        st.write(f"⭐ التقييم: {hotel['rating']} / 5")
        st.write(f"✨ المميزات: {hotel['features']}")
        st.markdown("---")

# ✉️ اتصل بنا
elif menu == "اتصل بنا":
    st.header("📬 اتصل بنا")
    name = st.text_input("الاسم")
    email = st.text_input("البريد الإلكتروني")
    msg = st.text_area("رسالتك")

    if st.button("إرسال"):
        if name and email and msg:
            st.success("✅ تم إرسال رسالتك، شكراً لتواصلك معنا.")
        else:
            st.error("❌ يرجى ملء جميع الحقول.")
