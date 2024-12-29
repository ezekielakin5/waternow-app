import streamlit as st

# Name your company
company_name = "WaterNow"

# Streamlit app

def main():
    # Title Section
    st.title(f"Welcome to {company_name}")
    st.header("Revolutionizing Water Access")
    st.write(
        "At WaterNow, we empower borehole owners to transform their manual water sales into seamless, automated transactions. Our smart QR-code system ensures accessibility, transparency, and scalability for water provision."
    )

    # Features Section
    st.subheader("Our Features")
    features = [
        "24/7 Automated Water Dispensing",
        "Cashless Payments via QR Code",
        "Real-Time Sales Tracking",
        "Tamper-Proof Water Management",
        "Insights and Analytics for Operators",
    ]
    for feature in features:
        st.write(f"- {feature}")

    # How It Works Section
    st.subheader("How It Works")
    st.write(
        "1. Customers scan the QR code outside the borehole property.\n"
        "2. They pay digitally via mobile money or bank transfer.\n"
        "3. Water is dispensed automatically based on the payment amount."
    )

    # Call to Action
    st.subheader("Get Started")
    st.write(
        "Join the thousands of borehole operators revolutionizing water sales today. Sign up now to bring smart water solutions to your community!"
    )
    st.button("Learn More")

# Run the app in Colab
if __name__ == "__main__":
    public_url = ngrok.connect(8501)
    print(f"Streamlit App URL: {public_url}")
    st._is_running_with_streamlit = True
    st.sidebar.info("Streamlit Web App")
    main()
