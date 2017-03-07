# Download assets for Irving & Holden. F1000Research.
# https://f1000research.com/articles/5-222
# Execute from the containing directory

# Download article version 1
# https://doi.org/10.12688/f1000research.8114.1
wget --output-document=irving-v1.pdf \
  https://f1000research.com/articles/5-222/v1/pdf

# Download article version 2
# https://doi.org/10.12688/f1000research.8114.2
wget --output-document=irving-v2.pdf \
  https://f1000research.com/articles/5-222/v2/pdf

# Download "Dataset 1. Unformatted text file"
# https://doi.org/10.5256/f1000research.8114.d114596
wget --output-document=dataset-1.docx \
  https://f1000researchdata.s3.amazonaws.com/datasets/8114/9c9f9a18-a852-40c6-953e-c75107abc714_Appendix_1_-_unformatted_text_file_.docx
