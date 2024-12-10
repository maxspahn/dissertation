import sys
from io import BytesIO
from pathlib import Path
from typing import List, Union

from PIL import Image
from pypdf import PageRange, PdfReader, PdfWriter, Transformation


def image_to_pdf(stamp_img: Union[Path, str]) -> PdfReader:
    img = Image.open(stamp_img)
    img_as_pdf = BytesIO()
    img.save(img_as_pdf, "pdf")
    return PdfReader(img_as_pdf)


def stamp_img(
    content_pdf: str,
    stamp_imgs: List[str],
    pdf_result: str,
    start_page: int = 1,
):

    writer = PdfWriter()
    reader = PdfReader(content_pdf)
    reader.pages
    writer.append(reader)

    # get page indices to take every other page
    page_indices = list(range(start_page, len(reader.pages)+1, 2))

    tf_matrix = Transformation().scale(sx=0.06, sy=0.06).translate(tx=365, ty=5)


    for img_index, page_index in enumerate(page_indices):
        if img_index >= len(stamp_imgs):
            break
        # Convert the image to a PDF
        stamp_pdf = image_to_pdf(stamp_imgs[img_index])

        # Then use the same stamp code from above
        stamp_page = stamp_pdf.pages[0]
        content_page = writer.pages[page_index - 1]
        content_page.merge_transformed_page(
            stamp_page,
            tf_matrix,
        )

    with open(pdf_result, "wb") as fp:
        writer.write(fp)

def main():
    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    start_page = int(sys.argv[3])
    images = sys.argv[4:]
    stamp_img(input_pdf, images, output_pdf, start_page=start_page)

if __name__ == "__main__":
    main()


