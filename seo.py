import streamlit as st
import pathlib
import logging
import shutil
from bs4 import BeautifulSoup

def modify_tag_content(tag_name, new_content, attributes=None):
    index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    logging.info(f'Editing {index_path}')
    
    try:
        soup = BeautifulSoup(index_path.read_text(), features="html.parser")
    except FileNotFoundError:
        print(f"Error: index.html not found at {index_path}")
        return
    
    target_tag = soup.find(tag_name, attrs=attributes)

    if target_tag:
        # اگر تگ هدف وجود داشته باشد
        if attributes is None:
            target_tag.string = new_content
        else:
            target_tag.attrs.update(attributes)
    else:
        # اگر تگ هدف وجود نداشته باشد، تگ جدیدی ایجاد کنید
        target_tag = soup.new_tag(tag_name, **(attributes or {}))
        target_tag.string = new_content
        if tag_name == 'meta' or tag_name == 'script' and soup.head:
            soup.head.append(target_tag)  # اضافه کردن به تگ head
    
    # ذخیره تغییرات
    bck_index = index_path.with_suffix('.bck')
    if not bck_index.exists():
        shutil.copy(index_path, bck_index)  # ایجاد بکاپ
    index_path.write_text(str(soup))  # نوشتن تغییرات در فایل

def add_favicon(icon_url):
    index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    try:
        soup = BeautifulSoup(index_path.read_text(), features="html.parser")
        
        # یافتن تگ link مربوط به favicon
        favicon_tag = soup.find("link", rel="shortcut icon")
        
        # اگر تگ favicon وجود دارد، مقدار href آن را تغییر دهید
        if favicon_tag:
            favicon_tag["href"] = icon_url
        else:
            # اگر تگ favicon وجود ندارد، آن را ایجاد و اضافه کنید
            favicon_tag = soup.new_tag("link", rel="shortcut icon", href=icon_url)
            if soup.head:
                soup.head.append(favicon_tag)

    except FileNotFoundError:
        print(f"Error: index.html not found at {index_path}")
        return

    # ذخیره تغییرات
    bck_index = index_path.with_suffix('.bck')
    if not bck_index.exists():
        shutil.copy(index_path, bck_index)  # ایجاد بکاپ
    index_path.write_text(str(soup))  # نوشتن تغییرات در فایل

# استفاده از تابع برای ویرایش تگ‌ها
modify_tag_content('title', 'باشگاه دلفین گربدان')
modify_tag_content('noscript', 'پخش زنده مسابقات فوتبال تیم دلفین گربدان و در چت آنلاین گروهی شرکت کنید و از اخبار جدید تیم مطلع شوید. باشگاه فوتبال دلفین گربدان یکی از پر افتخارترین و پر هوادارترین باشگاه‌های فوتبال در جزیره قشم است. دلفین گربدان پیش از انقلاب ستاره جنوب گربدان نام داشت. باشگاه هم اکنون در لیگ دسته دو قشم قرار گرفته و در سال 1324 در جزیره قشم روستای گربدان بنیان گذاری شده است.')

# اضافه کردن لوگو
add_favicon('https://gorbedan.liara.run/media/8bc016da4ca87099ad1a5bcc3482f41df92b4b45bf92949413951f6c.png')

# اضافه کردن متا تگ های Open Graph
modify_tag_content('meta', '', {'property': 'og:title', 'content': 'باشگاه دلفین گربدان'})
modify_tag_content('meta', '', {'property': 'og:description', 'content': 'پخش زنده مسابقات فوتبال تیم دلفین گربدان و در چت آنلاین گروهی شرکت کنید و از اخبار جدید تیم مطلع شوید. باشگاه فوتبال دلفین گربدان یکی از پر افتخارترین و پر هوادارترین باشگاه‌های فوتبال در جزیره قشم است. دلفین گربدان پیش از انقلاب ستاره جنوب گربدان نام داشت. باشگاه هم اکنون در لیگ دسته دو قشم قرار گرفته و در سال 1324 در جزیره قشم روستای گربدان بنیان گذاری شده است.'})
modify_tag_content('meta', '', {'property': 'og:image', 'content': 'https://gorbedan.liara.run/media/8bc016da4ca87099ad1a5bcc3482f41df92b4b45bf92949413951f6c.png'})
modify_tag_content('meta', '', {'property': 'og:url', 'content': 'https://gorbedan.liara.run'})

# اضافه کردن استراکچر دیتای وبسایت
modify_tag_content('script', '''
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "عبدالله چلاسی",
  "url": "https://gorbedan.liara.run",
  "logo": "https://gorbedan.liara.run/media/8bc016da4ca87099ad1a5bcc3482f41df92b4b45bf92949413951f6c.png"
}
''', {'type': 'application/ld+json'})
