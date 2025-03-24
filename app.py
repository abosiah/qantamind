import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# استيراد الوحدات من ملفات المشروع
from qantamind.ai_module import predict_energy_pattern
from qantamind.quantum_engine import compute_quantum_fluctuation
from qantamind.sound_analyzer import analyze_sound

st.set_page_config(page_title="QANTAMIND - Quantum Energy Interface", layout="centered")

# شعار QANTAMIND
st.image('assets/qantamind_logo.png', width=200)

st.title('🔮 QANTAMIND - منصة التحليل الكمومي للطاقة')

# القائمة الجانبية
analysis_type = st.sidebar.selectbox(
    'اختر نوع التحليل:',
    ('الطاقة السالبة', 'الفراغ الكمومي', 'الصوتيات', 'تنبؤ الذكاء الاصطناعي')
)

# الطاقة السالبة
def negative_energy(mass, velocity):
    c = 3 * 10**8
    return -mass * (velocity ** 2) / (2 * c ** 2)

# واجهات التفاعل حسب النوع
if analysis_type == 'الطاقة السالبة':
    st.header('🌀 تحليل الطاقة السالبة')
    mass = st.number_input('الكتلة (كجم):', min_value=0.0, value=1.0)
    velocity = st.number_input('السرعة (م/ث):', min_value=0.0, value=10.0)
    if st.button('ابدأ التحليل'):
        result = negative_energy(mass, velocity)
        st.success(f'الطاقة السالبة الناتجة: {result:.2e} جول')

elif analysis_type == 'الفراغ الكمومي':
    st.header('🌌 تحليل الفراغ الكمومي')
    freq = st.number_input('التردد (Hz):', min_value=0.0, value=1.0e14)
    if st.button('ابدأ التحليل'):
        result = compute_quantum_fluctuation(freq)
        st.info(f'طاقة الفراغ: {result:.2e} جول')

elif analysis_type == 'الصوتيات':
    st.header('🎵 تحليل الصوتيات')
    freq = st.number_input('التردد (Hz):', min_value=20.0, value=440.0)
    amp = st.number_input('السعة:', min_value=0.0, value=1.0)
    if st.button('ابدأ التحليل'):
        result = analyze_sound(freq, amp)
        st.success(f'شدة الصوت: {result:.2e} وحدة')

elif analysis_type == 'تنبؤ الذكاء الاصطناعي':
    st.header('🤖 تحليل الذكاء الاصطناعي - أنماط الطاقة')
    data_input = st.text_input("أدخل سلسلة استهلاكات طاقة مفصولة بفواصل (مثال: 50, 65, 72)")
    if st.button("ابدأ التنبؤ"):
        try:
            data = [float(x.strip()) for x in data_input.split(',') if x.strip()]
            prediction = predict_energy_pattern(data)
            st.success(f'تنبؤ استهلاك الطاقة التالي: {prediction:.2f} كيلو واط')
        except:
            st.error("⚠️ تأكد من إدخال أرقام مفصولة بفواصل بشكل صحيح.")

st.markdown("---")
st.caption("💡 QANTAMIND | ذكاء اصطناعي + طاقة + كمّيات ترددية... كل شيء في منصة واحدة.")
