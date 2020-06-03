import datetime
import requests

now = datetime.datetime.now()
nowDate = now.strftime('%Y-%m-%d')
login_info = {'id': 'minuk8119', 'password': '@alsdnr112'}
checkData = {'function_gubun': 'startWork', 'idx': '57', 'startDate': nowDate}

with requests.session() as s:
    s.post('http://work.iloveggbb.com/common/include/login_exec.php', data=login_info)
    check = s.post('http://work.iloveggbb.com/common/include/ajax.php', data=checkData)

    if (check.text == "duplicate"):
        print("이미 출석체크 완료.")
    else:
        print("출석체크 완료.")