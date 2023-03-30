from docxtpl import DocxTemplate

name = "Aliya"

doc = DocxTemplate("inviteTmpl.docx")

context = {
    "todayStr": "03.03.2023",
    "recipientName": name,
    "evntDtStr": "08.03.2023",
    "venueStr": "the beach",
    "bannerImg": ""
}

doc.render(context)

doc.save("aaaa_{0}.docx".format(name))
doc_name = str("aaaa_{0}.docx".format(name))
print(doc_name)