import streamlit as st
import pickle
from helper import recommend, fetch_poster, fetch_movie_details, fetch_profile_poster

movies = pickle.load(open('movies.pkl','rb'))
movies_list = movies['title'].values

st.title("Movie Recommendation System")

# Select your movie name to get recommendation.
selected_movie_name = st.selectbox( "Write the Name of Movie for Recommendation : ", movies_list)

if selected_movie_name:
    col1,col2 = st.columns(2)

    with col1 :
        movie_id = movies[movies['title'] == selected_movie_name].iloc[0].movie_id
        selected_movie_poster = fetch_poster(movie_id)

        st.write("You selected :", selected_movie_name)
        st.image(selected_movie_poster, use_container_width=True)

    with col2:
        movie_id = movies[movies['title'] == selected_movie_name].iloc[0].movie_id
        selected_movie_info = fetch_movie_details(movie_id)

        # Extracting details properly
        language, release_date, runtime, budget, revenue, tagline, rating, vote_count, overview = selected_movie_info

        # Displaying formatted output
        st.write("### Movie Details : ")
        st.write(f"📅 Release Date : {release_date}")
        st.write(f"⏳ Runtime : {runtime} minutes")
        st.write(f"🗣️ Language : {language}")
        st.write(f"💰 Budget : ${budget:,}")
        st.write(f"💵 Revenue : ${revenue:,}")
        st.write(f"⭐ Rating : {rating}/10  |  👥 Votes : {vote_count:,}")

        if tagline:
            st.write(f"🎬 Tagline : {tagline}")

        st.write("📖 Overview : ")
        st.markdown(overview)

# movie_id = movies[movies['title'] == selected_movie_name].iloc[0].movie_id
# cast_list = fetch_profile_poster(movie_id)
# for profile_poster, name, character in cast_list:
#     st.image(profile_poster, use_container_width=True)
#     st.write("Name:", name)
#     st.write("Character:", character)

if st.button("Show Star Cast",key = "show_star_cast_1"):
    movie_id = movies[movies['title'] == selected_movie_name].iloc[0].movie_id
    cast_list = fetch_profile_poster(movie_id)
# First Row (5)
    cols1 = st.columns(5)
    for i in range(5):
        with cols1[i]:
            st.image(cast_list[i][0], use_container_width=True)
            st.markdown(f"**{cast_list[i][1]}**")
            st.caption(cast_list[i][2])

    # Second Row (next 5)
    cols2 = st.columns(5)
    for i in range(5, 10):
        with cols2[i - 5]:
            st.image(cast_list[i][0], use_container_width=True)
            st.markdown(f"**{cast_list[i][1]}**")
            st.caption(cast_list[i][2])


st.sidebar.title("Click on the button to get recommended movies : ")

# if st.sidebar.button('Recommendation'):
#     recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
#
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.text(recommended_movie_names[0])
#         st.image(recommended_movie_posters[0])
#     with col2:
#         st.text(recommended_movie_names[1])
#         st.image(recommended_movie_posters[1])
#
#     with col3:
#         st.text(recommended_movie_names[2])
#         st.image(recommended_movie_posters[2])
#     with col4:
#         st.text(recommended_movie_names[3])
#         st.image(recommended_movie_posters[3])
#     with col5:
#         st.text(recommended_movie_names[4])
#         st.image(recommended_movie_posters[4])
#
#
#
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.text(recommended_movie_names[5])
#         st.image(recommended_movie_posters[5])
#     with col2:
#         st.text(recommended_movie_names[6])
#         st.image(recommended_movie_posters[6])
#
#     with col3:
#         st.text(recommended_movie_names[7])
#         st.image(recommended_movie_posters[7])
#     with col4:
#         st.text(recommended_movie_names[8])
#         st.image(recommended_movie_posters[8])
#     with col5:
#         st.text(recommended_movie_names[9])
#         st.image(recommended_movie_posters[9])


if st.sidebar.button("Recommendation"):
    st.title("These are the Top 10 Recommended Movies")
    names, posters = recommend(selected_movie_name)
    st.session_state["recommended_names"] = names
    st.session_state["recommended_posters"] = posters

if "recommended_names" in st.session_state and "recommended_posters" in st.session_state:
    names = st.session_state["recommended_names"]
    posters = st.session_state["recommended_posters"]


    # It's working well but understand this code first.
    # for row in range(2):  # 2 rows
    #     cols = st.columns(5)  # 5 columns in each row
    #     for i in range(5):
    #         index = row * 5 + i
    #         if index < len(names):
    #             with cols[i]:
    #                 if st.button("Select", key=f"btn{index + 1}"):
    #                     st.session_state["selected_movie"] = names[index]
    #                 st.image(posters[index], use_container_width=True)
    #                 st.write(f"**{names[index]}**")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("Select", key="btn1"):
            st.session_state["selected_movie"] = names[0]
        st.image(posters[0], use_container_width=True)
        st.write(f"**{names[0]}**")

    with col2:
        if st.button("Select", key="btn2"):
            st.session_state["selected_movie"] = names[1]
        st.image(posters[1], use_container_width=True)
        st.write(f"**{names[1]}**")

    with col3:
        if st.button("Select", key="btn3"):
            st.session_state["selected_movie"] = names[2]
        st.image(posters[2], use_container_width=True)
        st.write(f"**{names[2]}**")

    with col4:
        if st.button("Select", key="btn4"):
            st.session_state["selected_movie"] = names[3]
        st.image(posters[3], use_container_width=True)
        st.write(f"**{names[3]}**")

    with col5:
        if st.button("Select", key="btn5"):
            st.session_state["selected_movie"] = names[4]
        st.image(posters[4], use_container_width=True)
        st.write(f"**{names[4]}**")


    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("Select", key="btn6"):
            st.session_state["selected_movie"] = names[5]
        st.image(posters[5], use_container_width=True)
        st.write(f"**{names[5]}**")

    with col2:
        if st.button("Select", key="btn7"):
            st.session_state["selected_movie"] = names[6]
        st.image(posters[6], use_container_width=True)
        st.write(f"**{names[6]}**")

    with col3:
        if st.button("Select", key="btn8"):
            st.session_state["selected_movie"] = names[7]
        st.image(posters[7], use_container_width=True)
        st.write(f"**{names[7]}**")

    with col4:
        if st.button("Select", key="btn9"):
            st.session_state["selected_movie"] = names[8]
        st.image(posters[8], use_container_width=True)
        st.write(f"**{names[8]}**")

    with col5:
        if st.button("Select", key="btn10"):
            st.session_state["selected_movie"] = names[9]
        st.image(posters[9], use_container_width=True)
        st.write(f"**{names[9]}**")


if "selected_movie" in st.session_state:
    selected = st.session_state["selected_movie"]
    movie_id = movies[movies['title'] == selected].iloc[0].movie_id
    poster = fetch_poster(movie_id)
    details = fetch_movie_details(movie_id)

    st.subheader(f"You selected: {selected}")

    col1, col2 = st.columns(2)
    with col1:
        st.image(poster)

    with col2:
        movie_id = movies[movies['title'] == selected].iloc[0].movie_id
        selected_movie_info = fetch_movie_details(movie_id)

        # Extracting details properly
        language, release_date, runtime, budget, revenue, tagline, rating, vote_count, overview = selected_movie_info

        # Displaying formatted output
        st.write("### Movie Details : ")
        st.write(f"📅 Release Date : {release_date}")
        st.write(f"⏳ Runtime : {runtime} minutes")
        st.write(f"🗣️ Language : {language}")
        st.write(f"💰 Budget : ${budget:,}")
        st.write(f"💵 Revenue : ${revenue:,}")
        st.write(f"⭐ Rating : {rating}/10  |  👥 Votes : {vote_count:,}")

        if tagline:
            st.write(f"🎬 Tagline : {tagline}")

        st.write("📖 Overview : ")
        st.markdown(overview)

    if st.button("Show Star Cast", key = "show_star_cast_2"):
        movie_id = movies[movies['title'] == st.session_state["selected_movie"]].iloc[0].movie_id
        cast_list = fetch_profile_poster(movie_id)
        # First Row (5)
        cols1 = st.columns(5)
        for i in range(5):
            with cols1[i]:
                st.image(cast_list[i][0], use_container_width=True)
                st.markdown(f"**{cast_list[i][1]}**")
                st.caption(cast_list[i][2])

        # Second Row (next 5)
        cols2 = st.columns(5)
        for i in range(5, 10):
            with cols2[i - 5]:
                st.image(cast_list[i][0], use_container_width=True)
                st.markdown(f"**{cast_list[i][1]}**")
                st.caption(cast_list[i][2])
