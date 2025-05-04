import streamlit as st
from streamlit_option_menu import option_menu
from jdatetime import datetime
import sqlite3
import os
import re
import tempfile

# تنظیمات صفحه
st.set_page_config(
    page_title="باشگاه دلفین گربدان",
    page_icon="favicon.png",
    initial_sidebar_state='collapsed',
    layout='wide',
)

temp_dir = tempfile.gettempdir()

# ایجاد مسیر پایگاه داده
media_db_path = os.path.join(temp_dir, 'media.db')
messages_db_path = os.path.join(temp_dir, 'messages.db')
chat_db_path = os.path.join(temp_dir, 'chat.db')
db_path = os.path.join(temp_dir, 'gorbedan.db')


def create_database():

    

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS media (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            video BLOB,
            image BLOB,
            text TEXT
        )
    ''')
    conn.commit()
    conn.close()

# ایجاد جدول نظرات
def create_comments_table():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            comment TEXT NOT NULL,
            approved BOOLEAN NOT NULL DEFAULT 0,
            response TEXT
        )
    ''')
    conn.commit()
    conn.close()

# ذخیره رسانه در پایگاه داده
def save_to_database(video, image, text):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("INSERT INTO media (video, image, text) VALUES (?, ?, ?)", (video, image, text))
    conn.commit()
    conn.close()

# دریافت رسانه‌ها از پایگاه داده
def get_media():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM media ORDER BY id DESC")
    data = c.fetchall()
    conn.close()
    return data

# حذف رسانه از پایگاه داده
def delete_media(media_id):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("DELETE FROM media WHERE id = ?", (media_id,))
    conn.commit()
    conn.close()

# ذخیره نظر کاربر
def save_comment(name, comment):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("INSERT INTO comments (name, comment) VALUES (?, ?)", (name, comment))
    conn.commit()
    conn.close()

# دریافت نظرات از پایگاه داده
def get_comments():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM comments ORDER BY id DESC")
    data = c.fetchall()
    conn.close()
    return data

# تأیید نظر کاربر
def approve_comment(comment_id, response):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("UPDATE comments SET approved = 1, response = ? WHERE id = ?", (response, comment_id))
    conn.commit()
    conn.close()

# حذف نظر کاربر
def delete_comment(comment_id):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("DELETE FROM comments WHERE id = ?", (comment_id,))
    conn.commit()
    conn.close()

create_database()
create_comments_table()



# اتصال به پایگاه داده
con = sqlite3.connect(media_db_path)
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS pics(id TEXT, img BLOB, note TEXT)')

# بارگذاری استایل CSS
with open("cc.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)

now = datetime.now()
tim = now.strftime("%Y/%m/%d")

# منوی جانبی
with st.sidebar:
    menu_id = option_menu(
        menu_title=None,
        options=["صفحه اصلی", "خبرها", "ویدیوها", "بازیکنان"],
        icons=["house"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
        styles={
         "container": {"background-color": "#ffffff"},
         "icon" : {"color": "#000000"},
         "nav-link-selected": {"background-color": "#577BC1"},
         "nav-link": {"color" : "#000000","font-size": "19px", "text-align": "center_y: 0.0", "margin":"0px", "--hover-color": "#C4D9FF"},

        }
    )

st.subheader("باشگاه فرهنگی ورزشی دلفین گربدان")
# st.divider()
st.image("favicon.png", width=100)

if menu_id == "بازیکنان":
    st.divider()
    c1, c2, c3, c4 = st.columns([3, 2, 2, 1])

    with c1:
        
        st.image('i1.jpg')
        st.image('i3.jpg')
        st.image('i4.jpg')
        st.image('i5.jpg')
        st.image('i6.jpg')
        st.image('i7.jpg')
        st.image('i8.jpg')
        st.image('i9.jpg')
        st.image('i10.jpg')
        st.image('i11.jpg')
        st.image('i12.jpg')
        st.image('i13.jpg')
        st.image('i14.jpg')
        st.image('i15.jpg')
        st.image('i16.jpg')
        st.image('i17.jpg')
        st.image('i18.jpg')


    with c2:
        st.image('i19.jpg')
        st.image('i20.jpg')
        st.image('i21.jpg')
        st.image('i22.jpg')
        st.image('i23.jpg')
        st.image('i24.jpg')
        st.image('i25.jpg')
        st.image('i26.jpg')
        st.image('i27.jpg')
        st.image('i28.jpg')
        st.image('i29.jpg')
        st.image('i30.jpg')
        st.image('i31.jpg')
        st.image('i32.jpg')
        st.image('i33.jpg')

    with c3:
        st.image('i34.jpg')
        st.image('i35.jpg')
        st.image('i36.jpg')
        st.image('i37.jpg')
        st.image('i38.jpg')
        st.image('i39.jpg')
        st.image('i40.jpg')
        st.image('i41.jpg')
        st.image('i42.jpg')
        st.image('i43.jpg')
        st.image('i44.jpg')

if menu_id == "صفحه اصلی":
    selected = option_menu(
        menu_title=None,
        options=["پخش زنده","مسابقه ها", "چت آنلاین", "ادمین", "خانه"],
        icons=["phone", "","", "key", "house"],
        menu_icon="cast",
        default_index=4,
        orientation="horizontal",
        styles={
         "container": {"background-color": "#ffffff"},
         "icon" : {"color": "#000000"},
         "nav-link-selected": {"background-color": "#577BC1"},
         "nav-link": {"color" : "#000000","font-size": "19px", "text-align": "center_y: 0.0", "margin":"0px", "--hover-color": "#C4D9FF"},

        }
    )

    st.write("تاریخ امروز :", tim)


    if selected == "ادمین":
        username = st.text_input(label="رمز عبور", placeholder="Password")
        b = st.button("ورود")

        if username == "gorbedan":
            tab1, tab2 = st.tabs(['آپلود فایل', 'پخش زنده'])

            with tab1:
                st.success("خوش آمدی ادمین")
                media_type = st.selectbox("Select Media Type", options=["ویدیو", "تصاویر"])
                if media_type == "ویدیو":
                    uploaded_file = st.file_uploader("Upload Video", type=["mp4", "mov", "avi"])
                else:
                    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

                text_input = st.text_area("Enter Description")

                if st.button("Save", key="save_media"):
                    if uploaded_file is not None and text_input:
                        media_data = uploaded_file.read()
                        if media_type == "ویدیو":
                            save_to_database(media_data, None, text_input)  # ذخیره ویدیو
                        else:
                            save_to_database(None, media_data, text_input)  # ذخیره تصویر
                        st.success(f"{media_type} و متن با موفقیت ذخیره شد!")

                    else:
                        st.error("لطفا یک فایل و یک توضیح وارد کنید.")

                # نمایش رسانه‌های بارگذاری شده
                st.subheader("رسانه‌های بارگذاری شده")
                st.divider()
                media = get_media()
                for media_item in media:
                    if media_item[1]:  # بررسی وجود ویدیو
                        st.video(media_item[1])  # نمایش ویدیو
                    if media_item[2]:  # بررسی وجود تصویر
                        st.image(media_item[2], use_container_width=True)  # نمایش تصویر
                    st.write(media_item[3])  # نمایش متن
                    if st.button(f"حذف رسانه {media_item[0]}", key=f"delete_media_{media_item[0]}"):
                        delete_media(media_item[0])
                        st.success(f"رسانه {media_item[0]} با موفقیت حذف شد!")
                        st.rerun()

                    st.warning("") 

            with tab2:
                def is_valid_youtube_link(link):
                    youtube_regex = r'(https?://)?(www\.)?(youtube\.com/(watch\?v=|live/)|youtu\.be/)([a-zA-Z0-9_-]{11})'
                    return re.match(youtube_regex, link) is not None

                st.success("پخش زنده")
                conn = sqlite3.connect(messages_db_path)
                c = conn.cursor()
                c.execute('''
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    message TEXT NOT NULL
                )
                ''')
                conn.commit()

                c.execute('SELECT message FROM messages ORDER BY id DESC LIMIT 1')
                last_link = c.fetchone()
                conn.close()

                if last_link:
                    youtube_live_link = last_link[0]
                    st.write("لینک قبلی شما:", youtube_live_link)
                else:
                    youtube_live_link = st.text_input("برای روشن کردن پخش زنده لینک رو وارد کنید", "")

                e = st.button("روشن کردن پخش زنده")

                if e:
                    if is_valid_youtube_link(youtube_live_link):
                        if "youtube.com/watch?v=" in youtube_live_link:
                            video_id = youtube_live_link.split("watch?v=")[1].split("&")[0]
                        elif "youtube.com/live/" in youtube_live_link:
                            video_id = youtube_live_link.split("/live/")[1].split("?")[0]
                        else:
                            video_id = youtube_live_link.split("/")[-1]

                        embed_link = f"https://www.youtube.com/embed/{video_id}"

                        st.markdown(
                            f"""
                            <style>
                            .video-container {{
                                position: relative;
                                padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
                                height: 0;
                                overflow: hidden;
                            }}
                            .video-container iframe {{
                                position: absolute;
                                top: 0;
                                left: 0;
                                width: 100%;
                                height: 100%;
                            }}
                            </style>
                            <div class="video-container">
                                <iframe src="{embed_link}" frameborder="0" allowfullscreen></iframe>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                        conn = sqlite3.connect(messages_db_path)
                        c = conn.cursor()
                        c.execute('SELECT COUNT(*) FROM messages WHERE message = ?', (youtube_live_link,))
                        if c.fetchone()[0] == 0:
                            c.execute('INSERT INTO messages (message) VALUES (?)', (youtube_live_link,))
                            conn.commit()
                        conn.close()
                    else:
                        st.error("لینک وارد شده صحیح نیست.")

                st.divider()

                delete = st.button("برای حذف کامل ویدیو دوبار کلیک کنید")

                if delete:
                    if last_link:
                        conn = sqlite3.connect(messages_db_path)
                        c = conn.cursor()
                        c.execute('DELETE FROM messages WHERE message = ?', (last_link[0],))
                        conn.commit()
                        conn.close()
                        st.success("لینک ویدیو حذف شد. لطفاً لینک جدیدی وارد کنید.")
                        youtube_live_link = ""
                    else:
                        st.warning("هیچ لینکی برای حذف وجود ندارد.")

        else:
            st.error("لطفا رمز عبور را وارد کنید")


    elif selected == "مسابقه ها":
        st.warning("بازی های فوتسال جام اتحاد و همدلی دلفین گربدان 1403")
        col1, col2 ,col3 = st.columns(3)

        with col1:
            with st.expander("دلفین گربدان", expanded=True):
                st.video("https://www.youtube.com/watch?v=Mff7jVcv5a8&t=3s")
                st.caption("""
                    تیم جواهری رز :red[&] تیم درمانگاه آفرینش
                """)
                st.caption("""
                   :red[1403/11/01]
                """)


        with col2:
            with st.expander("دلفین گربدان", expanded=True):
                st.video("https://www.youtube.com/watch?v=_ArHu6i5v_Q")
                st.caption("""
                    تیم نوین کابینت :red[&] تیم نامبروان
                """)
                st.caption("""
                   :red[1403/11/03]
                """)
            st.warning("")
        

        with col3:
            c1,c2 = st.columns(2)
            with c1:
                st.image("t1.jpg",width=200)
                st.image("t2.jpg",width=200)
                st.image("t3.jpg",width=200)
                st.image("t4.jpg",width=200)

            with c2:
                st.image("t5.jpg",width=200)
                st.image("t6.jpg",width=200)
                st.image("t7.jpg",width=200)
                st.image("t8.jpg",width=200)

    if selected == "چت آنلاین":
        st.warning("توجه : برای مشاهده پیام های دیگران به صفحه دیگری بروید و دوباره به صفحه چت آنلاین بیایید .")

        with st.expander("چت آنلاین", expanded=True):
            st.subheader("🔻 چت آنلاین 🔻")
            conn = sqlite3.connect(chat_db_path)
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS messages
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT,
                        message TEXT,
                        timestamp DATETIME)''')
            conn.commit()

            def add_message(username, message):
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                c.execute("INSERT INTO messages (username, message, timestamp) VALUES (?, ?, ?)",
                          (username, message, timestamp))
                conn.commit()

            def get_messages():
                c.execute("SELECT id, username, message, timestamp FROM messages ORDER BY timestamp DESC LIMIT 100")
                return c.fetchall()

            def delete_message(message_id):
                c.execute("DELETE FROM messages WHERE id = ?", (message_id,))
                conn.commit()

            username = st.text_input(": نام خود را وارد کنید")
            messages = get_messages()
            new_message = st.text_input(": پیام خود را وارد کنید")
            ersal = st.button("ارسال")

            if ersal and username and new_message:
                add_message(username, new_message)
                st.rerun()
            elif ersal and username and new_message == "":
                st.error("لطفا پیام‌ خو بنویس")
            elif ersal and new_message and username == "":
                st.error("لطفا اسم خو بنویس")

            st.divider()

            for msg in messages:
                msg_id, msg_user, msg_text, msg_timestamp = msg
                st.success(f"{msg_timestamp} 🙋🏽‍♂️ {msg_user}: 💬 {msg_text}")

                if st.button("حذف", key=f"delete_{msg_id}"):
                    delete_message(msg_id)
                    st.rerun()

            conn.close()

    elif selected == "پخش زنده":

        st.warning("تمامی بازی های تیم دلفین گربدان اینجا برگزار خواهد شد")            
        def is_valid_youtube_link(link):
            youtube_regex = r'(https?://)?(www\.)?(youtube\.com/(watch\?v=|live/)|youtu\.be/)([a-zA-Z0-9_-]{11})'
            return re.match(youtube_regex, link) is not None

        conn = sqlite3.connect(messages_db_path)
        c = conn.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL
        )
        ''')
        conn.commit()

        c.execute('SELECT message FROM messages ORDER BY id DESC LIMIT 1')
        last_link = c.fetchone()
        conn.close()

        if last_link:
            youtube_live_link = last_link[0]
        else:
            youtube_live_link = ""

        # st.image("live.gif",width=50)
        e = st.button("🎥 روشن کردن پخش زنده 🔴")

        try:
            if e:
                if is_valid_youtube_link(youtube_live_link):
                    if "youtube.com/watch?v=" in youtube_live_link:
                        video_id = youtube_live_link.split("watch?v=")[1].split("&")[0]
                    elif "youtube.com/live/" in youtube_live_link:
                        video_id = youtube_live_link.split("/live/")[1].split("?")[0]
                    else:
                        video_id = youtube_live_link.split("/")[-1]

                    embed_link = f"https://www.youtube.com/embed/{video_id}"
                    st.markdown(
                        f"""
                        <style>
                        .video-container {{
                            position: relative;
                            padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
                            height: 0;
                            overflow: hidden;
                        }}
                        .video-container iframe {{
                            position: absolute;
                            top: 0;
                            left: 0;
                            width: 100%;
                            height: 100%;
                        }}
                        </style>
                        <div class="video-container">
                            <iframe src="{embed_link}" frameborder="0" allowfullscreen></iframe>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    conn = sqlite3.connect(messages_db_path)
                    c = conn.cursor()
                    c.execute('SELECT COUNT(*) FROM messages WHERE message = ?', (youtube_live_link,))
                    if c.fetchone()[0] == 0:
                        c.execute('INSERT INTO messages (message) VALUES (?)', (youtube_live_link,))
                        conn.commit()
                    conn.close()
                else:
                    st.error("پخش زنده وجود ندارد")
        except:
            st.error("پخش زنده وجود ندارد")

        st.divider()

        st.warning("هشدار : برای روشن کردن پخش زنده به فیلترشکن نیاز دارید")

    elif selected == "خانه":


        with st.expander("تیم دلفین گربدان", expanded=True):
            st.image("passdolfin.jpg")
            st.caption("""
            باشگاه فوتبال دلفین گربدان یکی از پر افتخارترین و پر هوادارترین باشگاه های فوتبال در جزیره قشم است. دلفین گربدان پیش از انقلاب ستاره جنوب گربدان نام داشت. باشگاه هم اکنون در لیگ دسته دو قشم قرار گرفته و در سال 1324 در جزیره قشم روستای گربدان بنیان گذاری شده است.
            """)

        st.divider()

        media = get_media()
        for media_item in media:
            if media_item[1]:  # بررسی وجود ویدیو
                st.video(media_item[1])

                
                  # نمایش ویدیو
            if media_item[2]:
                 # بررسی وجود تصویر
                st.image(media_item[2], use_container_width=True)  # نمایش تصویر
            st.write(media_item[3]) 
            st.warning("") 

if menu_id == "ویدیوها":
    st.divider()
    c1, c2 = st.columns(2)

    with c1:
        st.video("d1.mp4")
        st.video("d2.mp4")
    with c2:
        st.video("d3.mp4")
        st.video("d5.mp4")
        st.video("d6.mp4")

if menu_id == "خبرها":
    st.divider()
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.expander("همه نگاه‌ها به دلفین گربدان, لیگ 2 در اوج حساسیت", expanded=True):
            st.image("n1.jpg")
            st.image("n2.jpg")
            st.caption("""
            جزیره قشم از جمله شهرهایی در استان هرمزگان است که فوتبال در آن از اهمیت ویژه و پویایی خاصی برخوردار است و طی روزهای گذشته مسابقات لیگ دسته دوم قشم با حضور 9 تیم از شهر و روستاهای این شهرستان با هیجان خاصی دنبال می‌شود.
            """)

    with col2:
        with st.expander("برد پرگل دلفین گربدان مقابل قایقسازی رمچاه", expanded=True):
            st.image("n4.jpg")
            st.caption("""
            هفته پایانی رقابتهای لیگ دو امروز در حالی آغاز شد که در تک بازی امروز دلفین گربدان توانست قایقسازی رمچاه را گلباران کند.
            """)

            st.divider()
            st.caption("""
            رقابتهای لیگ دسته دو
            هفته نهم
            شنبه 1396/10/02
            دلفین گربدان 5 - 1 قایقسازی رمچاه
            """)

    with col3:
        with st.expander("افتتاح و بهره برداری زمین چمن مصنوعی دلفین روستای گربدان قشم", expanded=True):
            st.image("n3.jpg")
            st.caption("""
            زمین چمن مصنوعی دلفین روستای گربدان قشم افتتاح و به بهره‌برداری رسید.
            """)

st.divider()
st.markdown("[طراحی شده توسط عبدالله چلاسی](http://abdollahchelasi.ir)")

st.markdown("""
<style> 
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)
