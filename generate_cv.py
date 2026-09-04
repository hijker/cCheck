"""
CV Generator — Jacob Tomy  (base / general-purpose, staff-level positioning)
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_JUSTIFY, TA_LEFT
from datetime import datetime
from pathlib import Path

# RED      = colors.HexColor("#C0392B")
# DARK     = colors.HexColor("#1A1A2E")
# GREY     = colors.HexColor("#555555")

DARK = colors.HexColor("#1F2937")   # charcoal
BLUE = colors.HexColor("#1D4ED8")   # professional blue
GREY = colors.HexColor("#64748B")   # muted grey

PAGE_W, PAGE_H = A4
ML = 15*mm;  MR = 15*mm;  MT = 15*mm;  MB = 15*mm
BW = PAGE_W - ML - MR

def S(name, **kw):
    d = dict(fontName="Helvetica", fontSize=7.8, leading=10.5,
             textColor=DARK, spaceAfter=0, spaceBefore=0,
             leftIndent=0, rightIndent=0)
    d.update(kw)
    return ParagraphStyle(name, **d)

NAME    = S("N",  fontName="Helvetica-Bold", fontSize=19, leading=22, textColor=DARK, alignment=TA_CENTER)
TAGLINE = S("TL", fontSize=8.4, textColor=GREY, alignment=TA_CENTER, leading=11)
CONTACT = S("CT", fontSize=7.6, textColor=BLUE, alignment=TA_CENTER, leading=10)
SUMMARY = S("SU", fontSize=7.8, textColor=DARK, leading=11, spaceAfter=1, alignment=TA_LEFT)
SEC     = S("SC", fontName="Helvetica-Bold", fontSize=9, textColor=BLUE, spaceBefore=1, spaceAfter=0.5)
CO_NAME = S("CN", fontName="Helvetica-Bold", fontSize=8.4, textColor=BLUE)
CO_DOM  = S("CD", fontName="Helvetica-Oblique", fontSize=7.2, textColor=GREY, leading=9.5)
R_TITLE  = S("RT",  fontName="Helvetica-Bold", fontSize=8.2, textColor=DARK)
R_TITLE2 = S("RT2", fontName="Helvetica-Bold", fontSize=8.2, textColor=DARK, leading=10.5)
R_DATE   = S("RD",  fontSize=8.2, textColor=GREY, alignment=TA_RIGHT)
STACK   = S("ST", fontName="Helvetica-Oblique", fontSize=7.6, textColor=GREY, leading=10, spaceAfter=1)
BUL     = S("BL", fontSize=7.8, leading=10.2, leftIndent=8, firstLineIndent=-6, spaceAfter=2, alignment=TA_LEFT)
SK_KEY  = S("SKK", fontName="Helvetica-Bold", textColor=GREY, fontSize=7.8, leading=10.5)
SK_VAL  = S("SKV", fontSize=7.8, textColor=DARK, leading=10.5)
EDU_I   = S("EI", fontName="Helvetica-Bold", fontSize=8)
EDU_D   = S("ED", fontName="Helvetica-Oblique", fontSize=7.6, textColor=GREY)

def sec(title):
    return [Paragraph(title.upper(), SEC),
            HRFlowable(width=BW, thickness=0.55, color=BLUE, spaceAfter=2)]

def role_block(co, dom, t1, d1, t2=None, d2=None):
    col_w = [BW * 0.27, BW * 0.50, BW * 0.23]
    row0 = [Paragraph(f"<b>{co}</b>", CO_NAME),
            Paragraph(f"<b>{t1}</b>", R_TITLE),
            Paragraph(d1, R_DATE)]
    if t2 and d2:
        row1 = [Paragraph(dom, CO_DOM), Paragraph(t2, R_TITLE2), Paragraph(d2, R_DATE)]
    else:
        row1 = [Paragraph(dom, CO_DOM), Paragraph("", R_TITLE2), Paragraph("", R_DATE)]
    tbl = Table([row0, row1], colWidths=col_w)
    tbl.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"), ("LEFTPADDING",(0,0),(-1,-1),5),
        ("RIGHTPADDING",(0,0),(-1,-1),5), ("TOPPADDING",(0,0),(-1,-1),1),
        ("BOTTOMPADDING",(0,0),(-1,-1),1),
    ]))
    return tbl

def b(txt):
    return Paragraph(f"&#x2022; {txt}", BUL)

def build(out=None, intl=True):
    if out is None:
        out = f"cv/{datetime.now():%Y-%m-%d}/Jacob_Resume.pdf"

    path = Path(out)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    doc = SimpleDocTemplate(out, pagesize=A4, leftMargin=ML, rightMargin=MR,
                            topMargin=MT, bottomMargin=MB,
                            title="Jacob Tomy - CV", author="Jacob Tomy")
    s = []

    # HEADER
    s += [Paragraph("JACOB TOMY", NAME), Spacer(1,1),
          Paragraph("Senior Software Engineer (SDE 4) \u00b7 Distributed Systems & Platform Architecture \u00b7  8 Years Experience", TAGLINE),
          Spacer(1,1),
          Paragraph("jacobtomy721@gmail.com  \u00b7  linkedin.com/in/jacob-tomy  \u00b7  github.com/hijker  \u00b7  Bengaluru, India", CONTACT),
          Spacer(1,2),
          HRFlowable(width=BW, thickness=1.1, color=BLUE, spaceAfter=2)]

    # SUMMARY
    s.append(Paragraph(
        "Senior Software Development Engineer with 8 years of experience building and owning large-scale distributed systems using Java, Spring Boot, and Kafka."
        " Strong in platform architecture, event-driven systems, and reliability engineering, with measurable impact including 20x lower latency, "
        "40% lower storage/RU consumption, and 60% lower MTTR. Experienced in leading cross-team architecture, platform modernization, and reusable engineering solutions.",
        SUMMARY))
    s.append(Spacer(1,2))

    # EXPERIENCE
    s += sec("Experience")

    # Walmart
    s.append(role_block("Walmart Global Tech","Online Pick-up &amp; Delivery (OPD) \u00b7 E-Commerce",
                        "Senior Software Development Engineer (SDE 4)","2024 - Present",
                        "Software Development Engineer III","2022 - 2024"))
    s.append(Paragraph(
        "Java 25 \u00b7 Spring Boot 4.x \u00b7 Kafka \u00b7 Cosmos DB \u00b7 Opensearch \u00b7 Kubernetes \u00b7 Azure \u00b7 Python \u00b7 LLMs",
        STACK))
    for t in [
        "<b>OPD Platform Ownership:</b> Owned stability and reliability of Walmart\u2019s Online Pick-up & Delivery order platform across multiple teams, supporting"
        " <b>40+ engineers</b> and <b>6K OPM</b> average / <b>45K OPM</b> peak traffic; drove capacity planning, SLA adherence,"
        " and platform-wide incident resolution.",

        "<b>Stability and Reliability:</b> Championed platform modernization - Led Java 8/11 → 21/25 + Spring Boot 2.7 → 3.5/4.x migration "
        "for <b>3 teams</b> alongside the upgrades, "
        "standardized BOM adoption and eliminated legacy dependency risks across the platform.",

        "<b>End-to-End Initiative Ownership:</b> Led cross-team initiatives driving Walmart\u2019s quick-commerce growth, "
        "including real-time order amendments and Pay-for-Speed delivery; drove requirements, cross-team tradeoffs, API/design "
        "contracts, implementation with junior engineers, and production rollout.",

        "<b>Operational Intelligence:</b> Built an LLM-powered on-call agent surfacing runbook excerpts, "
        "incident history, and live dependency state - cutting mean time to resolution <b>(MTTR)</b> by <b>60%</b>.",

        "<b>Infrastructure Efficiency:</b> Architected <b>priority kafka pipeline</b> isolating express-order "
        "traffic, routing <b>10K+ peak OPM</b> at zero additional infrastructure cost by creating a custom reusable library;"
        " drove adoption across 5 OPD teams and more teams in post purchase, iterating on the library to simplify integration.",
        
        "<b>Cost Optimisation:</b> Designed in-house zstd dictionary-compression layer for high-volume Cosmos DB "
        "payloads - drove <b>40% storage and RU (Read Units) reduction</b>, reducing Azure cloud spend.",

        "<b>Data-Layer Migration:</b> Migrated audit data from Cosmos DB to Cassandra, saving "
        "<b>~$5K/month (~15% of total)</b> in storage costs; designed a generalized audit service now being adopted "
        "by other OPD teams.",

        "<b>Observability Tooling:</b> Built a customizable Kafka payload comparator with automated mismatch detection and Slack alerting, "
        "enabling teams to identify data-contract violations in real time.",

        "<b>Operational Hardening:</b> Hardened <b>35+</b> microservices across Docker, CI/CD, and container security, "
        "while optimizing container startup and resource usage to achieve 50% faster startup and 30% lower resource consumption",
    ]:
        s.append(b(t))
    s.append(Spacer(1,2))

    # Clari
    s.append(role_block("Clari","Revenue Intelligence \u00b7 CRM",
                        "Software Development Engineer II","2021 - 2022",
                        "Software Development Engineer I","2019 - 2021"))
    s.append(Paragraph("Java 8 \u00b7 Spring Boot \u00b7 PostgreSQL \u00b7 MongoDB \u00b7 AWS", STACK))
    for t in [
        "Built and maintained the Autocapture engine - automated activity-capture system with "
        "intelligent CRM matching, serving <b>200+ enterprise organizations</b>.",

        "Integrated G Suite and Outlook into Clari\u2019s platform, ingesting emails and calendar "
        "events for <b>500K+ end users</b>.",

        "Tuned PostgreSQL queries and REST endpoints, reducing <b>p99 latency</b>; "
        "overhauled exception handling (10% CPU reduction).",
    ]:
        s.append(b(t))
    s.append(Spacer(1,2))

    # SKILLS
    s += sec("Skills")
    skills = [
        ("Languages", "Java 25,  Python"),
        ("Backend",        "Spring Boot 4.x, REST, Kafka,  Kubernetes "),
        ("Cloud &amp; Platform",          "Azure,  AWS,  CI/CD (Looper), Docker, Prometheus,  Grafana"),
        ("Databases",          "Cosmos DB, Cassandra, Elastic/Opensearch, PostgreSQL, MongoDB"),
        ("AI",           "LLMs, AI Agents, LangGraph,  NL2SQL"),
        ("Architecture &amp; Engineering",      "HLD/LLD,  API Contracts, Distributed Systems, UML, Agile / Scrum"),
    ]
    sk_rows = [[Paragraph(k, SK_KEY), Paragraph(v, SK_VAL)] for k, v in skills]
    sk_table = Table(sk_rows, colWidths=[BW * 0.30, BW * 0.70])
    sk_table.setStyle(TableStyle([
        ("LEFTPADDING",(0,0),(-1,-1),5), ("RIGHTPADDING",(0,0),(-1,-1),5),
        ("TOPPADDING",(0,0),(-1,-1),0), ("BOTTOMPADDING",(0,0),(-1,-1),0),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
    ]))
    s.append(sk_table)
    s.append(Spacer(1,2))

    # ACHIEVEMENTS
    s += sec('<link href="https://github.com/hijker/Awards-and-Recognitions">Achievements</link>')
    ach = [
        ("<b>2nd Prize - lablab.ai Global AI Hackathon (2026)</b>",
         "NL2SQL + LangGraph enterprise dashboard with real-time alert engine."),
        ("<b>Excellence Award (2026) - Walmart</b>",
         "For delivering a reusable platform capability that drove measurable cloud-cost savings."),
        ("<b>Excellence Award (2025) - Walmart</b>",
         "For an optimization initiative that significantly reduced data storage and consumption costs."),
        ("<b>Bravo Award (2025) - Walmart</b>",
         "For applying Generative AI to improve on-call effectiveness and incident response"),
        ("<b>Bravo Award (2025) - Walmart</b>",
         "For accelerating modernization of legacy applications across the platform."),
        ("<b>Excellence Award (2023) - Walmart</b>",
         "For a platform scalability initiative supporting express-order growth without additional infrastructure investment"),
        ("<b>Walmart Global Techathon - Runner-Up (2022)</b>",
         "Cart-based nutritional recommendation product for Walmart customers."),
        ("<b>Clari Innovates Hackathon - Winner (2021)</b>",
         "Revamped internal tooling platform, adopted company-wide."),
    ]
    ach_style = S("ACH", fontSize=7.8, leading=10.5, leftIndent=0, spaceAfter=0.3, alignment=TA_LEFT)
    aw_rows = []
    for i in range(0, len(ach), 2):
        left_ach  = Paragraph(f"{ach[i][0]}: {ach[i][1]}", ach_style)
        right_ach = Paragraph(f"{ach[i+1][0]}: {ach[i+1][1]}", ach_style) if i+1 < len(ach) else Paragraph("", ach_style)
        aw_rows.append([left_ach, right_ach])
    aw_table = Table(aw_rows, colWidths=[BW*0.497, BW*0.497], hAlign="LEFT", spaceBefore=0)
    aw_table.setStyle(TableStyle([
        ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(-1,-1),6),
        ("TOPPADDING",(0,0),(-1,-1),1), ("BOTTOMPADDING",(0,0),(-1,-1),1),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
    ]))
    s.append(aw_table)
    s.append(Spacer(1,2))

    # EDUCATION
    s += sec("Education")
    iit_context = (
        " <font size='7.5' color='#555555'>"
        "(IIT - India\u2019s founding technical institutes, top 0.1% national admit rate)"
        "</font>"
    ) if intl else ""
    EDU_CERT = S("EC", fontName="Helvetica-Oblique", fontSize=7.4, textColor=DARK, leading=9.5)
    edu = Table([
        [Paragraph(f"Indian Institute of Technology, Kharagpur{iit_context}", EDU_I),
         Paragraph("2014 - 2019", S("edy", fontSize=8, textColor=GREY, alignment=TA_RIGHT))],
        [Paragraph("M.Tech + B.Tech, Computer Science &amp; Engineering (5-yr Dual Degree)", EDU_D),
         Paragraph("", EDU_D)],
        [Paragraph(
            "Certification: <b>Applied Al for Real-World Applications - IIT Kharagpur</b>"
            "<font color='#555555'>  (Delivered at Walmart)</font>", EDU_CERT),
         Paragraph("2026", S("ecy", fontSize=7.8, textColor=GREY, alignment=TA_RIGHT))],
    ], colWidths=[BW*0.78, BW*0.22])
    edu.setStyle(TableStyle([
        ("LEFTPADDING",(0,0),(-1,-1),5), ("RIGHTPADDING",(0,0),(-1,-1),5),
        ("TOPPADDING",(0,0),(-1,-1),0.5), ("BOTTOMPADDING",(0,0),(-1,-1),0.5),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
    ]))
    s.append(edu)
    doc.build(s)
    print(f"\u2705  CV written to: {out}")

if __name__ == "__main__":
    build(intl=True)
    build(intl=False)
