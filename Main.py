import streamlit as st


st.set_page_config(
    page_title='Upload once',
    layout='wide'
)

st.markdown('# Upload once')
st.markdown("Have a slow internet connection? 🐌 Don't worry! You only need to upload your video once, and we'll dispatch it wherever you want 🥳")
st.markdown("""---""")

cols = st.columns(3, gap='large')

with cols[0]:
    st.markdown('### Step 1: create a post')
    with st.form('video_form'):
        title = st.text_input('Title')
        description = st.text_area('Description')
        ai_generated = st.checkbox('The video was AI generated')
        video_file = st.file_uploader('Video file', type=['mp4'])
        st.form_submit_button()

with cols[1]:
    st.markdown('### Step 2: preview your video')
    if video_file:
        st.write(title)
        st.video(video_file)
        st.write(description)
        if ai_generated:
            st.info("You have marked the video as AI generated.")

    else:
        st.info("Finish step 1 and you'll see your video here.")

with cols[2]:
    st.markdown('### Step 3: upload it')

    social_medias = ['TikTok', 'Instagram', 'YouTube', 'Reddit']
    tabs = st.tabs(social_medias)

    for social_media, tab in zip(social_medias, tabs):
        with tab:
            if video_file:
                st.error(f'Pending API access from {social_media}. Hang on tight! We should be right back in a couple days!')
            else:
                st.info("Finish step 1 and you'll be able to publish it next.")
