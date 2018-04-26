#!/bin/bash
echo |\
openssl s_client -connect $1:$2 2>&1 |\
sed -n '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > ssltmp.crt |\
echo |\
cat ssltmp.crt 2>&1 |\
sed -e '/-----/d' > ssl.crt
#sed -e '/-----/d' ssltmp.cat > ssl.crt
