import streamlit as st
import time

from crew import resultoutput

st.set_page_config(page_title="AI News Research", page_icon="📰", layout="wide")

st.markdown(
    """
<style>

.main{
    background:#0f172a;
}

.stTextArea textarea{
    border-radius:12px;
}

.step{
    background:#1e293b;
    padding:12px;
    border-radius:10px;
    margin-bottom:10px;
}

.answer{
    background:#111827;
    border-radius:12px;
    padding:20px;
}

</style>
""",
    unsafe_allow_html=True,
)

st.title("📰 Multi-Agent News Research")
st.caption("CrewAI • Research Agent + Writer Agent")

topic = st.text_area("Enter a topic", placeholder="Example: Latest AI News", height=120)

if st.button("Research", use_container_width=True):

    if topic.strip() == "":
        st.warning("Please enter a topic.")
        st.stop()

    left, right = st.columns([1, 2])

    with left:

        st.subheader("🧠 Thinking")

        thinking = st.empty()

        steps = [
            "Understanding your topic",
            "Choosing research strategy",
            "Searching latest news",
            "Reading search results",
            "Summarizing information",
            "Writer Agent preparing article",
        ]

        output = ""

        for s in steps:
            output += f"""
<div class='step'>
✅ {s}
</div>
"""
            thinking.markdown(output, unsafe_allow_html=True)
            time.sleep(0.6)

    with right:

        st.subheader("⚡ Live Progress")

        status = st.empty()

        logs = [
            "Research Agent Started...",
            "Searching Google...",
            "Collecting Articles...",
            "Analyzing Results...",
            "Writer Agent Started...",
            "Generating Markdown...",
        ]

        txt = ""

        for log in logs:
            txt += f"• {log}\n\n"
            status.text(txt)
            time.sleep(0.5)

    st.divider()

    st.subheader("📄 Final Report")

    with st.spinner("Running CrewAI..."):

        try:
            result = resultoutput(topic)
        except TypeError:
            st.error(
                "Your crew.py still uses input(). Change resultoutput() to accept topic as a parameter."
            )
            st.stop()

    st.markdown(result)

    st.download_button(
        "Download Report",
        result,
        "result.md",
        "text/markdown",
        use_container_width=True,
    )
