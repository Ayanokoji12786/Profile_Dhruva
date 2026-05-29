
import streamlit as st
import re

st.set_page_config(
    page_title='My Portfolio',
    page_icon='🚀',
    layout='wide'
)

st.title('Welcome to My Portfolio 🚀')
st.header('Aspiring AI Engineer | SAT & STEM Scholar')

st.write("Hi, I'm Dhruva, an 11th-grade student passionate about Artificial Intelligence, mathematics, physics, and software development. I enjoy building projects that combine creativity, problem-solving, and technology.")

st.markdown(':green[This portfolio highlights my projects, technical skills, research interests, and academic journey. It reflects my passion for continuous learning, innovation, and building impactful solutions through technology.]')

st.divider()

with st.sidebar:

    st.header('Dhruva')

    st.image('/Users/MAC/Desktop/py learning folder 2/GIT Hub project final/PHOTO-2026-05-29-16-03-12.jpg')

    st.caption('🎓 | 11th Grade Student')
    st.caption('🚀 | AI Enthusiast')

    st.markdown('---')

    st.subheader('📞 Contact')

    st.write('dhruvanerella3@gmail.com')
    st.write('**Phone:** +91-9877238490')

    st.markdown('[📍 Hyderabad, Telangana](https://maps.app.goo.gl/t4d5sk9gthZp74a59)')

    st.divider()

    st.write('**Academics**')
    st.write('**- College:** Resonance')
    st.write('**- Board:** Telangana IPE')
    st.write('**- Stream:** MPC (Physics, Chemistry, Mathematics)')
    st.write('**- Expected Graduation:** 2027')

    st.write('**Languages:**')
    st.write(' - English')
    st.write(' - Telugu')
    st.write(' - Hindi')

    st.divider()

    st.markdown(':green[**Connect with me:**]')

    C1, C2, C3 = st.columns(3)

    with C1:
        st.markdown('[![Github](https://img.icons8.com/color/96/000000/github.png)](https://github.com/Ayanokoji12786)')
            

    with C2:
        st.markdown('[![WhatsApp](https://img.icons8.com/color/96/000000/whatsapp.png)](https://wa.me/916301297528)')

    with C3:
        st.markdown('[![Instagram](https://img.icons8.com/color/96/000000/instagram-new.png)](https://www.instagram.com/dhruvanerella12/)')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Projects', 'Bio-Data', 'Academics', 'Contact','Academic-History'])


with tab1:
    c1, c2 = st.columns(2)
 
    with c1:
 
        st.subheader('- **BMI Calculator**')
 
        st.write("**What is BMI?** 📊")
        st.write("Body Mass Index (BMI) is a measure of body fat based on height and weight. It's a simple screening tool to identify possible weight problems in adults.")
 
        st.write("**The Formula:** 📐")
        st.write("BMI = Weight (kg) / Height (m)²")
 
        st.write("**How I Built It:** 🛠️")
        st.write("This calculator was built using Python and Streamlit. It takes your weight and height as inputs, converts height to meters, and calculates your BMI using the standard formula. The result is then categorized into different health categories.")
 
    with c2:
 
        with st.expander('Click here to use the calculator'):
            st.subheader("BMI Calculator ⚖️")
            st.write("Calculate your Body Mass Index (BMI)")
 
            col1, col2 = st.columns(2)
 
            with col1:
                weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1, key="bmi_weight")
 
            with col2:
                height = st.number_input("Enter your height (cm):", min_value=1.0, step=0.1, key="bmi_height")
 
            if st.button("Calculate BMI", use_container_width=True, key="bmi_btn"):
 
                height_m = height / 100
                bmi = weight / (height_m ** 2)
 
                st.subheader(f"Your BMI: {bmi:.2f}")
 
                if bmi < 18.5:
                    st.info("📍 Underweight - BMI < 18.5")
 
                elif 18.5 <= bmi < 25:
                    st.success("✅ Normal Weight - BMI 18.5-24.9")
 
                elif 25 <= bmi < 30:
                    st.warning("⚠️ Overweight - BMI 25-29.9")
 
                else:
                    st.error("❌ Obese - BMI ≥ 30")
    st.divider()
 
 
    a1, a2 = st.columns(2)
 
    with a1:
 
        st.subheader('- **Unit Conversion Calculator**')
 
        st.write("**What is Unit Conversion?** 🌍")
        st.write("Unit conversion is the process of converting a quantity expressed in one unit of measurement to another unit of the same type. It's essential in science, engineering, cooking, and everyday life.")
 
        st.write("**Key Conversion Formulas:** 📐")
        st.write("Temperature: °F = (°C × 9/5) + 32")
        st.write("Weight: 1 kg = 2.20462 lbs")
        st.write("Length: 1 m = 3.28084 ft")
 
        st.write("**How I Built It:** 🛠️")
        st.write("This converter was built using Python and Streamlit with dropdown menus for selecting conversion types. It provides real-time conversions for temperature, weight, and length with high precision calculations.")
 
    with a2:
 
        with st.expander('Click here to use the converter'):
            st.subheader("Unit Converter 📏")
 
            conversion_type = st.selectbox(
                "Choose conversion type:",
                ["Temperature", "Weight", "Length"],
                key="conversion_type"
            )
 
            value = st.number_input("Enter the value:", key="converter_value")
 
            if conversion_type == "Temperature":
 
                option = st.selectbox(
                    "Choose conversion:",
                    ["Celsius to Fahrenheit", "Fahrenheit to Celsius"],
                    key="temp_option"
                )
 
                if st.button("Convert", key="temp_btn"):
 
                    if option == "Celsius to Fahrenheit":
                        result = (value * 9/5) + 32
                        st.success(f"Converted Value: {result:.2f} °F")
 
                    else:
                        result = (value - 32) * 5/9
                        st.success(f"Converted Value: {result:.2f} °C")
 
            elif conversion_type == "Weight":
 
                option = st.selectbox(
                    "Choose conversion:",
                    ["Kilograms to Pounds", "Pounds to Kilograms"],
                    key="weight_option"
                )
 
                if st.button("Convert", key="weight_btn"):
 
                    if option == "Kilograms to Pounds":
                        result = value * 2.20462
                        st.success(f"Converted Value: {result:.2f} lbs")
 
                    else:
                        result = value / 2.20462
                        st.success(f"Converted Value: {result:.2f} kg")
 
            elif conversion_type == "Length":
 
                option = st.selectbox(
                    "Choose conversion:",
                    ["Meters to Feet", "Feet to Meters"],
                    key="length_option"
                )
 
                if st.button("Convert", key="length_btn"):
 
                    if option == "Meters to Feet":
                        result = value * 3.28084
                        st.success(f"Converted Value: {result:.2f} ft")
 
                    else:
                        result = value / 3.28084
                        st.success(f"Converted Value: {result:.2f} m")
    st.divider()
    d1, d2 = st.columns(2)
 
    with d1:
 
        st.subheader('- **Password Strength Checker**')
 
        st.write("**What is Password Strength?** 🔐")
        st.write("Password strength is a measure of how effective a password is at resisting guessing and brute-force attacks. A strong password includes uppercase, lowercase, numbers, and special characters.")
 
        st.write("**How It Works:** 🛠️")
        st.write("Type a password and the app will check it against criteria like length (8+ characters), numbers, uppercase letters, and special characters. It displays real-time visual feedback with color coding.")
 
        st.write("**Feedback System:** 📊")
        st.write("Red (Weak) - Few criteria met | Orange (Medium) - Most criteria met | Green (Strong) - All criteria met")
 
    with d2:
 
        with st.expander('Click here to check password strength'):
            st.subheader("Password Strength Checker 🔐")
 
            import re
 
            password = st.text_input("Enter a password:", type="password", key="password_input")
 
            if password:
                strength = 0
                feedback = []
 
                if len(password) >= 8:
                    strength += 1
                else:
                    feedback.append("❌ Password should be at least 8 characters long")
 
                if re.search(r'[A-Z]', password):
                    strength += 1
                else:
                    feedback.append("❌ Add uppercase letters (A-Z)")
 
                if re.search(r'[a-z]', password):
                    strength += 1
                else:
                    feedback.append("❌ Add lowercase letters (a-z)")
 
                if re.search(r'[0-9]', password):
                    strength += 1
                else:
                    feedback.append("❌ Add numbers (0-9)")
 
                if re.search(r'[!@#$%^&*]', password):
                    strength += 1
                else:
                    feedback.append("❌ Add special characters (!@#$%^&*)")
 
                if strength <= 2:
                    st.error("🔴 Weak Password")
                elif strength <= 3:
                    st.warning("🟠 Medium Password")
                else:
                    st.success("🟢 Strong Password")
 
                st.write(f"**Strength Score:** {strength}/5")
 
                if feedback:
                    st.write("**Suggestions:**")
                    for item in feedback:
                        st.write(item)
    st.divider()
 
    e1, e2 = st.columns(2)
 
    with e1:
 
        st.subheader('- **Expense Tracker & Budget Splitter**')
 
        st.write("**What is Expense Splitting?** 💰")
        st.write("Splitting expenses is a way to divide the total cost of a shared bill equally among group members, often including a tip percentage.")
 
        st.write("**How It Works:** 🛠️")
        st.write("Enter the total bill amount, number of people, and tip percentage. The app instantly calculates how much each person should pay including their share of the tip.")
 
        st.write("**Features:** 📊")
        st.write("Real-time calculation | Adjustable tip with slider | Per-person breakdown")
 
    with e2:
 
        with st.expander('Click here to split expenses'):
            st.subheader("Expense Tracker & Budget Splitter 💳")
 
            total_bill = st.number_input("Enter total bill amount (₹):", min_value=0.0, key="total_bill")
 
            num_people = st.number_input("Number of people:", min_value=1, step=1, key="num_people")
 
            tip_percentage = st.slider("Tip percentage (%):", 0, 30, 15, key="tip_slider")
 
            if st.button("Calculate Split", key="split_btn"):
                tip_amount = (total_bill * tip_percentage) / 100
                total_with_tip = total_bill + tip_amount
                per_person = total_with_tip / num_people
 
                st.info(f"💵 Bill Amount: ₹{total_bill:.2f}")
                st.info(f"🎁 Tip Amount (₹{tip_percentage}%): ₹{tip_amount:.2f}")
                st.success(f"✅ Total Amount: ₹{total_with_tip:.2f}")
                st.success(f"👤 Per Person: ₹{per_person:.2f}")
    st.divider()
 
    f1, f2 = st.columns(2)
 
    with f1:
 
        st.subheader('- **Random Word / Quote Generator**')
 
        st.write("**What is Quote Generator?** 💡")
        st.write("A quote generator is a fun utility that displays random inspirational quotes or coding tips to motivate and inspire users.")
 
        st.write("**How It Works:** 🛠️")
        st.write("Click a button and get a random quote from a curated list. Perfect for daily motivation or finding coding inspiration.")
 
        st.write("**Features:** 📊")
        st.write("Random selection | Beautiful formatting | Multiple categories of quotes")
 
    with f2:
 
        with st.expander('Click here to generate quotes'):
            st.subheader("Random Quote Generator 🎯")
 
            import random
 
            quotes = [
                "The only way to do great work is to love what you do. - Steve Jobs",
                "Innovation distinguishes between a leader and a follower. - Steve Jobs",
                "Life is what happens when you're busy making other plans. - John Lennon",
                "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
                "It is during our darkest moments that we must focus to see the light. - Aristotle",
                "The only impossible journey is the one you never begin. - Tony Robbins",
                "Success is not final, failure is not fatal. - Winston Churchill",
                "Code is poetry written for computers. - Unknown",
                "Debugging is like being the detective in a crime drama. - Filipe Fortes",
                "The best error message is the one that never shows up. - Thomas Fuchs",
                "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
                "Everything you want is on the other side of fear. - Jack Canfield"
            ]
 
            if st.button("Generate Random Quote", key="quote_btn"):
                random_quote = random.choice(quotes)
                st.markdown(f"### ✨ {random_quote} ✨")
    st.divider()
 
    g1, g2 = st.columns(2)
 
    with g1:
 
        st.subheader('- **Simple To-Do List Application**')
 
        st.write("**What is a To-Do List?** ✅")
        st.write("A to-do list is a simple task management tool that helps you organize, track, and complete your daily tasks efficiently.")
 
        st.write("**How It Works:** 🛠️")
        st.write("Add tasks to your list, check off completed ones, and delete tasks you no longer need. Your tasks are saved as you work.")
 
        st.write("**Features:** 📊")
        st.write("Add new tasks | Mark tasks complete | Delete tasks | Real-time updates")
 
    with g2:
 
        with st.expander('Click here to manage your to-do list'):
            st.subheader("To-Do List Application ✅")
 
            if 'tasks' not in st.session_state:
                st.session_state.tasks = []
 
            new_task = st.text_input("Add a new task:", key="task_input")
 
            if st.button("Add Task", key="add_task_btn"):
                if new_task:
                    st.session_state.tasks.append({"task": new_task, "done": False})
                    st.session_state.task_input = ""
 
            if st.session_state.tasks:
                st.write("**Your Tasks:**")
                for i, item in enumerate(st.session_state.tasks):
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        done = st.checkbox(item["task"], value=item["done"], key=f"task_{i}")
                        st.session_state.tasks[i]["done"] = done
                    with col2:
                        if st.button("Delete", key=f"delete_{i}"):
                            st.session_state.tasks.pop(i)
                            st.rerun()
            else:
                st.write("No tasks yet. Add one to get started!")

with tab2:

    with st.container():

        st.subheader("👨‍💻 About Me")

        c1, c2 = st.columns([4, 1])

        with c1:

            st.markdown("""
Hey! I'm Dhruva, a student passionate about programming, Artificial Intelligence,
and building creative projects with Python and Streamlit.

I enjoy creating interactive web applications, exploring new technologies,
and continuously improving my problem-solving skills through coding and project development.

Recently, I have been working on:

- 🚀 Streamlit Web Applications
- 🤖 AI-based Projects
- 📊 Python Mini Projects
- 🌐 Portfolio & Profile Building
- 🧠 Learning Modern Development Tools

Alongside coding, I am also preparing for the SAT and focusing on building a strong
academic and technical foundation for future opportunities.

I enjoy learning through experimentation, project-building, and transforming ideas
into practical applications.

**🎯 Goals:**

- Develop strong expertise in Artificial Intelligence and Software Development
- Build impactful technology projects that solve real-world problems
- Strengthen my foundation in mathematics, physics, and computer science
- Contribute to innovative research and collaborative initiatives
- Continuously grow as a learner, programmer, and problem solver

**🌟 Personal Motto:**

> "Learning deeply, building creatively, and striving for continuous improvement."
""")

        with c2:

            st.markdown(":blue[**Dhruva**]")

            st.image("/Users/MAC/Desktop/py learning folder 2/GIT Hub project final/PHOTO-2026-05-29-16-06-19.jpg",caption="Coding, Innovation, and Continuous Learning")

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            with st.container(border=True):

                st.markdown(":orange[📋 Personal Information]")

                st.write("🎓 Grade: 12th")
                st.write("📍 Based in India")
                st.write("💻 Interests: Python, AI, Streamlit")
                st.write("🌐 Focus: AI, Web Applications, and Software Development")

        with col2:

            with st.container(border=True):

                st.markdown(":violet[🎯 Current Focus]")

                st.write("📚 Preparing for SAT")
                st.write("🚀 Building Streamlit Projects")
                st.write("🐍 Improving Python Skills")
                st.write("💡 Exploring Artificial Intelligence and Automation")

with tab3:

    with st.container(border=True):
        a1, a2 = st.columns(2)
        with a1:
            st.metric(label='Grand total', value ='460/470', delta = '97.8%')
        with a2:
            st.metric(label='Core STEM subjects', value='267/270', delta= '98.8%')

        st.header("📊 Academic Performance in CGPA")

        st.write("**Academic Progress Overview**")

        col1, col2 = st.columns([1, 3])

        with col1:
            st.write("Maths 1B")

        with col2:
            st.progress(0.98, text="73/75")

        col1, col2 = st.columns([1, 3])

        with col1:
            st.write("Maths1A")

        with col2:
            st.progress(1.00, text="75/75")

        col1, col2 = st.columns([1, 3])

        with col1:
            st.write("Physics")

        with col2:
            st.progress(0.99, text="59/60")

        col1, col2 = st.columns([1, 3])

        with col1:
            st.write("Chemistry")

        with col2:
            st.progress(1.0, text="60/60")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.subheader("📖 Core Courses")

            st.info("✅ Python Programming - Advanced")
            st.warning("✅ Streamlit Web Development")
            st.error("✅ Math, Physics and Chemistry")
            st.success("✅ AI & Automation Basics")

    with col2:

        with st.container(border=True):

            st.subheader("🏅 Certifications")

            st.info("✅ Python Fundamentals")
            st.warning("✅ Streamlit App Development")
            st.error("✅ AI Tools & Productivity")
            st.success("✅ Web App UI Design")

with tab4:

    st.subheader('Contact Me')

    st.markdown(':red[Please fill out the form below]')

    Email_validator = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    name_validator = r"^[A-Z]"

    with st.form(key="Dhruva_contact_form"):

        a, b, c = st.columns(3)

        with a:

            visitor_name = st.text_input("Enter your name:")

            email = st.text_input("Enter your email address:",placeholder="example@gmail.com")
            

            interested = st.checkbox("Interested in collaborating or connecting")
                
            

        with b:

            project_interest = st.selectbox("What are you interested in?",["--Select--","Python Projects","Streamlit Apps","AI Projects","SAT Preparation","General Collaboration"])

            skill_level = st.selectbox("Your coding level",["--Select--","Beginner", "Intermediate","Advanced"])
                    

            submit_form = st.form_submit_button("🚀 Submit", type='primary')

            if submit_form:

                email_2 = email.strip()

                if not visitor_name or not email_2:

                    st.warning("⚠️ Name and Email cannot be empty")

                elif "@" not in email_2 or ".com" not in email_2:

                    st.error("❌ Please enter a valid email address")

                elif project_interest == "--Select--":

                    st.error("❌ Please select an interest area")

                elif skill_level == '--Select--':

                    st.warning('⚠️ Please enter a valid skill level')

                else:

                    st.balloons()

                    st.success("✅ Form submitted successfully!")

                    st.info(f"Thanks for connecting, {visitor_name}!")

        with c:

            uploaded_file = st.file_uploader("Upload your project/resume (optional)")
            

    a1, b2, c3 = st.columns(3)

    a1.container(border=True).write("💻 **Main Focus:** Maths, Physics and Python & Streamlit Development")

    b2.container(border=True).write("📚 **Current Goal:** SAT Preparation & Profile Building")

    c3.container(border=True).write("🚀 **Interests:** AI, Web Apps & Creative Coding")


with tab5:
 
    st.subheader("📚 My Academic Journey")
 
    st.markdown("Here's a timeline of my educational path and achievements:")
 
    st.divider()
 
    col1, col2 = st.columns([1, 2])
 
    with col1:
        st.markdown("**🎓 Age 3**")
    with col2:
        st.markdown("Started my formal education journey, marking the beginning of my academic adventure.")
 
    st.divider()
 
    col1, col2 = st.columns([1, 2])
 
    with col1:
        st.markdown("**🏫 KG - Kindergarten**")
    with col2:
        st.markdown("**Academic Heights Public School**\nCompleted my kindergarten years at Academic Heights Public School, building a strong foundation in early learning.")
 
    st.divider()
 
    col1, col2 = st.columns([1, 2])
 
    with col1:
        st.markdown("**📖 1st - 4th Class**")
    with col2:
        st.markdown("**Vignan World One**\nStudied at Vignan World One from 1st to 4th standard, where I developed my passion for learning and academic excellence.")
 
    st.divider()
 
    col1, col2 = st.columns([1, 2])
 
    with col1:
        st.markdown("**🌈 5th Grade**")
    with col2:
        st.markdown("**Rainbow School**\nContinued my education at Rainbow School, where I explored diverse subjects and grew my interest in science and mathematics.")
 
    st.divider()
 
    col1, col2 = st.columns([1, 2])
 
    with col1:
        st.markdown("**📚 6th - 10th Class**")
    with col2:
        st.markdown("**Vignan Vidyalayam**\nCompleted my secondary education at Vignan Vidyalayam. During this period, I achieved a strong academic record with **93% in 10th grade**.")
 
    st.divider()
 
    col1, col2 = st.columns([1, 2])
 
    with col1:
        st.markdown("**🎓 11th - 12th Grade**")
    with col2:
        st.markdown("**Resonance Coaching Institute**\nCurrently studying at Resonance, focusing on MPC stream (Physics, Chemistry, Mathematics) with preparation for JEE and SAT exams.")
 
    st.divider()
 
    st.subheader("🏆 Achievements & Recognition")
 
    col1, col2, col3 = st.columns(3)
 
    with col1:
        with st.container(border=True):
            st.markdown("### 🌟 Student of the Year")
            st.write("Awarded for outstanding academic performance, character, and contribution to school activities.")
 
    with col2:
        with st.container(border=True):
            st.markdown("### 🥋 National Level Kung Fu Championship")
            st.write("Competed at the national level in Kung Fu, demonstrating discipline, dedication, and physical excellence.")
 
    with col3:
        with st.container(border=True):
            st.markdown("### 🏅 Inter-School Athletics Medals")
            st.write("Won multiple medals in inter-school level athletics competitions, excelling in various sports events.")
 
    st.divider()
 
    st.subheader("🏅 Academic Recognition")
 
    col1, col2 = st.columns(2)
 
    with col1:
        with st.container(border=True):
            st.markdown("### 📊 SOF Science Olympiad")
            st.write("Participated and performed well in the Science Olympiad Foundation (SOF) examination, showcasing strong problem-solving skills and scientific knowledge.")
 
    with col2:
        with st.container(border=True):
            st.markdown("### 📈 10th Grade Performance")
            st.write("**Score: 93%**\n\nAchieved excellent grades in 10th standard, demonstrating consistent academic excellence and mastery of core subjects.")
 
    st.divider()
 
    st.markdown("### 💡 Key Takeaways")
    st.write("✅ Consistent academic excellence across all educational institutions")
    st.write("✅ Strong foundation in core subjects (Mathematics, Science, English)")
    st.write("✅ Well-rounded personality with achievements in sports and co-curricular activities")
    st.write("✅ Discipline, dedication, and determination reflected in all endeavors")
    st.write("✅ Continuous growth mindset and passion for learning")


st.markdown('---')

st.caption("© 2026 Dhruva | Built with Python & Streamlit | Last Updated: May 2026")

st.caption("Dedicated to continuous learning, innovation, and building meaningful technology projects.")



