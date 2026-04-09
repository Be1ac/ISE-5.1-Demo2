import streamlit as st
import animate 
# Set up session state variables

if "ten_x" not in st.session_state:
    # ten_x mode changes our buttons to increment and decrement by 10 instead of by 1
    st.session_state.ten_x = 0

if "count" not in st.session_state:
    st.session_state.count = 0


# Set up callbacks for inputs
def increment():
    st.session_state.count += 10 if st.session_state.ten_x else 1


def decrement():
    st.session_state.count -= 10 if st.session_state.ten_x else 1
    if st.session_state.count < 0:
        # Minimum count value is zero
        st.session_state.count = 0


# Write to page
with st.expander("Options") as options:
    # The key of the checkbox (ten_x) will automatically be added to the session state
    st.checkbox("10x mode", key="ten_x", value=st.session_state.ten_x)

st.write(f"Total count is {st.session_state.count}")

st.button(
    f"plus {'10' if st.session_state.ten_x else '1'}",
    key="increment",
    on_click=increment,
)
st.button(
    f"minus {'10' if st.session_state.ten_x else '1'}",
    key="decrement",
    on_click=decrement,
)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Counter Project", "Animations"])

if page == "Animations":
    # 2. INTEGRATION: Call the logic from animate.py
    # Since animate.py already has a selectbox and plotly_chart call, 
    # we can run it like this:
    
    st.title("Gallery of Animations")
    
    # We need to handle the logic inside animate.py
    # If animate.py has code sitting at the top level (not inside a function),
    # it might run automatically, but the best practice is to wrap 
    # animate.py's display logic in a function and call it here.
    
    # For now, let's assume animate.py is structured as you showed.
    # We can trigger the selection logic here:
    choice = st.selectbox(
        "Select Visual", 
        ["Rotating 3D Helix", "Moving Sine Wave", "Bouncing Ball", "Expanding 3D Ripple"]
    )
    
    if choice == "Rotating 3D Helix":
        st.plotly_chart(animate.rotating_3d_helix())
    elif choice == "Moving Sine Wave":
        st.plotly_chart(animate.moving_sine_wave())
    elif choice == "Expanding 3D Ripple":
        st.plotly_chart(animate.expanding_3d_ripple())
    else:
        st.plotly_chart(animate.bouncing_ball())

        