import streamlit as st

# Name your company
company_name = "WaterNow"

# Streamlit app
def main():
    # Apply custom colors
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f8ff;
            color: #333;
            font-family: Arial, sans-serif;
        }
        .stButton > button {
            background-color: #007acc;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
        }
        .stButton > button:hover {
            background-color: #005f99;
        }
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #007acc;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Header Section
    st.markdown(f"<h1 class='title'>Welcome to {company_name}</h1>", unsafe_allow_html=True)
    st.markdown(
        "<h3>Revolutionizing Water Access</h3>", unsafe_allow_html=True
    )
    st.markdown(
        "At WaterNow, we empower borehole owners to transform their manual water sales into seamless, automated transactions. Our smart QR-code system ensures accessibility, transparency, and scalability for water provision."
    )

    # Add a banner graphic
    st.image(
        "https://via.placeholder.com/800x200.png?text=Revolutionizing+Water+Access", 
        use_column_width=True
    )

    # Features Section
    st.markdown("## Our Features")
    features = [
        "24/7 Automated Water Dispensing",
        "Cashless Payments via QR Code",
        "Real-Time Sales Tracking",
        "Tamper-Proof Water Management",
        "Insights and Analytics for Operators",
    ]
    for feature in features:
        st.markdown(f"- {feature}")

    # How It Works Section
    st.markdown("## How It Works")
    st.markdown(
        "1. Customers scan the QR code outside the borehole property.<br>"
        "2. They pay digitally via mobile money or bank transfer.<br>"
        "3. Water is dispensed automatically based on the payment amount.",
        unsafe_allow_html=True
    )

    # Add a graphic for "How It Works"
    st.image(
        "https://via.placeholder.com/600x300.png?text=How+It+Works", 
        use_column_width=True
    )

    # Call to Action Section
    st.markdown("## Get Started")
    st.markdown(
        "Join the thousands of borehole operators revolutionizing water sales today. Sign up now to bring smart water solutions to your community!"
    )

    # Add interactive buttons
    col1, col2 = st.columns(2)
    with col1:
        st.button("Learn More")
    with col2:
        st.button("Sign Up")

if __name__ == "__main__":
    main()


