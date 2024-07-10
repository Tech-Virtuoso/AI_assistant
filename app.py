import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech

# Custom CSS for styling
st.markdown(
    """
    <style>
    .title {
        font-size: 2.5em;
        font-weight: bold;
        text-align: left;
        color: #4CAF50;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.markdown('<p class="title"> AI Assistant 🌐</p>', unsafe_allow_html=True)

    
    if st.button("Ask me anything!"):
        with st.spinner("Listening..."):
            text = voice_input()
            response = llm_model_object(text)
            text_to_speech(response)

            # Display audio player and download link
            audio_file = open("speech.mp3", 'rb')
            audio_bytes = audio_file.read()
            
            st.text_area(label="Response:", value=response, height=350)
            st.audio(audio_bytes, format='audio/mp3')
            st.download_button(label="Download Speech",
                               data=audio_bytes,
                               file_name="speech.mp3",
                               mime="audio/mp3")
    else:
        st.markdown('</div>', unsafe_allow_html=True)  # Close the div if the button is not clicked

if __name__ == "__main__":
    main()

