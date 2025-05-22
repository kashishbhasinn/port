import streamlit as st
from streamlit.components.v1 import html

# Set page config
st.set_page_config(
    page_title="Kashish Bhasin - AI & Product Intern Application - Ostello",
    page_icon="🎮",
    layout="wide"
)

# Custom CSS for styling - updated with Ostello-inspired colors
st.markdown("""
    <style>
        .header {
            font-size: 2.5em;
            color: #6366F1;
            border-bottom: 2px solid #6366F1;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        .section-header {
            font-size: 1.8em;
            color: #6366F1;
            margin-top: 30px;
            margin-bottom: 15px;
        }
        .highlight {
            background-color: #a2b8ff;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #6366F1;
            margin-bottom: 15px;
        }
        .skill-item {
            padding: 8px 0;
            border-bottom: 1px solid #eee;
        }
        .cta-button {
            background-color: #4F46E5 !important;
            color: white !important;
            font-weight: bold !important;
            padding: 10px 20px !important;
            border-radius: 5px !important;
            margin-top: 30px !important;
        }
        .project-card {
            border-left: 4px solid #6366F1;
            padding: 15px;
            margin-bottom: 20px;
            background-color: #F9FAFB;
            border-radius: 5px;
        }
        .gamification-icon {
            font-size: 1.5em;
            color: #4F46E5;
            margin-right: 10px;
        }
        .progress-bar {
            height: 10px;
            background-color: #E0E7FF;
            border-radius: 5px;
            margin-bottom: 5px;
        }
        .progress-fill {
            height: 10px;
            background-color: #6366F1;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Header with Ostello-focused tagline
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<div class="header">Kashish Bhasin</div>', unsafe_allow_html=True)
    st.markdown('**AI & Product Intern | Gamification & EdTech Enthusiast**')
    st.markdown('*BTech in Computer Science with AI/ML specialization with experience in product management, AI systems, and personalized learning platforms*')

with col2:
    st.write("")  # Empty for layout balance

# Navigation Sidebar with gamification elements
with st.sidebar:
    st.markdown("## Quest Progress")
    nav_option = st.radio("", ["About Me", "Skills & Expertise", "Projects & Experience", "Why Ostello?", "Contact"])
    
    st.markdown("---")
    st.markdown("### Application Quest")
    
    # Gamified progress tracking
    progress_value = 0
    if nav_option == "About Me":
        progress_value = 20
        quest_status = "In Progress: Introducing yourself"
    elif nav_option == "Skills & Expertise":
        progress_value = 40
        quest_status = "In Progress: Showcasing abilities"
    elif nav_option == "Projects & Experience":
        progress_value = 60
        quest_status = "In Progress: Demonstrating experience"
    elif nav_option == "Why Ostello?":
        progress_value = 80
        quest_status = "In Progress: Explaining motivation"
    else:
        progress_value = 100
        quest_status = "Quest Complete! Ready to connect"
    
    st.markdown(f"""
        <div class="progress-bar">
            <div class="progress-fill" style="width: {progress_value}%;"></div>
        </div>
        <p>{quest_status}</p>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### Skills Mastery")
    
    skills = {
        "AI/ML": 85,
        "Product Strategy": 80,
        "Python": 90,
        "Gamification": 75,
        "Data Analysis": 85
    }
    
    for skill, level in skills.items():
        st.markdown(f"""
            <div>
                <p>{skill}</p>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {level}%;"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

# About Me Section
if nav_option == "About Me":
    st.markdown('<div class="section-header">About Me</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight">
        <p><span class="gamification-icon">🚀</span> Product strategist and AI developer with a passion for educational technology and gamified learning experiences.</p>
        <ul>
            <li>Currently pursuing BTech in Computer Science with AI/ML specialization at Manipal University Jaipur (CGPA: 9.29)</li>
            <li>Experience in product management, AI system development, and data analysis across multiple organizations</li>
            <li>Led cross-functional teams to develop AI-driven platforms and automated systems</li>
            <li>Passionate about creating engaging, personalized learning experiences through technology</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Education")
    with st.expander("View Education Details"):
        st.markdown("""
        - **BTech in Computer Science Engineering - AI/ML**  
          *Manipal University Jaipur* | Sept 2022 - Present  
          CGPA: 9.29 | Relevant Coursework: Machine Learning, NLP, Data Mining, Algorithms, DBMS
        
        - **Lotus Valley International School, Noida**  
          Class 12: 93.8% | Class 10: 94.6%
        """)
    
    st.markdown("### Key Achievements")
    achievement_col1, achievement_col2 = st.columns(2)
    
    with achievement_col1:
        st.markdown("""
        <div class="project-card">
            <p><span class="gamification-icon">🏆</span> <strong>PwC Data Analytics & AI Launchpad Trainee</strong></p>
            <p>Completed 4 specialized microcertifications with 92% average score</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="project-card">
            <p><span class="gamification-icon">🏆</span> <strong>AI ML Community Treasurer</strong></p>
            <p>Optimized budget allocation, increasing event participation by 200 attendees</p>
        </div>
        """, unsafe_allow_html=True)
    
    with achievement_col2:
        st.markdown("""
        <div class="project-card">
            <p><span class="gamification-icon">🏆</span> <strong>AWS Udacity AI/ML Scholarship</strong></p>
            <p>Selected among top 2,000 students worldwide for exclusive AI Programming course</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="project-card">
            <p><span class="gamification-icon">🏆</span> <strong>PASCH Youth Course Scholar</strong></p>
            <p>Among top 50 students from over 100 nations for fully-funded program</p>
        </div>
        """, unsafe_allow_html=True)

# Skills Section - Updated for Ostello focus
elif nav_option == "Skills & Expertise":
    st.markdown('<div class="section-header">Skills & Expertise</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight">
        <p><span class="gamification-icon">💡</span> My skill set perfectly aligns with Ostello's mission to create engaging, personalized learning experiences through AI and gamification.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### AI & Technical Skills")
    tech_col1, tech_col2 = st.columns(2)
    
    with tech_col1:
        st.markdown('<div class="skill-item">✅ <strong>Python (NumPy, Pandas, Scikit-learn)</strong> <em>(Advanced)</em></div>', unsafe_allow_html=True)
        st.caption("Relevance: Core foundation for developing AI learning algorithms")
        
        st.markdown('<div class="skill-item">✅ <strong>Machine Learning & NLP</strong> <em>(Advanced)</em></div>', unsafe_allow_html=True)
        st.caption("Relevance: Creating personalized learning experiences and assessments")
        
        st.markdown('<div class="skill-item">✅ <strong>LangChain, HuggingFace, ChromaDB</strong> <em>(Intermediate)</em></div>', unsafe_allow_html=True)
        st.caption("Relevance: Building intelligent AI tutoring systems")
    
    with tech_col2:
        st.markdown('<div class="skill-item">✅ <strong>SQL, MongoDB</strong> <em>(Intermediate)</em></div>', unsafe_allow_html=True)
        st.caption("Relevance: Managing learner data and progress tracking")
        
        st.markdown('<div class="skill-item">✅ <strong>Generative AI & RAG Systems</strong> <em>(Intermediate)</em></div>', unsafe_allow_html=True)
        st.caption("Relevance: Creating adaptive content and assessments")
        
        st.markdown('<div class="skill-item">✅ <strong>AWS/Azure Basics</strong> <em>(Basic)</em></div>', unsafe_allow_html=True)
        st.caption("Relevance: Cloud infrastructure for scalable learning platforms")
    
    st.markdown("### Product & Management Skills")
    prod_col1, prod_col2 = st.columns(2)
    
    with prod_col1:
        st.markdown('<div class="skill-item">✅ <strong>Product Roadmapping</strong> <em>(Intermediate)</em></div>', unsafe_allow_html=True)
        st.caption("Relevance: Planning and prioritizing learning features")
        
        st.markdown('<div class="skill-item">✅ <strong>Competitive Analysis</strong> <em>(Intermediate)</em></div>', unsafe_allow_html=True)
        st.caption("Relevance: Understanding EdTech market landscape")
        
        st.markdown('<div class="skill-item">✅ <strong>Agile Project Management</strong> <em>(Intermediate)</em></div>', unsafe_allow_html=True)
        st.caption("Relevance: Efficient development of learning features")
    
    with prod_col2:
        st.markdown('<div class="skill-item">✅ <strong>Market & User Research</strong> <em>(Intermediate)</em></div>', unsafe_allow_html=True)
        st.caption("Relevance: Understanding learner needs and behaviors")
        
        st.markdown('<div class="skill-item">✅ <strong>Feature Prioritization</strong> <em>(Intermediate)</em></div>', unsafe_allow_html=True)
        st.caption("Relevance: Focusing on high-impact learning features")
        
        st.markdown('<div class="skill-item">✅ <strong>Data Analysis & Reporting</strong> <em>(Advanced)</em></div>', unsafe_allow_html=True)
        st.caption("Relevance: Tracking learning outcomes and platform performance")

# Projects & Experience Section
elif nav_option == "Projects & Experience":
    st.markdown('<div class="section-header">Projects & Experience</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight">
        <p><span class="gamification-icon">🔍</span> My experience spans product management, AI system development, and data analysis - all directly applicable to Ostello's gamified learning platform.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Professional Experience")
    
    st.markdown("""
    <div class="project-card">
        <h4>Arogo AI, IIT Kharagpur | Product Strategist Intern</h4>
        <p><em>February 2025 - Present</em></p>
        <ul>
            <li><strong>Led a cross-functional team of 10+ specialists</strong> (UI/UX designers, developers, LLM engineers) in developing an AI-driven platform</li>
            <li><strong>Designed a CV pipeline for 300K+ patients</strong>, automating analysis using Swin-UNETR, Inception v3 and BLIP-2</li>
            <li><strong>Managed product roadmap, backlog, and sprint planning</strong> to ensure timely delivery of 5+ features</li>
        </ul>
        <p><strong>Relevance to Ostello:</strong> Experience in AI product development and cross-functional team leadership</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card">
        <h4>DRDO Defense Young Scientist Laboratory | AI Research Intern</h4>
        <p><em>June 2024 - July 2024</em></p>
        <ul>
            <li><strong>Developed a RAG system</strong> improving document retrieval efficiency by 70%</li>
            <li><strong>Optimized search workflows</strong> using LangChain, ChromaDB, and HuggingFaceEmbeddings</li>
            <li><strong>Conducted comparative analysis</strong> of 15+ vector databases for large-scale AI models</li>
        </ul>
        <p><strong>Relevance to Ostello:</strong> Experience with RAG systems and LLMs that can power personalized learning</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card">
        <h4>Indian Institute of Management Bangalore | Data Intern</h4>
        <p><em>January 2024 - October 2024</em></p>
        <ul>
            <li><strong>Built a Python-based web scraping tool</strong> with 92% accuracy, automating data extraction</li>
            <li><strong>Implemented an Agile project management process</strong> reducing manual handling time by 50%</li>
            <li><strong>Delivered weekly analytical reports</strong> improving strategic alignment by 30%</li>
        </ul>
        <p><strong>Relevance to Ostello:</strong> Data analysis skills for tracking learning outcomes and user engagement</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Relevant Projects")
    
    project_option = st.selectbox(
        "Select a project to view details:",
        ["AI-Powered Resume Analysis System", "AI Kitchen Assistant", "Pre-Trained Image Classifier"]
    )
    
    if project_option == "AI-Powered Resume Analysis System":
        st.markdown("""
        <div class="project-card">
            <h4>AI-Powered Resume Analysis System</h4>
            <p><strong>Problem:</strong> Job seekers struggle to optimize resumes for specific positions</p>
            <p><strong>Solution:</strong> Built an AI system using Python, Streamlit, and Google Gemini API that analyzes resumes and suggests improvements</p>
            <p><strong>Impact:</strong> Improved keyword matching accuracy to 65% through user feedback and data analytics</p>
            <p><strong>Relevance to Ostello:</strong> Demonstrates ability to build AI feedback systems similar to what would be needed for personalized learning assessments</p>
        </div>
        """, unsafe_allow_html=True)
    
    elif project_option == "AI Kitchen Assistant":
        st.markdown("""
        <div class="project-card">
            <h4>AI Kitchen Assistant</h4>
            <p><strong>Problem:</strong> Cooking planning and execution is inefficient for many users</p>
            <p><strong>Solution:</strong> Developed an AI-powered smart cooking assistant with voice command capabilities</p>
            <p><strong>Impact:</strong> 35% improved meal planning efficiency and 40% increased engagement through voice commands</p>
            <p><strong>Relevance to Ostello:</strong> Experience in building engaging AI assistants that guide users through complex processes - similar to an AI tutor</p>
        </div>
        """, unsafe_allow_html=True)
    
    elif project_option == "Pre-Trained Image Classifier":
        st.markdown("""
        <div class="project-card">
            <h4>Pre-Trained Image Classifier</h4>
            <p><strong>Problem:</strong> Need for efficient image classification in various applications</p>
            <p><strong>Solution:</strong> Built a deep learning model for image classification using PyTorch and pre-trained architectures</p>
            <p><strong>Impact:</strong> Achieved 80% accuracy and improved classification efficiency by 40%</p>
            <p><strong>Relevance to Ostello:</strong> Experience with machine learning models that could be applied to learning content recognition and categorization</p>
        </div>
        """, unsafe_allow_html=True)

# Why Ostello Section
elif nav_option == "Why Ostello?":
    st.markdown('<div class="section-header">Why Ostello?</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight">
        <p><span class="gamification-icon">🎯</span> Ostello's mission to create India's first gamified AI learning platform perfectly aligns with my skills and passion for EdTech innovation.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### The Perfect Match
    
    Ostello is revolutionizing education by addressing a critical problem: the lack of structured, engaging learning experiences. As someone passionate about both AI and product development, I'm excited about Ostello's approach for these reasons:
    
    1. **Gamification meets AI learning** - My experience in both product strategy and AI development positions me to contribute to Ostello's quest-based learning system
    
    2. **Personalized learning experiences** - My work with RAG systems and LLMs directly applies to creating adaptive assessments and personalized feedback
    
    3. **Outcome-driven approach** - My background in data analysis and product metrics aligns with Ostello's focus on measurable learning outcomes
    """)
    
    st.markdown("### How I Can Contribute")
    
    with st.expander("AI & Machine Learning"):
        st.markdown("""
        - Design and implement adaptive assessment algorithms based on learner performance
        - Develop RAG systems for personalized content delivery and feedback
        - Create AI-powered mentorship recommendation engines
        - Implement engagement analytics to optimize learning pathways
        """)
    
    with st.expander("Product Development"):
        st.markdown("""
        - Conduct user research to identify pain points in the learning journey
        - Develop product roadmaps for new learning features and quests
        - Create gamification mechanics that increase engagement and completion rates
        - Design A/B testing frameworks to optimize learning outcomes
        - Implement analytics dashboards to track user progress and engagement
        """)
    
    with st.expander("Cross-Functional Collaboration"):
        st.markdown("""
        - Experience working with developers, designers, and content creators
        - Strong communication skills to translate technical concepts for non-technical stakeholders
        - Agile project management experience to ensure timely feature delivery
        - Data visualization skills to communicate insights to the product team
        """)
    
    st.markdown("""
    <div class="highlight">
        <p><span class="gamification-icon">💪</span> <strong>Why I'm Different:</strong> My unique combination of product management experience at Arogo AI, RAG system development at DRDO, and data analytics work at IIM Bangalore positions me to make immediate contributions to Ostello's mission of creating engaging, personalized learning experiences.</p>
    </div>
    """, unsafe_allow_html=True)

# Contact Section
else:
    st.markdown('<div class="section-header">Connect With Me</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="line-height: 2;">
        <p>📧 <strong>Email:</strong> kashishbhasinn@gmail.com</p>
        <p>🔗 <strong>LinkedIn:</strong> <a href="https://linkedin.com/in/kashish-bhasin" target="_blank">linkedin.com/in/kashish-bhasin</a></p>
        <p>📱 <strong>Phone:</strong> (+91) 9811149303</p>
        <p>💻 <strong>GitHub:</strong> <a href="https://github.com/kashishbhasinn" target="_blank">github.com/kashishbhasinn</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Availability")
    st.markdown("""
    - Immediately available for AI & Product Intern opportunity at Ostello
    - Flexible with work arrangements (remote/hybrid/onsite)
    - Ready to contribute to Ostello's mission from day one
    """)
    
    st.markdown("""
    <div class="highlight">
        <p><span class="gamification-icon">🚀</span> <strong>Next Steps:</strong> I'd love to discuss how my experience in AI development, product strategy, and data analysis can help Ostello create even more engaging learning experiences. I'm particularly interested in exploring how we can further enhance the gamification aspects of the platform to drive user engagement and learning outcomes.</p>
    </div>
    """, unsafe_allow_html=True)

# "Join The Quest" CTA Button (renamed from "Hire Me")
if st.button("Join The Quest!", key="join_quest", help="Click to show your interest"):
    st.success("Ready to help Ostello revolutionize learning! 🚀")
    st.balloons()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9em;">
    <p>Thank you for considering my application. I look forward to the opportunity to contribute to Ostello's mission of making quality education accessible, engaging, and effective.</p>
    <p>© 2024 Kashish Bhasin - All rights reserved</p>
</div>
""", unsafe_allow_html=True)
