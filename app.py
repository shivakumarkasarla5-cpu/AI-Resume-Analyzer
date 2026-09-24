import streamlit as st
from pypdf import PdfReader

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer & Job Matcher")
st.write("Upload your resume and compare it with a job description.")


# ============================================================
# RESUME UPLOAD
# ============================================================

st.header("📤 Upload Your Resume")

resume = st.file_uploader(
    "Choose your resume PDF",
    type=["pdf"]
)


# ============================================================
# JOB DESCRIPTION
# ============================================================

st.header("💼 Job Description")

job_description = st.text_area(
    "Paste the job description here",
    height=200
)


# ============================================================
# ANALYZE BUTTON
# ============================================================

if st.button("🚀 Analyze Resume"):

    if resume is None:

        st.warning("Please upload your resume.")

    elif not job_description.strip():

        st.warning("Please enter the job description.")

    else:

        # ====================================================
        # READ PDF
        # ====================================================

        reader = PdfReader(resume)

        resume_text = ""

        for page in reader.pages:

            text = page.extract_text()

            if text:

                resume_text += text + "\n"

        st.success("Resume read successfully! ✅")


        # ====================================================
        # LOWERCASE TEXT
        # ====================================================

        resume_lower = resume_text.lower()
        job_lower = job_description.lower()


        # ====================================================
        # SKILLS
        # ====================================================

        skills = [
            "python",
            "java",
            "c++",
            "sql",
            "html",
            "css",
            "javascript",
            "react",
            "node.js",
            "machine learning",
            "data science",
            "pandas",
            "numpy",
            "scikit-learn",
            "tensorflow",
            "git",
            "github",
            "docker",
            "aws",
            "excel",
            "power bi",
            "tableau",
            "communication",
            "dsa"
        ]


        # ====================================================
        # FIND SKILLS IN RESUME
        # ====================================================

        resume_skills = []

        for skill in skills:

            if skill in resume_lower:

                resume_skills.append(skill)


        # ====================================================
        # FIND SKILLS IN JOB DESCRIPTION
        # ====================================================

        job_skills = []

        for skill in skills:

            if skill in job_lower:

                job_skills.append(skill)


        # ====================================================
        # MATCHING SKILLS
        # ====================================================

        matching_skills = []

        for skill in job_skills:

            if skill in resume_skills:

                matching_skills.append(skill)


        # ====================================================
        # MISSING SKILLS
        # ====================================================

        missing_skills = []

        for skill in job_skills:

            if skill not in resume_skills:

                missing_skills.append(skill)


        # ====================================================
        # WEIGHTED SKILL SCORE
        # ====================================================

        skill_weights = {
            "python": 15,
            "java": 15,
            "sql": 10,
            "dsa": 15,
            "git": 5,
            "github": 5,
            "html": 5,
            "css": 5,
            "javascript": 10,
            "machine learning": 5,
            "pandas": 3,
            "numpy": 2
        }

        total_weight = 0
        matched_weight = 0

        for skill in job_skills:

            weight = skill_weights.get(skill, 5)

            total_weight += weight

            if skill in matching_skills:

                matched_weight += weight

        if total_weight > 0:

            match_percentage = (
                matched_weight / total_weight
            ) * 100

        else:

            match_percentage = 0


        # ====================================================
        # JOB ROLE DETECTION
        # ====================================================

        job_role = "General Software/Technology Role"

        if (
            "machine learning" in job_skills
            or "data science" in job_skills
            or "pandas" in job_skills
            or "numpy" in job_skills
        ):

            job_role = "Data Science / Machine Learning Role"

        if (
            "java" in job_skills
            or "javascript" in job_skills
            or "html" in job_skills
            or "css" in job_skills
            or "react" in job_skills
        ):

            job_role = "Software Development Role"


        # ====================================================
        # DETECTED JOB ROLE
        # ====================================================

        st.subheader("💼 Detected Job Role")

        st.info(
            f"Detected Role: **{job_role}**"
        )


        # ====================================================
        # RESUME ANALYSIS
        # ====================================================

        st.header("📊 Resume Analysis")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Match Percentage",
                f"{match_percentage:.0f}%"
            )

        with col2:

            st.metric(
                "Matching Skills",
                len(matching_skills)
            )

        with col3:

            st.metric(
                "Missing Skills",
                len(missing_skills)
            )


        # ====================================================
        # SKILL MATCH PROGRESS
        # ====================================================

        st.subheader("📊 Skill Match Progress")

        st.progress(
            min(int(match_percentage), 100)
        )

        st.write(
            f"Your resume matches **{match_percentage:.0f}%** "
            f"of the detected job requirements."
        )


        # ====================================================
        # MATCHING SKILLS
        # ====================================================

        st.subheader("✅ Matching Skills")

        if matching_skills:

            st.write(
                ", ".join(matching_skills)
            )

        else:

            st.write(
                "No matching skills found."
            )


        # ====================================================
        # MISSING SKILLS
        # ====================================================

        st.subheader("❌ Missing Skills")

        if missing_skills:

            st.write(
                ", ".join(missing_skills)
            )

        else:

            st.write(
                "No major missing skills found."
            )


        # ====================================================
        # SKILL MATCH OVERVIEW
        # ====================================================

        st.subheader("📊 Skill Match Overview")

        # Use a DataFrame so the chart has clear categories
        # and does not produce confusing numeric x-axis labels.

        import pandas as pd

        chart_data = pd.DataFrame({
            "Skill Status": [
                "Matching Skills",
                "Missing Skills"
            ],
            "Number of Skills": [
                len(matching_skills),
                len(missing_skills)
            ]
        })

        st.bar_chart(
            chart_data.set_index("Skill Status"),
            height=300
        )


        # ====================================================
        # MATCH SCORE EXPLANATION
        # ====================================================

        st.subheader("🎯 Match Score Explanation")

        st.write(
            f"Your resume matches **{len(matching_skills)} "
            f"out of {len(job_skills)}** detected job skills."
        )

        st.info(
            f"Resume Match Score: **{match_percentage:.0f}%**"
        )


        # ====================================================
        # RESUME IMPROVEMENT SUGGESTIONS
        # ====================================================

        st.subheader(
            "💡 Resume Improvement Suggestions"
        )

        if missing_skills:

            st.write(
                "Consider adding or improving these skills:"
            )

            for skill in missing_skills:

                st.write(
                    f"👉 Learn or strengthen **{skill}**"
                )

        else:

            st.success(
                "Your resume covers all detected job skills! 🎉"
            )


        # ====================================================
        # SKILL PRIORITY
        # ====================================================

        st.subheader("🔥 Skill Priority")

        if missing_skills:

            priority_skills = []

            for skill in missing_skills:

                weight = skill_weights.get(
                    skill,
                    5
                )

                priority_skills.append(
                    (skill, weight)
                )

            priority_skills.sort(
                key=lambda x: x[1],
                reverse=True
            )

            st.write(
                "Based on the job requirements, "
                "focus on these missing skills first:"
            )

            for skill, weight in priority_skills:

                if weight >= 10:

                    priority = "🔴 High Priority"

                elif weight >= 5:

                    priority = "🟡 Medium Priority"

                else:

                    priority = "🟢 Lower Priority"

                st.write(
                    f"**{skill.upper()}** — {priority}"
                )

        else:

            st.success(
                "No missing skills. Your resume covers "
                "the detected requirements! 🎉"
            )


        # ====================================================
        # SKILL GAP ANALYSIS
        # ====================================================

        st.subheader("📈 Skill Gap Analysis")

        st.write(
            "This section shows the difference between "
            "the skills required by the job and the skills "
            "found in your resume."
        )

        if len(job_skills) > 0:

            skill_gap_percentage = (
                len(missing_skills)
                / len(job_skills)
            ) * 100

        else:

            skill_gap_percentage = 0

        gap_col1, gap_col2, gap_col3 = st.columns(3)

        with gap_col1:

            st.metric(
                "Required Skills",
                len(job_skills)
            )

        with gap_col2:

            st.metric(
                "Skills You Have",
                len(matching_skills)
            )

        with gap_col3:

            st.metric(
                "Skill Gap",
                f"{skill_gap_percentage:.0f}%"
            )


        # FIXED SKILL GAP CHART

        gap_chart_data = pd.DataFrame({
            "Skill Status": [
                "Skills You Have",
                "Skills Missing"
            ],
            "Number of Skills": [
                len(matching_skills),
                len(missing_skills)
            ]
        })

        st.bar_chart(
            gap_chart_data.set_index("Skill Status"),
            height=300
        )


        if missing_skills:

            st.write(
                "### 🎯 Skills to Close the Gap"
            )

            for skill in missing_skills:

                weight = skill_weights.get(
                    skill,
                    5
                )

                if weight >= 10:

                    level = "High"

                elif weight >= 5:

                    level = "Medium"

                else:

                    level = "Low"

                st.write(
                    f"🔧 **{skill.upper()}** — "
                    f"{level} importance"
                )

        else:

            st.success(
                "🎉 No skill gap detected for the skills "
                "identified in this job description."
            )


        # ====================================================
        # RESUME QUALITY ANALYSIS
        # ====================================================

        st.subheader(
            "📋 Resume Quality Analysis"
        )

        has_projects = (
            "project" in resume_lower
            or "projects" in resume_lower
        )

        has_education = (
            "education" in resume_lower
        )

        has_email = "@" in resume_text

        has_linkedin = (
            "linkedin" in resume_lower
        )

        has_github = (
            "github" in resume_lower
        )

        quality_checks = {
            "Projects section": has_projects,
            "Education section": has_education,
            "Email address": has_email,
            "LinkedIn profile": has_linkedin,
            "GitHub profile": has_github
        }

        for item, present in quality_checks.items():

            if present:

                st.write(
                    f"✅ {item}"
                )

            else:

                st.write(
                    f"❌ {item}"
                )


        # ====================================================
        # RESUME QUALITY SCORE
        # ====================================================

        resume_score = (
            sum(quality_checks.values())
            / len(quality_checks)
        ) * 100

        st.subheader(
            "⭐ Resume Quality Score"
        )

        st.metric(
            "Resume Score",
            f"{resume_score:.0f}/100"
        )

        st.progress(
            int(resume_score)
        )


        # ====================================================
        # DETECTED RESUME SKILLS
        # ====================================================

        st.subheader(
            "🧠 Skills Detected in Your Resume"
        )

        if resume_skills:

            st.write(
                ", ".join(resume_skills)
            )

        else:

            st.write(
                "No skills detected."
            )


        # ====================================================
        # AI RESUME IMPROVEMENT SUGGESTIONS
        # ====================================================

        st.subheader(
            "🤖 AI Resume Improvement Suggestions"
        )

        st.write(
            "Based on your resume, job requirements, "
            "skill gap, and resume quality, here are "
            "personalized areas you can improve."
        )


        # Target role

        if job_role == "Software Development Role":

            st.info(
                "💻 **Target Role:** This job focuses on "
                "Software Development. Highlight programming, "
                "DSA, databases, Git/GitHub, and software projects."
            )

        elif job_role == "Data Science / Machine Learning Role":

            st.info(
                "📊 **Target Role:** This job focuses on "
                "Data Science / Machine Learning. Highlight "
                "Python, Pandas, NumPy, Machine Learning, "
                "and data projects."
            )

        else:

            st.info(
                "🎯 **Target Role:** This is a general "
                "technology role. Clearly highlight your "
                "strongest technical skills and projects."
            )


        # Missing skills

        if missing_skills:

            st.write(
                "### 🔧 1. Improve Missing Skills"
            )

            for skill in missing_skills:

                weight = skill_weights.get(
                    skill,
                    5
                )

                if weight >= 10:

                    st.warning(
                        f"🔴 **{skill.upper()}** — "
                        "High-priority skill. Consider "
                        "learning and practicing this skill."
                    )

                elif weight >= 5:

                    st.write(
                        f"🟡 **{skill.upper()}** — "
                        "Medium-priority skill. Add "
                        "learning or project experience if relevant."
                    )

                else:

                    st.write(
                        f"🟢 **{skill.upper()}** — "
                        "Useful additional skill."
                    )

        else:

            st.success(
                "✅ Your resume contains all detected "
                "skills from this job description."
            )


        # Skill gap

        st.write(
            "### 📉 2. Reduce Your Skill Gap"
        )

        if skill_gap_percentage >= 50:

            st.warning(
                f"⚠️ Your current skill gap is "
                f"**{skill_gap_percentage:.0f}%**. "
                "Focus on the missing skills before "
                "applying to similar positions."
            )

        elif skill_gap_percentage >= 25:

            st.info(
                f"📚 Your skill gap is "
                f"**{skill_gap_percentage:.0f}%**. "
                "Strengthening the missing skills can "
                "improve your job match."
            )

        else:

            st.success(
                f"✅ Your skill gap is "
                f"**{skill_gap_percentage:.0f}%**."
            )


        # Resume quality

        st.write(
            "### 📄 3. Improve Resume Quality"
        )

        if not has_projects:

            st.warning(
                "🚀 Add a **Projects** section with "
                "2–3 relevant technical projects."
            )

        else:

            st.success(
                "✅ Projects section detected."
            )

        if not has_education:

            st.warning(
                "🎓 Add an **Education** section."
            )

        else:

            st.success(
                "✅ Education section detected."
            )

        if not has_linkedin:

            st.warning(
                "🔗 Add your **LinkedIn profile**."
            )

        else:

            st.success(
                "✅ LinkedIn profile detected."
            )

        if not has_github:

            st.warning(
                "💻 Add your **GitHub profile**."
            )

        else:

            st.success(
                "✅ GitHub profile detected."
            )

        if not has_email:

            st.warning(
                "📧 Add a professional email address."
            )

        else:

            st.success(
                "✅ Email address detected."
            )


        # Project recommendation

        st.write(
            "### 🚀 4. Project Recommendation"
        )

        if job_role == "Software Development Role":

            st.write(
                "Highlight projects involving "
                "**Python/Java, SQL, DSA, web technologies, "
                "APIs, Git/GitHub, or software development**."
            )

        elif job_role == "Data Science / Machine Learning Role":

            st.write(
                "Highlight projects involving "
                "**Python, Pandas, NumPy, Machine Learning, "
                "data analysis, and visualization**."
            )

        else:

            st.write(
                "Highlight projects that directly use "
                "the most important skills mentioned "
                "in the job description."
            )


        # Summary

        st.write(
            "### 📝 5. Improvement Summary"
        )

        if missing_skills:

            st.write(
                f"Your resume currently has "
                f"**{len(matching_skills)} matching skills** "
                f"and **{len(missing_skills)} missing skills**."
            )

            st.write(
                "Focus first on the high-priority missing "
                "skills, then strengthen your projects "
                "and resume sections."
            )

        else:

            st.success(
                "🎉 Your resume covers all detected "
                "job skills. Focus on demonstrating "
                "these skills through strong projects "
                "and measurable achievements."
            )


        # ====================================================
        # ATS RESUME ANALYSIS
        # ====================================================

        st.subheader(
            "📋 ATS Resume Analysis"
        )

        st.write(
            "This section checks how well your resume "
            "matches important job keywords and basic "
            "resume sections commonly used by ATS systems."
        )


        # ----------------------------------------------------
        # ATS KEYWORD ANALYSIS
        # ----------------------------------------------------

        ats_keyword_total = len(job_skills)

        ats_keyword_found = len(matching_skills)

        ats_keyword_missing = len(missing_skills)

        if ats_keyword_total > 0:

            ats_keyword_percentage = (
                ats_keyword_found
                / ats_keyword_total
            ) * 100

        else:

            ats_keyword_percentage = 0


        # ----------------------------------------------------
        # ATS SECTION CHECKS
        # ----------------------------------------------------

        ats_sections = {

            "Contact Information": has_email,

            "Education": has_education,

            "Projects": has_projects,

            "LinkedIn": has_linkedin,

            "GitHub": has_github

        }

        ats_sections_found = sum(
            ats_sections.values()
        )

        ats_sections_total = len(
            ats_sections
        )


        # ----------------------------------------------------
        # ATS SCORE
        # ----------------------------------------------------

        # 60% keyword matching
        # 40% resume structure

        ats_score = (
            (ats_keyword_percentage * 0.60)
            +
            (
                (
                    ats_sections_found
                    / ats_sections_total
                ) * 100 * 0.40
            )
        )

        ats_score = min(
            max(ats_score, 0),
            100
        )


        # ----------------------------------------------------
        # ATS SCORE DISPLAY
        # ----------------------------------------------------

        st.write(
            "### 🎯 ATS Score"
        )

        ats_col1, ats_col2, ats_col3 = st.columns(3)

        with ats_col1:

            st.metric(
                "ATS Score",
                f"{ats_score:.0f}/100"
            )

        with ats_col2:

            st.metric(
                "Keywords Found",
                ats_keyword_found
            )

        with ats_col3:

            st.metric(
                "Keywords Missing",
                ats_keyword_missing
            )

        st.progress(
            int(ats_score)
        )


        # ----------------------------------------------------
        # ATS KEYWORD MATCH
        # ----------------------------------------------------

        st.write(
            "### 🔑 ATS Keyword Analysis"
        )

        if matching_skills:

            st.success(
                "✅ Keywords found in your resume:"
            )

            st.write(
                ", ".join(matching_skills)
            )

        else:

            st.warning(
                "No matching job keywords were detected."
            )

        if missing_skills:

            st.warning(
                "⚠️ Important keywords missing from "
                "your resume:"
            )

            st.write(
                ", ".join(missing_skills)
            )

        else:

            st.success(
                "🎉 No detected job keywords are missing."
            )


        # ----------------------------------------------------
        # ATS RESUME STRUCTURE
        # ----------------------------------------------------

        st.write(
            "### 📄 ATS Resume Structure Check"
        )

        for section, present in ats_sections.items():

            if present:

                st.write(
                    f"✅ {section}"
                )

            else:

                st.write(
                    f"❌ {section}"
                )


        # ----------------------------------------------------
        # ATS RECOMMENDATIONS
        # ----------------------------------------------------

        st.write(
            "### 💡 ATS Recommendations"
        )

        if ats_score >= 80:

            st.success(
                "✅ Your resume has strong keyword coverage "
                "and the basic sections detected by this scanner."
            )

        elif ats_score >= 60:

            st.info(
                "📌 Your resume has moderate ATS coverage. "
                "Adding relevant missing keywords and improving "
                "resume sections can increase the score."
            )

        else:

            st.warning(
                "⚠️ Your resume has several ATS improvement "
                "areas. Focus on relevant job keywords and "
                "complete resume sections."
            )


        # Missing keywords

        if missing_skills:

            st.write(
                "🔧 **Add relevant missing keywords naturally** "
                "to your Skills or Projects sections when "
                "you genuinely have that knowledge or experience."
            )


        # Missing sections

        missing_sections = []

        for section, present in ats_sections.items():

            if not present:

                missing_sections.append(section)

        if missing_sections:

            st.write(
                "📄 **Resume sections to improve:** "
                + ", ".join(missing_sections)
            )


        # Final ATS message

        st.success(
            "✅ ATS analysis complete!"
        )
                # ====================================================
        # SMART PROJECT RECOMMENDATION SYSTEM
        # ====================================================

        st.subheader("🚀 Smart Project Recommendation System")

        st.write(
            "Based on the job description, missing skills, "
            "and detected job role, here are project ideas "
            "that can help you strengthen your profile."
        )

        # Project database
        project_database = [

            {
                "name": "💻 Full-Stack Job Portal",
                "skills": [
                    "html",
                    "css",
                    "javascript",
                    "react",
                    "node.js",
                    "sql",
                    "git",
                    "github"
                ],
                "technologies": (
                    "HTML, CSS, JavaScript, React, Node.js, "
                    "SQL, Git, GitHub"
                ),
                "description": (
                    "Build a complete job portal where users "
                    "can register, search jobs, apply for jobs, "
                    "and manage applications."
                )
            },

            {
                "name": "🧠 DSA Problem-Solving Tracker",
                "skills": [
                    "dsa",
                    "python",
                    "java",
                    "sql",
                    "git",
                    "github"
                ],
                "technologies": (
                    "Python/Java, DSA, SQL, Git, GitHub"
                ),
                "description": (
                    "Build an application that tracks coding "
                    "problems, difficulty levels, topics, "
                    "solutions, and progress."
                )
            },

            {
                "name": "🤖 AI Resume Analyzer & Job Matcher",
                "skills": [
                    "python",
                    "machine learning",
                    "pandas",
                    "numpy",
                    "scikit-learn",
                    "sql",
                    "git",
                    "github"
                ],
                "technologies": (
                    "Python, Pandas, NumPy, Scikit-learn, "
                    "Streamlit, Git, GitHub"
                ),
                "description": (
                    "Analyze resumes, compare them with job "
                    "descriptions, detect skills, calculate "
                    "match scores, and identify skill gaps."
                )
            },

            {
                "name": "📊 Student Performance Analytics",
                "skills": [
                    "python",
                    "sql",
                    "pandas",
                    "numpy",
                    "data science",
                    "excel",
                    "power bi"
                ],
                "technologies": (
                    "Python, Pandas, NumPy, SQL, Excel, Power BI"
                ),
                "description": (
                    "Analyze student performance data and "
                    "create dashboards showing marks, attendance, "
                    "subjects, and performance trends."
                )
            },

            {
                "name": "🌐 REST API Task Manager",
                "skills": [
                    "python",
                    "javascript",
                    "node.js",
                    "sql",
                    "git",
                    "github"
                ],
                "technologies": (
                    "Python/Node.js, JavaScript, SQL, REST API, "
                    "Git, GitHub"
                ),
                "description": (
                    "Create a task management application with "
                    "REST APIs for creating, updating, deleting, "
                    "and tracking tasks."
                )
            }

        ]

        # Calculate project relevance
        recommended_projects = []

        for project in project_database:

            matched_project_skills = []

            for skill in project["skills"]:

                if skill in missing_skills:
                    matched_project_skills.append(skill)

            # Also consider skills already present
            existing_project_skills = []

            for skill in project["skills"]:

                if skill in matching_skills:
                    existing_project_skills.append(skill)

            relevance_score = (
                len(matched_project_skills) * 2
                + len(existing_project_skills)
            )

            if relevance_score > 0:

                recommended_projects.append(
                    (
                        relevance_score,
                        project,
                        matched_project_skills,
                        existing_project_skills
                    )
                )

        # Sort projects by relevance
        recommended_projects.sort(
            key=lambda x: x[0],
            reverse=True
        )

        # Display recommendations
        if recommended_projects:

            st.write(
                "### 🎯 Recommended Projects for This Job"
            )

            for index, (
                score,
                project,
                matched_project_skills,
                existing_project_skills
            ) in enumerate(
                recommended_projects[:3],
                start=1
            ):

                st.markdown(
                    f"### {index}. {project['name']}"
                )

                st.write(
                    f"**Description:** "
                    f"{project['description']}"
                )

                st.write(
                    f"**Technologies:** "
                    f"{project['technologies']}"
                )

                if matched_project_skills:

                    st.write(
                        "🔴 **Missing skills this project can help "
                        "you develop:** "
                        + ", ".join(
                            matched_project_skills
                        )
                    )

                if existing_project_skills:

                    st.write(
                        "🟢 **Skills you already have that this "
                        "project can demonstrate:** "
                        + ", ".join(
                            existing_project_skills
                        )
                    )

                st.write("---")

        else:

            st.info(
                "No project recommendation could be generated "
                "from the detected skills."
            )

        # Personalized next-step message
        st.write(
            "### 📌 Project Strategy"
        )

        if missing_skills:

            st.info(
                "Build projects that genuinely demonstrate "
                "your missing skills. After completing a project, "
                "add the technologies you actually used to your "
                "resume and GitHub repository."
            )

        else:

            st.success(
                "🎉 Your resume covers the detected job skills. "
                "Focus on building strong projects that demonstrate "
                "real-world implementation."
            )