"""
CV Generator — Jacob Tomy  (German-market standard, staff-level positioning)
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT

# ── palette ───────────────────────────────────────────────────────────────────
NAVY     = colors.HexColor("#1B3A5C")
DARK     = colors.HexColor("#1A1A2E")
GREY     = colors.HexColor("#555555")
LGREY    = colors.HexColor("#888888")
ACCENT   = colors.HexColor("#2B5E8C")

PAGE_W, PAGE_H = A4
ML = 15*mm;  MR = 15*mm;  MT = 12*mm;  MB = 10*mm
BW = PAGE_W - ML - MR

# ── style factory ─────────────────────────────────────────────────────────────
def S(name, **kw):
    d = dict(fontName="Helvetica", fontSize=7.8, leading=10.5,
             textColor=DARK, spaceAfter=0, spaceBefore=0,
             leftIndent=0, rightIndent=0)
    d.update(kw)
    return ParagraphStyle(name, **d)

NAME     = S("N",  fontName="Helvetica-Bold", fontSize=20, leading=24,
             textColor=NAVY, alignment=TA_LEFT)
TAGLINE  = S("TG", fontSize=8.5, textColor=GREY, alignment=TA_LEFT, leading=11)

SEC      = S("SC", fontName="Helvetica-Bold", fontSize=9.2, textColor=NAVY,
             spaceBefore=3, spaceAfter=0.5)

PROFILE  = S("PR", fontSize=7.8, textColor=GREY, leading=11, alignment=TA_LEFT)

CO_NAME  = S("CN", fontName="Helvetica-Bold", fontSize=8.4, textColor=NAVY)
CO_LOC   = S("CL", fontName="Helvetica-Oblique", fontSize=7.2, textColor=LGREY, leading=9.5)
R_TITLE  = S("RT", fontName="Helvetica-Bold", fontSize=8, textColor=DARK)
R_DATE   = S("RD", fontSize=7.8, textColor=GREY, alignment=TA_RIGHT)
STACK    = S("ST", fontName="Helvetica-Oblique", fontSize=7.4, textColor=GREY,
             leading=9.5, spaceAfter=1)
BUL      = S("BL", fontSize=7.6, leading=10.2, leftIndent=8, spaceAfter=0.4,
             alignment=TA_LEFT)

SK_KEY   = S("SKK", fontName="Helvetica-Bold", fontSize=7.6, leading=10)
SK_VAL   = S("SKV", fontSize=7.6, textColor=GREY, leading=10)

EDU_I    = S("EI", fontName="Helvetica-Bold", fontSize=7.8)
EDU_D    = S("ED", fontName="Helvetica-Oblique", fontSize=7.4, textColor=GREY, leading=9.5)
EDU_DATE = S("EDT", fontSize=7.8, textColor=GREY, alignment=TA_RIGHT)

FOOTER   = S("FT", fontSize=7.4, textColor=LGREY, alignment=TA_RIGHT, spaceBefore=4)

# ── helpers ───────────────────────────────────────────────────────────────────
def sec(title):
    return [Paragraph(title.upper(), SEC),
            HRFlowable(width=BW, thickness=0.6, color=ACCENT, spaceAfter=2)]

def role_header(company, location, title, dates):
    col_w = [BW * 0.22, BW * 0.53, BW * 0.25]
    row = [Paragraph(f"<b>{company}</b>", CO_NAME),
           Paragraph(f"<b>{title}</b>", R_TITLE),
           Paragraph(dates, R_DATE)]
    tbl = Table([row], colWidths=col_w)
    tbl.setStyle(TableStyle([
        ("VALIGN",       (0,0),(-1,-1), "MIDDLE"),
        ("LEFTPADDING",  (0,0),(-1,-1), 0),
        ("RIGHTPADDING", (0,0),(-1,-1), 0),
        ("TOPPADDING",   (0,0),(-1,-1), 0.5),
        ("BOTTOMPADDING",(0,0),(-1,-1), 0.5),
    ]))
    return tbl

def role_block(company, domain, t1, d1, t2, d2):
    col_w = [BW * 0.22, BW * 0.53, BW * 0.25]
    row0 = [Paragraph(f"<b>{company}</b>", CO_NAME),
            Paragraph(f"<b>{t1}</b>", R_TITLE),
            Paragraph(d1, R_DATE)]
    row1 = [Paragraph(domain, CO_LOC),
            Paragraph(f"<b>{t2}</b>", R_TITLE),
            Paragraph(d2, R_DATE)]
    tbl = Table([row0, row1], colWidths=col_w)
    tbl.setStyle(TableStyle([
        ("VALIGN",       (0,0),(-1,-1), "MIDDLE"),
        ("LEFTPADDING",  (0,0),(-1,-1), 0),
        ("RIGHTPADDING", (0,0),(-1,-1), 0),
        ("TOPPADDING",   (0,0),(-1,-1), 0.5),
        ("BOTTOMPADDING",(0,0),(-1,-1), 0.5),
    ]))
    return tbl

def b(txt):
    return Paragraph(f"&#x2022; {txt}", BUL)


def build(out="cv/germany/Jacob_Resume.pdf"):
    doc = SimpleDocTemplate(out, pagesize=A4,
                            leftMargin=ML, rightMargin=MR,
                            topMargin=MT, bottomMargin=MB,
                            title="Jacob Tomy - Lebenslauf",
                            author="Jacob Tomy")
    s = []

    # ══════════════════════════════════════════════════════════════════════════
    # HEADER
    # ══════════════════════════════════════════════════════════════════════════
    s.append(Paragraph("JACOB TOMY", NAME))
    s.append(Paragraph(
        "Senior Software Development Engineer  *  Operational Excellence, Distributed Systems &amp; Applied AI  *  7 Years Experience",
        TAGLINE))
    s.append(Spacer(1, 2))

    info_lbl = S("IL", fontName="Helvetica-Bold", fontSize=7.4, textColor=GREY, leading=10)
    info_val = S("IV", fontSize=7.4, textColor=DARK, leading=10)

    info_data = [
        [Paragraph("Email", info_lbl),       Paragraph("jacobtomy721@gmail.com", info_val),
         Paragraph("Location", info_lbl),    Paragraph("Bengaluru, India", info_val)],
        [Paragraph("LinkedIn", info_lbl),    Paragraph("linkedin.com/in/jacob-tomy", info_val),
         Paragraph("Languages", info_lbl),   Paragraph("English (professional proficiency)", info_val)],
    ]
    info_tbl = Table(info_data, colWidths=[BW*0.11, BW*0.35, BW*0.11, BW*0.35], hAlign="CENTER")
    info_tbl.setStyle(TableStyle([
        ("LEFTPADDING",  (0,0),(-1,-1), 0), ("RIGHTPADDING",(0,0),(-1,-1), 2),
        ("TOPPADDING",   (0,0),(-1,-1), 0.5), ("BOTTOMPADDING",(0,0),(-1,-1), 0.5),
        ("VALIGN",       (0,0),(-1,-1), "TOP"),
    ]))
    s.append(info_tbl)
    s.append(Spacer(1, 1))
    s.append(HRFlowable(width=BW, thickness=1.2, color=NAVY, spaceAfter=2))

    # ══════════════════════════════════════════════════════════════════════════
    # PROFILE
    # ══════════════════════════════════════════════════════════════════════════
    s += sec("Profile")
    s.append(Paragraph(
        "Backend, DevOps and AI-focused Senior Software Development Engineer with 7 years owning the reliability, "
        "performance, and cost efficiency of high-throughput distributed systems at Walmart Global Tech "
        "and Clari. Core competencies in <b>Apache Kafka</b>, event-driven architectures, "
        "database optimisation (<b>Cosmos DB, Cassandra, Elasticsearch, PostgreSQL, MongoDB</b>), "
        "<b>cloud-native deployments</b> (Azure, AWS, Kubernetes), and <b>applied Generative AI</b>. "
        "Proven track record: "
        "<b>20x latency reductions, 40% storage-cost savings, 60% MTTR improvement</b> - "
        "combined with cross-team technical ownership and engineering mentorship.",
        PROFILE))
    s.append(Spacer(1, 2))

    # ══════════════════════════════════════════════════════════════════════════
    # PROFESSIONAL EXPERIENCE
    # ══════════════════════════════════════════════════════════════════════════
    s += sec("Professional Experience")

    # ── Walmart ───────────────────────────────────────────────────────────────
    s.append(role_block("Walmart Global Tech",
                        "Online Pick-up &amp; Delivery (OPD)  *  E-Commerce",
                        "Senior Software Development Engineer", "05/2024 - Present",
                        "Software Development Engineer III", "05/2022 - 05/2024"))
    s.append(Paragraph(
        "Java 21 * Spring Boot 3.x * Apache Kafka * Cosmos DB * Elasticsearch * Kubernetes * Azure * Docker",
        STACK))
    for t in [
        "<b>Owned reliability of the OPD order platform</b> across multiple teams - "
        "a <b>40+ engineer</b> system processing <b>6K OPM avg / 40K OPM peak</b>.",

        "<b>Championed Java 8/11 -> 21 migration</b> (virtual threads, Spring Boot 3.x); "
        "guided 3 teams through the upgrade and standardised dependency management.",

        "<b>Led multiple cross-team initiatives end to end</b> - Real-Time Order Amends, "
        "Pay-for-Speed (expedited delivery tiers) - from understanding requirements across "
        "product and dependent teams, through tradeoff negotiation, contract &amp; design delivery, "
        "implementation with guidance for junior developers, integration testing, and production rollout.",

        "<b>Architected priority-routing Kafka pipeline</b> isolating express-order traffic - "
        "<b>1K+ OPM</b> at zero additional infrastructure cost.",

        "<b>Drove 40% storage-cost reduction</b> via custom zstd dictionary compression "
        "for high-volume Cosmos DB payloads - significantly lowering Azure cloud spend.",

        "<b>Migrated audit data from Cosmos DB to Cassandra</b>, saving <b>~$5K/month</b> in storage "
        "costs; built a generalised service now being adopted by more OPD teams.",

        "<b>Reduced end-to-end latency from 400ms to 20ms</b> by re-architecting "
        "the mid-delivery order-amendment flow across multiple backend services.",

        "<b>Built in-house Kafka payload comparator</b> - customisable mismatch detection "
        "with automated Slack alerting, enabling teams to catch data-contract violations during migrations in real time.",

        "<b>Split and consolidated microservices</b> as traffic patterns and service responsibilities "
        "evolved - right-sizing the platform's service boundaries over time.",

        "<b>Hardened 25+ microservices</b> - Docker configs, CI/CD pipelines, release "
        "workflows - <b>50% faster startup</b>, <b>30% lower resource usage</b>.",
    ]:
        s.append(b(t))
    s.append(Spacer(1, 0.5))

    # ── Clari ─────────────────────────────────────────────────────────────────
    s.append(role_block("Clari (Revenue Intelligence)",
                        "CRM &amp; Data Ingestion",
                        "Software Development Engineer II", "01/2021 - 05/2022",
                        "Software Development Engineer I", "07/2019 - 12/2020"))
    s.append(Paragraph("Java 8 * Spring Boot * PostgreSQL * MongoDB * AWS * REST APIs", STACK))
    for t in [
        "Owned the Autocapture data-ingestion engine - high-throughput, "
        "fault-tolerant data capture to CRM across <b>200+ enterprise organisations</b>.",

        "Built API connectors (G Suite, Outlook) ingesting emails and calendar events "
        "for <b>500K+ end users</b> with high availability.",

        "Optimised PostgreSQL queries and REST endpoints - reduced <b>p99 latency</b>; "
        "overhauled exception handling (10% CPU reduction).",
    ]:
        s.append(b(t))
    s.append(Spacer(1, 0.5))

    s.append(Spacer(1, 2))

    # ══════════════════════════════════════════════════════════════════════════
    # EDUCATION
    # ══════════════════════════════════════════════════════════════════════════
    s += sec("Education")
    edu_data = [
        [Paragraph("<b>Indian Institute of Technology (IIT), Kharagpur</b>", EDU_I),
         Paragraph("2014 - 2019", EDU_DATE)],
        [Paragraph("M.Tech + B.Tech, Computer Science &amp; Engineering (5-Year Integrated Dual Degree)", EDU_D),
         Paragraph("", EDU_D)],
        [Paragraph("Thesis: Blockchain-based healthcare records system developed in collaboration with AIIMS clinicians", EDU_D),
         Paragraph("", EDU_D)],
    ]
    edu_tbl = Table(edu_data, colWidths=[BW*0.78, BW*0.22])
    edu_tbl.setStyle(TableStyle([
        ("LEFTPADDING",  (0,0),(-1,-1), 0), ("RIGHTPADDING",(0,0),(-1,-1), 0),
        ("TOPPADDING",   (0,0),(-1,-1), 0.3), ("BOTTOMPADDING",(0,0),(-1,-1), 0.3),
        ("VALIGN",       (0,0),(-1,-1), "TOP"),
    ]))
    s.append(edu_tbl)
    s.append(Spacer(1, 0.5))

    cert_data = [
        [Paragraph("<b>Generative AI Certification</b> - IIT Kharagpur (delivered at Walmart)", EDU_D),
         Paragraph("2026", EDU_DATE)],
    ]
    cert_tbl = Table(cert_data, colWidths=[BW*0.78, BW*0.22])
    cert_tbl.setStyle(TableStyle([
        ("LEFTPADDING",  (0,0),(-1,-1), 0), ("RIGHTPADDING",(0,0),(-1,-1), 0),
        ("TOPPADDING",   (0,0),(-1,-1), 0.3), ("BOTTOMPADDING",(0,0),(-1,-1), 0.3),
        ("VALIGN",       (0,0),(-1,-1), "TOP"),
    ]))
    s.append(cert_tbl)
    s.append(Spacer(1, 2))

    # ══════════════════════════════════════════════════════════════════════════
    # TECHNICAL SKILLS
    # ══════════════════════════════════════════════════════════════════════════
    s += sec("Technical Skills")
    skills = [
        ("Languages &amp; Frameworks", "Java (8, 17, 21),  Spring Boot (2.7, 3.x),  Python,  ReactJS"),
        ("Event Streaming",            "Apache Kafka (schema design, priority routing, event-driven pipelines)"),
        ("SQL Databases",              "PostgreSQL,  Cassandra"),
        ("NoSQL Databases",            "Cosmos DB,  MongoDB,  Elasticsearch"),
        ("Cloud &amp; DevOps",         "Azure,  AWS,  Kubernetes,  Docker,  CI/CD Pipelines,  GitHub Actions,  Prometheus,  Grafana"),
        ("Architecture",               "Distributed Systems,  Microservices,  HLD / LLD,  API Contracts,  Agile / Scrum"),
    ]
    sk_rows = [[Paragraph(k, SK_KEY), Paragraph(v, SK_VAL)] for k, v in skills]
    sk_table = Table(sk_rows, colWidths=[BW * 0.28, BW * 0.72])
    sk_table.setStyle(TableStyle([
        ("LEFTPADDING",  (0,0),(-1,-1), 0), ("RIGHTPADDING",(0,0),(-1,-1), 2),
        ("TOPPADDING",   (0,0),(-1,-1), 0.3), ("BOTTOMPADDING",(0,0),(-1,-1), 0.3),
        ("VALIGN",       (0,0),(-1,-1), "TOP"),
    ]))
    s.append(sk_table)
    s.append(Spacer(1, 2))

    # ══════════════════════════════════════════════════════════════════════════
    # AWARDS
    # ══════════════════════════════════════════════════════════════════════════
    s += sec("Awards")
    ach = [
        "<b>2nd Prize</b> - lablab.ai Global AI Hackathon in Dubai (2026): NL2SQL real-time analytics dashboard.",
        "<b>Excellence Award</b> - Walmart (2025): 40% storage-cost reduction via zstd compression.",
        "<b>Bravo Award</b> - Walmart (2025): AI on-call agent reducing incident MTTR by 60%.",
        "<b>Bravo Award</b> - Walmart (2025): Quick migration of legacy applications to modern platform stack.",
        "<b>Bravo Award</b> - Walmart (2024): On-call champion - proactive in identifying and mitigating production issues.",
        "<b>Excellence Award</b> - Walmart (2024): Priority Kafka pipeline - zero extra infrastructure cost.",
        "<b>Runner-Up</b> - Walmart Global Techathon (2022): Data-driven recommendation engine.",
        "<b>Winner</b> - Clari Innovates Hackathon (2021): Internal tooling platform, adopted company-wide.",
    ]
    ach_style = S("AW2", fontSize=7.4, leading=9.8, leftIndent=0, spaceAfter=0.2)
    aw_rows = []
    for i in range(0, len(ach), 2):
        left  = Paragraph(f"&#x2022; {ach[i]}", ach_style)
        right = Paragraph(f"&#x2022; {ach[i+1]}", ach_style) if i+1 < len(ach) else Paragraph("", ach_style)
        aw_rows.append([left, right])
    aw_table = Table(aw_rows, colWidths=[BW*0.497, BW*0.497], hAlign="LEFT")
    aw_table.setStyle(TableStyle([
        ("LEFTPADDING",  (0,0),(-1,-1), 0), ("RIGHTPADDING",(0,0),(-1,-1), 4),
        ("TOPPADDING",   (0,0),(-1,-1), 0.5), ("BOTTOMPADDING",(0,0),(-1,-1), 0.5),
        ("VALIGN",       (0,0),(-1,-1), "TOP"),
    ]))
    s.append(aw_table)

    # ══════════════════════════════════════════════════════════════════════════
    # FOOTER
    # ══════════════════════════════════════════════════════════════════════════
    s.append(Spacer(1, 4))
    s.append(Paragraph("Bengaluru, May 2026", FOOTER))

    doc.build(s)
    print(f"\u2705  German-standard CV written to: {out}")


if __name__ == "__main__":
    build()
