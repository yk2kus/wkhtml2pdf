import subprocess
wkhtmltopdf = ['/usr/bin/wkhtmltopdf', '--cookie', 'session_id', '8c76c03ba1e253835acc2ee98b9ad170ad9047a3', '--quiet', '--page-size', 'Letter', '--margin-top', '40.0', '--dpi', '90', '--header-spacing', '35', '--margin-left', '7.0', '--margin-bottom', '25.0', '--margin-right', '7.0', '--orientation', 'Portrait', '--header-html', 'report.header.tmp.cr15k11a.html', '--footer-html', 'report.footer.tmp.tjp3keh0.html', 'report.body.tmp.0.2rq7mfqu.html', 'report.tmp.daznyt8r.pdf']

process = subprocess.Popen(wkhtmltopdf, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = process.communicate()
