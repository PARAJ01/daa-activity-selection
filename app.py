import streamlit as st
import pandas as pd

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Activity Selection - DAA",
    page_icon="📊",
    layout="wide"
)

# -------------------------------------------------
# TITLE
# -------------------------------------------------
st.markdown(
    "<h1 style='text-align:center;'>📊 Activity Selection Problem</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;'>Design and Analysis of Algorithms (Greedy Algorithm)</p>",
    unsafe_allow_html=True
)

# -------------------------------------------------
# SIDEBAR INPUT
# -------------------------------------------------
st.sidebar.header("⚙️ Input Controls")

num_activities = st.sidebar.number_input(
    "Number of Activities",
    min_value=1,
    max_value=15,
    value=5
)

# -------------------------------------------------
# INPUT ACTIVITIES
# -------------------------------------------------
st.subheader("📝 Enter Activity Details")

activities = []

for i in range(num_activities):
    col1, col2 = st.columns(2)

    with col1:
        start_time = st.number_input(
            f"Start Time of A{i+1}",
            min_value=0,
            key=f"s{i}"
        )

    with col2:
        finish_time = st.number_input(
            f"Finish Time of A{i+1}",
            min_value=start_time + 1,
            key=f"f{i}"
        )

    activities.append({
        "Activity": f"A{i+1}",
        "Start Time": start_time,
        "Finish Time": finish_time
    })

df = pd.DataFrame(activities)

st.markdown("### 📋 Activity Table")
st.dataframe(df, use_container_width=True)

# -------------------------------------------------
# GREEDY ALGORITHM FUNCTION
# -------------------------------------------------
def activity_selection(data):
    # Sort by finish time
    sorted_data = data.sort_values(by="Finish Time").reset_index(drop=True)

    selected_activities = []
    last_finish_time = -1

    for _, row in sorted_data.iterrows():
        if row["Start Time"] >= last_finish_time:
            selected_activities.append(row)
            last_finish_time = row["Finish Time"]

    return sorted_data, pd.DataFrame(selected_activities)

# -------------------------------------------------
# RUN BUTTON
# -------------------------------------------------
if st.button("🚀 Run Activity Selection Algorithm"):
    sorted_df, selected_df = activity_selection(df)

    st.markdown("---")
    st.subheader("🔄 Activities Sorted by Finish Time")
    st.dataframe(sorted_df, use_container_width=True)

    st.subheader("✅ Selected Activities")
    st.success(
        f"Maximum number of non-overlapping activities = {len(selected_df)}"
    )
    st.dataframe(selected_df, use_container_width=True)

    st.markdown("---")
    st.subheader("📘 Explanation")
    st.markdown("""
    - All activities are first **sorted by finish time**.
    - The activity which finishes earliest is selected first.
    - Each next activity is selected **only if** it does not overlap
      with the previously selected activity.
    - This greedy choice ensures the **maximum number of activities**.
    """)

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown(
    "<hr><p style='text-align:center;'>DAA Mini Project | Activity Selection | Greedy Algorithm</p>",
    unsafe_allow_html=True
)
