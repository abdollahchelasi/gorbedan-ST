import streamlit as st
from streamlit_option_menu import option_menu
from jdatetime import datetime
import sqlite3




st.set_page_config(
        page_title="باشگاه دلفین گربدان",
        page_icon="logo.png",
        initial_sidebar_state='collapsed',
        layout='wide',
    )


con=sqlite3.connect('sql.db')
cur=con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS pics(id TEXT, img BLOB, note TEXT)')

with open("c.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)

# st.snow()
# st.image("logo.png")


now = datetime.now()
tim = now.strftime("%Y/%m/%d")

# col1,col2 = st.columns(2)

# with col1:



with st.sidebar:
   menu_id = option_menu (
      menu_title=None,
      options=[ "صفحه اصلی","خبرها" , "ویدیوها", "بازیکنان"],
      icons=["house"],
      menu_icon="cast",
      default_index=0,
      orientation="vertical",

      styles={
        "container" : {"background-color" : "#de7f1b", "border-radius" : "10px",},
        "icon" : {"color": "#ffffff"},
        "nav-link" : {"color" : "#ffffff", "--hover-color" : "#49B618", "border-radius" : "5px"},
        "nav-link-selected" : {"background-color" : "#009200", "border-radius" : "px"},
        }
    )





st.subheader("باشگاه فرهنگی ورزشی دلفین گربدان")
st.image("logo.png",width=100)


if menu_id == "بازیکنان":
   
   st.divider()

   c1 , c2 , c3 , c4 = st.columns([3,2,2,1])

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
      st.image('i29.jpg')
      st.image('i30.jpg')

   with c2:
      st.image('i14.jpg')
      st.image('i15.jpg')
      st.image('i16.jpg')
      st.image('i17.jpg')
      st.image('i18.jpg')
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
      

   with c3:
      st.image('i31.jpg')
      st.image('i32.jpg')
      st.image('i33.jpg')
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
  
  selected = option_menu (
      menu_title=None,
      options=[ "تیمچت" ,"ادمین", "صفحه اصلی"],
      icons=["phone","key","house" ],
      menu_icon="cast",
      default_index=2,
      orientation="horizontal",

      styles={
         "container": {"background-color": "#de7f1b"},
         "nav-link-selected": {"background-color": "#040b3e"},
         "nav-link": {"font-size": "20px", "text-align": "center_y: 0.0", "margin":"0px", "--hover-color": "#afb8fb"},

        }
    )












  if selected == "ادمین":
     username = st.text_input(label="نام کاربری", placeholder="Username")
     password = st.text_input(label="پسورد", placeholder="password", type="password")
     b = st.button("ورود")

     if username == "a" and password == "ch":
        st.success("خوش آمدی ادمین")

        st.success(
        "توجه : لطفا با اضافه کردن محصول محصولات خود رو کامل پر کنید (عکس محصول , کد محصول , نام محصول) این ها نباید خالی باشد"
    )
        st.error(
        "هشدار : کد و نام محصولات شما نباید مثل محصولات دیگه ای که اضافه میکنید باشد. کد محصولات رو با اعداد انگلیسی و از شماره بالا به پایین شروع کنید . مانند : ( از 999 شروع کنید به پایین) "
    )

        if st.button("اضافه کردن محصول"):
          cur.execute("INSERT INTO pics(id, img, note) VALUES(?,?,?)", ("", "", ""))
          con.commit()

        st.write("---")

        for row in cur.execute("SELECT rowid, id, img, note FROM pics ORDER BY id"):
          with st.form(f"ID-{row[0]}", clear_on_submit=True):

            imgcol, notecol = st.columns([3, 2])
            id = notecol.text_input("کد محصول", row[1])
            note = notecol.text_area("نام محصول", row[3])
            if row[2]:
                
                img = row[2]
                imgcol.image(row[2])
            file = imgcol.file_uploader("تصاویر", ["png", "jpg", "gif", "jpeg", "bmp"])
            if file:
                img = file.read()
            if notecol.form_submit_button("ذخیره محصول"):
                try:
                   
                  cur.execute(
                    "UPDATE pics SET id=?, img=?, note=? WHERE id=?;",
                    (id, img, note, str(row[1])),
                )

                  con.commit()
                  st.experimental_rerun()

                except:
                   st.error("لطفا کامل پر کنید")

            if notecol.form_submit_button("حذف محصول"):
                cur.execute(f"""DELETE FROM pics WHERE rowid="{row[0]}";""")
                con.commit()
                st.experimental_rerun()

     elif username or password == "admin":
        st.error("لطفا درست وارد کنید")
  
  














  if selected == "تیمچت":

    
    st.warning("توجه : برای مشاهده پیام های دیگران به صفحه دیگری بروید و دوباره به صفحه تیمچت بیایید .")

    with st.expander("تیمچت", expanded=True):
      
    #   st.image('g2.png')

        conn = sqlite3.connect('chat.db')
        c = conn.cursor()

        # ایجاد جدول پیام‌ها اگر وجود نداشته باشد
        c.execute('''CREATE TABLE IF NOT EXISTS messages
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    message TEXT,
                    timestamp DATETIME)''')
        conn.commit()

        # تابع افزودن پیام جدید
        def add_message(username, message):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            c.execute("INSERT INTO messages (username, message, timestamp) VALUES (?, ?, ?)",
                      (username, message, timestamp))
            conn.commit()

        # تابع دریافت تمام پیام‌ها
        def get_messages():
            c.execute("SELECT id, username, message, timestamp FROM messages ORDER BY timestamp DESC LIMIT 100")
            return c.fetchall()

        # تابع حذف پیام
        def delete_message(message_id):
            c.execute("DELETE FROM messages WHERE id = ?", (message_id,))
            conn.commit()

        # ورود نام کاربری
        
           
        username = st.text_input(": نام خود را وارد کنید")

        # نمایش پیام‌های موجود
        messages = get_messages()
        new_message = st.text_input(": پیام خود را وارد کنید")
        ersal = st.button("ارسال") 
        
        # ورودی پیام جدید
        if ersal and username and new_message :
           
           add_message(username, new_message)
           st.rerun()
        
        elif ersal and username and new_message == "":
            # add_message(username, new_message)
            st.error("لطفا پیام‌ خو بنویس" )

        elif ersal and new_message and username == "":
            # add_message(username, new_message)
            st.error("لطفا اسم خو بنویس")


        


        st.subheader("⬇️ تیمچت ⬇️")
        st.divider()

        for msg in messages:  # بدون معکوس کردن لیست پیام‌ها
            msg_id, msg_user, msg_text, msg_timestamp = msg
            st.success(f"{msg_timestamp} 🙋🏽‍♂️ {msg_user}: 💬 {msg_text}")
            
            # افزودن دکمه برای حذف پیام
            if st.button("حذف", key=f"delete_{msg_id}"):
                delete_message(msg_id)
                st.rerun()

        # بستن اتصال به پایگاه داده
        conn.close()








  


  # st.divider()
  elif selected == "صفحه اصلی":

    

    st.write("تاریخ امروز :", tim)

    with st.expander("تیم دلفین گربدان", expanded=True):
      st.image("passdolfin.jpg")
    
      st.caption("""
    باشگاه فوتبال دلفین گربدان یکی از پر افتخارترین و پر هوادارترین باشگاه های فوتبال در جزیره قشم است دلفین گربدان پیش از انقلاب ستاره جنوب گربدان نام داشت باشگاه هم اکنون در لیگ دسته دو قشم قرار گرفته , دلفین گربدان در سال 1324 در جزیره قشم روستای گربدان بنیان گذاری شده است

    """)
      
    for row in cur.execute('SELECT rowid, id, img, note FROM pics ORDER BY id'):
    # with st.form(f'ID-{row[0]}', clear_on_submit=True):
        st.write("---")
        imgcol, notecol = st.columns([3, 2])
    # id=notecol.text_input('id', row[1])
        id=notecol.text_input('کد محصول', row[1])
        note=notecol.text_area('اسم محصول', row[3])

        
        if row[2]:
            img=row[2]
            imgcol.image(row[2])
            # st.markdown(f"[باز کردن نمونه کار]()")







if menu_id == "ویدیوها":

  st.divider()
  c1 , c2  = st.columns(2)


  with c1:
      st.video("d1.mp4")
      st.video("d2.mp4")
  with c2:
      st.video("d3.mp4")
      st.video("d5.mp4")
      st.video("d6.mp4")










if menu_id == "خبرها":

  st.divider()

  col1 , col2 ,col3 = st.columns(3)

  with col1:
     with st.expander("""
همه نگاه‌ها به دلفین گربدان, لیگ 2 در اوج حساسیت
""", expanded=True):
        
        st.image("n1.jpg")
        st.image("n2.jpg")
        st.caption(
              """
جزیره قشم از جمله شهرهایی در استان هرمزگان است که فوتبال در آن از اهمیت ویژه و پویایی خاصی برخوردار است و طی روزهای گذشته مسابقات لیگ دسته دوم قشم با حضور 9 تیم از شهر و روستاهای این شهرستان با هیجان خاصی دنبال می‌شود.

به گزارش خبرگزاری گربدان از قشم، جزیره قشم از جمله شهرهایی در استان هرمزگان است که فوتبال در آن از اهمیت ویژه و پویایی خاصی برخوردار است، کما اینکه از اول سال جاری و در ماه‌های اخیر طبق تقویم سالیانه به صورت مستمر تمام مسابقات از جمله بازی‌های رده سنی زیر 10 سال، زیر 12 سال، زیر 14 سال، نوجوانان و رده سنی جوانان برگزار شده و در حال حاضر طی روزهای گذشته مسابقات لیگ دسته دوم قشم با حضور 9 تیم از شهر و روستاهای این شهرستان با هیجان خاصی دنبال می‌شود. در اتفاقی جالب در این دوره از مسابقات تیم دولفین روستای گربدان با مدیرعاملی مصطفی زارعی که برای نخستین بار در مسابقات رسمی پا به عرصه فوتبال گذاشته این تیم برابر قرعه، هفته اول را به استراحت پرداخت. اما در دیگر بازی‌ها در هفته اول این مسابقات تیم پاس قشم با نتیجه یک بر صفر تیم پیروزی قشم را شکست داد، مهتشان بندر لافت با نتیجه چهار بر دو از سد تیم عقاب قشم گذشت، والفجر با نتیجه چهار بر یک استقلال قشم را شکست داد و پریما اسپرت با 6 گل وحدت گیاهدان را گلباران کرد. اما در هفته دوم لیگ دسته دو قشم تیم دولفین روستای گربدان اولین بازی رسمی خود را به مصاف تیم عقاب قشم رفت و علی رغم شایستگی بازیکنان این تیم به دلیل بی‌تجربگی سه امتیاز این دیدار را به حریف قشمی خود واگذار کرد. در دیگر بازی‌های هفته دوم با انجام چهار بازی در این مسابقات دو تیم همشهری پاس و استقلال قشم به مصاف یکدیگر رفتند و استقلال توانست با نتیجه سه بر صفر از سد آبی‌پوشان بگذرد، مهتشان بندرلافت با نتیجه پنج بر دو وحدت گیاهدان را در هم کوبید، والفجر و پریما اسپرت نیز با تساوی دو بر دو رضایت دادند. در هفته سوم این بازی ها تیم پیروزی قشم که در هفته اول شکست خورده بود در مصاف با استقلال این شهر با نتیجه یک بر صفر پیروز شد. اما در دومین روز از هفته سوم این لیگ تیم دولفین روستای گربدان که با ترکیب یعقوب محمدی، اسماعیل صالحی پور، یعقوب نیکخواه، حیدر فجر، حسن زارعی، یحیی شادان، ماجد کوهی‌نژاد، فرشاد خاکی، امید زارعی، فرهاد زارعی و صلاح الدین‌نیکخواه در مصاف با تیم وحدت گیاهدان پا به مستطیل سبز گذاشت، توانست با حریف قدر خود با اتحاد و انسجام با گل های یعقوب محمدی ،حیدر فجر و امیر کاروان با نتیجه پرگل سه بر صفر اولین برد و سه امتیاز خود را در مسابقات رسمی ثبت و با انگیزه و امید به دیگر بازی‌ها نیم نگاهی به معتبرترین لیگ قشم مسابقات لیگ دسته اول قشم داشته باشد.

دیگر بازیکنان این تیم عبدالقادر مقدسی، معین‌فروزنده، امیر کاروان، لقمان‌زارعی، عبدالله نیکخواه، ولید فروزان، مسعود خوه،خلیل شادمان و محمد زارعی به مربیگری عادل‌نیکخواه و سرمربیگری محمد متوسل بودند. قضاوت این دیدار برعهده فرزاد شیرمردی ،امین زارعی و امیر همتی بود. در حال حاضر تیم‌های مهتشان بندر لافت و پاس فجر قشم با شش امتیاز به ترتیب در مکان اول و دوم، پریما اسپرت و والفجر قشم با چهار امتیاز در مکان سوم و چهارم، تیم های عقاب و دولفین گربدان با سه امتیاز در مکان پنجم و ششم و تیم پیروزی قشم با سه امتیاز در مکان هفتم وتیم های استقلال و وحدت گیاهدان نیز بدون امتیاز در مکان های هشتم و نهم جدول قرار دارند.
به گزارش خبرگذاری گربدان از قشم، روستای گربدان از توابع بخش مرکزی با جمعیتی بالغ بر یک‌هزار و 100 نفر در فاصله 45 کیلومتری شهر قشم واقع شده است.



              """
            )


  with col2:
     with st.expander("""
برد پرگل دلفین گربدان مقابل قایقسازی رمچاه
""", expanded=True):
        
        st.image("n4.jpg")
        st.caption(
              """
هفته پایانی رقابتهای لیگ دو امروز در حالی آغاز شد که در تک بازی امروز دلفین گربدان توانست قایقسازی رمچاه را گلباران کند. در این دیدار که برای دو تیم کاملأ تشریفاتی بود، دلفین گربدان توانست با گلهای یعقوب محمدی با نتیجه 5 بر 1 از سد قایقسازی رمچاه بگذرد تا با 11 امتیاز به کار خود در این فصل پایان دهد. از سویی قایقسازی رمچاه نیز که در این فصل موفق نشده بود امتیازی کسب کند در این دیدار هم تن به شکست داد تا با نه شکست متوالی بدترین رکورد ممکن را از آن خود کند.یعقوب محمدی با بثمر رساندن پنج گل برای دلفین گربدان توانست به تنهایی 10 گل زده در صدر جدول گلزنان قرار بگیرد و تک گل قایقسازی رمچاه را نیز حسام اسلامی وارد دروازه دلفین گربدان کرد.


              """
            )
        st.divider()
        st.caption("""
  رقابتهای لیگ دسته دو

هفته نهم

شنبه 1396/10/02

دلفین گربدان 5 - 1 قایقسازی رمچاه


""")



  with col3:
     with st.expander("""
افتتاح و بهره برداری زمین چمن مصنوعی دلفین روستای گربدان قشم
""", expanded=True):
        st.image("n3.jpg")
        
        st.caption(
              """
زمین چمن مصنوعی دلفین روستای گربدان قشم افتتاح و به بهربرداری رسید. با حضور دکتر تقی زاده معاون حقوقی، مجلس و امور استان های وزارت ورزش و جوانان،دکترمرادی نماینده مردم استان در مجلس شورای اسلامی، امیاری مدیرکل ورزش و جوانان هرمزگان و جمعی از مسوولین محلی زمین چمن مصنوعی دلفین روستای گربدان قشم افتتاح شد. شایان گفتن است ، زمین چمن مصنوعی محله ای روستای گربدان بخش مرکزی شهرستان قشم با اعتباری بالغ بر ۶۰۰ میلیون تومان و متراژ ۹۲۴ متر مربع از محل اعتبارات استانی و در سال ۹۹ شروع و در ۲۳ خرداد۱۴۰۰ مورد بهره برداری و دراختیار مردم روستای گربدان قشم قرارگرفت.



              """
            )
   












st.markdown("""
<style> 
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""",unsafe_allow_html=True)
