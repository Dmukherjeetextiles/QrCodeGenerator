# QrCodeGenerator
This Streamlit application generates QR codes from a list of URLs provided by the user.  It allows the user to dynamically add or remove input fields for URLs and then generates and allows the user to download an SVG image of the QR code.

## Features

*   **Dynamic URL Input:** Allows users to add or remove URL input fields as needed.  A minimum of one input field is always present.
*   **QR Code Generation:**  Generates a QR code from the combined list of URLs.
*   **SVG Download:** Provides a button to download the generated QR code as an SVG file.
*   **Clear User Interface:**  Uses Streamlit to provide an intuitive and easy-to-use interface.

## Prerequisites

*   Python 3.7+
*   Streamlit (`pip install streamlit`)
*   qrcodegen library (`pip install qrcodegen`)

## Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/Dmukherjeetextiles/QrCodeGenerator.git
    cd QrCodeGenerator
    ```

2.  Install the required packages:

    ```bash
    pip install streamlit qrcodegen
    ```

## Usage

1.  Run the Streamlit application:

    ```bash
    streamlit run qrApp.py
    ```

2.  Open the application in your web browser (usually at `http://localhost:8501`).

3.  Add the URLs in the input fields. Use the "Add URL" button to add more fields or the "Remove" button to remove them.

4.  Click the "Generate QR Code" button. The QR code will be displayed on the screen.

5.  Click the "Download SVG" button to download the QR code as an SVG file.

## Code Overview

*   `qrApp.py`: The main script containing the Streamlit application code.
*   `qrcodegen.py`: (From the qrcodegen library) Library for generating QR codes.

### Functions

*   `to_svg_str(qr: QrCode, border: int) -> str`: Converts a `QrCode` object to an SVG string.
*   `generate_qr_code(text: str, border: int = 4) -> str`: Generates a QR code SVG string from the given text.
*   `download_svg(svg_string: str, filename: str = "qrcode.svg") -> None`: Provides a download button for the SVG string.
*   `qrApp()`:  The main Streamlit application function.

## Customization

*   **QR Code Size:**  Modify the `width` and `height` attributes in the `<svg>` tag within the `to_svg_str` function to adjust the size of the generated QR code.
*   **Border Size:**  Modify the `border` parameter in the `generate_qr_code` function to adjust the border around the QR code.  Smaller borders result in smaller overall QR codes, but may affect scannability.
*   **Error Correction Level:**  The error correction level is set to `QrCode.Ecc.LOW`. This can be changed in the `generate_qr_code` function if desired.  Higher error correction levels result in larger QR codes but can tolerate more damage or obstruction.

## Example

A user enters the following URLs:

*   `https://www.facebook.com/example`
*   `https://www.twitter.com/example`
*   `https://www.instagram.com/example`

The application generates a QR code containing these URLs, which can be scanned to access all three social media profiles.  The user can then download this QR code as an SVG file for use in print or digital media.

## Dependencies

*   [Streamlit](https://streamlit.io/)
*   [qrcodegen](https://github.com/nayuki/QR-Code-generator)

## Demo
[Demo link](https://qrcodetosvg.streamlit.app/)
