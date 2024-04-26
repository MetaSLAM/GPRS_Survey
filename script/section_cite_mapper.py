# Usage: python3 section_cite_mapper.py > output_file.md

import re
from PyPDF2 import PdfReader

def remove_duplicates(my_list):
    return list(dict.fromkeys(my_list))

# Function to find references in text
def find_references(text, sections):
    ref_pattern = re.compile(r'\[(\d+)\]')  # Example pattern for references like [1], [23]
    section_indices = [text.find(section) for section in sections if text.find(section) != -1]
    section_citations = {section: [] for section in sections}
    print(section_indices)

    for match in ref_pattern.finditer(text):
      ref_id = match.group(1)
      pos = match.start()
      for i in range(len(section_indices)):
        if i < len(section_indices) - 1:
           if pos > section_indices[i] and pos < section_indices[i+1]:
              section_citations[sections[i]].append(ref_id)
        else:
           if pos > section_indices[i]:
            section_citations[sections[i]].append(ref_id)

    return section_citations

def extract_reference(text):
    reference_indices = text.find('REFERENCES')
    pattern = re.compile(r'\] (.*?)\[')
    reference_list = ['placehole']
    for match in pattern.finditer(text):
       pos = match.start()
       if pos > reference_indices:
          text_citation = match.group(1).replace(']', '').replace('[', '')
          reference_list.append(text_citation)
    return reference_list

if __name__ == '__main__':
  reader = PdfReader("/home/jjiao/Downloads/tro_gprs.pdf")
  text = ""
  for page in reader.pages:
      text += page.extract_text()
  text = text.replace('\n', '').replace('\r', '')
  # print(text)

  reference_list = extract_reference(text)
  # for idx, ref in enumerate(reference_list):
  #   print(f"[{idx+1}]{ref}")

  sections = ['ELATED', 'REFERENCES']
  sections = ['Summary', 'Contributions', \
              '2) Camera', '3) Range', 'Graph:', 'Embeddings:', \
              'A. Appearance Change', 'B. Viewpoint Difference', 'C. Generalization Ability', 'D. Efficiency', 'E. Uncertainty Estimation',
              'A. Long-Term & Large-Scale Navigation', 'B. Visual Terrain Relative Navigation', 'C. Multi-Agent Localization and Mapping', 'D. Bio-Inspired and Lifelong Autonomy', \
              'A. Public Datasets', 'C. Supported Libraries', \
              'REFERENCES']
  citations_by_section = find_references(text, sections)
  for section, citations in citations_by_section.items():
      rm_citations = remove_duplicates(citations)
      print(f"### {section} =========================")
      for id_citation in rm_citations:
          if int(id_citation) <= len(reference_list) - 1:
            print(f"[{id_citation}] {reference_list[int(id_citation)]}")
