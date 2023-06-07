#!/bin/bash

# Parse command-line arguments and update config.json
if [ "$ip_address" ]; then
    jq --arg ip_address "$ip_address" '.ip_address = $ip_address' ./config.json > temp.json && mv temp.json ./config.json
fi

if [ "$ip_port" ]; then
    jq --arg ip_port "$ip_port" '.ip_port = $ip_port' ./config.json > temp.json && mv temp.json ./config.json
fi

if [ "$show_google" ]; then
    jq --arg show_google "$show_google" '.show_google = $show_google' ./config.json > temp.json && mv temp.json ./config.json
fi

# Start the Streamlit application
streamlit run ./app.py