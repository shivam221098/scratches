from pprint import pprint
from lxml import etree


def get_pmid(elements):
    for ele in elements:
        if ele.tag == "PMID":
            return ele.text


def get_nln_uid(elements):
    for element in elements:
        if element.tag == "MedlineJournalInfo":
            journal_info = element.getchildren()
            for journal in journal_info:
                if journal.tag == "NlmUniqueID":
                    return "MedlineJournalInfo", {
                            "NlmUniqueID": journal.text
                        }

    return "MedlineJournalInfo", {
                            "NlmUniqueID": None
                        }


def get_coi(elements):
    for element in elements:
        if element.tag == "CoiStatement":
            return "CoiStatement", element.text

    return "CoiStatement", None


def get_revised_date(elements):
    for element in elements:
        if element.tag == "DateRevised":
            revised_date = element.getchildren()

            year = None
            month = None
            day = None

            for date in revised_date:
                if date.tag == "Year":
                    year = date.text

                if date.tag == "Month":
                    month = date.text

                if date.tag == "Day":
                    day = date.text

            return "DateRevised", {
                "Year": year,
                "Month": month,
                "Day": day
            }

    return "DateRevised", {
        "Year": None,
        "Month": None,
        "Day": None
    }


def parseXML(xml_file_name):
    xml_file = {
        "PubmedArticleSet": {
            "PubmedArticle":
                [

                ]
        }
    }

    with open(xml_file_name, "r", encoding="utf-8") as file:
        root = etree.parse(file)

        for row in root.xpath("/PubmedArticleSet/PubmedArticle"):
            medline = {}
            medline_citation = row[0]
            pubmed_data = row[1]

            medline.update({"PMID": get_pmid(medline_citation)})

            nlm = get_nln_uid(medline_citation)
            medline.update({nlm[0]: nlm[1]})

            coi = get_coi(medline_citation)
            medline.update({coi[0]: coi[1]})

            date_revised = get_revised_date(medline_citation)

            medline.update({date_revised[0]: date_revised[1]})

            xml_file.get("PubmedArticleSet").get("PubmedArticle").append(medline)

    return xml_file


pprint(parseXML("pubmed21n0869.xml"))