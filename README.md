docker build -t sushil3125/ocr_citizenship . <br />
docker run -it -p 8501:8501 -e ip_address="127.0.0.1" -e ip_port="6011" -e show_google="true" sushil3125/ocr_citizenship