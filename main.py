import streamlit as st
import whisper
import yt_dlp
import os

st.set_page_config(page_title="Miraa KW", page_icon="🎧")
st.title("📝 AI Transcribe & Study (UT Semarang Edition)")
st.write("Tempel link YouTube materi kuliahmu di bawah untuk mendapatkan teksnya.")

url = st.text_input("Link YouTube:", placeholder="https://youtube.com/...")

if st.button("Mulai Transkrip Sekarang"):
    if url:
        with st.spinner("Sedang memproses audio... Sabar ya, AI sedang bekerja."):
            # 1. Download Audio
            ydl_opts = {'format': 'bestaudio/best', 'outtmpl': 'audio.mp3'}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            # 2. AI Transcribe (Pakai model 'tiny' supaya cepat di HP)
            model = whisper.load_model("tiny")
            result = model.transcribe("audio.mp3")

            # 3. Tampilkan Hasil
            st.success("Selesai! Ini hasil transkripnya:")
            st.text_area("Hasil Teks:", result["text"], height=300)

            # 4. Tombol Simpan ke HP (TXT)
            st.download_button("Simpan ke Catatan (TXT)", result["text"])

            # Bersihkan file sampah
            os.remove("audio.mp3")
    else:
        st.warning("Masukkan link videonya dulu dong!")
