<a name="readme-top"></a>


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">OCR CITIZENSHIP</h3>

  <p align="center">
    Extract valuable entities from just the photo of the citizenship card.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]]

The OCR Citizenship is a powerful software program designed to streamline the extraction of valuable entities from citizenship images. Leveraging advanced image processing techniques, Optical Character Recognition (OCR), and Natural Language Processing (NLP) algorithms, this project automates the process of extracting essential information from citizenship documents, reducing manual effort and enhancing efficiency. The user interface and front-end of the system are built using Streamlit, providing a seamless and interactive experience for users.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* Python
* Tensorflow
* Tesseract/ PyTesseract
* Streamlit
* OpenCV
* Numpy
* Docker
* Google OCR

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

1. Clone the repo
   ```sh
   git clone git@github.com:sushilld/ocr_citizenship.git
2. Install Docker
   ```sh
   https://docs.docker.com/engine/install/
   ```
3. Install Docker Compose
   ```sh
   https://docs.docker.com/compose/install/
   ```
4. Build Docker Image
   ```sh
   docker build -t ocr_citizenship .
   ```
5. Run Docker Container
   ```sh
   docker run -it -p 8501:8501 -e ip_address="127.0.0.1" -e ip_port="6011" -e show_google="true" sushil3125/ocr_citizenship

6. Login using test as username and test as password

7. Upload both of the images of the citizenship (Front and Back)

8. Click on Submit button and you will see a preview of your citienship card.

9. Navigate to specific tab to see the extracted entities from the image.

### Prerequisites

Following are the prerequisites for this project.

* Docker
  ```sh
    https://docs.docker.com/engine/install/
    ```
* Docker Compose
    ```sh
        https://docs.docker.com/compose/install/
  ```
* Python
  ```sh
    https://www.python.org/downloads/
    ```

### Installation

1. Clone the repo
   ```sh
   git clone git@github.com:sushilld/ocr_citizenship.git
2. Install Docker
   ```sh
   https://docs.docker.com/engine/install/
   ```
3. Install Docker Compose
   ```sh
   https://docs.docker.com/compose/install/
   ```
4. Build Docker Image
   ```sh
   docker build -t ocr_citizenship .
   ```
5. Run Docker Container
   ```sh
   docker run -it -p 8501:8501 -e ip_address="127.0.0.1" -e ip_port="6011" -e show_google="true" sushil3125/ocr_citizenship
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

This project is designed to extract valuable entities from citizenship images. The user interface and front-end of the system are built using Streamlit, providing a seamless and interactive experience for users. The user can upload the image of the citizenship card and the system will extract the following entities from the image.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Your Name - [@sushil3125](https://linkedin.com/in/sushil3125) - sushilldhakal25@gmail.com

Project Link: [https://github.com/sushilld/ocr_citizenship.git](https://github.com/sushilld/ocr_citizenship.git)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Thanks to the following resources for helping me build this project.

* [![Streamlit][Streamlit.io]][Streamlit-url]
* [![Tensorflow][Tensorflow.org]][Tensorflow-url]
* [![PyTesseract][PyTesseract.org]][PyTesseract-url]
* [![OpenCV][OpenCV.org]][OpenCV-url]
* [![Numpy][Numpy.org]][Numpy-url]
* and many more...

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- docker build -t sushil3125/ocr_citizenship . <br />
docker run -it -p 8501:8501 -e ip_address="127.0.0.1" -e ip_port="6011" -e show_google="true" sushil3125/ocr_citizenship -->