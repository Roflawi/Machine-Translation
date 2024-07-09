import streamlit as st
from translate import Translator

# Function to translate text
def translate(text, src_lang, tgt_lang):
    try:
        translator = Translator(from_lang=src_lang, to_lang=tgt_lang)
        translated = translator.translate(text)
        return translated
    except Exception as e:
        return f'Error: {e}'

# Streamlit UI
st.title('Word translator with Streamlit')

st.write("Translate words using the Translator library.")

# Bahasa yang didukung
lang_dict = {'Indonesia': 'id', 'English': 'en', 'Melayu': 'ms'}
lang_keys = list(lang_dict.keys())

# Pilihan bahasa sumber dan target
src_lang = st.selectbox('Translate from', lang_keys)
tgt_lang = st.selectbox('Translate to', lang_keys)

# Input kata
word = st.text_input('Enter text')
st.text('Max 500 characters.')

# Tombol terjemahkan
if st.button('Translate'):
    if word:
        translation = translate(word, lang_dict[src_lang], lang_dict[tgt_lang])
        # st.write(f'Terjemahan: {translation}')
        st.success(f'Terjemahan: {translation}')
        st.write(f"You wrote {len(translation)} characters.")
    else:
        # st.write('Silakan masukkan kata untuk diterjemahkan.')
        st.success('Enter text.')

