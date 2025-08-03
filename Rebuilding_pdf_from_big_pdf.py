'''
Title: Rebuilding PDF from a Big PDF (with missing images/fonts and with issues)
Author: Shahriar Rahman
Version: v5
Date: 3 August 2025
'''

import fitz
from PIL import Image
import os

def rebuild_pdf_as_images(input_pdf_path, output_pdf_path, dpi=300):  # set the dpi as per requirements
    input_pdf_path = os.path.abspath(input_pdf_path)
    output_pdf_path = os.path.abspath(output_pdf_path)

    if not os.path.exists(input_pdf_path):
        print(f"[!] File not found: {input_pdf_path}")
        return False

    try:
        doc = fitz.open(input_pdf_path)
        images = []
        skipped_pages = []

        print(f"[*] Total pages: {len(doc)}")

        for i in range(len(doc)):
            try:
                page = doc.load_page(i)
                zoom = dpi / 72  # say default resolution is 72 dpi
                mat = fitz.Matrix(zoom, zoom)
                pix = page.get_pixmap(matrix=mat)
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                images.append(img)
                print(f"[✓] Page {i + 1} rendered successfully.")
            except Exception as e:
                print(f"[!] Skipping page {i + 1}: {e}")
                skipped_pages.append(i + 1)
        if not images:
            print("[!] No pages could be rendered. Aborting.")
            return False

        images[0].save(output_pdf_path, save_all=True, append_images=images[1:], resolution=dpi)
        print(f"\n[+] Final image-based PDF saved to:\n{output_pdf_path}")
        if skipped_pages:
            print(f"[!] Skipped pages: {skipped_pages}")
        else:
            print("[✓] All pages processed.")
        return True

    except Exception as e:
        print(f"[!] Unexpected error: {e}")
        return False

input_pdf_path = r"E:\PDF\ABCD.pdf"
output_pdf_path = r"E:\PDF\ABCD_rebuild.pdf"

rebuild_pdf_as_images(input_pdf_path, output_pdf_path)
