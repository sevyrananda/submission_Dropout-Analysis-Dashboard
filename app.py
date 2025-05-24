import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from joblib import load
import plotly.graph_objects as go

# Set layout lebar
st.set_page_config(page_title="Dropout Analysis Dashboard", layout="wide")

# =======================
# --- SIDEBAR ---
# =======================
st.sidebar.title("Dropout Analysis Dashboard")
add_selectbox = st.sidebar.selectbox(
    "Pilih Halaman",
    ("Dashboard", "Prediction")
)

# --- IDENTITAS ---
st.sidebar.markdown("## 👤 Identitas")
st.sidebar.markdown("**👩🏻‍💻 Nama:** Sevyra Nanda Octavianti  \n"
                    "**📧 Email:** sevyra02@gmail.com  \n"
                    "**🆔 ID Dicoding:** sevyrananda")
st.sidebar.markdown("---")

data = pd.read_csv("dataset_siap.csv", delimiter=",")
data_0 = data.loc[data['Status']==0]
data_1 = data.loc[data['Status']==1]
data_2 = data.loc[data['Status']==2]

category_mapping = {
    33: 'Biofuel Production Technologies',
    171: 'Animation and Multimedia Design',
    8014: 'Social Service (evening attendance)',
    9003: 'Agronomy',
    9070: 'Communication Design',
    9085: 'Veterinary Nursing',
    9119: 'Informatics Engineering',
    9130: 'Equinculture',
    9147: 'Management',
    9238: 'Social Service',
    9254: 'Tourism',
    9500: 'Nursing',
    9556: 'Oral Hygiene',
    9670: 'Advertising and Marketing Management',
    9773: 'Journalism and Communication',
    9853: 'Basic Education',
    9991: 'Management (evening attendance)'
}
data['Course_Label'] = data['Course'].replace(category_mapping)


def add_rating(content):
   
    return f"""
        <div style='
            height: auto;
            border: 2px solid #ccc;
            border-radius: 5px;
            font-size: 25px;
            padding-bottom: 38px;
            padding-top: 38px;
            background-color: #8E1616;
            text-align: center; /* Center text horizontally */
            display: flex;
            justify-content: center;
            align-items: center;
            '>{content}</div>
        """

def add_card(content, bg_color="#969797"):
   
    return f"""
        <div style='
            height: auto;
            font-size: 18px;
            border: 2px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            margin-bottom: 10px;
            background-color: {bg_color};
            text-align: center; /* Center text horizontally */
            display: flex; /* Center text vertically */
            justify-content: center; /* Center text vertically */
            align-items: center;
            line-height: 70px;
            color: #212121;
            '>{content}</div>
        """

def create_pie_chart(column, title):
    try:
        value_counts = kelas[column].value_counts()
        if len(value_counts) > 1:
            names = [False, True]
        else:
            if value_counts.index==1:
                names = [True]
            elif value_counts.index==0:
                names= [False]
        colors = px.colors.qualitative.Set2
        fig = px.pie(
            values=value_counts,
            names=names,
            title=title,
            color_discrete_sequence=px.colors.qualitative.Set2)
        fig.update_layout(
            height=200,
            margin=dict(l=0, r=10, t=70, b=10),
            title=dict(
                x=0,
                font=dict(size=15),
            ),
        )
        st.plotly_chart(fig)
    except UnboundLocalError as e:
        st.write("No data available to display.")

if add_selectbox == "Dashboard":
    st.title("🎓 Jaya Jaya Institute - Dropout Analysis Dashboard")
    st.markdown("""
        Dashboard ini menyajikan analisis untuk mengidentifikasi penyebab tingginya angka *dropout* di Jaya Jaya Institute. 
        Gunakan filter di bawah untuk mengeksplorasi data berdasarkan status, jurusan, gender, dan waktu kehadiran.
    """)
    with st.container(border=True):

        st.markdown("""🔍 Filter Data""")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            status_list = ['None', 'Dropout', 'Not Dropout']
            selected_status = st.selectbox('Select status', (status_list), key='initial_status')
            if selected_status == 'Dropout':
                selected_status = 0
            elif selected_status == 'Not Dropout':
                st.session_state['split_columns'] = True
                status_list = ['None', 'Enrolled', 'Graduated']
                selected_status = st.selectbox('Select type of Not Dropout', (status_list), key='not_dropout_type')
                if selected_status == 'None':
                    selected_status = 'Not Dropout'
                if selected_status == 'Enrolled':
                    selected_status = 1
                if selected_status == 'Graduated':
                    selected_status = 2
                kelas_selected_status = data[data.Status == selected_status]

        with col2:
            course_list = list(data.Course_Label.unique())[::-1]
            course_list.sort()
            course_list.insert(0,"None")
            selected_course = st.selectbox('Select course', (course_list))
            kelas_selected_course = data[data.Course_Label == selected_course]

        with col3:
            time_list = ['None', 'Daytime', 'Evening']
        
            selected_time = st.selectbox('Select attendance time', (time_list))
            kelas_selected_time = data[data.Daytime_evening_attendance == selected_time]
            if selected_time == 'Daytime':
                selected_time = 1
            elif selected_time == 'Evening':
                selected_time = 0

        with col4:
            gender_list = ['None', 'Male', 'Female']
            selected_gender = st.selectbox('Select gender', (gender_list))
            kelas_selected_gender = data[data.Course_Label == selected_gender]
            if selected_gender=='Male':
                selected_gender=1
            elif selected_gender=='Female':
                selected_gender=0
        
        if selected_status=='None':
            kelas = data
        elif selected_status=='Not Dropout':
            kelas = data.loc[data['Status_New']==1]
        else:
            kelas = data.loc[data['Status']==selected_status]

        if selected_course=="None":
            kelas = kelas
        else:
            kelas = kelas.loc[kelas['Course_Label']==selected_course]

        if selected_time=="None":
            kelas = kelas
        else:
            kelas = kelas.loc[kelas['Daytime_evening_attendance']==selected_time]

        if selected_gender=="None":
            kelas = kelas
        else:
            kelas = kelas.loc[kelas['Gender']==selected_gender]


    st.subheader('Overview Data')
    
    #===============================================
    containerB = st.container(border=True)
    containerA = st.container(border=True)

    colSt,colDr = st.columns([2,1])

    
    with containerA:
        
        with colSt:

            data_total = kelas['Status_0'].sum()+kelas['Status_1'].sum()+kelas['Status_2'].sum()
            st.markdown(add_card(f"<b>Total students</b><br>{data_total}"), unsafe_allow_html=True)
 
            col1, col2, col3 = st.columns(3)

            with col1:
                    data_do = kelas['Status_0'].sum()
                    st.markdown(add_card(f"<b>Dropped out student</b><br>{data_do}","#cc676f"), unsafe_allow_html=True)

            with col2:
                    data_enrolled = kelas['Status_1'].sum()
                    st.markdown(add_card(f"<b>Enrolled student</b><br>{data_enrolled}", "#d6bc66"), unsafe_allow_html=True)

            with col3:
                    data_graduated = kelas['Status_2'].sum()
                    st.markdown(add_card(f"<b>Graduated student</b><br>{data_graduated}", "#5bc073"), unsafe_allow_html=True)


    with containerB:   
       with colDr:
            dropout_rate = str(round((kelas['Status_0'].sum()/(kelas['Status_0'].sum()+kelas['Status_1'].sum()+kelas['Status_2'].sum()))*100,3))+"%"
            enrolled_rate = str(round((kelas['Status_1'].sum()/(kelas['Status_0'].sum()+kelas['Status_1'].sum()+kelas['Status_2'].sum()))*100,3))+"%"
            graduation_rate = str(round((kelas['Status_2'].sum()/(kelas['Status_0'].sum()+kelas['Status_1'].sum()+kelas['Status_2'].sum()))*100,3))+"%"
            st.markdown(add_rating(f"<b>Dropout Rate</b><br>{dropout_rate}"), unsafe_allow_html=True)
        
    #------------------------
    st.markdown("## 📊 Analisis Faktor Dropout Mahasiswa")
    col1, col2 = st.columns(2)

    if selected_status=="None":
        grouper = "Status"
    elif selected_status=='Not Dropout':
        grouper = "Status_New"
    else:
        grouper = "Status_"+str(selected_status)

    with col1:
        st.subheader('💸 Pemegang Beasiswa berdasarkan Status')
        
        status_labels = {0: "Dropout", 1: "Enrolled", 2: "Graduated"}
        a = kelas.groupby("Status")["Scholarship_holder"].sum()
        a.index = a.index.map(status_labels)

        fig = px.bar(
            x=a.index,
            y=a.values,
            labels={'x': 'Status', 'y': 'Jumlah Penerima Beasiswa'},
            text=a.values,
            color=a.index,
            color_discrete_sequence=px.colors.qualitative.Set1
        )
        fig.update_layout(height=300)
        st.plotly_chart(fig)

    #------------------------
    
    with col2:
        st.subheader("📘 Rata-Rata Nilai Per Semester")

        kelas_notdo = kelas  # pastikan kelas adalah DataFrame yang valid

        avg_1 = kelas_notdo.groupby(grouper)['Curricular_units_1st_sem_grade'].mean()
        avg_2 = kelas_notdo.groupby(grouper)['Curricular_units_2nd_sem_grade'].mean()

        # Pemetaan label status jika grouper adalah Status
        if grouper == 'Status':
            status_labels = {0: "Dropout", 1: "Enrolled", 2: "Graduated"}
            avg_1.index = avg_1.index.map(status_labels)
            avg_2.index = avg_2.index.map(status_labels)

        fig = go.Figure()

        fig.add_trace(go.Bar(name='Semester 1', x=avg_1.index, y=avg_1, marker_color='cornflowerblue'))
        fig.add_trace(go.Bar(name='Semester 2', x=avg_2.index, y=avg_2, marker_color='orange'))

        fig.update_layout(
            barmode='group',
            height=300,
            xaxis_title='Status' if grouper == 'Status' else grouper,
            yaxis_title='Rata-rata Nilai',
        )

        st.plotly_chart(fig)

    st.markdown("---")

    #------------------------
    container = st.container(border=True)
    col1, col2 = st.columns([4,1])
    with container:
       with col1:
        st.subheader("📚 Course dengan Tingkat Dropout Tertinggi")

        course_kls = kelas.copy()

        # Mapping dan cek course yang tidak ditemukan
        course_kls['Course'] = course_kls['Course'].map(category_mapping)
        if course_kls['Course'].isnull().any():
            st.warning("Beberapa course tidak dikenali dalam mapping dan telah dihapus.")
            course_kls = course_kls.dropna(subset=['Course'])

        # Data dropout dan non-dropout
        data_do = course_kls[course_kls['Status_0'] == 1]
        data_notdo = course_kls[course_kls['Status_0'] == 0]

        # Hitung jumlah dropout dan tidak dropout per course
        course_do = data_do.groupby('Course')['Status_0'].sum()
        course_notdo = data_notdo.groupby('Course')['Status_0'].count()

        # Hitung persentase dropout
        dropout_by_course = course_do / (course_do + course_notdo) * 100

        # Slider untuk jumlah course yang ditampilkan
        top_n = st.slider("Tampilkan Top-N Jurusan Dropout", min_value=3, max_value=len(dropout_by_course), value=5)
        top_dropouts = dropout_by_course.sort_values(ascending=False).head(top_n)

        # Visualisasi
        fig = px.bar(
            top_dropouts,
            x=top_dropouts.values,
            y=top_dropouts.index,
            orientation='h',
            text=[f"{v:.2f}%" for v in top_dropouts.values],
            color=top_dropouts.index,
            color_discrete_sequence=px.colors.qualitative.Set2,
            labels={'x': 'Dropout Rate (%)', 'y': 'Course'}
        )

        fig.update_layout(
            title=f"Top {top_n} Jurusan dengan Tingkat Dropout Tertinggi",
            height=400
        )

        st.plotly_chart(fig)


        #-----
        with col2:
            st.markdown("### 🧩 Faktor Tambahan")
            create_pie_chart('Educational_special_needs', 'Educational Special Needs <br>Distribution')
            create_pie_chart('Debtor', 'Debtor Distribution')
            create_pie_chart('Tuition_fees_up_to_date', 'Tuition Fees Up to Date<br>Distribution')
        #---------------------------------------------
    
    container = st.container(border=True)
    colors = px.colors.qualitative.Set2
    with container:
        colA, colB = st.columns([4,1])
        with colA:
            st.subheader("🎂 Distribusi Usia Mahasiswa")
            try:
                fig = px.histogram(
                    kelas,
                        x='Age_at_enrollment',
                        color_discrete_sequence=px.colors.qualitative.Set2
                    )
                
                st.plotly_chart(fig)

            except ValueError as e:
                st.write("No data available to display.")

        with colB:
            max_age = (kelas['Age_at_enrollment'].max())
            mean_age =  (kelas['Age_at_enrollment'].mean())
            min_age = (kelas['Age_at_enrollment'].min())
            st.markdown(add_card(f"<b>Minimum age</b><br>{min_age}"), unsafe_allow_html=True)
            st.markdown(add_card(f"<b>Average age</b><br>{mean_age}"), unsafe_allow_html=True)
            st.markdown(add_card(f"<b>Maximum age</b><br>{max_age}"), unsafe_allow_html=True)

    with st.expander("📌 Rekomendasi Aksi"):
        st.markdown("""
        - 🎯 Fokus pada jurusan dengan tingkat dropout tertinggi untuk peninjauan kurikulum atau dukungan belajar tambahan.
        - 🎓 Berikan perhatian lebih kepada siswa dengan nilai semester pertama rendah, karena berkorelasi dengan DO.
        - 💸 Monitoring status *Debtor* dan *Tuition Not Up-to-Date* bisa menjadi indikator risiko DO.
        - 💡 Pertimbangkan untuk memberi *intervensi awal* kepada siswa dengan usia pendaftaran lebih tinggi dari rata-rata.
        """)

if add_selectbox == "Prediction":
    st.title("🎯 Prediksi Risiko Dropout Mahasiswa")
    st.markdown("Isi formulir berikut berdasarkan profil mahasiswa untuk memprediksi kemungkinan dropout.")

    with st.container(border=True):
        st.subheader("🧾 Informasi Akademik & Pribadi")

        col1, col2 = st.columns(2)
        with col1:
            course_list = list(data.Course_Label.unique())
            course_list.sort()
            course_selected = st.selectbox('🎓 Pilih Course', course_list, help="Ubah jika perlu dengan memilih course yang ada pada dropdown sesuai course Anda")
        with col2:
            admgrade_selected = st.number_input("📝 Nilai Tes Masuk", value=0.0, step=0.1, min_value=0.0, max_value=100.0, help="Masukkan nilai antara 0 hingga 100")

        reverse_mapping = {v: k for k, v in category_mapping.items()}
        course_code = reverse_mapping[course_selected]
        time_selected = 0 if course_code in [9991, 8014] else 1

        col3, col4, col5 = st.columns(3)
        with col3:
            gender_selected = st.selectbox("🚻 Gender", ['Male', 'Female'], help="Ubah jika perlu gender dengan memilih Female (Perempuan) dan Male (Laki-laki)")
            gender_selected = 1 if gender_selected == 'Male' else 0

        with col4:
            age_selected = st.number_input("🎂 Usia Saat Masuk", min_value=17, max_value=70, step=1, help="Masukkan usia antara 17 hingga 70 tahun")

        with col5:
            attendance = st.selectbox("Tipe Kehadiran", ["Daytime", "Evening"])
            attendance_code = 0 if attendance == "Daytime" else 1

    with st.container(border=True):
        st.subheader("💡 Faktor Risiko Tambahan", help="Ubah jika perlu masing-masing faktor tambahan yang ada di bawah ini dengan Yes atau No")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            special_selected = st.radio("🧠 Kebutuhan Khusus", ['Yes', 'No'])
            special_selected = 1 if special_selected == 'Yes' else 0

        with col2:
            debtor_selected = st.radio("💳 Memiliki Tunggakan?", ['Yes', 'No'])
            debtor_selected = 1 if debtor_selected == 'Yes' else 0

        with col3:
            tuition_selected = st.radio("💰 Pembayaran Lengkap?", ['Yes', 'No'])
            tuition_selected = 1 if tuition_selected == 'Yes' else 0

        with col4:
            scholarship_selected = st.radio("🎓 Penerima Beasiswa?", ['Yes', 'No'])
            scholarship_selected = 1 if scholarship_selected == 'Yes' else 0

    with st.container(border=True):
        st.subheader("📚 Nilai Semester Mahasiswa")
        col1, col2 = st.columns(2)

        with col1:
            grade1_selected = st.number_input("Semester 1", help="Masukkan nilai antara 0 hingga 100", value=0.0, step=0.1, min_value=0.0, max_value=100.0)
        with col2:
            grade2_selected = st.number_input("Semester 2", help="Masukkan nilai antara 0 hingga 100", value=0.0, step=0.1, min_value=0.0, max_value=100.0)

    st.markdown('<style>div.stButton > button {margin: 0 auto; display: block; background: #003f5c; color: white; padding: 0.6em 2em; font-weight: bold;}</style>', unsafe_allow_html=True)
    if st.button("🔍 Prediksi Sekarang"):
        model = load('model.joblib')
        user_data = {
            'Course': [course_code],
            'Daytime_evening_attendance': [time_selected],
            'Admission_grade': [round(admgrade_selected, 1)],
            'Educational_special_needs': [special_selected],
            'Debtor': [debtor_selected],
            'Tuition_fees_up_to_date': [tuition_selected],
            'Gender': [gender_selected],
            'Scholarship_holder': [scholarship_selected],
            'Age_at_enrollment': [age_selected],
            'Curricular_units_1st_sem_grade': [round(grade1_selected, 2)],
            'Curricular_units_2nd_sem_grade': [round(grade2_selected, 2)]
        }

        X_new = pd.DataFrame(user_data)
        predictions = model.predict(X_new)

        st.subheader("📢 Hasil Prediksi")
        if predictions[0] == 0:
            st.error("❌ Mahasiswa berpotensi **Dropout**. Perlu perhatian lebih!")
        else:
            st.success("✅ Mahasiswa **tidak berisiko Dropout**. Tetap pantau kemajuan akademik.")

        with st.expander("ℹ️ Penjelasan Model"):
            st.markdown("""
            Model prediksi ini dibangun menggunakan algoritma Machine Learning dengan mempertimbangkan beberapa faktor akademik dan non-akademik. 
            Silakan gunakan hasil ini sebagai bahan pertimbangan tambahan, bukan keputusan tunggal.
            """)
