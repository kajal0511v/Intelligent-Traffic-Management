import os
import joblib
import pandas as pd
import streamlit as st


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Intelligent Traffic Management",
    page_icon="🚦",
    layout="wide"
)


# ==================================================
# MODEL FILE
# ==================================================

MODEL_FILE = "traffic_model.pkl"


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        opacity: 0.75;
        margin-bottom: 25px;
    }

    .result-card {
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(128,128,128,0.3);
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .big-result {
        font-size: 32px;
        font-weight: bold;
    }

    .small-text {
        font-size: 14px;
        opacity: 0.7;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# CHECK MODEL
# ==================================================

if not os.path.exists(MODEL_FILE):

    st.warning(
        "AI model not found. Please run train_model.py first."
    )

    st.stop()


# ==================================================
# LOAD MODEL
# ==================================================

model = joblib.load(
    MODEL_FILE
)


# ==================================================
# TITLE
# ==================================================

st.markdown(
    '<div class="main-title">🚦 Intelligent Traffic Management System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-based traffic congestion prediction and smart signal recommendation'
    '</div>',
    unsafe_allow_html=True
)


# ==================================================
# PROJECT INTRODUCTION
# ==================================================

st.info(
    """
    This system uses Machine Learning to analyze traffic conditions,
    predict congestion levels and recommend intelligent traffic-signal
    decisions.
    """
)


# ==================================================
# INPUT SECTION
# ==================================================

st.header("1️⃣ Enter Traffic Conditions")


# --------------------------------------------------
# FIRST ROW
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)


with col1:

    hour = st.slider(
        "Hour of Day",
        min_value=0,
        max_value=23,
        value=18
    )


with col2:

    day_type = st.selectbox(
        "Day Type",
        [
            "Weekday",
            "Weekend"
        ]
    )


with col3:

    weather = st.selectbox(
        "Weather",
        [
            "Clear",
            "Rain",
            "Fog"
        ]
    )


with col4:

    emergency = st.selectbox(
        "Emergency Vehicle?",
        [
            "No",
            "Yes"
        ]
    )


# --------------------------------------------------
# SECOND ROW
# --------------------------------------------------

st.subheader("🚗 Vehicle Count")


col1, col2, col3, col4 = st.columns(4)


with col1:

    lane1 = st.number_input(
        "Lane 1 Vehicles",
        min_value=0,
        max_value=150,
        value=70
    )


with col2:

    lane2 = st.number_input(
        "Lane 2 Vehicles",
        min_value=0,
        max_value=150,
        value=50
    )


with col3:

    lane3 = st.number_input(
        "Lane 3 Vehicles",
        min_value=0,
        max_value=150,
        value=40
    )


with col4:

    lane4 = st.number_input(
        "Lane 4 Vehicles",
        min_value=0,
        max_value=150,
        value=30
    )


# --------------------------------------------------
# SPEED
# --------------------------------------------------

avg_speed = st.slider(
    "Average Vehicle Speed (km/h)",
    min_value=5,
    max_value=100,
    value=30
)


# ==================================================
# INPUT DATAFRAME
# ==================================================

input_data = pd.DataFrame(
    [
        {
            "hour": hour,

            "day_type": day_type,

            "weather": weather,

            "emergency_vehicle":
                1 if emergency == "Yes" else 0,

            "lane1_vehicles": lane1,

            "lane2_vehicles": lane2,

            "lane3_vehicles": lane3,

            "lane4_vehicles": lane4,

            "avg_speed": avg_speed
        }
    ]
)


# ==================================================
# ANALYZE BUTTON
# ==================================================

if st.button(
    "🚦 ANALYZE TRAFFIC",
    use_container_width=True,
    type="primary"
):


    # ==================================================
    # MACHINE LEARNING PREDICTION
    # ==================================================

    prediction = model.predict(
        input_data
    )[0]


    # ==================================================
    # MODEL CONFIDENCE
    # ==================================================

    probabilities = model.predict_proba(
        input_data
    )[0]

    confidence = (
        max(probabilities) * 100
    )


    # ==================================================
    # TRAFFIC CALCULATION
    # ==================================================

    lane_counts = [
        lane1,
        lane2,
        lane3,
        lane4
    ]

    total_vehicles = sum(
        lane_counts
    )


    # Find busiest lane

    busiest_lane_index = (
        lane_counts.index(
            max(lane_counts)
        )
    )

    priority_lane = (
        busiest_lane_index + 1
    )


    # ==================================================
    # SMART SIGNAL DECISION
    # ==================================================

    if emergency == "Yes":

        green_time = 60

        action = (
            f"🚑 Emergency Priority: "
            f"Give immediate green signal "
            f"to Lane {priority_lane}."
        )


    elif prediction == "Severe":

        green_time = 55

        action = (
            f"🔴 Severe Congestion: "
            f"Prioritize Lane {priority_lane} "
            f"and significantly extend green time."
        )


    elif prediction == "High":

        green_time = 45

        action = (
            f"🟠 High Traffic: "
            f"Prioritize Lane {priority_lane} "
            f"with extended green time."
        )


    elif prediction == "Medium":

        green_time = 35

        action = (
            f"🟡 Moderate Traffic: "
            f"Give slightly higher green time "
            f"to Lane {priority_lane}."
        )


    else:

        green_time = 25

        action = (
            "🟢 Traffic Flow is Normal: "
            "Use normal signal timing."
        )


    # ==================================================
    # RESULT HEADER
    # ==================================================

    st.header(
        "2️⃣ AI Prediction"
    )


    # ==================================================
    # RESULT CARDS
    # ==================================================

    result1, result2, result3, result4 = st.columns(4)


    with result1:

        st.metric(
            "Congestion",
            prediction
        )


    with result2:

        st.metric(
            "AI Confidence",
            f"{confidence:.1f}%"
        )


    with result3:

        st.metric(
            "Total Vehicles",
            total_vehicles
        )


    with result4:

        st.metric(
            "Priority Lane",
            f"Lane {priority_lane}"
        )


    # ==================================================
    # SMART DECISION
    # ==================================================

    st.markdown(
        f"""
        <div class="result-card">

        <div class="big-result">
        {action}
        </div>

        <br>

        <div class="small-text">
        Recommended green signal time:
        approximately {green_time} seconds.
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # ==================================================
    # SIGNAL TIMING
    # ==================================================

    st.subheader(
        "🚦 Recommended Signal Timing"
    )


    total = max(
        total_vehicles,
        1
    )


    # Calculate proportion of traffic

    lane_weights = [
        count / total
        for count in lane_counts
    ]


    suggested_times = [
        round(
            20 + weight * (green_time - 20),
            1
        )

        for weight in lane_weights
    ]


    timing_data = pd.DataFrame(
        {
            "Lane": [
                "Lane 1",
                "Lane 2",
                "Lane 3",
                "Lane 4"
            ],

            "Vehicles": lane_counts,

            "Suggested Green Time (seconds)":
                suggested_times
        }
    )


    st.dataframe(
        timing_data,
        use_container_width=True,
        hide_index=True
    )


    # ==================================================
    # TRAFFIC GRAPH
    # ==================================================

    st.subheader(
        "📊 Traffic Distribution"
    )


    chart_data = pd.DataFrame(
        {
            "Lane 1": [lane1],
            "Lane 2": [lane2],
            "Lane 3": [lane3],
            "Lane 4": [lane4]
        }
    )


    st.bar_chart(
        chart_data.T
    )


    # ==================================================
    # DECISION EXPLANATION
    # ==================================================

    st.subheader(
        "🧠 Why did the system make this decision?"
    )


    # Vehicle explanation

    if total_vehicles >= 200:

        st.write(
            "• Total vehicle count is very high, "
            "which increases congestion risk."
        )

    elif total_vehicles >= 100:

        st.write(
            "• Vehicle volume is moderate."
        )

    else:

        st.write(
            "• Vehicle volume is relatively low."
        )


    # Speed explanation

    if avg_speed < 30:

        st.write(
            "• Average speed is low, "
            "indicating slower traffic flow."
        )

    else:

        st.write(
            "• Average speed is reasonably high."
        )


    # Rush hour

    if (
        8 <= hour <= 10
        or
        17 <= hour <= 20
    ):

        st.write(
            "• The selected time falls within "
            "a typical rush-hour period."
        )

    else:

        st.write(
            "• The selected time is outside "
            "the main rush-hour period."
        )


    # Weather

    if weather != "Clear":

        st.write(
            f"• {weather} conditions may reduce "
            "traffic flow."
        )


    # Emergency

    if emergency == "Yes":

        st.write(
            "• Emergency vehicle detected. "
            "The system therefore gives "
            "emergency traffic priority."
        )


    # ==================================================
    # DISCLAIMER
    # ==================================================

    st.divider()

    st.caption(
        """
        Academic Prototype:
        The current model uses demonstration traffic data.
        Real-world deployment would require real-time traffic
        sensors, CCTV, GPS or municipal traffic data.
        """
    )


# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "Intelligent Traffic Management using AI | "
    "Random Forest + Streamlit"
)