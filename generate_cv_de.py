"""
CV Generator — Jacob Tomy  (German-market standard, staff-level positioning)

Layout follows German Lebenslauf conventions:
  - Conservative colour palette (navy blue accent)
  - Structured personal-details block
  - Languages section with proficiency levels
  - European date format (MM/YYYY)
  - Education given strong weight
  - Factual, metric-driven bullet points (active verbs)
  - City + Date footer
  - Single A4 page

Staff-level positioning:
  - Ownership language throughout
  - Operational excellence, reliability, performance, cost savings
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
CONTACT  = S("CT", fontSize=7.8, textColor=GREY, leading=10.5)

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

FOOTER   = S("FT", fontSize=7.4, textColor=LGREY, alignment=TA_RIGHT,
             spaceBefore=4)

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
        ("VALIGN",       (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING",  (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING",   (0,0), (-1,-1), 0.5),
        ("BOTTOMPADDING",(0,0), (-1,-1), 0.5),
    ]))
    return tbl

def b(txt):
    return Paragraph(f"&#x2022; {txt}", BUL)


def build(out="cv/germany/resume.pdf"):
    """Generate German-market-standard CV with staff-level positioning."""

    doc = SimpleDocTemplate(out, pagesize=A4,
                            leftMargin=ML, rightMargin=MR,
                            topMargin=MT, bottomMargin=MB,
                            title="Jacob Tomy \u2014 Lebenslauf",
                            author="Jacob Tomy")
    s = []

    # ══════════════════════════════════════════════════════════════════════════
    # HEADER
    # ══════════════════════════════════════════════════════════════════════════
    s.append(Paragraph("JACOB TOMY", NAME))
    s.append(Paragraph(
        "Senior Java Engineer  \u00b7  Operational Excellence &amp; Distributed Systems  \u00b7  7 Years Experience",
        TAGLINE))
    s.append(Spacer(1, 2))

    # Personal details table
    info_lbl = S("IL", fontName="Helvetica-Bold", fontSize=7.4, textColor=GREY, leading=10)
    info_val = S("IV", fontSize=7.4, textColor=DARK, leading=10)

    info_data = [
        [Paragraph("Email", info_lbl),       Paragraph("jacobtomy721@gmail.com", info_val),
         Paragraph("Location", info_lbl),    Paragraph("Bengaluru, India", info_val)],
        [Paragraph("LinkedIn", info_lbl),    Paragraph("linkedin.com/in/jacob-tomy", info_val),
         Paragraph("GitHub", info_lbl),      Paragraph("github.com/jacob-tomy", info_val)],
        [Paragraph("Nationality", info_lbl), Paragraph("Indian", info_val),
         Paragraph("Languages", info_lbl),   Paragraph("English (professional proficiency), Malayalam (native)", info_val)],
    ]
    info_tbl = Table(info_data, colWidths=[BW*0.11, BW*0.36, BW*0.11, BW*0.42])
    info_tbl.setStyle(TableStyle([
        ("LEFTPADDING",  (0,0),(-1,-1), 0), ("RIGHTPADDING",(0,0),(-1,-1), 2),
        ("TOPPADDING",   (0,0),(-1,-1), 0.5), ("BOTTOMPADDING",(0,0),(-1,-1), 0.5),
        ("VALIGN",       (0,0),(-1,-1), "TOP"),
    ]))
    s.append(info_tbl)
    s.append(Spacer(1, 1))
    s.append(HRFlowable(width=BW, thickness=1.2, color=NAVY, spaceAfter=2))

    # ══════════════════════════════════════════════════════════════════════════
    # PROFILE — staff-level: ownership, operational excellence, reliability, cost
    # ══════════════════════════════════════════════════════════════════════════
    s += sec("Profile")
    s.append(Paragraph(
        "Backend-focused Senior Java Engineer with 7 years owning the reliability, performance, and "
        "cost efficiency of high-throughput distributed systems at Walmart Global Tech and Clari. "
        "Core competencies in <b>Apache Kafka, Change Data Capture (CDC), RDBMS integration</b> "
        "(PostgreSQL, Cosmos DB, MongoDB, Cassandra), and <b>cloud-native deployments</b> "
        "(Azure, AWS, Kubernetes). Proven track record: "
        "<b>20\u00d7 latency reductions, 40% storage-cost savings, 60% MTTR improvement</b> \u2014 "
        "combined with cross-team technical ownership and engineering mentorship.",
        PROFILE))
    s.append(Spacer(1, 2))

    # ══════════════════════════════════════════════════════════════════════════
    # PROFESSIONAL EXPERIENCE
    # ══════════════════════════════════════════════════════════════════════════
    s += sec("Professional Experience")

    # ── Walmart: Senior SDE ──────────────────────────────────────────────────
    s.append(role_header("Walmart Global Tech", "Bengaluru, India",
                         "Senior Software Development Engineer", "05/2024 \u2013 Present"))
    s.append(Paragraph("Bengaluru, India  \u00b7  E-Commerce &amp; Retail  \u00b7  Platform Reliability", CO_LOC))
    s.append(Paragraph(
        "Java 21 \u00b7 Spring Boot 3.x \u00b7 Apache Kafka \u00b7 Cosmos DB \u00b7 PostgreSQL \u00b7 Kubernetes \u00b7 Azure \u00b7 Docker",
        STACK))
    for t in [
        "<b>Owned end-to-end reliability</b> of event-driven order platform processing "
        "<b>6K OPM avg / 40K OPM peak</b> \u2014 authored Kafka schemas, API contracts, "
        "and HLD/LLD docs adopted across a <b>20-engineer platform</b>.",

        "<b>Established schema governance</b> and cross-team code-review standards; "
        "managed contributions from upstream/downstream teams in open-source-style processes.",

        "<b>Architected priority-routing Kafka pipeline</b> isolating express-order traffic \u2014 "
        "<b>300+ OPM</b> at zero additional infrastructure cost.",

        "<b>Drove 40% storage-cost reduction</b> via custom zstd dictionary compression "
        "for high-volume Cosmos DB payloads \u2014 significantly lowering Azure cloud spend.",

        "<b>Reduced cross-service latency from 400\u202fms to 20\u202fms</b> by re-architecting "
        "real-time order-amendment flow across multiple backend services.",

        "<b>Championed Java 8/11 \u2192 21 migration</b> (virtual threads, Spring Boot 3.x); "
        "guided 3 teams through the upgrade and standardised dependency management.",

        "<b>Hardened 25+ microservices</b> \u2014 Docker configs, CI/CD pipelines, release "
        "workflows \u2014 <b>50% faster startup</b>, <b>30% lower resource usage</b>.",

        "<b>Mentored 3 engineers</b> through system-design reviews, feature planning, and code reviews.",
    ]:
        s.append(b(t))
    s.append(Spacer(1, 0.5))

    # ── Walmart: SDE III ─────────────────────────────────────────────────────
    s.append(role_header("Walmart Global Tech", "Bengaluru, India",
                         "Software Development Engineer III", "05/2022 \u2013 05/2024"))
    s.append(Paragraph(
        "Promoted within the same platform team. Key contributions listed above span both roles.",
        S("note", fontName="Helvetica-Oblique", fontSize=7.2, textColor=LGREY, leading=9.5)))
    s.append(Spacer(1, 1.5))

    # ── Clari ────────────────────────────────────────────────────────────────
    s.append(role_header("Clari (Revenue Intelligence)", "Bengaluru, India",
                         "Software Development Engineer II", "01/2021 \u2013 05/2022"))
    s.append(Paragraph("Bengaluru, India  \u00b7  CRM &amp; Data Ingestion", CO_LOC))
    s.append(Paragraph("Java 8 \u00b7 Spring Boot \u00b7 PostgreSQL \u00b7 MongoDB \u00b7 AWS \u00b7 REST APIs", STACK))
    for t in [
        "<b>Owned the Autocapture data-ingestion engine</b> \u2014 high-throughput, "
        "fault-tolerant data loading across <b>200+ enterprise organisations</b>.",

        "<b>Built API connectors</b> (G Suite, Outlook) ingesting emails and calendar events "
        "for <b>500K+ end users</b> with high availability.",

        "<b>Optimised PostgreSQL queries and REST endpoints</b> \u2014 reduced <b>p99 latency</b>; "
        "overhauled exception handling (10% CPU reduction).",
    ]:
        s.append(b(t))
    s.append(Spacer(1, 0.5))

    # ── Clari SDE I ──────────────────────────────────────────────────────────
    s.append(role_header("Clari (Revenue Intelligence)", "Bengaluru, India",
                         "Software Development Engineer I", "07/2019 \u2013 12/2020"))
    s.append(Paragraph(
        "Contributed to the same Autocapture platform. Promoted to SDE II based on performance.",
        S("note2", fontName="Helvetica-Oblique", fontSize=7.2, textColor=LGREY, leading=9.5)))
    s.append(Spacer(1, 2))

    # ══════════════════════════════════════════════════════════════════════════
    # EDUCATION
    # ══════════════════════════════════════════════════════════════════════════
    s += sec("Education")

    edu_data = [
        [Paragraph("<b>Indian Institute of Technology (IIT), Kharagpur</b>", EDU_I),
         Paragraph("09/2014 \u2013 06/2019", EDU_DATE)],
        [Paragraph("M.Tech + B.Tech, Computer Science &amp; Engineering (5-Year Integrated Dual Degree)", EDU_D),
         Paragraph("", EDU_D)],
        [Paragraph("Thesis: Healthcare records system developed in collaboration with AIIMS clinicians", EDU_D),
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
        [Paragraph("<b>Generative AI Certification</b> \u2014 IIT Kharagpur (delivered at Walmart)", EDU_D),
         Paragraph("2025 \u2013 2026", EDU_DATE)],
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
        ("Data Streaming &amp; CDC",   "Apache Kafka (schema design, CDC patterns, priority routing),  Debezium (familiar),  Event Sourcing"),
        ("Databases",                  "PostgreSQL,  Cosmos DB,  MongoDB,  Cassandra,  Elasticsearch"),
        ("Cloud &amp; DevOps",         "Azure,  AWS,  Kubernetes,  Docker,  CI/CD Pipelines,  GitHub Actions,  Prometheus,  Grafana"),
        ("Data Formats",               "zstd Compression,  Parquet (familiar),  Apache Iceberg (familiar),  JSON / Avro Schemas"),
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
        "<b>2nd Prize</b> \u2014 lablab.ai Global AI Hackathon (2026): NL2SQL real-time analytics dashboard.",
        "<b>Excellence Award</b> \u2014 Walmart (2025): 40% storage-cost reduction via zstd compression.",
        "<b>Bravo Award</b> \u2014 Walmart (2025): AI on-call agent reducing incident MTTR by 60%.",
        "<b>Excellence Award</b> \u2014 Walmart (2024): Priority Kafka pipeline \u2014 zero extra infrastructure cost.",
        "<b>Runner-Up</b> \u2014 Walmart Global Techathon (2022): Data-driven recommendation engine.",
        "<b>Winner</b> \u2014 Clari Innovates Hackathon (2021): Internal tooling platform, adopted company-wide.",
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
