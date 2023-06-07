docker build -t sushil3125/ocr_citizenship . <br />
docker run -it -p 8501:8501 -e ip_address="192.168.41.111" -e ip_port="6011" -e show_google=false sushil3125/ocr_citizenship