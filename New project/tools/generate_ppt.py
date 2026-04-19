from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from textwrap import dedent
from zipfile import ZIP_DEFLATED, ZipFile
from xml.sax.saxutils import escape


OUTPUT = Path("Cloud_Based_Smart_Healthcare_Monitoring_System_Presentation.pptx")


SLIDES = [
    {
        "title": "Cloud-Based Smart Healthcare Monitoring System Using Machine Learning",
        "bullets": [
            "Final year project presentation",
            "Healthcare risk prediction without IoT devices",
            "Prepared for report, seminar, and viva presentation",
        ],
        "variant": "cover",
    },
    {
        "title": "Introduction",
        "bullets": [
            "Healthcare monitoring is important for early risk detection and timely intervention.",
            "Many smart healthcare systems depend on wearable sensors and IoT devices.",
            "Such systems increase cost, hardware dependency, and maintenance effort.",
            "This project proposes a software-based alternative using machine learning.",
        ],
        "variant": "content",
    },
    {
        "title": "Problem Statement",
        "bullets": [
            "Existing healthcare monitoring systems often require IoT devices and sensor infrastructure.",
            "These systems are not always affordable or accessible in low-resource environments.",
            "A low-cost ML-based monitoring solution is needed using manually entered healthcare data.",
        ],
        "variant": "content",
    },
    {
        "title": "Objectives",
        "bullets": [
            "Develop a healthcare monitoring system without IoT devices.",
            "Predict patient risk using machine learning.",
            "Provide a simple web-based interface for user interaction.",
            "Build a cloud-oriented solution suitable for future deployment.",
        ],
        "variant": "content",
    },
    {
        "title": "System Workflow",
        "bullets": [
            "Generate synthetic healthcare dataset.",
            "Train Random Forest model on structured patient features.",
            "Save model and metrics as artifacts.",
            "Accept manual patient input through Streamlit app.",
            "Predict Low, Medium, or High risk and show recommendation.",
        ],
        "variant": "content",
    },
    {
        "title": "Input Features",
        "bullets": [
            "Age",
            "BMI",
            "Systolic and Diastolic Blood Pressure",
            "Heart Rate and Glucose Level",
            "Oxygen Saturation and Sleep Hours",
            "Activity Minutes, Symptom Severity, and Chronic Condition History",
        ],
        "variant": "content",
    },
    {
        "title": "Technology Stack",
        "bullets": [
            "Python for implementation",
            "Streamlit for web application interface",
            "Pandas and NumPy for data handling",
            "Scikit-learn for machine learning",
            "Joblib for model saving and loading",
        ],
        "variant": "content",
    },
    {
        "title": "Model and Results",
        "bullets": [
            "Model used: Random Forest Classifier",
            "Dataset size: 1000 synthetic healthcare records",
            "Validation accuracy: 71.5%",
            "Output classes: Low Risk, Medium Risk, High Risk",
            "System displays prediction confidence and recommendation",
        ],
        "variant": "content",
    },
    {
        "title": "Advantages and Future Scope",
        "bullets": [
            "No IoT hardware dependency",
            "Low-cost and easy to use",
            "Suitable for telemedicine and academic demonstration",
            "Future scope includes real datasets, database support, cloud deployment, and explainable AI",
        ],
        "variant": "content",
    },
    {
        "title": "Conclusion",
        "bullets": [
            "The project successfully demonstrates healthcare monitoring using ML without IoT devices.",
            "It combines dataset generation, model training, and web-based prediction in one system.",
            "The system is practical as an academic prototype and can be extended further.",
            "Thank You",
        ],
        "variant": "closing",
    },
]


def emu(inches: float) -> int:
    return int(inches * 914400)


def bullet_paragraphs(lines: list[str], *, color: str = "1F1F1F", size: int = 2200) -> str:
    parts = []
    for i, line in enumerate(lines):
        bullet = (
            '<a:pPr marL="342900" indent="-171450"><a:buChar char="•"/></a:pPr>'
            if i > 0
            else '<a:pPr/>'
        )
        parts.append(
            f"<a:p>{bullet}<a:r><a:rPr lang=\"en-US\" sz=\"{size}\"><a:solidFill><a:srgbClr val=\"{color}\"/></a:solidFill></a:rPr>"
            f"<a:t>{escape(line)}</a:t></a:r><a:endParaRPr lang=\"en-US\" sz=\"2200\"/></a:p>"
        )
    return "".join(parts)


def cover_slide_xml(title: str, bullets: list[str], idx: int) -> str:
    title_x, title_y, title_cx, title_cy = emu(0.85), emu(1.15), emu(9.5), emu(1.7)
    sub_x, sub_y, sub_cx, sub_cy = emu(0.95), emu(3.45), emu(7.0), emu(2.1)
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
 xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:bg>
      <p:bgPr>
        <a:solidFill><a:srgbClr val="F4F9FF"/></a:solidFill>
        <a:effectLst/>
      </p:bgPr>
    </p:bg>
    <p:spTree>
      <p:nvGrpSpPr>
        <p:cNvPr id="1" name=""/>
        <p:cNvGrpSpPr/>
        <p:nvPr/>
      </p:nvGrpSpPr>
      <p:grpSpPr>
        <a:xfrm>
          <a:off x="0" y="0"/>
          <a:ext cx="0" cy="0"/>
          <a:chOff x="0" y="0"/>
          <a:chExt cx="0" cy="0"/>
        </a:xfrm>
      </p:grpSpPr>
      <p:sp>
        <p:nvSpPr>
          <p:cNvPr id="2" name="Left Accent"/>
          <p:cNvSpPr/>
          <p:nvPr/>
        </p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="{emu(0)}" y="{emu(0)}"/><a:ext cx="{emu(1.0)}" cy="{emu(7.5)}"/></a:xfrm>
          <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
          <a:solidFill><a:srgbClr val="1E5BB8"/></a:solidFill>
          <a:ln><a:noFill/></a:ln>
        </p:spPr>
        <p:txBody><a:bodyPr/><a:lstStyle/><a:p/></p:txBody>
      </p:sp>
      <p:sp>
        <p:nvSpPr>
          <p:cNvPr id="3" name="Main Card"/>
          <p:cNvSpPr/>
          <p:nvPr/>
        </p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="{emu(0.75)}" y="{emu(0.75)}"/><a:ext cx="{emu(10.8)}" cy="{emu(5.9)}"/></a:xfrm>
          <a:prstGeom prst="roundRect"><a:avLst/></a:prstGeom>
          <a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill>
          <a:ln w="19050"><a:solidFill><a:srgbClr val="D9E9FF"/></a:solidFill></a:ln>
          <a:effectLst>
            <a:outerShdw blurRad="38100" dist="25400" dir="5400000" algn="ctr" rotWithShape="0">
              <a:srgbClr val="B8CDEE"><a:alpha val="30000"/></a:srgbClr>
            </a:outerShdw>
          </a:effectLst>
        </p:spPr>
        <p:txBody><a:bodyPr/><a:lstStyle/><a:p/></p:txBody>
      </p:sp>
      <p:sp>
        <p:nvSpPr>
          <p:cNvPr id="4" name="Title {idx}"/>
          <p:cNvSpPr txBox="1"/>
          <p:nvPr/>
        </p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="{title_x}" y="{title_y}"/><a:ext cx="{title_cx}" cy="{title_cy}"/></a:xfrm>
          <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
          <a:noFill/>
          <a:ln><a:noFill/></a:ln>
        </p:spPr>
        <p:txBody>
          <a:bodyPr wrap="square" rtlCol="0" anchor="ctr"/>
          <a:lstStyle/>
          <a:p><a:pPr algn="l"/><a:r><a:rPr lang="en-US" sz="3200" b="1"><a:solidFill><a:srgbClr val="173A73"/></a:solidFill></a:rPr><a:t>{escape(title)}</a:t></a:r><a:endParaRPr lang="en-US" sz="3200" b="1"/></a:p>
        </p:txBody>
      </p:sp>
      <p:sp>
        <p:nvSpPr>
          <p:cNvPr id="5" name="Subtitle {idx}"/>
          <p:cNvSpPr txBox="1"/>
          <p:nvPr/>
        </p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="{sub_x}" y="{sub_y}"/><a:ext cx="{sub_cx}" cy="{sub_cy}"/></a:xfrm>
          <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
          <a:noFill/>
          <a:ln><a:noFill/></a:ln>
        </p:spPr>
        <p:txBody>
          <a:bodyPr wrap="square" lIns="91440" tIns="91440" rIns="91440" bIns="91440"/>
          <a:lstStyle/>
          {bullet_paragraphs(bullets, color="3A4A63", size=2200)}
        </p:txBody>
      </p:sp>
      <p:sp>
        <p:nvSpPr>
          <p:cNvPr id="6" name="Footer Tag"/>
          <p:cNvSpPr txBox="1"/>
          <p:nvPr/>
        </p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="{emu(0.95)}" y="{emu(6.2)}"/><a:ext cx="{emu(4.0)}" cy="{emu(0.5)}"/></a:xfrm>
          <a:prstGeom prst="roundRect"><a:avLst/></a:prstGeom>
          <a:solidFill><a:srgbClr val="1E5BB8"/></a:solidFill>
          <a:ln><a:noFill/></a:ln>
        </p:spPr>
        <p:txBody>
          <a:bodyPr anchor="ctr"/>
          <a:lstStyle/>
          <a:p><a:pPr algn="ctr"/><a:r><a:rPr lang="en-US" sz="1600" b="1"><a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill></a:rPr><a:t>Integral University</a:t></a:r><a:endParaRPr lang="en-US" sz="1600"/></a:p>
        </p:txBody>
      </p:sp>
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sld>
"""


def content_slide_xml(title: str, bullets: list[str], idx: int, *, closing: bool = False) -> str:
    title_x, title_y, title_cx, title_cy = emu(0.9), emu(0.55), emu(10.6), emu(0.75)
    body_x, body_y, body_cx, body_cy = emu(1.0), emu(1.55), emu(10.2), emu(4.8)
    accent = "173A73" if not closing else "1E5BB8"
    footer = "Project Presentation" if not closing else "Thank you"
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
 xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:bg>
      <p:bgPr>
        <a:solidFill><a:srgbClr val="F8FBFF"/></a:solidFill>
        <a:effectLst/>
      </p:bgPr>
    </p:bg>
    <p:spTree>
      <p:nvGrpSpPr>
        <p:cNvPr id="1" name=""/>
        <p:cNvGrpSpPr/>
        <p:nvPr/>
      </p:nvGrpSpPr>
      <p:grpSpPr>
        <a:xfrm>
          <a:off x="0" y="0"/>
          <a:ext cx="0" cy="0"/>
          <a:chOff x="0" y="0"/>
          <a:chExt cx="0" cy="0"/>
        </a:xfrm>
      </p:grpSpPr>
      <p:sp>
        <p:nvSpPr><p:cNvPr id="2" name="Top Band"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="0" y="0"/><a:ext cx="{emu(13.333)}" cy="{emu(0.22)}"/></a:xfrm>
          <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
          <a:solidFill><a:srgbClr val="1E5BB8"/></a:solidFill>
          <a:ln><a:noFill/></a:ln>
        </p:spPr>
        <p:txBody><a:bodyPr/><a:lstStyle/><a:p/></p:txBody>
      </p:sp>
      <p:sp>
        <p:nvSpPr>
          <p:cNvPr id="3" name="Title {idx}"/>
          <p:cNvSpPr txBox="1"/>
          <p:nvPr/>
        </p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="{title_x}" y="{title_y}"/><a:ext cx="{title_cx}" cy="{title_cy}"/></a:xfrm>
          <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
          <a:noFill/>
          <a:ln><a:noFill/></a:ln>
        </p:spPr>
        <p:txBody>
          <a:bodyPr anchor="ctr"/>
          <a:lstStyle/>
          <a:p><a:pPr algn="l"/><a:r><a:rPr lang="en-US" sz="2600" b="1"><a:solidFill><a:srgbClr val="{accent}"/></a:solidFill></a:rPr><a:t>{escape(title)}</a:t></a:r><a:endParaRPr lang="en-US" sz="2600" b="1"/></a:p>
        </p:txBody>
      </p:sp>
      <p:sp>
        <p:nvSpPr>
          <p:cNvPr id="4" name="Content Card {idx}"/>
          <p:cNvSpPr txBox="1"/>
          <p:nvPr/>
        </p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="{body_x}" y="{body_y}"/><a:ext cx="{body_cx}" cy="{body_cy}"/></a:xfrm>
          <a:prstGeom prst="roundRect"><a:avLst/></a:prstGeom>
          <a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill>
          <a:ln w="19050"><a:solidFill><a:srgbClr val="D7E7FF"/></a:solidFill></a:ln>
          <a:effectLst>
            <a:outerShdw blurRad="38100" dist="19050" dir="5400000" algn="ctr" rotWithShape="0">
              <a:srgbClr val="C6D8F6"><a:alpha val="28000"/></a:srgbClr>
            </a:outerShdw>
          </a:effectLst>
        </p:spPr>
        <p:txBody>
          <a:bodyPr wrap="square" lIns="228600" tIns="182880" rIns="228600" bIns="182880"/>
          <a:lstStyle/>
          {bullet_paragraphs(bullets, color="243447", size=2200)}
        </p:txBody>
      </p:sp>
      <p:sp>
        <p:nvSpPr><p:cNvPr id="5" name="Footer"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="{emu(0.95)}" y="{emu(6.83)}"/><a:ext cx="{emu(3.5)}" cy="{emu(0.35)}"/></a:xfrm>
          <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
          <a:noFill/>
          <a:ln><a:noFill/></a:ln>
        </p:spPr>
        <p:txBody>
          <a:bodyPr/>
          <a:lstStyle/>
          <a:p><a:pPr algn="l"/><a:r><a:rPr lang="en-US" sz="1400"><a:solidFill><a:srgbClr val="5F7393"/></a:solidFill></a:rPr><a:t>{footer}</a:t></a:r><a:endParaRPr lang="en-US" sz="1400"/></a:p>
        </p:txBody>
      </p:sp>
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sld>
"""


def slide_xml(title: str, bullets: list[str], idx: int, variant: str = "content") -> str:
    if variant == "cover":
        return cover_slide_xml(title, bullets, idx)
    return content_slide_xml(title, bullets, idx, closing=(variant == "closing"))


def slide_layout_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldLayout xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
 xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" type="blank" preserve="1">
  <p:cSld name="Blank">
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr>
        <a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm>
      </p:grpSpPr>
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sldLayout>
"""


def slide_master_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldMaster xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
 xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld name="Office Theme">
    <p:bg>
      <p:bgPr><a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill><a:effectLst/></p:bgPr>
    </p:bg>
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr>
        <a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm>
      </p:grpSpPr>
    </p:spTree>
  </p:cSld>
  <p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>
  <p:sldLayoutIdLst><p:sldLayoutId id="2147483649" r:id="rId1"/></p:sldLayoutIdLst>
  <p:txStyles>
    <p:titleStyle/>
    <p:bodyStyle/>
    <p:otherStyle/>
  </p:txStyles>
</p:sldMaster>
"""


def theme_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Office Theme">
  <a:themeElements>
    <a:clrScheme name="Office">
      <a:dk1><a:sysClr val="windowText" lastClr="000000"/></a:dk1>
      <a:lt1><a:sysClr val="window" lastClr="FFFFFF"/></a:lt1>
      <a:dk2><a:srgbClr val="1F1F1F"/></a:dk2>
      <a:lt2><a:srgbClr val="F7FAFF"/></a:lt2>
      <a:accent1><a:srgbClr val="1E5BB8"/></a:accent1>
      <a:accent2><a:srgbClr val="4A90E2"/></a:accent2>
      <a:accent3><a:srgbClr val="153E7A"/></a:accent3>
      <a:accent4><a:srgbClr val="7AA6E8"/></a:accent4>
      <a:accent5><a:srgbClr val="8FB5FF"/></a:accent5>
      <a:accent6><a:srgbClr val="C7DAFF"/></a:accent6>
      <a:hlink><a:srgbClr val="0000FF"/></a:hlink>
      <a:folHlink><a:srgbClr val="800080"/></a:folHlink>
    </a:clrScheme>
    <a:fontScheme name="Office">
      <a:majorFont><a:latin typeface="Arial"/><a:ea typeface=""/><a:cs typeface=""/></a:majorFont>
      <a:minorFont><a:latin typeface="Arial"/><a:ea typeface=""/><a:cs typeface=""/></a:minorFont>
    </a:fontScheme>
    <a:fmtScheme name="Office"><a:fillStyleLst/><a:lnStyleLst/><a:effectStyleLst/><a:bgFillStyleLst/></a:fmtScheme>
  </a:themeElements>
  <a:objectDefaults/>
  <a:extraClrSchemeLst/>
</a:theme>
"""


def content_types_xml(slide_count: int) -> str:
    overrides = "\n".join(
        f'<Override PartName="/ppt/slides/slide{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>'
        for i in range(1, slide_count + 1)
    )
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
  <Override PartName="/ppt/presProps.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presProps+xml"/>
  <Override PartName="/ppt/viewProps.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.viewProps+xml"/>
  <Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>
  <Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>
  <Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
  {overrides}
</Types>
"""


def rels_root_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>
"""


def app_xml(slide_count: int) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
 xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Microsoft Office PowerPoint</Application>
  <Slides>{slide_count}</Slides>
  <Notes>0</Notes>
  <HiddenSlides>0</HiddenSlides>
  <MMClips>0</MMClips>
  <ScaleCrop>false</ScaleCrop>
  <HeadingPairs>
    <vt:vector size="2" baseType="variant">
      <vt:variant><vt:lpstr>Slides</vt:lpstr></vt:variant>
      <vt:variant><vt:i4>{slide_count}</vt:i4></vt:variant>
    </vt:vector>
  </HeadingPairs>
  <TitlesOfParts>
    <vt:vector size="{slide_count}" baseType="lpstr">
      {''.join(f'<vt:lpstr>{escape(slide["title"])}</vt:lpstr>' for slide in SLIDES)}
    </vt:vector>
  </TitlesOfParts>
  <Company>Integral University</Company>
  <LinksUpToDate>false</LinksUpToDate>
  <SharedDoc>false</SharedDoc>
  <HyperlinksChanged>false</HyperlinksChanged>
  <AppVersion>16.0000</AppVersion>
</Properties>
"""


def core_xml() -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
 xmlns:dc="http://purl.org/dc/elements/1.1/"
 xmlns:dcterms="http://purl.org/dc/terms/"
 xmlns:dcmitype="http://purl.org/dc/dcmitype/"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>Cloud-Based Smart Healthcare Monitoring System Using Machine Learning</dc:title>
  <dc:creator>Codex</dc:creator>
  <cp:lastModifiedBy>Codex</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified>
</cp:coreProperties>
"""


def presentation_xml(slide_count: int) -> str:
    slides = "\n".join(
        f'<p:sldId id="{256+i}" r:id="rId{i+2}"/>' for i in range(slide_count)
    )
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
 xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"
 saveSubsetFonts="1" autoCompressPictures="0">
  <p:sldMasterIdLst><p:sldMasterId id="2147483648" r:id="rId1"/></p:sldMasterIdLst>
  <p:sldIdLst>{slides}</p:sldIdLst>
  <p:sldSz cx="12192000" cy="6858000"/>
  <p:notesSz cx="6858000" cy="9144000"/>
</p:presentation>
"""


def presentation_rels_xml(slide_count: int) -> str:
    slide_rels = "\n".join(
        f'<Relationship Id="rId{i+2}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{i+1}.xml"/>'
        for i in range(slide_count)
    )
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>
  {slide_rels}
</Relationships>
"""


def slide_rels_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
</Relationships>
"""


def slide_layout_rels_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="../slideMasters/slideMaster1.xml"/>
</Relationships>
"""


def slide_master_rels_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="../theme/theme1.xml"/>
</Relationships>
"""


def simple_xml(root: str) -> str:
    return dedent(root).strip() + "\n"


def build_pptx() -> None:
    slide_count = len(SLIDES)
    with ZipFile(OUTPUT, "w", compression=ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types_xml(slide_count))
        zf.writestr("_rels/.rels", rels_root_xml())
        zf.writestr("docProps/app.xml", app_xml(slide_count))
        zf.writestr("docProps/core.xml", core_xml())
        zf.writestr("ppt/presentation.xml", presentation_xml(slide_count))
        zf.writestr("ppt/_rels/presentation.xml.rels", presentation_rels_xml(slide_count))
        zf.writestr("ppt/presProps.xml", simple_xml("""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentationPr xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"/>"""))
        zf.writestr("ppt/viewProps.xml", simple_xml("""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:viewPr xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:normalViewPr><p:restoredLeft sz="15620"/><p:restoredTop sz="94660"/></p:normalViewPr>
  <p:slideViewPr><p:cSldViewPr snapToGrid="1"/></p:slideViewPr>
  <p:outlineViewPr/>
  <p:notesTextViewPr/>
  <p:gridSpacing cx="72008" cy="72008"/>
</p:viewPr>"""))
        zf.writestr("ppt/theme/theme1.xml", theme_xml())
        zf.writestr("ppt/slideMasters/slideMaster1.xml", slide_master_xml())
        zf.writestr("ppt/slideMasters/_rels/slideMaster1.xml.rels", slide_master_rels_xml())
        zf.writestr("ppt/slideLayouts/slideLayout1.xml", slide_layout_xml())
        zf.writestr("ppt/slideLayouts/_rels/slideLayout1.xml.rels", slide_layout_rels_xml())

        for i, slide in enumerate(SLIDES, start=1):
            zf.writestr(f"ppt/slides/slide{i}.xml", slide_xml(slide["title"], slide["bullets"], i))
            zf.writestr(f"ppt/slides/_rels/slide{i}.xml.rels", slide_rels_xml())


if __name__ == "__main__":
    build_pptx()
    print(f"Created {OUTPUT}")
