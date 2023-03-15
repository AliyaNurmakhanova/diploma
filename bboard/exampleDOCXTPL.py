from docxtpl import DocxTemplate
from .models import Students

students = Students.objects.all()
for pItr, p in enumerate(students):
    doc = DocxTemplate("inviteTmpl.docx")

    context = {
        "todayStr": "03.03.2023",
        "recipientName": p.name,
        "evntDtStr": "08.03.2023",
        "venueStr": "the beach",
        "bannerImg": ""
    }

    doc.render(context)

    doc.save("aaaa_{0}.docx".format(p))