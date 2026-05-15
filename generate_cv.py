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

RED      = colors.HexColor("#C0392B")
DARK     = colors.HexColor("#1A1A2E")
GREY     = colors.HexColor("#555555")

PAGE_W, PAGE_H = A4
ML = 15*mm;  MR = 15*mm;  MT = 10*mm;  MB = 8*mm
BW = PAGE_W - ML - MR

def S(name, **kw):
    d = dict(fontName="Helvetica", fontSize=7.8, leading=10.5,
             textColor=DARK, spaceAfter=0, spaceBefore=0,
             leftIndent=0, rightIndent=0)
    d.update(kw)
    return ParagraphStyle(name, **d)

NAME    = S("N",  fontName="Helvetica-Bold", fontSize=19, leading=22, textColor=DARK, alignment=TA_CENTER)
TAGLINE = S("TL", fontSize=8.4, textColor=GREY, alignment=TA_CENTER, leading=11)
CONTACT = S("CT", fontSize=7.6, textColor=RED, alignment=TA_CENTER, leading=10)
SUMMARY = S("SU", fontSize=7.8, textColor=GREY, leading=11, alignment=TA_LEFT)
SEC     = S("SC", fontName="Helvetica-Bold", fontSize=9, textColor=RED, spaceBefore=1, spaceAfter=0.5)
CO_NAME = S("CN", fontName="Helvetica-Bold", fontSize=8.4, textColor=RED)
CO_DOM  = S("CD", fontName="Helvetica-Oblique", fontSize=7.2, textColor=GREY, leading=9.5)
R_TITLE  = S("RT",  fontName="Helvetica-Bold", fontSize=8.2, textColor=DARK)
R_TITLE2 = S("RT2", fontName="Helvetica-Bold", fontSize=8.2, textColor=DARK, leading=10.5)
R_DATE   = S("RD",  fontSize=8.2, textColor=GREY, alignment=TA_RIGHT)
STACK   = S("ST", fontName="Helvetica-Oblique", fontSize=7.6, textColor=GREY, leading=10, spaceAfter=1)
BUL     = S("BL", fontSize=7.8, leading=10.2, leftIndent=8, spaceAfter=0.3, alignment=TA_LEFT)
SK_KEY  = S("SKK", fontName="Helvetica-Bold", fontSize=7.8, leading=10.5)
SK_VAL  = S("SKV", fontSize=7.8, textColor=GREY, leading=10.5)
EDU_I   = S("EI", fontName="Helvetica-Bold", fontSize=8)
EDU_D   = S("ED", fontName="Helvetica-Oblique", fontSize=7.6, textColor=GREY)

def sec(title):
    return [Paragraph(title.upper(), SEC),
            HRFlowable(width=BW, thickness=0.55, color=RED, spaceAfter=2)]

def role_block(co, dom, t1, d1, t2=None, d2=None):
    col_w = [BW * 0.20, BW * 0.57, BW * 0.23]
    row0 = [Paragraph(f"<b>{co}</b>", CO_NAME),
            Paragraph(f"<b>{t1}</b>", R_TITLE),
            Paragraph(d1, R_DATE)]
    if t2 and d2:
        row1 = [Paragraph(dom, CO_DOM), Paragraph(t2, R_TITLE2), Paragraph(d2, R_DATE)]
    else:
        row1 = [Paragraph(dom, CO_DOM), Paragraph("", R_TITLE2), Paragraph("", R_DATE)]
    tbl = Table([row0, row1], colWidths=col_w)
    tbl.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"), ("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0), ("TOPPADDING",(0,0),(-1,-1),1),
        ("BOTTOMPADDING",(0,0),(-1,-1),1),
    ]))
    return tbl

def b(txt):
    return Paragraph(f"&#x2022; {txt}", BUL)

def build(out=None, intl=True):
    if out is None:
        out = "cv/base/Jacob_Resume_intl.pdf" if intl else "cv/base/Jacob_Resume.pdf"

    doc = SimpleDocTemplate(out, pagesize=A4, leftMargin=ML, rightMargin=MR,
                            topMargin=MT, bottomMargin=MB,
                            title="Jacob Tomy \u2014 CV", author="Jacob Tomy")
    s = []

    # HEADER
    s += [Paragraph("JACOB TOMY", NAME), Spacer(1,1),
          Paragraph("Senior Software Development Engineer  \u00b7  Backend &amp; Platform Reliability  \u00b7  7 Years Experience", TAGLINE),
          Spacer(1,1),
          Paragraph("jacobtomy721@gmail.com  \u00b7  linkedin.com/in/jacob-tomy  \u00b7  github.com/hijker  \u00b7  Bengaluru, India", CONTACT),
          Spacer(1,2),
          HRFlowable(width=BW, thickness=1.1, color=RED, spaceAfter=2)]

    # SUMMARY
    s.append(Paragraph(
        "Backend-focused Senior SDE with 7 years owning high-throughput distributed systems at Walmart "
        "and Clari. Driven by <b>operational excellence</b> \u2014 building for reliability, performance, "
        "and cost efficiency across event-driven architectures (Kafka), cloud-native deployments "
        "(Azure/Kubernetes), and applied Generative AI. "
        "Track record of measurable platform impact \u2014 20\u00d7 latency reductions, 40% storage-cost "
        "savings, 60% MTTR improvement \u2014 while setting cross-team technical standards and mentoring engineers.",
        SUMMARY))
    s.append(Spacer(1,2))

    # EXPERIENCE
    s += sec("Experience")

    # Walmart
    s.append(role_block("Walmart Global Tech","Online Pick-up &amp; Delivery (OPD) \u00b7 E-Commerce",
                        "Senior Software Development Engineer","May 2024 \u2013 Present",
                        "Software Development Engineer III","May 2022 \u2013 May 2024"))
    s.append(Paragraph(
        "Java 21 \u00b7 Spring Boot 3.x \u00b7 Kafka \u00b7 Cosmos DB \u00b7 Elasticsearch \u00b7 Kubernetes \u00b7 Azure \u00b7 Redis \u00b7 Python \u00b7 LLMs",
        STACK))
    for t in [
        "<b>OPD Platform Ownership:</b> Owned reliability of Walmart\u2019s Online Pick-up &amp; Delivery "
        "order platform across multiple teams \u2014 a <b>40+ engineer</b> system processing "
        "<b>6K OPM</b> avg, <b>40K OPM</b> at peak.",

        "<b>Platform Migration:</b> Championed Java 8/11 \u2192 Java 21 + Spring Boot 3.x migration "
        "(virtual threads); guided <b>3 teams</b> through the upgrade, standardised BOM adoption, "
        "and eliminated legacy dependency risks across the platform.",

        "<b>Operational Intelligence:</b> Built GPT-4o-powered on-call agent surfacing runbook excerpts, "
        "incident history, and live dependency state \u2014 cutting mean time to resolution by <b>60%</b>.",

        "<b>End-to-End Initiative Ownership:</b> Led multiple cross-team initiatives \u2014 real-time "
        "order amends, Pay-for-Speed (expedited delivery tiers) \u2014 end to end: understanding "
        "requirements across product and dependent teams, tradeoff negotiation, contract &amp; design "
        "delivery, implementation alongside junior developers, integration testing, and production rollout.",

        "<b>Performance Engineering:</b> Re-architected mid-delivery order-amendment flow across "
        "multiple backend services, reducing end-to-end latency from <b>400\u202fms \u2192 20\u202fms</b>.",

        "<b>Cost Optimisation:</b> Designed zstd dictionary-compression layer for high-volume Cosmos DB "
        "payloads \u2014 drove <b>40% storage reduction</b>, significantly lowering Azure cloud spend.",

        "<b>Data-Layer Migration:</b> Migrated audit data from Cosmos DB to Cassandra, saving "
        "<b>~$5K/month</b> in storage costs; built a generalised migration service now being adopted "
        "by other OPD teams.",

        "<b>Infrastructure Efficiency:</b> Architected priority Kafka pipeline isolating express-order "
        "traffic \u2014 routing <b>1K+ OPM</b> at zero additional infrastructure cost.",

        "<b>Revenue Impact:</b> Delivered end-to-end premium delivery feature enabling faster fulfilment "
        "tiers, directly contributing to Walmart\u2019s quick-commerce revenue growth.",

        "<b>Observability Tooling:</b> Built in-house customisable Kafka payload comparator \u2014 "
        "automated mismatch detection with Slack alerting, enabling teams to catch data-contract "
        "violations in real time.",

        "<b>Service Topology:</b> Split and consolidated microservices as traffic patterns and service "
        "responsibilities evolved \u2014 right-sizing the platform\u2019s service boundaries over time.",

        "<b>Operational Hardening:</b> Secured <b>25+ microservices</b> \u2014 Docker configs, CI/CD "
        "pipelines, container security \u2014 <b>50% faster startup</b>, <b>30% lower resource usage</b>.",
    ]:
        s.append(b(t))
    s.append(Spacer(1,2))

    # Clari
    s.append(role_block("Clari","Revenue Intelligence \u00b7 CRM",
                        "Software Development Engineer II","2021 \u2013 2022",
                        "Software Development Engineer I","2019 \u2013 2021"))
    s.append(Paragraph("Java 8 \u00b7 Spring Boot \u00b7 PostgreSQL \u00b7 MongoDB \u00b7 AWS", STACK))
    for t in [
        "Built and maintained the Autocapture engine \u2014 automated activity-capture system with "
        "intelligent CRM matching, live across <b>200+ enterprise organisations</b>.",

        "Integrated G Suite and Outlook into Clari\u2019s platform, ingesting emails and calendar "
        "events for <b>500K+ end users</b>.",

        "Tuned PostgreSQL queries and REST endpoints, reducing <b>p99 latency</b> on AWS; "
        "overhauled exception handling (10% CPU reduction).",
    ]:
        s.append(b(t))
    s.append(Spacer(1,2))

    # SKILLS
    s += sec("Skills")
    skills = [
        ("Languages &amp; Frameworks", "Java (8, 17, 21),  Spring Boot (2.7, 3.x),  Python,  ReactJS"),
        ("Distributed Systems",        "Kafka,  Kubernetes,  Docker,  REST APIs,  Redis"),
        ("Cloud &amp; Infra",          "Azure,  AWS,  CI/CD (Looper),  Prometheus,  Grafana"),
        ("Databases (NoSQL)",          "Cosmos DB,  MongoDB,  Cassandra,  Elasticsearch"),
        ("Databases (SQL)",            "PostgreSQL"),
        ("AI &amp; Tooling",           "LLMs,  LangGraph,  NL2SQL,  AI Agents,  Claude Code"),
        ("Design &amp; Delivery",      "HLD,  LLD,  API Contracts,  UML,  JIRA,  Agile / Scrum"),
    ]
    sk_rows = [[Paragraph(k, SK_KEY), Paragraph(v, SK_VAL)] for k, v in skills]
    sk_table = Table(sk_rows, colWidths=[BW * 0.30, BW * 0.70])
    sk_table.setStyle(TableStyle([
        ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(-1,-1),3),
        ("TOPPADDING",(0,0),(-1,-1),0.5), ("BOTTOMPADDING",(0,0),(-1,-1),0.5),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
    ]))
    s.append(sk_table)
    s.append(Spacer(1,2))

    # ACHIEVEMENTS
    s += sec("Achievements")
    ach = [
        ("\u2605\u2605 <b>2nd Prize \u2014 lablab.ai Global AI Hackathon (2026)</b>",
         "NL2SQL + LangGraph enterprise dashboard with real-time alert engine."),
        ("\u2605 <b>Excellence Award (2025) \u2014 Walmart</b>",
         "zstd compression: 40% Cosmos DB storage reduction, lower Azure spend."),
        ("\u2605 <b>Bravo Award (2025) \u2014 Walmart</b>",
         "GPT-4o on-call agent surfacing live incident context, cutting MTTR by 60%."),
        ("\u2605 <b>Bravo Award (2025) \u2014 Walmart</b>",
         "Quick migration of legacy applications to modern platform stack."),
        ("\u2605 <b>Bravo Award (2024) \u2014 Walmart</b>",
         "On-call champion of the team."),
        ("\u2605 <b>Excellence Award (2024) \u2014 Walmart</b>",
         "Priority Kafka pipeline \u2014 100% of express orders, zero extra cost."),
        ("\u25cf <b>Walmart Global Techathon \u2014 Runner-Up (2022)</b>",
         "Cart-based nutritional recommendation product for Walmart customers."),
        ("\u25cf <b>Clari Innovates Hackathon \u2014 Winner (2021)</b>",
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
        "(IIT \u2014 India\u2019s founding technical institutes, top 0.1% national admit rate)"
        "</font>"
    ) if intl else ""
    EDU_CERT = S("EC", fontName="Helvetica-Oblique", fontSize=7.4, textColor=GREY, leading=9.5)
    edu = Table([
        [Paragraph(f"Indian Institute of Technology, Kharagpur{iit_context}", EDU_I),
         Paragraph("2014 \u2013 2019", S("edy", fontSize=8, textColor=GREY, alignment=TA_RIGHT))],
        [Paragraph("M.Tech + B.Tech, Computer Science &amp; Engineering (5-yr Dual Degree)", EDU_D),
         Paragraph("", EDU_D)],
        [Paragraph("M.Tech Project: Healthcare records system built in collaboration with AIIMS clinicians", EDU_D),
         Paragraph("", EDU_D)],
        [Paragraph(
            "\u25cf <b>Generative AI \u2014 IIT Kharagpur</b>"
            "<font color='#555555'>  (Certification programme delivered at Walmart)</font>", EDU_CERT),
         Paragraph("2026", S("ecy", fontSize=7.8, textColor=GREY, alignment=TA_RIGHT))],
    ], colWidths=[BW*0.78, BW*0.22])
    edu.setStyle(TableStyle([
        ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),0.5), ("BOTTOMPADDING",(0,0),(-1,-1),0.5),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
    ]))
    s.append(edu)
    doc.build(s)
    print(f"\u2705  CV written to: {out}")

if __name__ == "__main__":
    build(intl=True)
    build(intl=False)
