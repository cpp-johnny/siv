# to run on localhost type `python -m streamlit run app.py`
# take note that you need to be in the correct directory
# to update on production type 
# `git  add .`
# `git commit -m "enter message"`
# `git push -u origin master`
from PIL import Image, ImageDraw      # pip install Pillow
import streamlit as st      # pip install streamlit
import requests
import streamlit as st
from streamlit_lottie import st_lottie      # pip instal streamlit-lottie
import io
import base64

st.set_page_config(page_title="Project Cognition", page_icon="🫧", layout="wide")


# Custom CSS to change the font
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');

body {
    font-family: 'Inter', sans-serif; /* Change the font family here */
}
</style>
"""

# Display the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Using local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# Load Asset using Lottie
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_rdss = Image.open("images/rdss.png")

# Function to crop image into circle
def crop_to_circle(image):
    width, height = image.size
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, width, height), fill=255)
    result = Image.new("RGBA", (width, height))
    result.paste(image, (0, 0), mask)
    return result

# Load the images for members
member_images = [
    Image.open("images/c.jpeg"),
    Image.open("images/j.jpeg"),
    Image.open("images/b.jpeg"),
    Image.open("images/s.jpeg"),
    Image.open("images/f.jpg")
]

# Crop images to circles
member_images_circles = [crop_to_circle(img) for img in member_images]

# Convert images to bytes
member_images_bytes = []
for img in member_images:
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    member_images_bytes.append(img_bytes.getvalue())

# Define member names and role
member_names = [
    {"name": "Clark", "role": "Project Coordinator ⚙️"},
    {"name": "Johnson", "role": "Progammer 👨‍💻"},
    {"name": "Bangyu", "role": "Merch Design 🔥"},
    {"name": "Song Bo", "role": "Secretary ⚡️"},
    {"name": "Feiyang  ", "role": "Treasurer 💵"}
]
img_bytes = io.BytesIO()
img_rdss.save(img_bytes, format='PNG')
img_str = base64.b64encode(img_bytes.getvalue()).decode()

# Function to crop image into circle
def crop_to_circle(image):
    width, height = image.size
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, width, height), fill=255)
    result = Image.new("RGBA", (width, height))
    result.paste(image, (0, 0), mask)
    return result

# Load the images for products
product_images = [
    Image.open("images/keychain.jpg"),
    Image.open("images/pin.jpg"),
    Image.open("images/plushie.jpg"),
    Image.open("images/accessories.jpg"),
    Image.open("images/socks.jpg"),
    Image.open("images/fan.jpg"),
    Image.open("images/sticker.jpg")
]

# Define product names and prices
product_info = [
    {"name": "Keychains", "price": "$2.50"},
    {"name": "Enamel Pins", "price": "$4.50 - 9"},
    {"name": "Plushie", "price": "$10 - 20"},
    {"name": "Table Accessories", "price": "$0.50-3"},
    {"name": "Socks", "price": "$8"},
    {"name": "Fans", "price": "$4"},
    {"name": "Stickers", "price": "$5"}
]

# link to product price pdf or something on google dribe idk
product_link = "https://drive.google.com/file/d/16YTpfqXpXwK0K7DTLAtuv9pieFL_m3sG/view?usp=sharing"  # Set the link for all products

# Top
with st.container(): 
    left_column, right_column = st.columns(2)  
    with left_column:   
        st.title("Project Cognition")
        st.write("A student initiated VIA :heart:")
    with right_column:
        st_lottie(lottie_coding, height=100, key="coding") 

# why are we doinf tis and our benficary
with st.container():
    st.write("---")  # this is a line break
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("<h1 style='text-align: center;'>Why are we doing this?</h1>", unsafe_allow_html=True)
        st.markdown("<p1 style='text-align: center;'>People with rare diseases face many problems, from lack of awareness of the rare disease to lack of funding to support the costly medical fee. Due to lack of support and poor understanding of the issue, many of these patients face lack of support and get left out. About 0.4% of Singaporeans have rare diseases, and there are many that still do not receive help. Out of the 2000/3000 Singaporeans that have rare diseases, only 9 have received help from the Rare Disease Fund (RDF) since 2019. As such, more work needs to be done to ensure those patients live quality lives. We believe that everyone should have a fighting chance, and this SIV aims to raise awareness and funds to support them. </p1>", unsafe_allow_html=True)
    with right_column:
        st.markdown("<h1 style='text-align: center;'>Our beneficiary</h1>", unsafe_allow_html=True)
        st.markdown(f'<a href="https://www.rdss.org.sg/"><img src="data:image/png;base64,{img_str}" width="100%"></a>', unsafe_allow_html=True)

# Our Members section
with st.container():
    st.write("---")
    st.markdown("<h1 style='text-align: center;'>Our Members</h1>", unsafe_allow_html=True)

    # Display images, names, and roles of members
    col1, col2, col3, col4, col5 = st.columns(5)
    for i, col in enumerate([col1, col2, col3, col4, col5]):
        col.image(member_images_bytes[i], use_column_width='always', output_format='PNG')
        col.markdown(f"<p style='text-align: center; font-size: larger; font-weight: bold;'>{member_names[i]['name']}</p>", unsafe_allow_html=True)
        col.markdown(f"<p style='text-align: center;'> {member_names[i]['role']}</p>", unsafe_allow_html=True)  # Display role here

# Our Products section
with st.container():    
    # Our Products section
    st.write("---")
    st.markdown("<h1 style='text-align: center;'>Our Products</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Check out the <a href='https://drive.google.com/file/d/16YTpfqXpXwK0K7DTLAtuv9pieFL_m3sG/view?usp=sharing'>catalogue</a> for more in-depth details!</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'>note: these are not all the products available, please check out the catalogue for more items :)</div>", unsafe_allow_html=True)
    st.write("")
    st.write("")

    # Display images, names, and prices of products
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    for i, col in enumerate([col1, col2, col3, col4, col5, col6, col7]):
        col.image(product_images[i], use_column_width='always', output_format='PNG')
        col.markdown(f"<p style='text-align: center;'>{product_info[i]['name']}</p>", unsafe_allow_html=True)
        col.markdown(f"<p style='text-align: center;'><a href='{product_link}' target='_blank'>Price: {product_info[i]['price']}</a></p>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    st.markdown("<div style='text-align: center;'>To purchase, please visit <a href='https://docs.google.com/forms/d/e/1FAIpQLSeK7s6_n-zulZAszlklLkfx44Gz8NPMpZKL51I5_ezVLwNdvA/viewform?usp=sf_link'>this Google Form</a>.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'>Thank you for your support! 🙏🙏🙏 All funds collected will go to RDSS</div>", unsafe_allow_html=True)

# Contact area
with st.container():
    st.write("---")
    st.header("contact us! :grin:")

    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/estreller.rianclark.angeles@dhs.edu.sg " method="POST">
        <input type="hidden" name="_captcha" value="true">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">', unsafe_allow_html=True)

# Instagram link
INSTAGRAM_LINK = "https://www.instagram.com/sivprojectcognition?igsh=MTN3am45NHRxdjJ0MQ=="

# Custom CSS for styling
custom_css = """
<style>
.instagram-link {
    font-size: 18px;
    color: #405DE6;
    text-decoration: none;
    font-weight: bold;
}

.instagram-link:hover {
    color: #5865F2;
}
</style>
"""

# Display the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Include Font Awesome CSS
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">', unsafe_allow_html=True)

# Social section
st.write("---")
st.header("Social")

# Display Instagram link with custom CSS and icon
st.markdown(f"<a href='{INSTAGRAM_LINK}' class='instagram-link' target='_blank'><i class='fa fa-instagram'></i> Follow us on Instagram!</a>", unsafe_allow_html=True)


# GitHub link
GITHUB_LINK = "https://github.com/cpp-johnny/siv"

# Custom CSS for styling
github_css = """
<style>
.github-link {
    font-size: 18px;
    color: #24292e; /* GitHub's default link color */
    text-decoration: none;
    font-weight: bold;
}

.github-link:hover {
    color: #0366d6; /* GitHub's default hover color */
}
</style>
"""

# Display the custom CSS for GitHub
st.markdown(github_css, unsafe_allow_html=True)


# Display GitHub link with custom CSS and icon
st.markdown(f"<a href='{GITHUB_LINK}' class='github-link' target='_blank'><i class='fa fa-github'></i> Check out the source code on GitHub!</a>", unsafe_allow_html=True)
