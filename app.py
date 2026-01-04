import streamlit as st
from dotenv import load_dotenv

from agents.question_generator import QuestionGeneratorAgent
from agents.research_agent import ResearchAgent
from agents.report_compiler import ReportCompilerAgent

load_dotenv()


def main() -> None:
    """
    Entry point for the AI Market Research Agent.
    """

    st.set_page_config(
        page_title="AI Market Research Agent",
        page_icon="📊",
        layout="wide",
    )

    # Custom CSS for glassmorphism light red theme
    st.markdown("""
        <style>
        .main .block-container {
            padding-top: 3rem;
        }
        .stApp {
            background: linear-gradient(135deg, #fff5f5 0%, #ffe8e8 50%, #fff0f0 100%);
        }
        .glass-card {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-radius: 16px;
            border: 1px solid rgba(255, 182, 193, 0.3);
            padding: 1.5rem;
            margin: 1rem 0;
            box-shadow: 0 8px 32px 0 rgba(255, 182, 193, 0.15);
        }
        .stTextInput > div > div > input {
            background-color: rgba(255, 255, 255, 0.8);
            border: 1px solid rgba(255, 182, 193, 0.4);
        }
        .stTextInput > div > div > input:focus {
            border-color: #ff9aa2;
            box-shadow: 0 0 0 0.2rem rgba(255, 154, 162, 0.25);
        }
        .stButton > button {
            padding: 0.75rem 1.5rem;
            font-size: 1.05rem;
            font-weight: 600;
            border-radius: 12px;
            background: linear-gradient(135deg, #ff9aa2 0%, #ffb3ba 100%);
            border: none;
            color: white;
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(255, 154, 162, 0.4);
        }
        h1 {
            color: #d63384;
        }
        h3 {
            color: #c9526a;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header Section
    st.title("AI Market Research Agent")
    st.markdown(
        "<p style='font-size: 1.1rem; color: #666; margin-bottom: 1.5rem;'>"
        "Generate research questions, run multi-source research, "
        "and compile a professional market research report."
        "</p>",
        unsafe_allow_html=True
    )
    
    # How it works section
    with st.container():
        st.markdown("### How this agent works")
        st.markdown("""
        - **Question Generation**: Analyzes your topic and domain to create focused research questions
        - **Multi-source Research**: Searches across the web in parallel to gather comprehensive insights
        - **Parallel Analysis**: Processes multiple questions simultaneously for faster results
        - **Report Synthesis**: Compiles all findings into a cohesive, professional research report
        """)
        st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)

    # Input Section - Centered, constrained width
    col1, col2, col3 = st.columns([2, 6, 2])
    
    with col2:
        st.markdown("### Research Parameters")
        st.markdown("<div style='margin-bottom: 1rem;'></div>", unsafe_allow_html=True)
        
        topic = st.text_input(
            "Research Topic",
            placeholder="e.g. AI adoption in Indian Fintech",
            label_visibility="visible",
        )

        domain = st.text_input(
            "Industry / Domain",
            placeholder="e.g. Payments, Lending, SaaS",
            label_visibility="visible",
        )

        st.markdown("<div style='margin-bottom: 1rem;'></div>", unsafe_allow_html=True)

        # Primary CTA - Proportional button (aligned with inputs)
        run_button = st.button("🚀 Run Market Research", type="primary")

    if run_button:
        if not topic or not domain:
            st.warning("Please enter both a research topic and a domain.")
            return

        # -----------------------------
        # Step 1: Generate questions
        # -----------------------------
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("1️⃣ Research Questions")
        st.markdown("<div style='margin-bottom: 1rem;'></div>", unsafe_allow_html=True)

        with st.spinner("Generating research questions..."):
            question_agent = QuestionGeneratorAgent()
            questions = question_agent.generate(topic=topic, domain=domain)

        with st.container():
            for q in questions:
                st.markdown(f"• {q}")
            st.markdown("<div style='margin-bottom: 1.5rem;'></div>", unsafe_allow_html=True)

        # -----------------------------
        # Step 2: Research each question
        # -----------------------------
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("2️⃣ Research Findings")
        st.markdown("<div style='margin-bottom: 1rem;'></div>", unsafe_allow_html=True)

        research_agent = ResearchAgent()

        async def run_parallel_research():
            tasks = [
                research_agent.research(question)
                for question in questions
            ]
            return await asyncio.gather(*tasks)

        with st.spinner("Running parallel research..."):
            import asyncio
            results = asyncio.run(run_parallel_research())

        for idx, result in enumerate(results, start=1):
            with st.container():
                st.markdown(f"#### Question {idx}")
                st.markdown(f"**{result['question']}**")
                st.markdown("<div style='margin-bottom: 0.5rem;'></div>", unsafe_allow_html=True)

                st.markdown("**Answer:**")
                st.write(result["answer"])
                st.markdown("<div style='margin-bottom: 0.75rem;'></div>", unsafe_allow_html=True)

                if result["sources"]:
                    st.markdown("**Sources:**")
                    for src in result["sources"]:
                        st.markdown(f"• {src}")
                
                if idx < len(results):
                    st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)

        # -----------------------------
        # Step 3: Compile final report
        # -----------------------------
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("3️⃣ Compiled Market Research Report")
        st.markdown("<div style='margin-bottom: 1rem;'></div>", unsafe_allow_html=True)

        with st.spinner("Compiling final report..."):
            compiler = ReportCompilerAgent()
            report = compiler.compile(results)

        with st.container():
            st.markdown(report)



if __name__ == "__main__":
    main()
