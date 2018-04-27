echo |\
cat ssltmp.crt 2>&1 |\
sed -e '/-----/d' > ssl.crt
