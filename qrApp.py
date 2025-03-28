from qrcodegen import QrCode, QrSegment
import streamlit as st
import io
from typing import List

# ---- Utilities ----

def to_svg_str(qr: QrCode, border: int) -> str:
    """Returns a string of SVG code for an image depicting the given QR Code, with the given number
    of border modules. The string always uses Unix newlines (\n), regardless of the platform."""
    if border < 0:
        raise ValueError("Border must be non-negative")
    parts: list[str] = []
    for y in range(qr.get_size()):
        for x in range(qr.get_size()):
            if qr.get_module(x, y):
                parts.append(f"M{x+border},{y+border}h1v1h-1z")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 {qr.get_size()+border*2} {qr.get_size()+border*2}" stroke="none" width="200" height="200">
    <rect width="100%" height="100%" fill="#FFFFFF"/>
    <path d="{" ".join(parts)}" fill="#000000"/>
</svg>
"""


def generate_qr_code(text: str, border: int = 4) -> str:
    """Generates an SVG string for a QR code from the given text."""
    errcorlvl = QrCode.Ecc.LOW
    qr = QrCode.encode_text(text, errcorlvl)
    return to_svg_str(qr, border)

def download_svg(svg_string: str, filename: str = "qrcode.svg") -> None:
    """Provides a download button for the SVG string."""
    b = io.StringIO()
    b.write(svg_string)
    svg_bytes = b.getvalue().encode()
    st.download_button(
        label="Download SVG",
        data=svg_bytes,
        file_name=filename,
        mime="image/svg+xml",
    )

# ---- QR Code Generator App ----

def qrApp():
    """
    QR Code Generator:
    This function generates a QR code for a given input string.
    """
    st.logo("logo.png")
    st.title(":red[QR Code Generator]", anchor=False)
    st.write("Enter URLs below to generate a QR code.")

    # There should be always a minimum of 1 URL input field
    if 'num_urls' not in st.session_state:
        st.session_state['num_urls'] = 1

    # Function to add and remove URL input fields
    def add_url():
        st.session_state['num_urls'] += 1
    def remove_url():
        if st.session_state['num_urls'] > 1:
            st.session_state['num_urls'] -= 1
    # Limit the number of URLs to 15
    if st.session_state['num_urls'] > 15:
        st.warning("You have reached the maximum number of URLs.")
        st.session_state['num_urls'] -=1

    # Create input fields for URLs
    url_inputs: List[str] = []
    for i in range(st.session_state['num_urls']):
        url_inputs.append(st.text_input(f"URL No. {i+1}:", key=f"url_{i}"))

    col1, col2, _ = st.columns([1, 1, 5])  
    with col1:
        st.button("Add URL", on_click=add_url, type="primary")
    with col2:
        st.button("Remove", on_click=remove_url, type="primary")

    if st.button("Generate QR Code", type="primary"):
        # Remove empty URLs
        social_media_urls = [url for url in url_inputs if url]

        if social_media_urls:
            combined_text = "\n".join(social_media_urls)
            svg = generate_qr_code(combined_text)
            st.write(svg, unsafe_allow_html=True)
            download_svg(svg)
        else:
            st.warning("Please enter at least one URL.")

if __name__ == "__main__":
    qrApp()