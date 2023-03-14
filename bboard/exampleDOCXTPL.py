from docxtpl import DocxTemplate

personNames = ["Aliya", "Samal", "Safia", "Kamshat"]

for pItr, p in enumerate(personNames):
    doc = DocxTemplate("inviteTmpl.docx")

    context = {
        "todayStr":"03.03.2023",
        "recipientName":p,
        "evntDtStr":"08.03.2023",
        "venueStr":"the beach",
        "bannerImg":""
    }

    doc.render(context)

    doc.save("aaaa_{0}.docx".format(p))