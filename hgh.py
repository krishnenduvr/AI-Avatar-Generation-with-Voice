import streamlit as st
from py_avataaars import PyAvataaar
from gtts import gTTS
import tempfile
import time
from py_avataaars import (AvatarStyle, TopType, HairColor, ClotheGraphicType, EyesType, EyebrowType, SkinColor, MouthType, NoseType,ClotheType)
def zara_avatar(mouth,talking_star):
    avatar = PyAvataaar(
        style=AvatarStyle.CIRCLE,
        top_type=TopType.LONG_HAIR_STRAIGHT,
        hair_color=HairColor.BLACK,
        clothe_graphic_type=ClotheGraphicType.DIAMOND,
        eye_type=EyesType.DEFAULT,
        eyebrow_type=EyebrowType.DEFAULT_NATURAL,
        skin_color=SkinColor.LIGHT,
        mouth_type=mouth,
        nose_type=NoseType.DEFAULT,
        clothe_type=ClotheType.SHIRT_V_NECK)
    avatar.render_png_file(talking_star)
zara_avatar(MouthType.SMILE, "zara_closed")
zara_avatar(MouthType.SERIOUS, "zara_mid")
zara_avatar(MouthType.EATING, "zara_open")
st.title('* welcome to my avatar *')
st.header("zara")
def text_to_speech(text):
    a=gTTS(text)
    b=tempfile.NamedTemporaryFile(delete=False)
    a.save(b.name)
    return b.name
c=st.text_input("Enter your text:")
if st.button('her voice'):
    d=text_to_speech(c)
    st.audio(d,format='mp3')
f=st.empty()
e=['zara_closed','zara_mid','zara_open','zara_mid']
g =len(c.split())*0.4
h=time.time()
while time.time()-h<g:
    for k in e:
        f.image(k,width=400)
        time.sleep(0.1)
else:
     st.warning("Please enter some text first.")






