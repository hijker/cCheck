"""
CV Generator — Jacob Tomy  (single-page, best-of-three)
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_JUSTIFY, TA_LEFT

# ── palette ───────────────────────────────────────────────────────────────────
RED      = colors.HexColor("#C0392B")
DARK     = colors.HexColor("#1A1A2E")
GREY     = colors.HexColor("#555555")

PAGE_W, PAGE_H = A4
ML = 15*mm;  MR = 15*mm;  MT = 10*mm;  MB = 8*mm
BW = PAGE_W - ML - MR          # body width

# ── style shorthand ───────────────────────────────────────────────────────────
def S(name, **kw):
    d = dict(fontName="Helvetica", fontSize=8.2, leading=11.5,
             textColor=DARK, spaceAfter=0, spaceBefore=0,
             leftIndent=0, rightIndent=0)
    d.update(kw)
    return ParagraphStyle(name, **d)

NAME    = S("N",  fontName="Helvetica-Bold", fontSize=20, leading=24,
            textColor=DARK, alignment=TA_CENTER)
TAGLINE = S("TL", fontSize=8.8, textColor=GREY,  alignment=TA_CENTER, leading=12)
CONTACT = S("CT", fontSize=8,   textColor=RED,   alignment=TA_CENTER, leading=11)
SUMMARY = S("SU", fontSize=8.3, textColor=GREY,  leading=12.2, alignment=TA_LEFT)

SEC     = S("SC", fontName="Helvetica-Bold", fontSize=9.5, textColor=RED,
            spaceBefore=3, spaceAfter=1)

CO_NAME = S("CN", fontName="Helvetica-Bold", fontSize=8.8, textColor=RED)
CO_DOM  = S("CD", fontName="Helvetica-Oblique", fontSize=7.5, textColor=GREY, leading=10.5)
R_TITLE  = S("RT",  fontName="Helvetica-Bold", fontSize=8.5, textColor=DARK)
R_TITLE2 = S("RT2", fontName="Helvetica-Bold", fontSize=8.5, textColor=DARK, leading=11.5)
R_DATE   = S("RD",  fontSize=8.5, textColor=GREY, alignment=TA_RIGHT)
STACK   = S("ST", fontName="Helvetica-Oblique", fontSize=8, textColor=GREY,
            leading=11, spaceAfter=2)
BUL     = S("BL", fontSize=8.2, leading=11.2, leftIndent=8, spaceAfter=0.8, alignment=TA_LEFT)

SK_KEY  = S("SKK", fontName="Helvetica-Bold", fontSize=8.3, leading=11.5)
SK_VAL  = S("SKV", fontSize=8.3, textColor=GREY, leading=11.5)

AW      = S("AW", fontSize=8, leading=11, leftIndent=0, spaceAfter=1)

EDU_I   = S("EI", fontName="Helvetica-Bold", fontSize=8.5)
EDU_D   = S("ED", fontName="Helvetica-Oblique", fontSize=8, textColor=GREY)

# ── helpers ───────────────────────────────────────────────────────────────────
def sec(title):
    return [Paragraph(title.upper(), SEC),
            HRFlowable(width=BW, thickness=0.55, color=RED, spaceAfter=2)]

def role_block(co, dom, t1, d1, t2=None, d2=None):
    """Flat 2-row table: col0=company/domain, col1=title, col2=date.
    All columns share the same physical rows — no nested table height mismatch."""
    col_w = [BW * 0.20, BW * 0.57, BW * 0.23]

    row0 = [Paragraph(f"<b>{co}</b>",   CO_NAME),
            Paragraph(f"<b>{t1}</b>",   R_TITLE),
            Paragraph(d1,               R_DATE)]

    if t2 and d2:
        row1 = [Paragraph(dom,  CO_DOM),
                Paragraph(t2,   R_TITLE2),
                Paragraph(d2,   R_DATE)]
        data = [row0, row1]
    else:
        row1 = [Paragraph(dom,  CO_DOM),
                Paragraph("",   R_TITLE2),
                Paragraph("",   R_DATE)]
        data = [row0, row1]

    tbl = Table(data, colWidths=col_w)
    tbl.setStyle(TableStyle([
        ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING",  (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING",   (0, 0), (-1, -1), 1),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 1),
    ]))
    return tbl

def b(txt):
    return Paragraph(f"&#x2022; {txt}", BUL)

def build(out=None, intl=True):
    """Generate CV.
    intl=True  → includes IIT context note (for international recruiters)
    intl=False → omits IIT context note (for Indian recruiters who know IIT)
    """
    if out is None:
        out = "cv/jacob_tomy_cv_intl.pdf" if intl else "cv/jacob_tomy_cv.pdf"

    doc = SimpleDocTemplate(out, pagesize=A4,
                            leftMargin=ML, rightMargin=MR,
                            topMargin=MT, bottomMargin=MB,
                            title="Jacob Tomy — CV", author="Jacob Tomy")
    s = []

    # HEADER
    s += [Paragraph("JACOB TOMY", NAME), Spacer(1,2),
          Paragraph("Senior Software Development Engineer  \u00b7  Backend  \u00b7  7 Years Experience", TAGLINE),
          Spacer(1,2),
          Paragraph("jacobtomy721@gmail.com  \u00b7  linkedin.com/in/jacob-tomy  \u00b7  Bengaluru, India", CONTACT),
          Spacer(1,3),
          HRFlowable(width=BW, thickness=1.1, color=RED, spaceAfter=3)]

    # SUMMARY
    s.append(Paragraph(
        "Backend-focused Senior SDE with 7 years building high-throughput distributed systems at Walmart and "
        "Clari. Specialised in event-driven architectures (Kafka), cloud-native deployments (Azure/Kubernetes), "
        "and applied Generative AI \u2014 shipping LLM-powered tooling and NL2SQL products. "
        "Track record of measurable impact \u2014 20\u00d7 latency reductions, 40% storage savings \u2014 "
        "while driving cross-team technical standards and mentoring engineers.",
        SUMMARY))
    s.append(Spacer(1,4))

    # EXPERIENCE
    s += sec("Experience")

    # Walmart — bullets ordered: Staff cross-team signals first, then impact metrics, then ops/leadership
    s.append(role_block("Walmart Global Tech","E-Commerce \u00b7 Retail",
                        "Senior Software Development Engineer","2024 \u2013 Present",
                        "Software Development Engineer III","2022 \u2013 2024"))
    s.append(Paragraph(
        "Java 21 \u00b7 Spring Boot 3.x \u00b7 Kafka \u00b7 Cosmos DB \u00b7 Kubernetes \u00b7 Azure \u00b7 Redis \u00b7 Python \u00b7 LLMs",
        STACK))
    for t in [
        # ── Staff signals: cross-team ownership & platform-wide influence ──────
        "<b>API Contract Ownership:</b> Authored Kafka payload schemas and HLD/LLD docs "
        "(service interactions, data flow diagrams) adopted by upstream/downstream teams on a "
        "<b>20-engineer platform</b> processing <b>6K OPM</b> avg, <b>40K OPM</b> at peak.",
        "<b>Java 21 Migration:</b> Migrated Java 8/11 \u2192 Java 21 + Spring Boot 3.x (virtual threads); "
        "guided <b>3 teams</b> through the same upgrade and standardised BOM adoption across the platform.",
        # ── High-impact technical achievements ────────────────────────────────
        "<b>AI On-Call Agent:</b> GPT-4o-powered Slack bot that surfaces runbook excerpts, incident history "
        "and live dependency state to on-call engineers \u2014 cutting mean time to resolution by <b>60%</b>.",
        "<b>Real-time Order Amendment:</b> Synchronised mid-delivery add-item flow across multiple backend services, "
        "slashing amendment latency from <b>400\u202fms \u2192 20\u202fms</b>.",
        "<b>Custom Dictionary Compression:</b> zstd-based layer for high-volume Cosmos DB payloads; "
        "achieved <b>40% storage reduction</b>, significantly lowering Azure cloud spend.",
        "<b>Priority Kafka Pipeline:</b> Dedicated pipeline isolating express-order traffic "
        "\u2014 routing <b>300+ OPM of express orders</b> at zero additional infrastructure cost.",
        # ── Product & operational ─────────────────────────────────────────────
        "<b>Pay for Speed:</b> End-to-end premium delivery feature enabling faster fulfilment tiers, "
        "directly contributing to Walmart\u2019s quick-commerce revenue growth.",
        "<b>Container Security &amp; CI/CD:</b> Hardened <b>25+ microservices</b>, tightened Docker "
        "configs and pipelines \u2014 <b>50% faster startup</b>, <b>30% lower resource usage</b>.",
        "<b>Team Leadership:</b> Led 3 junior engineers through feature planning, system-design "
        "mentorship, and code reviews \u2014 consistent on-time sprint delivery.",
    ]:
        s.append(b(t))
    s.append(Spacer(1,3))

    # Clari
    s.append(role_block("Clari","Revenue Intelligence \u00b7 CRM",
                        "Software Development Engineer II","2021 \u2013 2022",
                        "Software Development Engineer I","2019 \u2013 2021"))
    s.append(Paragraph("Java 8 \u00b7 Spring Boot \u00b7 PostgreSQL \u00b7 MongoDB \u00b7 AWS", STACK))
    for t in [
        "<b>Autocapture Engine:</b> Automated activity-capture system with intelligent CRM matching "
        "\u2014 live across <b>200+ enterprise organisations</b>.",
        "<b>Workspace Integrations:</b> Integrated G Suite and Outlook into Clari, ingesting emails "
        "and calendar events to surface revenue insights and meeting summaries for <b>500K+ end users</b>.",
        "<b>Performance &amp; Reliability:</b> Overhauled exception handling (10% CPU reduction, "
        "improved cron accuracy); tuned REST endpoints reducing <b>p99 latency</b> on AWS.",
    ]:
        s.append(b(t))
    s.append(Spacer(1,4))

    # SKILLS
    s += sec("Skills")
    skills = [
        ("Languages &amp; Frameworks", "Java (8, 17, 21),  Spring Boot (2.7, 3.x),  Python,  ReactJS"),
        ("Distributed Systems",        "Kafka,  Kubernetes,  Docker,  REST APIs,  Redis,  Elasticsearch"),
        ("Cloud &amp; Infra",          "Azure,  AWS,  CI/CD (Looper),  Prometheus,  Grafana"),
        ("Databases",                  "Cosmos DB,  PostgreSQL,  MongoDB,  Cassandra"),
        ("AI &amp; Tooling",           "LLMs,  LangGraph,  NL2SQL,  AI Agents,  Claude Code"),
        ("Design &amp; Delivery",      "HLD,  LLD,  API Contracts,  UML,  JIRA,  Agile / Scrum"),
    ]
    # Single-column skills layout
    sk_rows = [[Paragraph(k, SK_KEY), Paragraph(v, SK_VAL)] for k, v in skills]
    sk_table = Table(sk_rows, colWidths=[BW * 0.30, BW * 0.70])
    sk_table.setStyle(TableStyle([
        ("LEFTPADDING",  (0,0),(-1,-1), 0), ("RIGHTPADDING",(0,0),(-1,-1), 3),
        ("TOPPADDING",   (0,0),(-1,-1), 0.5), ("BOTTOMPADDING",(0,0),(-1,-1), 0.5),
        ("VALIGN",       (0,0),(-1,-1), "TOP"),
    ]))
    s.append(sk_table)
    s.append(Spacer(1,4))

    # ACHIEVEMENTS  — 2-column layout
    s += sec("Achievements")
    ach = [
        ("\u2605\u2605 <b>2nd Prize \u2014 lablab.ai Global AI Hackathon (2026)</b>",
         "NL2SQL + LangGraph enterprise dashboard with real-time alert engine."),
        ("\u2605 <b>Excellence Award (2025) \u2014 Walmart</b>",
         "zstd compression: 40% Cosmos DB storage reduction, lower Azure spend."),
        ("\u2605 <b>Bravo Award (2025) \u2014 Walmart</b>",
         "GPT-4o on-call agent surfacing live incident context, cutting MTTR by 60%."),
        ("\u2605 <b>Excellence Award (2024) \u2014 Walmart</b>",
         "Priority Kafka pipeline \u2014 100% of express orders, zero extra cost."),
        ("\u25cf <b>Walmart Global Techathon \u2014 Runner-Up (2022)</b>",
         "Cart-based nutritional recommendation product for Walmart customers."),
        ("\u25cf <b>Clari Innovates Hackathon \u2014 Winner (2021)</b>",
         "Revamped internal tooling platform, adopted company-wide."),
    ]
    ach_style = S("ACH", fontSize=8.3, leading=11.8, leftIndent=0, spaceAfter=0.5,
                  alignment=TA_LEFT)
    aw_rows = []
    for i in range(0, len(ach), 2):
        left_ach  = Paragraph(f"{ach[i][0]}: {ach[i][1]}", ach_style)
        right_ach = Paragraph(f"{ach[i+1][0]}: {ach[i+1][1]}", ach_style) if i+1 < len(ach) else Paragraph("", ach_style)
        aw_rows.append([left_ach, right_ach])

    aw_table = Table(aw_rows, colWidths=[BW*0.497, BW*0.497],
                     hAlign="LEFT", spaceBefore=0)
    aw_table.setStyle(TableStyle([
        ("LEFTPADDING",  (0,0),(-1,-1), 0), ("RIGHTPADDING",(0,0),(-1,-1), 6),
        ("TOPPADDING",   (0,0),(-1,-1), 1), ("BOTTOMPADDING",(0,0),(-1,-1), 1),
        ("VALIGN",       (0,0),(-1,-1), "TOP"),
    ]))
    s.append(aw_table)
    s.append(Spacer(1,4))

    # EDUCATION
    s += sec("Education")
    iit_context = (
        " <font size='7.5' color='#555555'>"
        "(IIT \u2014 India\u2019s founding technical institutes, top 0.1% national admit rate)"
        "</font>"
    ) if intl else ""
    EDU_CERT = S("EC", fontName="Helvetica-Oblique", fontSize=7.8, textColor=GREY, leading=10.5)
    edu = Table(
        [
            # Row 0: institute name + date
            [Paragraph(f"Indian Institute of Technology, Kharagpur{iit_context}", EDU_I),
             Paragraph("2014 \u2013 2019", S("edy", fontSize=8, textColor=GREY, alignment=TA_RIGHT))],
            # Row 1: degree
            [Paragraph("M.Tech + B.Tech, Computer Science &amp; Engineering (5-yr Dual Degree)", EDU_D),
             Paragraph("", EDU_D)],
            # Row 2: M.Tech project
            [Paragraph("M.Tech Project: Healthcare records system built in collaboration with AIIMS clinicians", EDU_D),
             Paragraph("", EDU_D)],
            # Row 3: GenAI certification
            [Paragraph(
                "\u25cf <b>Generative AI \u2014 IIT Kharagpur</b>"
                "<font color='#555555'>"
                "  (Certification programme delivered at Walmart)"
                "</font>", EDU_CERT),
             Paragraph("2025 \u2013 2026", S("ecy", fontSize=7.8, textColor=GREY, alignment=TA_RIGHT))],
        ],
        colWidths=[BW*0.78, BW*0.22])
    edu.setStyle(TableStyle([
        ("LEFTPADDING",  (0,0),(-1,-1), 0), ("RIGHTPADDING",(0,0),(-1,-1), 0),
        ("TOPPADDING",   (0,0),(-1,-1), 0.5), ("BOTTOMPADDING",(0,0),(-1,-1), 0.5),
        ("VALIGN",       (0,0),(-1,-1), "TOP"),
    ]))
    s.append(edu)

    doc.build(s)
    print(f"✅  CV written to: {out}")


if __name__ == "__main__":
    build(intl=True)   # → cv/jacob_tomy_cv_intl.pdf  (international recruiters)
    build(intl=False)  # → cv/jacob_tomy_cv.pdf        (Indian recruiters)
