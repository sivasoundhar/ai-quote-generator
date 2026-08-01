from io import BytesIO
from datetime import datetime

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate


def generate_pdf(
    quote,
    category,
    language,
):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b>AI Quote Generator</b>",
            styles["Heading1"],
        )
    )

    story.append(
        Paragraph(
            f"<b>Category:</b> {category}",
            styles["Normal"],
        )
    )

    story.append(
        Paragraph(
            f"<b>Language:</b> {language}",
            styles["Normal"],
        )
    )

    story.append(
        Paragraph(
            "<br/><br/>",
            styles["Normal"],
        )
    )

    story.append(
        Paragraph(
            quote,
            styles["BodyText"],
        )
    )

    story.append(
        Paragraph(
            "<br/><br/>",
            styles["Normal"],
        )
    )

    story.append(
        Paragraph(
            datetime.now().strftime(
                "%d-%m-%Y %H:%M"
            ),
            styles["Italic"],
        )
    )

    doc.build(story)

    buffer.seek(0)

    return buffer