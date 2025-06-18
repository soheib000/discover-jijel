import streamlit as st
import folium
from streamlit_folium import st_folium

# إعداد الصفحة
st.set_page_config(page_title="اكتشف جيجل", page_icon="🌊", layout="wide")

# القائمة الجانبية
st.sidebar.title("اكتشف جيجل")
menu = st.sidebar.radio("انتقل إلى:", ["الرئيسية", "الأماكن السياحية", "الفنادق", "الخريطة", "معرض الصور", "اتصل بنا"])

# البيانات
places = {
    "البحور": [
        {"name": "شاطئ كتامة", "img": "images/ketama.jpg", "desc": "شاطئ رملي واسع بمياه زرقاء صافية."},
        {"name": "شاطئ أندرمان", "img": "images/anderman.jpg", "desc": "من الشواطئ الهادئة والرائعة لعشاق الاستجمام."},
        {"name": "شاطئ الكورنيش", "img": "images/corniche.jpg", "desc": "يمتد على طول طريق الكورنيش بمناظر رائعة."},
        {"name": "شاطئ الصخر الأسود", "img": "images/black_rock.jpg", "desc": "شاطئ صخري غريب المنظر."},
        {"name": "شاطئ تاسوست", "img": "images/tassoust.jpg", "desc": "شاطئ طويل ونظيف بالقرب من الميناء."},
        {"name": "شاطئ بني بلعيد", "img": "images/beni_belaid.jpg", "desc": "من أجمل شواطئ شرق جيجل."}
    ],
    "الوديان": [
        {"name": "وادي الزهور", "img": "images/oued_fleurs.jpg", "desc": "وادٍ تحيط به الزهور والأشجار، مناسب للنزهات."},
        {"name": "وادي الكبير", "img": "images/oued_kebir.jpg", "desc": "وادي شهير يمر وسط التضاريس الجبلية."},
        {"name": "وادي جن جن", "img": "images/oued_jijel.jpg", "desc": "وادي معروف يصب قرب الميناء."}
    ],
    "الغابات": [
        {"name": "غابة بوجموعان", "img": "images/boujemaa.jpg", "desc": "غابة كثيفة ومحمية طبيعية."},
        {"name": "غابة تامنتوت", "img": "images/tamntout.jpg", "desc": "غابة جبلية خلابة."},
        {"name": "غابة زيامة", "img": "images/ziama.jpg", "desc": "غابة جميلة على طريق الكورنيش."}
    ],
    "الكهوف": [
        {"name": "الكهوف العجيبة", "img": "images/grottes.jpg", "desc": "كهوف تحت الأرض ذات أشكال غريبة."},
        {"name": "مغارة أوقاس", "img": "images/oukass.jpg", "desc": "مغارة أثرية جميلة."},
        {"name": "مغارة سيدي معروف", "img": "images/sidi_maarouf.jpg", "desc": "كهف داخل منطقة جبلية مشهورة."}
    ]
}

hotels = [
    {"name": "فندق جيجل الكبير", "location": "وسط المدينة", "price": "7000 دج", "stars": 4, "rating": 4.2},
    {"name": "إقامة المرجان", "location": "القنار", "price": "5000 دج", "stars": 3, "rating": 4.0},
    {"name": "نزل العافية", "location": "رأس العافية", "price": "4000 دج", "stars": 2, "rating": 3.8},
    {"name": "فندق الكورنيش", "location": "طريق البحر", "price": "8000 دج", "stars": 4, "rating": 4.5}
]

gallery_images = [place["img"] for group in places.values() for place in group]

# الصفحة الرئيسية
if menu == "الرئيسية":
    st.title("🌊 مرحباً بكم في ولاية جيجل")
    st.image("images/jijel_cover.jpg", use_column_width=True)
    st.markdown("""
    **جيجل**، جوهرة البحر الأبيض المتوسط، تجمع بين الطبيعة الخلابة، الغابات الكثيفة، الشواطئ الساحرة، والكهوف الغامضة.

    - 🗺️ استكشف الأماكن السياحية حسب الفئة
    - 🌍 شاهد خريطة تفاعلية
    - 📸 تصفح معرض الصور
    - 📬 تواصل معنا
    """)

# الأماكن السياحية
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

# الفنادق
elif menu == "الفنادق":
    st.header("🏨 قائمة الفنادق المقترحة")
    for hotel in hotels:
        st.subheader(f"{hotel['name']} {'⭐' * hotel['stars']}")
        st.write(f"📍 الموقع: {hotel['location']}")
        st.write(f"💰 السعر: {hotel['price']}")
        st.write(f"⭐ التقييم: {hotel['rating']} / 5")
        st.markdown("---")

# الخريطة
elif menu == "الخريطة":
    st.header("🌍 خريطة تفاعلية للأماكن السياحية")
    m = folium.Map(location=[36.82, 5.77], zoom_start=10)
    folium.Marker([36.82, 5.77], tooltip="شاطئ كتامة").add_to(m)
    folium.Marker([36.75, 5.88], tooltip="الكهوف العجيبة").add_to(m)
    folium.Marker([36.85, 5.74], tooltip="غابة بوجموعان").add_to(m)
    st_folium(m, width=700, height=500)

# معرض الصور
elif menu == "معرض الصور":
    st.header("📸 معرض صور جيجل")
    cols = st.columns(3)
    for i, img in enumerate(gallery_images):
        with cols[i % 3]:
            st.image(img, use_column_width=True)

# اتصل بنا
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
