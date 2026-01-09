#!/bin/bash

# --- Color Definitions ---
GREEN='\033[1;32m'
CYAN='\033[1;36m'
WHITE='\033[1;37m'
RESET='\033[0m'

# --- Clear Screen ---
clear

# --- Fancy Header: ChatSweep ---
echo -e "${GREEN}  ___ _         _   ___                     "
echo -e " / __| |_  __ _| |_/ __|_ __ _____ ___ _ __ "
echo -e "| (__| ' \/ _\` |  _\\__ \\ V  V / -_) -_) '_ \\"
echo -e " \___|_||_\__,_|\__|___/\\_/\_/\___\___| .__/"
echo -e "                                       |_|   ${RESET}"

echo -e "${CYAN}--------------------------------------------${RESET}"
echo -e "${WHITE}  Whatsapp Chat Sweep | ${GREEN}By: Zenith0x01${RESET}"
echo -e "${CYAN}--------------------------------------------${RESET}"
echo ""


read -p "Enter user name: " USER_NAME
read -p "How many last messages you want to delete: " USER_COUNT

python main.py "$USER_NAME" "$USER_COUNT"


