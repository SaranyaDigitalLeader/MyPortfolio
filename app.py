import streamlit as st
import plotly.graph_objects as go

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title='Saranya Somasundaram Portfolio',
    layout='wide'
)

# ---------- CUSTOM CSS FOR PROFESSIONAL LOOK ----------
st.markdown(
    """
    <style>
    body {
        background-color: #101C2C;
    }
    .metric-card {
        background: #192841;
        border-radius: 15px;
        padding: 1.2em 1em 1.2em 1em;
        box-shadow: 0 2px 12px rgba(16,28,44,0.08);
        color: #FFFFFF !important;
        text-align: center !important;
        min-height: 88px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        width: 100%;
        max-width: 340px;
        margin-left: auto;
        margin-right: auto;
    }
    .metric-header {
        font-size: 1.15rem;
        font-weight: 700;
        color: #60A3D9;
        margin-bottom: 0.18em;
        letter-spacing: 0.7px;
    }
    .metric-value {
        font-size: 1.35rem;
        font-weight: 700;
        color: #F1B43C;
        line-height: 1.1em;
        white-space: nowrap;
    }
    .section-title {
        font-size: 2rem !important;
        font-weight: 900;
        margin-bottom: 0.7em;
        color: #81C3D7;
    }
    .product-card {
        background: #23334d;
        border-radius: 13px;
        padding: 1.25em 1em 1.25em 1em;
        color: #fff;
        min-height: 190px;
        box-shadow: 0 1px 8px rgba(60, 80, 120, 0.06);
        margin-bottom: 0.7em;
        text-align: center;
    }
    hr {
        border-top: 1px solid #203044;
        margin-top: 2.5em;
        margin-bottom: 2em;
    }
    .sidebar-content {
        color: #112D4E !important;
        font-size: 1rem;
        padding-top: .5rem;
        padding-bottom: .5rem;
    }
    /* Responsive metric card width for consistent sizing */
    @media (max-width: 1400px) {
        .metric-card {
            max-width: 255px;
            min-width: 180px;
        }
    }
    @media (max-width: 950px) {
        .metric-card {
            padding: 1.2em 0.5em 1.2em 0.5em;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- SIDEBAR ----------
with st.sidebar:
    
    st.markdown(
        """
        <div class="sidebar-content">
        <h2 style='font-weight:800; color:#60A3D9;'>Saranya Somasundaram <br> PMP | CSPO | CSM</h2>
        <p><b>Location:</b> Basking Ridge, New Jersey</p>
        <p><b>Email:</b> <a style="color:#F2BE49;" href="mailto:saranyasovib@gmail.com">saranyasovib@gmail.com</a></p>
        <p><b>LinkedIn:</b> <a style="color:#F1B43C;" href="https://www.linkedin.com/in/saranyasomasundaram/" target="_blank">linkedin.com/in/saranyasomasundaram</a></p>
        <br>
        <h3 style='font-weight:700; color:#F2BE49;'>Engineering-Led Execution</h3>
        <p> 
        <b>Technical edge is my North Star</b><br>
        - Use technical literacy to vet estimations<br>
        - Identify hidden risks before they become bottlenecks<br>
        - Act as a high-fidelity bridge between business & engineering<br>
        <br>
        Objective: High-quality, predictable delivery backed by architectural rigor.
    
</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# ---------- PORTFOLIO HEADER ----------
st.markdown("<div class='section-title'>Strategic Digital Leader And Technical Product Ownership</div>",unsafe_allow_html=True)



# ---------- HIGH IMPACT HEADER (METRICS) ----------
col1, col2, col3 = st.columns([1, 1, 1], gap="large")
with col1:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-header">Order Speed</div>
            <div class="metric-value">60% Faster Orders</div>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-header">Quality</div>
            <div class="metric-value">15% Defect Reduction</div>
        </div>
        """, unsafe_allow_html=True)
with col3:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-header">Efficiency</div>
            <div class="metric-value">30+ Hrs Saved/Week</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ---------- INNOVATION SPOTLIGHT (STAR STORIES 2x2 GRID) ----------
st.markdown("<div class='section-title'>Innovation Spotlight: Impact Stories</div>", unsafe_allow_html=True)
spotlight_col0, spotlight_col1 = st.columns(2, gap="large")

# --------- 1st ROW ---------
with spotlight_col0:
    st.markdown(
        """
        <div class="product-card" style="min-height:340px;">
            <h4 style="color:#60A3D9;font-weight:700;">Metadata-Driven UI Orchestration</h4>
            <ul>
                <li><b>Situation:</b> Custom client forms required code changes/deployments for every variation.</li>
                <li><b>Task:</b> Decouple UI logic from core codebase for rapid, data-driven configuration.</li>
                <li><b>Action:</b> Directed metadata-driven configuration layer; admins toggle fields/validation without deployments.</li>
                <li><b>Result:</b> <b>Enabled instant Push-to-Live UI updates, eliminated onboarding delays.</b></li>
            </ul>
        </div>
        """, unsafe_allow_html=True
    )

with spotlight_col1:
    st.markdown(
        """
        <div class="product-card" style="min-height:340px;">
            <h4 style="color:#60A3D9;font-weight:700;">System-Driven Technical Mapping (NC/NCI)</h4>
            <ul>
                <li><b>Situation:</b> Agents used 'cheatsheets' for complex network codes, risking errors.</li>
                <li><b>Task:</b> Automate code lookup into a system-driven process.</li>
                <li><b>Action:</b> Developed backend engine; auto-maps technical codes based on user input.</li>
                <li><b>Result:</b> <b>Eliminated errors and 100% provisioning accuracy.</b></li>
            </ul>
        </div>
        """, unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# --------- 2nd ROW ---------
spotlight_col2, spotlight_col3 = st.columns(2, gap="large")

with spotlight_col2:
    st.markdown(
        """
        <div class="product-card" style="min-height:380px;">
            <h4 style="color:#60A3D9;font-weight:700;">Intelligent Order Cloning (SaveAs)</h4>
            <ul>
                <li><b>Situation:</b> Users wasted ~8 min on repeat orders, causing errors.</li>
                <li><b>Task:</b> Launch feature to reduce manual labor per order.</li>
                <li><b>Action:</b> Shadowed users, designed 'Intelligent SaveAs' that clones static data, clears technical fields.</li>
                <li><b>Result:</b> <b>Reduced order time by 60% (8min → 2min); reclaimed 30+ hours/week.</b></li>
            </ul>
        """, unsafe_allow_html=True
    )
    # Bar chart for 8 min vs 2 min
    saveas_fig = go.Figure(
        data=[
            go.Bar(
                x=['Before SaveAs', 'With SaveAs'],
                y=[8, 2],
                marker_color=['#60A3D9', '#F1B43C'],
                text=['8 min', '2 min'],
                textposition='auto'
            )
        ]
    )
    saveas_fig.update_layout(
        xaxis_title="", yaxis_title="Order Creation Time (minutes)",
        plot_bgcolor='#23334d',
        paper_bgcolor='#23334d',
        font_color='#EEF3FA',
        bargap=0.5,
        margin=dict(l=20, r=20, t=30, b=10),
        height=160
    )
    saveas_fig.update_xaxes(
        tickfont=dict(size=13, color='#EEF3FA'),
        linecolor='#CCCCCC',
    )
    saveas_fig.update_yaxes(
        range=[0, 10],
        tickfont=dict(size=13, color='#EEF3FA'),
        linecolor='#CCCCCC',
        gridcolor='#334060'
    )
    st.plotly_chart(saveas_fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with spotlight_col3:
    st.markdown(
        """
        <div class="product-card" style="min-height:380px;">
            <h4 style="color:#60A3D9;font-weight:700;">Strategic Stakeholder Negotiation</h4>
            <ul>
                <li><b>Situation:</b> 10 new required fields risked 20% more order time.</li>
                <li><b>Task:</b> Balance data integrity with user experience.</li>
                <li><b>Action:</b> Proved 6 fields backend-populatable;
                 negotiated only 4 required manually.</li>
                <li><b>Result:</b> <b>Maintained bottleneck at 5% vs projected 20%.</b></li>
            </ul>
        """, unsafe_allow_html=True
    )
    # Efficiency Metric Bar (5% vs 20%)
    negotiation_fig = go.Figure(
        data=[
            go.Bar(
                x=['Negotiated', 'Original Ask'],
                y=[5, 20],
                marker_color=['#81C3D7', '#E36414'],
                text=['5%', '20%'],
                textposition='auto'
            )
        ]
    )
    negotiation_fig.update_layout(
        xaxis_title="",
        yaxis_title="Order Time Increase",
        plot_bgcolor='#23334d',
        paper_bgcolor='#23334d',
        font_color='#EEF3FA',
        bargap=0.5,
        margin=dict(l=20, r=20, t=30, b=10),
        height=160
    )
    negotiation_fig.update_xaxes(
        tickfont=dict(size=13, color='#EEF3FA'),
        linecolor='#CCCCCC',
    )
    negotiation_fig.update_yaxes(
        range=[0, 22],
        tickfont=dict(size=13, color='#EEF3FA'),
        linecolor='#CCCCCC',
        gridcolor='#334060'
    )
    st.plotly_chart(negotiation_fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ---------- PRODUCT PORTFOLIO (4-COLUMN GRID) ----------
st.markdown("<div class='section-title'>Razorflow Product Portfolio</div>", unsafe_allow_html=True)
prod_col1, prod_col2, prod_col3, prod_col4 = st.columns(4, gap="large")

with prod_col1:
    st.markdown(
        """
        <div class="product-card">
            <h5 style="color:#F1B43C; font-weight: 700;">Common Ordering Solution (Flagship)</h5>
            <ul style="text-align:left;">
                <li>API-first global platform for enterprise ordering</li>
                <li>End-to-end product management: strategy to launch</li>
                <li>Modernized telecom ordering with architectural rigor</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with prod_col2:
    st.markdown(
        """
        <div class="product-card">
            <h5 style="color:#F1B43C; font-weight: 700;">Virtual Front Office (VFO)</h5>
            <ul style="text-align:left;">
                <li>Legacy telecom ordering solution/UX</li>
                <li>Led platform maintenance and feature evolution</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with prod_col3:
    st.markdown(
        """
        <div class="product-card">
            <h5 style="color:#F1B43C; font-weight: 700;">ConnectNX Integration</h5>
            <ul style="text-align:left;">
                <li>Seamless sync between ordering & billing (ConnectNX)</li>
                <li>APIs for end-to-end data interoperability</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with prod_col4:
    st.markdown(
        """
        <div class="product-card">
            <h5 style="color:#F1B43C; font-weight: 700;">ExpenseNX Integration</h5>
            <ul style="text-align:left;">
                <li>Cross-suite integration for expense management</li>
                <li>Ensured smooth enterprise workflows</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)