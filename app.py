import streamlit as st
from services.transcription import transcribe_audio

st.set_page_config(page_title="Voice Notes", page_icon="🎤")
st.title("🎤 Voice Notes + Action Items")
st.write("Upload or record a voice note to transcribe (100% FREE!)")

col1, col2 = st.columns(2)
with col1:
    uploaded_file = st.file_uploader("Upload audio", type=["mp3", "wav", "m4a", "ogg"])
with col2:
    recorded_audio = st.audio_input("Or record a voice note")

audio_file = uploaded_file or recorded_audio

if audio_file:
    st.audio(audio_file)
    if st.button("Transcribe", key="transcribe_btn"):
        with st.spinner("Transcribing..."):
            try:
                transcript = transcribe_audio(audio_file)
                st.success("✅ Transcription complete!")
                st.subheader("📝 Transcript")
                st.write(transcript)
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")